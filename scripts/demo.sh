#!/bin/sh
# Demo: good change -> RECOMMEND PASS, bad change -> BLOCK.
# Run from the repo root. Exit 0 if both verdicts are as expected.
set -u
cd "$(dirname "$0")/.." || exit 2
echo "=== GOOD CHANGE ==="
python3 gate/gate.py --repo demo/good --guide demo/shipping-guide.md
good=$?
echo "exit=$good"
echo ""
echo "=== BAD CHANGE ==="
python3 gate/gate.py --repo demo/bad --guide demo/shipping-guide.md
bad=$?
echo "exit=$bad"
echo ""
if [ "$good" -eq 0 ] && [ "$bad" -eq 1 ]; then
  echo "DEMO OK: good passes, bad blocks"
else
  echo "DEMO FAIL: expected good=0 bad=1, got good=$good bad=$bad"
  exit 1
fi
