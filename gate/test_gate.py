#!/usr/bin/env python3
"""Self-tests for gate.py. Run: python3 gate/test_gate.py"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GATE = ROOT / "gate.py"
GUIDE = ROOT.parent / "demo" / "shipping-guide.md"


def run_gate(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(GATE), "--repo", str(repo), "--guide", str(GUIDE)],
        capture_output=True, text=True,
    )


def write_repo(tmp: Path, app: str, test: str) -> Path:
    tmp.mkdir(parents=True, exist_ok=True)
    (tmp / "app.py").write_text(app)
    (tmp / "test_app.py").write_text(test)
    return tmp


GOOD_APP = "def add(a, b):\n    return a + b\n"
GOOD_TEST = (
    "import unittest\nfrom app import add\n\n"
    "class T(unittest.TestCase):\n"
    "    def test_add(self):\n        self.assertEqual(add(2, 3), 5)\n\n"
    "if __name__ == '__main__':\n    unittest.main()\n"
)
BAD_APP = "def add(a, b):\n    return a + b + 1  # wrong\n"
SECRET_APP = GOOD_APP + "\napi_key = 'supersecret123'\n"


class TestGate(unittest.TestCase):
    def test_good_passes(self):
        with tempfile.TemporaryDirectory() as d:
            repo = write_repo(Path(d), GOOD_APP, GOOD_TEST)
            proc = run_gate(repo)
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertIn("RECOMMEND PASS", proc.stdout)
            self.assertIn("HUMAN DECISION REQUIRED", proc.stdout)

    def test_failing_test_blocks(self):
        with tempfile.TemporaryDirectory() as d:
            repo = write_repo(Path(d), BAD_APP, GOOD_TEST)
            proc = run_gate(repo)
            self.assertEqual(proc.returncode, 1)
            self.assertIn("BLOCK", proc.stdout)
            self.assertIn("Tests: FAIL", proc.stdout)

    def test_secret_blocks_even_when_tests_pass(self):
        with tempfile.TemporaryDirectory() as d:
            repo = write_repo(Path(d), SECRET_APP, GOOD_TEST)
            proc = run_gate(repo)
            self.assertEqual(proc.returncode, 1)
            self.assertIn("hard-coded api_key", proc.stdout)

    def test_missing_repo_is_error_not_pass(self):
        proc = subprocess.run(
            [sys.executable, str(GATE), "--repo", "/nonexistent-repo-xyz"],
            capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
