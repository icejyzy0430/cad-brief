#!/usr/bin/env python3
"""Validate structural integrity of a cad-brief Markdown handoff.

This validator checks the package contract only. It does not verify source
truth, image interpretation, CAD geometry, manufacturability, or engineering
safety.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


VALID_STATUS = {"ready", "provisional", "blocked"}
VALID_INTENT = {"concept", "fit", "manufacturing-intent", "engineering-review"}
VALID_TASK = {"new part", "assembly", "modification"}
VALID_RESEARCH = {"yes", "not-applicable", "unavailable"}
VALID_TYPES = {"hard", "functional", "visual", "negative", "manufacturing"}
VALID_PRIORITIES = {"critical", "required", "preferred"}
VALID_EVIDENCE = {
    "user-confirmed",
    "official-source",
    "dimensioned-source",
    "exactly-derived",
    "calibrated-image",
    "visual-estimate",
    "proposed-default",
    "unknown",
    "conflict",
}
VALID_REQUIREMENT_STATUS = {"confirmed", "derived", "provisional", "unknown", "conflict"}

COMMON_SECTIONS = [
    "Purpose and scope",
    "Sources",
    "Research and derivation notes",
    "Overall geometry and coordinates",
    "Parameters",
    "Parts and components",
    "Requirements",
    "Interfaces and positioning",
    "Manufacturing intent",
    "Recommended attachments",
    "Assumptions and delegated choices",
    "Conflicts and blocking unknowns",
    "Limitations",
]

TTC_FIELDS = [
    "Model",
    "Task type",
    "Inputs",
    "Units",
    "Coordinate convention",
    "Overall dimensions",
    "Functional features",
    "Manufacturing assumptions",
    "Positioning/mating",
    "Paths",
    "Validation targets",
    "Assumptions",
]

SOURCE_HEADERS = ["ID", "Source", "Type", "Supports", "Notes"]
REQUIREMENT_HEADERS = [
    "ID",
    "Type",
    "Priority",
    "Requirement",
    "Value / unit",
    "Source",
    "Evidence state",
    "Status",
    "CAD mapping",
    "Validation",
]

MAPPING_RE = re.compile(
    r"\b(parameter|feature|datum|joint|occurrence|placement|assembly|snapshot|exclusion|body|part)\b",
    re.IGNORECASE,
)
VALIDATION_RE = re.compile(
    r"\b(refs|measure|align|frame|diff|snapshot|user[- ]review|source[- ]review|external[- ]review)\b"
    r"|TTC cannot verify",
    re.IGNORECASE,
)
DETERMINISTIC_RE = re.compile(r"\b(refs|measure|align|frame|diff)\b", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"<(?!https?://|br\s*/?>)[^>\n]+>", re.IGNORECASE)
ABSOLUTE_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:[A-Za-z]:[\\/]|\\\\[^\\\s]+\\[^\\\s]+|file://|\.\.[\\/]|/(?:Users|home|tmp|var|mnt|workspace)/)",
    re.IGNORECASE,
)


@dataclass
class Report:
    path: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    facts: dict[str, object] = field(default_factory=dict)

    @property
    def valid(self) -> bool:
        return not self.errors

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)

    def as_dict(self) -> dict[str, object]:
        return {
            "path": self.path,
            "valid": self.valid,
            "errors": self.errors,
            "warnings": self.warnings,
            "facts": self.facts,
        }


def clean_cell(value: str) -> str:
    return value.strip().strip("`").strip()


def split_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [clean_cell(cell.replace(r"\|", "|")) for cell in re.split(r"(?<!\\)\|", value)]


def is_separator_row(cells: Iterable[str]) -> bool:
    cells = list(cells)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def extract_metadata(text: str) -> dict[str, str]:
    wanted = {
        "Contract version",
        "Status",
        "Intent level",
        "Suggested basename",
        "Target",
        "Task type",
        "Primary output",
        "Secondary outputs",
        "Question rounds used",
        "Research performed",
    }
    metadata: dict[str, str] = {}
    for match in re.finditer(r"(?m)^- ([A-Za-z ]+):\s*(.*?)\s*$", text):
        key, value = match.group(1), clean_cell(match.group(2))
        if key in wanted and key not in metadata:
            metadata[key] = value
    return metadata


def find_section_headings(text: str) -> list[tuple[str, int, int]]:
    headings: list[tuple[str, int, int]] = []
    in_fence = False
    fence_char = ""
    fence_length = 0
    offset = 0
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        fence = re.match(r"(`{3,}|~{3,})", stripped)
        if fence:
            marker = fence.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_length = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_length:
                in_fence = False
                fence_char = ""
                fence_length = 0
        elif not in_fence:
            heading = re.match(r"## ([^\r\n]+)\s*$", line)
            if heading:
                headings.append((heading.group(1).strip(), offset, offset + heading.end()))
        offset += len(line)
    return headings


def extract_sections(text: str) -> tuple[dict[str, str], list[str], list[str]]:
    matches = find_section_headings(text)
    sections: dict[str, str] = {}
    order: list[str] = []
    duplicates: list[str] = []
    for index, (name, _heading_start, heading_end) in enumerate(matches):
        start = heading_end
        end = matches[index + 1][1] if index + 1 < len(matches) else len(text)
        if name not in sections:
            sections[name] = text[start:end].strip()
            order.append(name)
        else:
            duplicates.append(name)
    return sections, order, duplicates


def parse_table(section: str, expected_headers: list[str]) -> tuple[list[dict[str, str]], str | None]:
    lines = [line for line in section.splitlines() if line.strip().startswith("|")]
    for index in range(len(lines) - 1):
        headers = split_row(lines[index])
        separator = split_row(lines[index + 1])
        if headers == expected_headers and is_separator_row(separator):
            rows: list[dict[str, str]] = []
            for line in lines[index + 2 :]:
                cells = split_row(line)
                if len(cells) != len(headers) or is_separator_row(cells):
                    continue
                rows.append(dict(zip(headers, cells)))
            return rows, None
    return [], f"expected Markdown table header not found: {' | '.join(expected_headers)}"


def empty_or_placeholder(value: str) -> bool:
    normalized = value.strip().lower()
    return not normalized or normalized in {"none", "n/a", "na", "-"} or bool(PLACEHOLDER_RE.search(value))


def validate(path: Path) -> Report:
    report = Report(str(path))
    try:
        text = path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        report.error(f"cannot read UTF-8 Markdown: {exc}")
        return report

    if path.name.lower().endswith(".cad-requirements.md") is False:
        report.error("filename must end with .cad-requirements.md")

    if not re.search(r"(?m)^# CAD Requirements Contract\s*$", text):
        report.error("missing exact title '# CAD Requirements Contract'")

    if "<!--" in text or "-->" in text:
        report.error("template HTML comments remain; remove all template instructions")
    placeholders = PLACEHOLDER_RE.findall(text)
    if placeholders:
        report.error(f"unresolved angle-bracket placeholders remain: {', '.join(placeholders[:5])}")

    initial_headings = find_section_headings(text)
    metadata_scope = text[: initial_headings[0][1]] if initial_headings else text
    metadata = extract_metadata(metadata_scope)
    required_metadata = [
        "Contract version",
        "Status",
        "Intent level",
        "Suggested basename",
        "Target",
        "Task type",
        "Primary output",
        "Secondary outputs",
        "Question rounds used",
        "Research performed",
    ]
    for key in required_metadata:
        if key not in metadata or not metadata[key]:
            report.error(f"missing metadata: {key}")
        occurrences = re.findall(rf"(?m)^- {re.escape(key)}:\s*.*$", metadata_scope)
        if len(occurrences) > 1:
            report.error(f"duplicate metadata key: {key}")

    status = metadata.get("Status", "").lower()
    intent = metadata.get("Intent level", "").lower()
    task_type = metadata.get("Task type", "").lower()
    research = metadata.get("Research performed", "").lower()
    basename = metadata.get("Suggested basename", "")

    if metadata.get("Contract version") and metadata["Contract version"] != "1":
        report.error("Contract version must be 1")

    if status and status not in VALID_STATUS:
        report.error(f"invalid Status: {status}")
    if intent and intent not in VALID_INTENT:
        report.error(f"invalid Intent level: {intent}")
    if task_type and task_type not in VALID_TASK:
        report.error(f"invalid Task type: {task_type}")
    if research and research not in VALID_RESEARCH:
        report.error(f"invalid Research performed value: {research}")
    if metadata.get("Primary output", "").upper() != "STEP":
        report.error("Primary output must be STEP")

    if basename:
        if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", basename):
            report.error("Suggested basename must use lowercase letters, digits, hyphens, or underscores")
        expected_name = f"{basename}.cad-requirements.md"
        if path.name != expected_name:
            report.warn(f"filename does not match Suggested basename; expected {expected_name}")

    rounds_raw = metadata.get("Question rounds used", "")
    try:
        rounds = int(rounds_raw)
        if rounds not in {0, 1, 2}:
            report.error("Question rounds used must be 0, 1, or 2")
    except ValueError:
        if rounds_raw:
            report.error("Question rounds used must be an integer")

    if ABSOLUTE_PATH_RE.search(text):
        report.error("session-specific absolute path found; use portable filenames or URLs")

    if re.search(r"#[ofevs]\d", text, re.IGNORECASE):
        report.warn("preselected STEP selector found; discover selectors after generation instead")

    sections, order, duplicate_sections = extract_sections(text)
    for name in duplicate_sections:
        report.error(f"duplicate section: ## {name}")
    for name in COMMON_SECTIONS:
        if name not in sections:
            report.error(f"missing required section: ## {name}")
        elif not sections[name].strip():
            report.error(f"empty required section: ## {name}")

    positions = [order.index(name) for name in COMMON_SECTIONS if name in order]
    if positions != sorted(positions):
        report.error("common sections are not in the required order")

    sources: list[dict[str, str]] = []
    if "Sources" in sections:
        sources, table_error = parse_table(sections["Sources"], SOURCE_HEADERS)
        if table_error:
            report.error(f"Sources: {table_error}")
        if not sources:
            report.error("Sources table must contain at least one source row")

    declared_sources: set[str] = set()
    for row in sources:
        source_id = row["ID"]
        if not re.fullmatch(r"SRC-\d{3}", source_id):
            report.error(f"invalid source ID: {source_id or '<empty>'}")
        elif source_id in declared_sources:
            report.error(f"duplicate source ID: {source_id}")
        else:
            declared_sources.add(source_id)
        for key in ("Source", "Type", "Supports"):
            if empty_or_placeholder(row[key]):
                report.error(f"{source_id or 'source row'} has empty {key}")

    requirements: list[dict[str, str]] = []
    if "Requirements" in sections:
        requirements, table_error = parse_table(sections["Requirements"], REQUIREMENT_HEADERS)
        if table_error:
            report.error(f"Requirements: {table_error}")
        if not requirements:
            report.error("Requirements table must contain at least one requirement row")

    seen_requirements: set[str] = set()
    for row in requirements:
        req_id = row["ID"]
        req_type = row["Type"].lower()
        priority = row["Priority"].lower()
        evidence = row["Evidence state"].lower()
        req_status = row["Status"].lower()

        if not re.fullmatch(r"REQ-\d{3}", req_id):
            report.error(f"invalid requirement ID: {req_id or '<empty>'}")
        elif req_id in seen_requirements:
            report.error(f"duplicate requirement ID: {req_id}")
        else:
            seen_requirements.add(req_id)

        if req_type not in VALID_TYPES:
            report.error(f"{req_id}: invalid Type '{row['Type']}'")
        if priority not in VALID_PRIORITIES:
            report.error(f"{req_id}: invalid Priority '{row['Priority']}'")
        if evidence not in VALID_EVIDENCE:
            report.error(f"{req_id}: invalid Evidence state '{row['Evidence state']}'")
        if req_status not in VALID_REQUIREMENT_STATUS:
            report.error(f"{req_id}: invalid Status '{row['Status']}'")
        if evidence == "unknown" and req_status != "unknown":
            report.error(f"{req_id}: unknown evidence must use unknown requirement status")
        if evidence == "conflict" and req_status != "conflict":
            report.error(f"{req_id}: conflict evidence must use conflict requirement status")

        source_refs = set(re.findall(r"SRC-\d{3}", row["Source"]))
        if not source_refs:
            report.error(f"{req_id}: Source must cite at least one SRC-###")
        for source_id in source_refs - declared_sources:
            report.error(f"{req_id}: cites undeclared source {source_id}")

        if priority in {"critical", "required"}:
            if empty_or_placeholder(row["Requirement"]):
                report.error(f"{req_id}: requirement text is empty")
            if empty_or_placeholder(row["CAD mapping"]) or not MAPPING_RE.search(row["CAD mapping"]):
                report.error(f"{req_id}: critical/required CAD mapping is missing or unsupported")
            if empty_or_placeholder(row["Validation"]) or not VALIDATION_RE.search(row["Validation"]):
                report.error(f"{req_id}: critical/required validation is missing or unsupported")

        combined = " ".join(row.values())
        if "align" in row["Validation"].lower() and not re.search(r"\b(flush|center|centered)\b", combined, re.IGNORECASE):
            report.warn(f"{req_id}: align is intended for flush/center checks; clarify the relation")
        if "diff" in row["Validation"].lower() and task_type != "modification":
            report.warn(f"{req_id}: diff is normally relevant only to modification tasks")
        if req_type in {"hard", "functional", "manufacturing"}:
            if "snapshot" in row["Validation"].lower() and not DETERMINISTIC_RE.search(row["Validation"]):
                if "external review" not in row["Validation"].lower():
                    report.error(f"{req_id}: non-visual requirement cannot rely on snapshot alone")

        if status == "ready" and (req_type == "hard" or priority == "critical"):
            if req_status not in {"confirmed", "derived"}:
                report.error(
                    f"{req_id}: ready package requires hard/critical status confirmed or derived, got {req_status}"
                )
        if status == "provisional" and priority == "critical" and req_type in {
            "hard",
            "functional",
            "manufacturing",
        } and req_status in {"unknown", "conflict"}:
            report.error(f"{req_id}: provisional package leaves a critical controlling requirement unresolved")

        if req_status in {"provisional", "unknown", "conflict"}:
            disclosure = "\n".join(
                (
                    sections.get("Assumptions and delegated choices", ""),
                    sections.get("Conflicts and blocking unknowns", ""),
                )
            )
            if req_id not in disclosure:
                report.error(f"{req_id}: {req_status} requirement is not disclosed in assumptions/conflicts")

    if status in {"ready", "provisional"}:
        for name in ("TTC CAD brief", "Copy prompt for TTC"):
            if name not in sections:
                report.error(f"{status} package must include ## {name}")
            elif not sections[name].strip():
                report.error(f"{status} package has empty ## {name}")
        if "TTC handoff withheld" in sections:
            report.error(f"{status} package must not include TTC handoff withheld")

        brief = sections.get("TTC CAD brief", "")
        if brief and "CAD brief:" not in brief:
            report.error("TTC CAD brief section must contain 'CAD brief:'")
        for field_name in TTC_FIELDS:
            if not re.search(rf"(?m)^- {re.escape(field_name)}:\s*\S", brief):
                report.error(f"TTC CAD brief missing field: {field_name}")
        inputs_match = re.search(r"(?m)^- Inputs:\s*(.+)$", brief)
        if inputs_match and basename and f"{basename}.cad-requirements.md" not in inputs_match.group(1):
            report.error("TTC Inputs must name the requirements package")
        paths_match = re.search(r"(?m)^- Paths:\s*(.+)$", brief)
        if paths_match:
            paths_value = paths_match.group(1)
            if ".py" not in paths_value or ".step" not in paths_value:
                report.error("TTC Paths must name both relative .py and .step targets")
            if basename and (f"{basename}.py" not in paths_value or f"{basename}.step" not in paths_value):
                report.error("TTC Paths must use the Suggested basename for .py and .step")

        validation_targets_match = re.search(r"(?m)^- Validation targets:\s*(.+)$", brief)
        validation_targets = validation_targets_match.group(1) if validation_targets_match else ""
        if validation_targets and "refs" not in validation_targets.lower():
            report.error("TTC Validation targets must include refs")
        if validation_targets and "snapshot" not in validation_targets.lower():
            report.error("TTC Validation targets must include snapshot")

        traced_ids = {
            row["ID"]
            for row in requirements
            if row["Type"].lower() in {"hard", "negative"}
            or row["Priority"].lower() == "critical"
        }
        for req_id in sorted(traced_ids):
            if req_id not in validation_targets:
                report.error(f"TTC Validation targets omit controlling requirement {req_id}")

        used_methods: set[str] = set()
        for row in requirements:
            for method in ("refs", "measure", "align", "frame", "diff", "snapshot"):
                if re.search(rf"\b{method}\b", row["Validation"], re.IGNORECASE):
                    used_methods.add(method)
        for method in sorted(used_methods):
            if method not in validation_targets.lower():
                report.error(f"TTC Validation targets omit ledger validation method: {method}")

        assumptions_match = re.search(r"(?m)^- Assumptions:\s*(.+)$", brief)
        assumptions_value = assumptions_match.group(1) if assumptions_match else ""
        for row in requirements:
            if row["Status"].lower() == "provisional" and row["ID"] not in assumptions_value:
                report.error(f"TTC Assumptions omit provisional requirement {row['ID']}")

        prompt = sections.get("Copy prompt for TTC", "")
        prompt_requirements = {
            "$cad": r"\$cad\b",
            "requirements filename": re.escape(f"{basename}.cad-requirements.md") if basename else r"\.cad-requirements\.md",
            "gen_step()": r"gen_step\(\)",
            "STEP": r"\bSTEP\b",
            "baseline refs": r"refs\s+--facts\s+--planes\s+--positioning",
            "snapshot": r"\bsnapshot\b",
            "passed": r"\bpassed\b",
            "failed": r"\bfailed\b",
            "not verified": r"\bnot[ -]verified\b",
        }
        for label, pattern in prompt_requirements.items():
            if not re.search(pattern, prompt, re.IGNORECASE):
                report.error(f"Copy prompt for TTC missing required instruction: {label}")
        if status == "provisional" and "provisional" not in prompt.lower():
            report.error("provisional Copy prompt for TTC must state provisional")
    elif status == "blocked":
        if "TTC CAD brief" in sections or "Copy prompt for TTC" in sections:
            report.error("blocked package must omit TTC CAD brief and Copy prompt for TTC")
        if "TTC handoff withheld" not in sections:
            report.error("blocked package must include ## TTC handoff withheld")
        conflicts = sections.get("Conflicts and blocking unknowns", "")
        if not re.search(r"(?m)^- BLOCKER:", conflicts):
            report.error("blocked package must include at least one '- BLOCKER:' line")

    report.facts = {
        "status": status or None,
        "intent_level": intent or None,
        "question_rounds_used": metadata.get("Question rounds used") or None,
        "sources": len(sources),
        "requirements": len(requirements),
    }
    return report


def print_text(report: Report) -> None:
    outcome = "PASS" if report.valid else "FAIL"
    print(f"{outcome}: {report.path}")
    for message in report.errors:
        print(f"ERROR: {message}")
    for message in report.warnings:
        print(f"WARNING: {message}")
    if report.facts:
        facts = ", ".join(f"{key}={value}" for key, value in report.facts.items())
        print(f"FACTS: {facts}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a cad-brief .cad-requirements.md handoff package."
    )
    parser.add_argument("path", type=Path, help="Requirements Markdown file")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as validation failures",
    )
    args = parser.parse_args()

    report = validate(args.path)
    if args.format == "json":
        print(json.dumps(report.as_dict(), ensure_ascii=False, indent=2))
    else:
        print_text(report)

    if any(message.startswith("cannot read UTF-8 Markdown") for message in report.errors):
        return 2
    if report.errors or (args.strict and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
