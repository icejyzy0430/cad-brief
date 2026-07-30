from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "cad-brief" / "scripts" / "validate_handoff.py"
FIXTURES = ROOT / "tests" / "fixtures"

# Test discovery imports the validator before the package-cleanliness test runs.
# Prevent that import from creating a cache inside the skill under test.
sys.dont_write_bytecode = True
SPEC = importlib.util.spec_from_file_location("cad_brief_validate_handoff", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class ValidateHandoffTests(unittest.TestCase):
    def fixture(self, state: str, name: str) -> Path:
        return FIXTURES / state / name

    def test_ready_fixture_passes(self) -> None:
        report = VALIDATOR.validate(
            self.fixture("ready", "mounting_plate.cad-requirements.md")
        )
        self.assertTrue(report.valid, report.errors)
        self.assertEqual(report.facts["status"], "ready")

    def test_provisional_fixture_passes(self) -> None:
        report = VALIDATOR.validate(
            self.fixture("provisional", "camera_body.cad-requirements.md")
        )
        self.assertTrue(report.valid, report.errors)
        self.assertEqual(report.facts["status"], "provisional")

    def test_blocked_fixture_passes_without_launch_prompt(self) -> None:
        path = self.fixture("blocked", "exact_photo_fit.cad-requirements.md")
        report = VALIDATOR.validate(path)
        self.assertTrue(report.valid, report.errors)
        self.assertEqual(report.facts["status"], "blocked")
        text = path.read_text(encoding="utf-8")
        self.assertNotIn("## TTC CAD brief", text)
        self.assertNotIn("## Copy prompt for TTC", text)

    def test_invalid_fixture_aggregates_errors(self) -> None:
        report = VALIDATOR.validate(
            self.fixture("invalid", "missing_prompt.cad-requirements.md")
        )
        self.assertFalse(report.valid)
        joined = "\n".join(report.errors)
        self.assertIn("Primary output must be STEP", joined)
        self.assertIn("Question rounds used must be 0, 1, or 2", joined)
        self.assertIn("ready package must include ## TTC CAD brief", joined)
        self.assertGreaterEqual(len(report.errors), 5)

    def test_isolated_json_cli(self) -> None:
        path = self.fixture("ready", "mounting_plate.cad-requirements.md")
        completed = subprocess.run(
            [sys.executable, "-I", str(SCRIPT), str(path), "--format", "json"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["valid"])
        self.assertEqual(payload["facts"]["status"], "ready")

    def test_strict_cli_passes_clean_fixture(self) -> None:
        path = self.fixture("ready", "mounting_plate.cad-requirements.md")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(path), "--strict"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout)

    def test_invalid_cli_returns_one(self) -> None:
        path = self.fixture("invalid", "missing_prompt.cad-requirements.md")
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(path)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1)

    def test_missing_file_returns_two(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), str(FIXTURES / "does-not-exist.md")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 2)

    def test_absolute_path_is_rejected(self) -> None:
        source = self.fixture("ready", "mounting_plate.cad-requirements.md")
        text = source.read_text(encoding="utf-8").replace(
            "mounting_plate.py", "C:\\private\\mounting_plate.py", 1
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mounting_plate.cad-requirements.md"
            path.write_text(text, encoding="utf-8")
            report = VALIDATOR.validate(path)
        self.assertFalse(report.valid)
        self.assertTrue(any("absolute path" in error for error in report.errors))

    def test_unresolved_template_marker_is_rejected(self) -> None:
        source = self.fixture("ready", "mounting_plate.cad-requirements.md")
        text = source.read_text(encoding="utf-8").replace(
            "Dimensioned mounting plate", "<part or assembly name>", 1
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mounting_plate.cad-requirements.md"
            path.write_text(text, encoding="utf-8")
            report = VALIDATOR.validate(path)
        self.assertFalse(report.valid)
        self.assertTrue(any("placeholder" in error for error in report.errors))

    def test_validator_has_no_network_dependency(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        for token in ("requests", "urllib.request", "http.client", "socket"):
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
