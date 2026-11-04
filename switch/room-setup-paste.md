# Paste this to the agent in the Release Gate room (one message)

Set up this room as a release gate, using the repo at ~/switch-release-gate:

1. Room briefing — use this text for the room instructions:
"This room ships one service. Answer questions about current behavior from
the repository, not from memory. Every change gets reviewed before it goes
out. Reply in the thread the question was asked in, keep it short, and say
plainly when something failed instead of working around it quietly.
The gate recommends only. It never approves, merges, or deploys.
A human posts approve or reject in the thread. Only the exclusive
release-manager role logs that decision."

2. Define a SHARED job `reviewer` with these instructions:
"Review open changes against the conventions in the shipping guide.
Run gate/gate.py, post findings in the thread of the change, not at the
room root. Approve nothing yourself. Say what you'd change and hand it
back."

3. Define an EXCLUSIVE job `release-manager` with these instructions:
"Log only decisions a human has already posted in the thread. Never
approve, merge, or deploy on your own. If you do not hold this job
exclusively, do not log a decision. One release, one log entry, with
the human's name, the verdict, and the gate report attached."

4. Attach references: this repository ("The service source. Check here
before answering anything about current behavior.") and
demo/shipping-guide.md ("The shipping guide. Check every change against
it before you recommend anything. Read this file, and don't search the
repository for it.")

Then confirm with `!roles` that reviewer is shared and release-manager
is exclusive, and that you are holding neither job until asked.
