# Demo transcript — Release Gate in the Switch room (verified Nov 4, 2026)

Room: Mattermost team `switch`, channel `release-gate`.
Agent: `ceo` (Codex). Setup confirmed with `!roles`: reviewer shared,
release-manager exclusive, both with no holders at setup.

## Good change — demo/good

- `@ceo` assumed the `reviewer` role.
- Gate report: **RECOMMEND PASS** — no guide violations, tests PASS.
- Human posted approve in the review thread (not at the room root —
  the agent refused a root-level approve, correctly).
- `@ceo` assumed the exclusive `release-manager` role and logged:
  "Release log — Human: user · Verdict: APPROVE · Release: demo/good.
  Gate report attached. Logged by the exclusive release-manager role."
- Nothing was merged or deployed by the gate or the agent.

## Bad change — demo/bad

- `@ceo` assumed the `reviewer` role.
- Gate report: **BLOCK** — hard-coded api_key assignment in app.py,
  tests FAIL.
- Recommendation: do not ship. Remove the hard-coded API key and fix
  the failing test, then rerun the gate. No approval path was offered.

## Note

`switch-buddy-admin` is not used in this demo: it fails on an
unsupported model configured for its Codex account. `ceo` is the
working agent in this room.
