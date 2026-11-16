Date/Time: 11/10/26, after class (held after the Sprint 2 review and retrospective)

Participants: Sam Haddad, Hai-Dang Le, Miles Porter, Yasemin Fekadu (Esther Finotti absent: school trip to KubeCon; assignment confirmed in #project2-dev that evening)

Goal Statement: Students can see and cancel their reservations (US6), and vendors can edit or cancel their listings and see who reserved them (US5). Stretch: students can rate a pickup (US10). Finish US9, carried over from Sprint 2, and prepare the final release (v3).

## Sprint dates

Nov 9 - Nov 15

## Stories and assignments

| Story | Points | Owner | Depends on | Target |
| --- | --- | --- | --- | --- |
| US6: View and cancel my reservations | 3 | Hai-Dang Le | US4 | Done (merged Nov 10) |
| US9: Impact dashboard (optional, carried over) | 3 | Yasemin Fekadu | US7 | Nov 12 |
| US5: Manage listings | 5 | Esther Finotti | US2, US4 | Nov 12 |
| US10: Rate a pickup (optional) | 3 | Miles Porter | US7 | Nov 12 |

Planned: 11 new points, plus 3 points carried over from US9. US7 and US8, also carried over from Sprint 2, were merged on Nov 10.

Tester: Sam Haddad.

Stories are due Nov 12, leaving Nov 13-15 for testing, integration, documentation, and the v3 release.

## Decisions (from the Sprint 2 retrospective)

- @-mention teammates in #project2-dev when work is ready for review or testing, instead of relying on the CI bot.
- Post a quick status update in #project2-dev when something is finished.
- The sprint's tester is assigned during sprint planning (Sam Haddad for Sprint 3).

## Task tracking

The team did not keep a separate Kanban board. Stories were assigned at sprint planning (in person), and work was tracked in Slack: status updates in #project2-dev and #daily-scrum, and GitHub events in #project2-ci, where the GitHub bot posted each event as it happened. Those bot posts map to the board columns as follows:

| Column | Evidence in #project2-ci |
| --- | --- |
| To Do | Story assigned at sprint planning (see above) |
| In Progress | "Branch created" |
| In Review | "Pull request opened" (reviewers and tester assigned) |
| Done | "Pull request merged" into dev |

Status at the end of Sprint 3 (Nov 15, 9:30 PM), from the bot posts:

| Column | Work |
| --- | --- |
| Done | US7 (#15) and US8 (#11) (merged Nov 10), US6 (#16, merged Nov 10), US9 (#17, merged Nov 11), student UI (#18, merged Nov 13), US5 (#19, merged Nov 15), US5 manual tests (#25, merged Nov 15), UML diagrams (#8, merged Nov 15), manual test table fix (#28, merged Nov 15), deployment files (#26, merged Nov 15), vendor UI and Clear Filter button (#21, merged Nov 15) |
| In Review | US1, US3, US8 manual tests (#29), Scrum evidence (#20) |
| To Do | US10 (optional) |

board.png shows the #project2-ci posts for Sprint 3 (Nov 9 - Nov 15), stacked in date order from top to bottom.
