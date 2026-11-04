# Decision log example (what release-manager writes, one entry per release)

- Release: demo/good, commit to be named at demo time
- Gate report: RECOMMEND PASS — no guide violations, tests PASS
- Human decision: approve, posted in-thread by the human
- Logged by: release-manager (exclusive job holder)
- Result: decision recorded, no deploy performed by the gate

A BLOCK report is never logged as an approval. A decision is only logged
after a human has posted it in the thread.
