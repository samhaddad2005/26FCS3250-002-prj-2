Date/Time: 11/03/26, after class (held after the Sprint 1 review and retrospective)

Participants: Sam Haddad, Hai-Dang Le, Esther Finotti, Miles Porter, Yasemin Fekadu

Goal Statement: Students can reserve portions from a listing and receive a pickup code (US4), and vendors can confirm a pickup by entering that code (US7). Stretch: vendors can see an impact dashboard (US9). Finish US8, carried over from Sprint 1.

## Sprint dates

Nov 3 - Nov 8 (ending on a Sunday, per the Sprint 1 retrospective)

## Stories and assignments

| Story | Points | Owner | Depends on | Target |
| --- | --- | --- | --- | --- |
| US8: Filter listings (optional, carried over) | 2 | Yasemin Fekadu | US3 | Nov 4 |
| US4: Reserve portions | 5 | Hai-Dang Le | US1, US3 | Nov 5 |
| US7: Confirm pickup | 3 | Miles Porter | US4 | Nov 6 |
| US9: Impact dashboard (optional) | 3 | Yasemin Fekadu | US7 | After US7 |

Planned: 11 new points, plus 2 points carried over from US8 (already in progress).

Order: US4, then US7, then US9.

Testing and review: Sam Haddad, who also works on the UI design. Yasemin Fekadu helps with design.

## Decisions (from the Sprint 1 retrospective)

- One tester's approval is enough to merge a PR, and the PR's author merges it into dev after approval.
- Each story gets a target date so the sprint ends on a Sunday.

## Task tracking

The team did not keep a separate Kanban board. Stories were assigned at sprint planning (in person), and work was tracked in Slack: status updates in #project2-dev and #daily-scrum, and GitHub events in #project2-ci, where the GitHub bot posted each event as it happened. Those bot posts map to the board columns as follows:

| Column | Evidence in #project2-ci |
| --- | --- |
| To Do | Story assigned at sprint planning (see above) |
| In Progress | "Branch created" |
| In Review | "Pull request opened" (reviewers and tester assigned) |
| Done | "Pull request merged" into dev |

Status at the end of Sprint 2 (Nov 8), from the bot posts:

| Column | Work |
| --- | --- |
| Done | US4 (#12, merged Nov 5), US4 manual tests (#14, merged Nov 5), US1 tests (#4), US2 manual tests (#6), and Sprint 0 backlog update (#7) (all three merged Nov 7) |
| In Review | US8 (#11), US7 (#15), UML diagrams (#8) |
| To Do | US9 (carried over to Sprint 3) |

board.png shows the #project2-ci posts for Sprint 2 (Nov 3 - Nov 8), stacked in date order from top to bottom.
