# Paste this to switch-buddy in Switch Console (not in Mattermost yet)

You are my Switch assistant. Set up the Release Gate room for me, and
confirm each step before you create anything:

1. Create a room called "Release Gate" on Mattermost, add me, and add my
   Codex agent (ceo) (replace this with its registered name from Your
   Agents: @YOUR-AGENT-NAME). The agent's working directory is
   ~/switch-release-gate.
2. Set the room briefing to the text in switch/room-instructions.md.
3. Define a SHARED job `reviewer` and an EXCLUSIVE job `release-manager`
   exactly as in switch/roles.md.
4. Attach references: this repository, and demo/shipping-guide.md.
5. Restrict who can edit the room to me and admins only.
6. Confirm with `!roles` that reviewer is shared and release-manager is
   exclusive, and tell me the room's Mattermost channel name.

After that, I will demo in that channel: good change, human approve,
release-manager log, then bad change blocked.
