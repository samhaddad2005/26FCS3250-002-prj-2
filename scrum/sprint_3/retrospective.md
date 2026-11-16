Date/Time: 11/15/26, evening (asynchronous, in Slack)

Participants: Esther Finotti (Scrum Master). The rest of the team was busy finishing the release on the final day and no other responses were received before submission, so the points below are the Scrum Master's observations from the sprint and the team's Slack threads.

## Were Sprint 2's action items carried out?

1. @-mention teammates in #project2-dev when work is ready: **Partly carried out.** Updates and @-mentions in the dev channel increased (for example, US9 retesting on Nov 11 and the UI PR review request on Nov 13).
2. Post quick status updates when something is finished: **Partly carried out.** Most finished work was announced in the dev channel, but US5 and US10 slipped past the Nov 12 target without updates until Hai-Dang checked in on Nov 13.
3. Assign the tester and reviewer during sprint planning: **Carried out.** Sam was assigned as the Sprint 3 tester on Nov 10.

## What went well

- Every required story (US1 to US7) and the optional US8 and US9 were merged into dev.
- The #project2-ci channel gave an automatic, dated record of every branch, PR, and merge, which made it possible to reconstruct each sprint's progress.
- Teammates responded quickly on the final day: Hai-Dang updated the UML, Yasemin resolved the UI merge conflicts and added the Clear filters button, and Sam fixed the manual test table, all within hours of being asked.
- Testing the app the way the instructor will run it (a fresh docker compose up with no .env) caught real problems before submission.

## What didn't go well

- The team never used a Kanban board or GitHub issues; work was tracked only through in-person planning and Slack.
- The Docker files were removed early in Sprint 1 and only restored on the final day, so the deployment was not tested end to end until Nov 15.
- The UML diagrams described the planned design from Nov 2 and were not updated to match the code until the final day.
- Releases were not tagged at the end of each sprint as planned; v1, v2, and v3 were all created at the end of the project.
- US10 (optional) was not started.

## Action items (for future projects)

1. Set up a Kanban board with one GitHub issue per task in Sprint 1, and move cards as work progresses.
2. Keep the Docker deployment working from the start, and test it from a fresh clone at the end of every sprint.
3. Merge dev into main and tag the release at each sprint's end, instead of at the end of the project.
4. Update design documents (UML) whenever the implementation changes them.
5. When a fix is shared in chat, say who will push it.
