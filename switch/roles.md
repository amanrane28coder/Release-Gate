# Switch roles for the Release Gate room

## reviewer (shared)

Several agents reviewing different changes do not collide, so this job is
shared. Instruction to the agent holding it:

> Review open changes against the conventions in the shipping guide.
> Run gate/gate.py, post findings in the thread of the change, not at the
> room root. Approve nothing yourself. Say what you'd change and hand it
> back.

## release-manager (exclusive)

Two agents carrying the same release would contradict each other, so this
job is exclusive. Instruction to the agent holding it:

> Log only decisions a human has already posted in the thread. Never
> approve, merge, or deploy on your own. If you do not hold this job
> exclusively, do not log a decision. One release, one log entry, with
> the human's name, the verdict, and the gate report attached.

## Room commands (documented Switch commands)

- `!roles` — see the room's jobs and who holds each.
- `!set-alias @<agent> @<short-name>` — e.g. give the reviewer a short
  handle in this room, after checking it does not clash with another
  agent, alias, or job name.
- `!follow-ups off` — if you want every instruction to a deploy-capable
  agent to name it explicitly.

## Permissions

A new agent answers only its owner and the owner's other agents at first.
Permit the team deliberately in the agent's settings, scoped to this room,
rather than opening it everywhere. The release-manager agent in
particular takes instructions only from people who should give them.
