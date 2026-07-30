# Text-to-CAD handoff

Use this reference to compile a `ready` or `provisional` requirements contract
into a natural-language handoff for the `earthtojake/text-to-cad` `$cad` skill.

## Contents

- [Actual TTC boundary](#actual-ttc-boundary)
- [Supported validation mapping](#supported-validation-mapping)
- [REQ-ID handling](#req-id-handling)
- [TTC CAD brief](#ttc-cad-brief)
- [Copy prompt](#copy-prompt)
- [Blocked handoff](#blocked-handoff)
- [Downstream clarification caveat](#downstream-clarification-caveat)

## Actual TTC boundary

TTC does not expose a requirements-package API and does not natively consume this
skill's custom tables. A downstream Agent reads the Markdown and writes TTC's
internal natural-language CAD brief before authoring build123d source.

Keep the rich source and requirement ledgers outside the TTC brief. The brief is
a compact compatibility layer, not a duplicate of the full research report.

TTC owns:

```text
natural-language CAD brief
→ named parameters and feature/datum plan
→ build123d Python gen_step()
→ STEP
→ deterministic inspection
→ mandatory snapshot review
→ source repair and regeneration
```

This skill owns only the evidence-backed requirements package.

## Supported validation mapping

Use only capabilities TTC actually has:

| Requirement | TTC mapping |
| --- | --- |
| overall dimensions and scale | `refs --facts`, targeted `measure` |
| solid/part/assembly count and labels | `refs --facts --positioning` |
| planes, major datums, placement-ready refs | `refs --planes --positioning` |
| distance, thickness, offset, clearance, hole position | `measure` |
| flush or centered mating relationship | `align` |
| orientation and occurrence world placement | `frame` |
| preservation after a modification | `diff` |
| visual form, silhouette, semantics, reference-image resemblance | `snapshot` plus user review |

Snapshot is diagnostic, not authoritative. Never let it override a failed
dimension or interface measurement.

TTC cannot by itself prove structural safety, FEA, thermal performance,
manufacturing certification, tolerance-system compliance, or regulatory
approval. Map those to an explicit external review or test.

## REQ-ID handling

REQ IDs are not native STEP feature identifiers. Ask the downstream Agent to
preserve them where practical in:

- Python source comments,
- parameter and feature planning,
- named feature functions or intermediate variables,
- stable datums and assembly occurrence labels,
- the final validation report.

Do not require every hole, boolean cut, fillet, face, or edge to retain a stable
REQ label through STEP export.

## TTC CAD brief

Use all fields below and preserve their labels:

```markdown
## TTC CAD brief

CAD brief:
- Model: <part or assembly name and intended fidelity>
- Task type: <new part, assembly, or modification>
- Inputs: <requirements filename and portable attachment filenames/URLs>
- Units: <explicit or assumed>
- Coordinate convention: <origin, base plane, up axis>
- Overall dimensions: <envelope and source/evidence state where important>
- Functional features: <parts, features, counts, dimensions, and negative constraints>
- Manufacturing assumptions: <only geometry-affecting assumptions and scope limits>
- Positioning/mating: <interfaces, datums, placements, joints, and alignment rules>
- Paths: `<suggested-basename>.py` generator and `<suggested-basename>.step` primary output in the TTC workspace; same stem
- Validation targets: <facts, measurements, alignments, frames, diffs, snapshots, and external reviews>
- Assumptions: <meaningful provisional choices, exclusions, and unresolved non-blockers>
```

Do not use current-session absolute paths. Give explicit relative filenames for
the future TTC workspace.

## Copy prompt

Append this section, localized to the user's language while retaining tool names
and file names:

````markdown
## Copy prompt for TTC

```text
Use $cad.

Read `<suggested-basename>.cad-requirements.md` completely, together with the
available attachments listed in Recommended attachments. Treat its `TTC CAD
brief` as the modeling contract and retain the Requirements table as the
traceability and acceptance ledger.

Before coding, make a concise plan of named parameters, parts/features,
datums/positioning, and validation targets. Do not re-guess `user-confirmed`,
`official-source`, `dimensioned-source`, or `exactly-derived` values. Make every
provisional dimension a named, replaceable parameter and report it at handoff.
Do not silently resolve a confirmed conflict or missing controlling interface.

Author build123d Python with `gen_step()`. Keep
`<suggested-basename>.py` and `<suggested-basename>.step` in the TTC workspace
with the same stem. Treat STEP as the primary validated artifact; create
secondary mesh outputs only when requested.

Preserve REQ IDs in source comments, planning, stable datum/occurrence names, and
the final validation report where practical. Do not claim that every REQ ID is a
stable STEP feature label.

After generation, run the baseline `refs --facts --planes --positioning`, then
the contract's targeted `measure`, `align`, `frame`, or `diff` checks. Run and
review the mandatory snapshot packet, including reference-matched or section
views specified by the contract. Visual review cannot override deterministic
failures.

Repair the smallest responsible source section and rerun affected checks until
the contract passes or a real blocker is reported. Finally report every critical
and required REQ as passed, failed, or not verified, plus all provisional values,
assumptions, external-review items, and limitations.
```
````

The generated prompt may be shorter when the full contract is simple, but it
must retain these rules:

- read the entire requirements file,
- respect evidence precedence,
- parameterize provisional values,
- use build123d and STEP-first output,
- run TTC's actual validation and mandatory snapshot,
- report requirement-level results and limitations.

## Blocked handoff

For status `blocked`, omit both the TTC brief and copy prompt. Use:

```markdown
## TTC handoff withheld

No `$cad` launch prompt was generated because the requested intent depends on
the blockers listed above. Clear those blockers or explicitly accept a
provisional concept scope before geometry generation.
```

This prevents a partial research document from being mistaken for an executable
modeling contract.

## Downstream clarification caveat

A strong package should reduce questions, but it cannot guarantee that TTC will
never ask another focused clarification. TTC may discover a new fit-, safety-,
compliance-, or source-critical blocker during actual modeling. Do not promise
zero downstream questions.
