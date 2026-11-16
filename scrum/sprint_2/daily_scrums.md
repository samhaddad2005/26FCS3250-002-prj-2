Daily scrums were held asynchronously in Slack. Each weekday at noon a reminder in #daily-scrum asked: (1) what did you work on yesterday, (2) what are you working on today, (3) any blockers. Team members answered in #daily-scrum or posted status updates in #project2-dev; each note below says which channel it came from. Times are Mountain Time.

Sprint 2: Nov 3 - Nov 8.

# 11/04/26-05:56

Participants: Yasemin Fekadu, Sam Haddad, Hai-Dang Le, Miles Porter

- Yas (#project2-dev): Finishing US8 this morning; confirmed US4 does not depend on it. Asked for target dates per story so sprints can end on Sundays. At 8:28 AM: opened the US8 PR; multiple dietary tags are combined with AND logic, since they are restrictions rather than preferences. Offered to help with design.
- Sam (#project2-dev, 6:44 AM): Sprint 2 order is US4, then US7, then US9. Will be testing throughout and working on design; asked for help with testing. At 9:20 AM: agreed with AND logic for US8.
- Hai-Dang (#project2-dev, 11:57 AM): Working on US4; aiming to finish by midnight Thursday, Nov 5.
- Miles (#project2-dev, 1:17 PM): Has an exam tomorrow; plans to do US7 on Friday once US4 testing is done.
- Hai-Dang (#daily-scrum, 9:58 PM): Yesterday: started US4 and set up the development environment. Today: completed US4; all four initial tests passed, including the concurrency test; created a PR. Blockers: waiting for Sam's review and testing.

# 11/05/26-13:59

Participants: Miles Porter, Sam Haddad, Yasemin Fekadu, Hai-Dang Le

- Miles (#daily-scrum): Yesterday: more US1 test coverage (not pushed yet). Today: start US7 if the US4 review is done, otherwise tomorrow. Blockers: waiting on US4 testing and review.
- Sam (#project2-dev, 4:36 PM): Nearly finished testing US4. Tested the concurrency criterion by reserving the last portion from two browsers at once; only one reservation succeeded.
- Yas (#project2-dev, 4:42 PM): Offered to help with the simultaneous-reservation test.
- Sam (#project2-dev, 5:09 PM): Merged the US4 PR; Miles is clear to start US7. Asked Hai-Dang to move the US2 and US3 manual test results into tests/manual-tests.md, as the README requires one file.
- Hai-Dang (#project2-dev, 5:21 PM): Agreed to consolidate the manual tests.

# 11/06/26-00:50

Participants: Sam Haddad

- Sam (#daily-scrum): Yesterday: no project work. Today: manually tested US4. Blockers: none.

# 11/07/26-19:07

Participants: Miles Porter, Esther Finotti

- Miles (#daily-scrum): Almost done with US7; one more piece to implement, then testing, and the PR tonight.
- Esther (#project2-dev, 8:48 PM): Checked in with the team and offered to test branches or help with design.

# 11/08/26-17:04

Participants: Yasemin Fekadu, Hai-Dang Le

- Yas (#project2-dev): Asked whether US7 is done; ready to start US9 tomorrow morning.
- Hai-Dang (#project2-dev, 11:01 PM): Last day of Sprint 2. Still open: US7, US9, the Sprint Review and Retrospective, the UML diagrams, and the v2 release. Sprint 3 covers US5, US6, and US10, due Nov 15. Will work on US6, aiming for Tuesday, Nov 10. Asked the team to communicate more often, especially when stories depend on each other.
