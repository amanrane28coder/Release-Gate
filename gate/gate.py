#!/usr/bin/env python3
"""Release Gate: reviewer check that recommends, never approves, never deploys.

Usage:
    python3 gate/gate.py --repo demo/good --guide demo/shipping-guide.md
    python3 gate/gate.py --repo demo/bad --guide demo/shipping-guide.md

Exit codes: 0 = RECOMMEND PASS (still needs a human approve in the Switch room),
            1 = BLOCK, 2 = usage / run error.

Checks, in order:
  0. Changed files (git status if a git repo, else the file list).
  1. Shipping-guide rules (regex scans of the repo, excluding .git).
     - No hard-coded secret-like tokens (AKIA..., generic api_key assignments).
     - No `TODO: ship` markers left in code.
  2. Test suite, run as a subprocess in the repo directory.
     Default: `python3 -m unittest discover -s . -q`
     Override with --test-cmd, e.g. `python3 -m pytest -q`.

Output is a short thread-ready report on stdout, plus --report to write it
to a file. This script never deploys, never merges, and never records a
human decision. In the Switch room, the human posts approve/reject and the
exclusive release-manager role logs that decision separately.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

SECRET_PATTERNS = [
    (r"AKIA[0-9A-Z]{16}", "AWS-style access key pattern"),
    (r"(?i)api[_-]?key\s*=\s*['\"][^'\"]{8,}['\"]", "hard-coded api_key assignment"),
    (r"(?i)password\s*=\s*['\"][^'\"]{4,}['\"]", "hard-coded password assignment"),
]
TODO_PATTERN = re.compile(r"TODO:\s*ship", re.IGNORECASE)


def scan_guide_rules(repo: Path) -> list[str]:
    findings = []
    for path in sorted(repo.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(errors="ignore")
        except OSError:
            continue
        rel = str(path.relative_to(repo))
        for pattern, label in SECRET_PATTERNS:
            if re.search(pattern, text):
                findings.append(f"{rel}: guide violation - {label}")
        if TODO_PATTERN.search(text):
            findings.append(f"{rel}: guide violation - TODO: ship marker left in code")
    return findings


def run_tests(repo: Path, test_cmd: str) -> tuple[bool, str]:
    try:
        proc = subprocess.run(
            test_cmd, shell=True, cwd=repo, capture_output=True, text=True, timeout=120
        )
    except subprocess.TimeoutExpired:
        return False, "tests timed out after 120s"
    tail = (proc.stdout + proc.stderr).strip().splitlines()[-5:]
    summary = "\n".join(tail) if tail else "(no test output)"
    return proc.returncode == 0, summary


def diff_summary(repo: Path) -> list[str]:
    """Changed files, from git if available, else the file list itself."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), "status", "--porcelain"],
            capture_output=True, text=True, timeout=15,
        )
        if proc.returncode == 0:
            changed = [line[3:] for line in proc.stdout.splitlines() if line.strip()]
            return changed if changed else ["(no uncommitted changes; reviewing the working tree as-is)"]
    except (OSError, subprocess.TimeoutExpired):
        pass
    return sorted(
        str(p.relative_to(repo))
        for p in repo.rglob("*")
        if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Release Gate reviewer check")
    parser.add_argument("--repo", required=True, help="Path to the change to review")
    parser.add_argument("--guide", default=None, help="Path to shipping-guide.md (checked for existence only)")
    parser.add_argument("--test-cmd", default="python3 -m unittest discover -s . -q")
    parser.add_argument("--report", default=None, help="Write the report to this file too")
    args = parser.parse_args(argv)

    repo = Path(args.repo)
    if not repo.is_dir():
        print(f"ERROR: repo not found: {repo}", file=sys.stderr)
        return 2
    if args.guide and not Path(args.guide).is_file():
        print(f"ERROR: shipping guide not found: {args.guide}", file=sys.stderr)
        return 2

    guide_findings = scan_guide_rules(repo)
    tests_ok, tests_summary = run_tests(repo, args.test_cmd)
    changed = diff_summary(repo)

    blocked = bool(guide_findings) or not tests_ok
    verdict = "BLOCK" if blocked else "RECOMMEND PASS"
    lines = [
        f"Release Gate verdict: {verdict}",
        f"Repo: {repo}",
        "",
        "Changed files:",
    ]
    lines += [f"  - {f}" for f in changed]
    lines += [
        "",
        "Guide checks:",
    ]
    if guide_findings:
        lines += [f"  - {f}" for f in guide_findings]
    else:
        lines.append("  - no guide violations found")
    lines += [
        "",
        f"Tests: {'PASS' if tests_ok else 'FAIL'}",
        "  " + tests_summary.replace("\n", "\n  "),
        "",
        "HUMAN DECISION REQUIRED: this report recommends only. "
        "It does not approve, merge, or deploy. A human must post "
        "approve/reject in the Switch room; only the exclusive "
        "release-manager role may log that decision.",
    ]
    report = "\n".join(lines)
    print(report)
    if args.report:
        Path(args.report).write_text(report + "\n")
    return 1 if blocked else 0


if __name__ == "__main__":
    raise SystemExit(main())
