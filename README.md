# Release Gate — Flip the Switch, Track 1: Best Business Workflow

A workflow where a human and an AI agent ship a change together, in a
team chat, with the human holding the last switch.

## What it does

A human posts a change in a Switch room (Mattermost, bundled with local
Switch — no Slack admin needed). A reviewer agent runs the gate and posts
a report in-thread. The gate recommends only. A human approves or
rejects. Only the exclusive release-manager role logs that decision.

This is the whole point: without Switch, there is no room, no shared
reviewer job, no exclusive release-manager, and no in-thread decision
log. A lone agent in a terminal can run the same script, but it cannot
be the team's gate.

## How Switch is used

- **Agent:** Codex (ceo), via Switch Console, with this repo as its
  working directory. It runs `gate/gate.py` when asked in the room.
- **Channel:** a Switch room on Mattermost (local Switch server in
  Docker). Room briefing: `switch/room-instructions.md`.
- **Roles:** `reviewer` (shared) and `release-manager` (exclusive),
  defined in `switch/roles.md`. The reviewer approves nothing itself;
  the release-manager logs only human-posted decisions.
- **References:** this repo (source of truth for current behavior) and
  `demo/shipping-guide.md` (the rulebook every change is checked
  against).

## Run it (no Switch needed, for the gate itself)

```sh
sh scripts/demo.sh
# good change -> RECOMMEND PASS (exit 0)
# bad change  -> BLOCK, failing test + hard-coded secret (exit 1)

python3 gate/gate.py --repo demo/good --guide demo/shipping-guide.md
python3 gate/gate.py --repo demo/bad --guide demo/shipping-guide.md
python3 gate/test_gate.py
```

Gate exit codes: 0 = recommend pass (human approve still required),
1 = block, 2 = run error. The gate never deploys, merges, or approves.

## Full Switch setup

See `switch/setup-mac.md`. Short version: OrbStack + Switch
Console + Codex (ceo) on macOS, create the room, paste the briefing,
define the two jobs, demo good-then-bad in-thread.

## Submission checklist

- [x] Public repo: https://github.com/amanrane28coder/Release-Gate
- [ ] Demo video of the workflow running in the Switch room
- [ ] This README, explaining Switch use (agents, channel, how to run)
- [ ] Submitted before Nov 7, 2026, 11:59 PM IST
