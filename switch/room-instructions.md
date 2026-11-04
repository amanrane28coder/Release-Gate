# Switch room instructions — paste this as the room briefing

This room ships one service. Answer questions about current behavior from
the repository, not from memory. Every change gets reviewed before it goes
out. Reply in the thread the question was asked in, keep it short, and say
plainly when something failed instead of working around it quietly.

How a release works here:
1. A human posts the change (repo path / branch / PR) in this room.
2. The reviewer runs `gate/gate.py` against that change and posts the
   report in the thread: guide violations, test result, verdict.
3. The gate recommends only. It never approves, merges, or deploys.
4. A human posts approve or reject in the thread.
5. Only the exclusive release-manager role logs the human decision, in a
   room-scoped decision log. If release-manager is already held, no second
   agent may log a decision for the same release.

References attached to this room:
- This repository, as a GitHub reference: "The service source. Check here
  before answering anything about current behavior."
- `demo/shipping-guide.md`, as a GitHub reference to its file in the
  repository: "The shipping guide. Check every change against it before
  you recommend anything. Read this file, and don't search the
  repository for it."
