# Demo video script — Release Gate (about 2 minutes)

Shot list, in the Switch room on Mattermost. Record the room, not a terminal.

## 0:00 — The room
Show the room, the agents, and `!roles`: `reviewer` (shared),
`release-manager` (exclusive). Say in one line: a human and an agent ship
a change together, the human holds the last switch.

## 0:20 — Good change
Post the good change in the room. Ask @reviewer to run the gate.
Show the in-thread report: no guide violations, tests PASS,
verdict RECOMMEND PASS. Note on screen: the gate recommends only.

## 0:50 — Human approve
A human posts approve in the thread. The exclusive release-manager logs
the decision (see `switch/decision-log-example.md` for the format).
No second agent can log the same release, because the job is exclusive.

## 1:10 — Bad change
Post the bad change. Ask @reviewer to run the gate.
Show the in-thread report: BLOCK — failing test + hard-coded secret.
No approval path is offered, nothing is merged or deployed.

## 1:40 — Why Switch is central
Without the room there is no shared reviewer job, no exclusive
release-manager, and no in-thread decision log. A lone agent in a
terminal can run `gate/gate.py`, but it cannot be the team's gate.

## End card
Repo: https://github.com/amanrane28coder/Release-Gate
Run it: `sh scripts/demo.sh` — good passes, bad blocks.
