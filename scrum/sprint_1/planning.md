Date/Time: 10/27/26, after class

Participants: Sam Haddad, Hai-Dang Le, Esther Finotti, Miles Porter, Yasemin Fekadu

Goal Statement: Deliver the foundation of CampusEats: users can register and log in as a student or vendor (US1), vendors can post surplus food listings (US2), and students can browse the listings that are currently available (US3). Stretch: students can filter listings by dietary tag and location (US8).

## Sprint dates

Oct 27 - Nov 2

## Stories and assignments

| Story | Points | Owner | Depends on |
| --- | --- | --- | --- |
| US1: Register and log in | 5 | Sam Haddad | - |
| US2: Post a listing | 3 | Yasemin Fekadu | US1 |
| US3: Browse listings | 2 | Esther Finotti | US2 |
| US8: Filter listings (optional) | 2 | Yasemin Fekadu | US3 |

Planned: 12 points (team capacity: 12 points per sprint).

Testers: Miles Porter and Hai-Dang Le.

## Other tasks

- UML class diagram and US4 sequence diagram (Hai-Dang Le).
- Update the backlog scoring, release plan, and burndown chart with the optional stories (Esther Finotti).

## Decisions

- Sprint 0 (backlog scoring and release plan) was reviewed with Dr. Mota and approved.
- The due date moved to Nov 15, so capacity was raised from 10 to 12 points per sprint and the optional stories were added to the plan: US8 in Sprint 1, US9 in Sprint 2, US10 in Sprint 3.
- US2 and US3 wait for Sam's go-ahead once the US1 PR is ready for testing and approval.
- Everyone who works on the project posts a daily scrum in #daily-scrum.

## Task tracking

The team did not keep a separate Kanban board. Stories were assigned at sprint planning (in person), and work was tracked in Slack: status updates in #project2-dev and #daily-scrum, and GitHub events in #project2-ci, where the GitHub bot posted each event as it happened. Those bot posts map to the board columns as follows:

| Column | Evidence in #project2-ci |
| --- | --- |
| To Do | Story assigned at sprint planning (see above) |
| In Progress | "Branch created" |
| In Review | "Pull request opened" (reviewers and tester assigned) |
| Done | "Pull request merged" into dev |

Status at the end of Sprint 1 (Nov 2), from the bot posts:

| Column | Work |
| --- | --- |
| Done | US1 (#3, merged Oct 29), US2 (#5, merged Nov 2), US3 (#9, merged Nov 2), US3 Selenium tests (#10, merged Nov 2) |
| In Review | US1 tests (#4), US2 manual tests (#6), Sprint 0 backlog update (#7), UML diagrams (#8) |
| To Do | US8 (carried over to Sprint 2) |

board.png shows the #project2-ci posts for Sprint 0 and Sprint 1 (Oct 22 - Nov 2), stacked in date order from top to bottom.
