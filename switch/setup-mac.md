# Setup on the Mac (Switch + Mattermost, no Slack admin needed)

Prereqs, verified against the Switch quickstart:
- Docker, installed and running. Switch runs its server on your computer
  inside Docker. Note: as of Nov 4, 2026, Docker was NOT installed on
  Aman's Mac — install Docker Desktop first, before Switch Console.
  Update, Nov 4, 2026 22:24 IST: Docker Desktop is still NOT installed,
  but OrbStack 2.2.5 was already on the Mac and provides a Docker daemon
  (Docker 29.8.2, verified running). Launch OrbStack instead of installing
  Docker Desktop, unless Switch Console specifically requires Docker
  Desktop — that part is untested.
- An AI coding agent on the Mac: Claude Code (2.1.312 verified Nov 4),
  Codex, or OpenCode, plus a subscription or API key for it.
- Switch Console (macOS build) from the hackathon Resources page:
  https://www.wemakedevs.org/hackathons/switch/resources

Steps:
1. Register for the hackathon on
   https://www.wemakedevs.org/hackathons/switch (WeMakeDevs account),
   star the Switch repo, join the WeMakeDevs Discord.
2. Install Docker Desktop, start it, then install and start Switch
   Console. Follow the Switch quickstart until an agent answers you in
   a Switch room (about 10 minutes once Docker is running).
   Local Switch bundles Mattermost, so the demo room needs no company
   Slack workspace or admin access.
3. Copy this repo to the Mac. In Switch Console, add a Claude Code agent
   with this repo as its working directory.
4. Create a Switch room, paste `switch/room-instructions.md` as the room
   briefing, attach this repo and `demo/shipping-guide.md` as references,
   and define the `reviewer` (shared) and `release-manager` (exclusive)
   jobs from `switch/roles.md`.
5. Demo, in the room, in-thread:
   - Post the good change, ask @reviewer to run the gate: expect
     RECOMMEND PASS, then a human approve, then release-manager logs it.
   - Post the bad change, ask @reviewer to run the gate: expect BLOCK
     (failing test + hard-coded secret), and no approval path.
6. Record the demo video (screen capture of the Mattermost room + the
   gate reports), then submit repo + video + README before
   Nov 7, 2026, 11:59 PM IST. Do NOT push to a public repo until Aman
   explicitly approves the push — submission requires a public repo,
   so that approval is a separate step.
