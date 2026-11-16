Daily scrums were held asynchronously in Slack. Each weekday at noon a reminder in #daily-scrum asked: (1) what did you work on yesterday, (2) what are you working on today, (3) any blockers. Team members answered in #daily-scrum or posted status updates in #project2-dev; each note below says which channel it came from. Times are Mountain Time.

Sprint 0 (planning): Oct 22 - Oct 26. Sprint 1: Oct 27 - Nov 2.

## Sprint 0 (planning)

# 10/22/26-17:54

Participants: Esther Finotti, Sam Haddad

- Esther (#project2-dev): Posted the draft backlog scoring (priority = user value / story points) and release plan (capacity 10 points per sprint, required stories US1-US7). Asked everyone to confirm the estimates, their weekly hours, and whether to attempt US8. Shared the first draft of the burndown chart at 7:11 PM.
- Esther (#daily-scrum): Set up the daily scrum channel and the weekday noon reminder.
- Sam (#project2-dev, 8:40 PM): Asked about the rank order; can commit 7-9 hours per week; agrees with the plan.

# 10/23/26-22:24

Participants: Hai-Dang Le

- Hai-Dang (#project2-dev): Story point estimates look reasonable; can commit 7-9 hours per week; suggested attempting US8 for the bonus.

# 10/25/26-21:56

Participants: Hai-Dang Le

- Hai-Dang (#project2-dev): Shared a draft task plan spreadsheet (tasks, dependencies, owners, proposed dates) based on the release plan. Proposed compressed 6/4/4-day sprints to fit the original Nov 8 deadline. Volunteered for the UML class and sequence diagrams and US1 testing, and to help test US2 and US3.

# 10/26/26-09:31

Participants: Sam Haddad, Yasemin Fekadu

- Sam (#project2-dev): Setting up the project files (models, classes, and shared setup) so the user stories are easier to build.
- Yas (#project2-dev, 5:59 PM): Will start US2 tomorrow, or as soon as US1 is done.

## Sprint 1

# 10/27/26-13:28

Participants: Sam Haddad, Esther Finotti

- Sam (#project2-dev): Finished the basic project setup and most of US1. Docker files and Docker Compose still need to be added later. Asked everyone to look at the models before starting their stories. At 3:33 PM: US1 still needs the role options.
- Esther (#daily-scrum, 6:38 PM): Yesterday: no project work. Today: in class the team reviewed the burndown chart and backlog priority chart with Dr. Mota, passed Sprint 0, confirmed the new due date, and assigned Sprint 1 roles. Tonight: add US8, US9, and US10 to the sprint plan. Blockers: none.
- Esther (#project2-dev, 6:45 PM): Posted the Sprint 1 assignments: US1 Sam, US2 Yas, US3 Esther, US8 Yas, testers Miles and Hai-Dang. US8 added to Sprint 1, US9 to Sprint 2, US10 to Sprint 3.

# 10/28/26-00:37

Participants: Sam Haddad, Hai-Dang Le, Yasemin Fekadu

- Sam (#project2-dev): US1 is done. Decided each person will add their own story's model fields to keep collaboration realistic.
- Hai-Dang (#daily-scrum, 12:03 PM): Yesterday: completed the UML class diagram and started the US4 sequence diagram. Today: continue the sequence diagram. Blockers: none.
- Yas (#project2-dev, 2:07 PM): Starting US2 later today.
- Sam (#daily-scrum, 8:21 PM): Yesterday: no project work. Today: finished US1 and attended the scrum meeting. Blockers: none.

# 10/29/26-08:47

Participants: Yasemin Fekadu, Sam Haddad, Esther Finotti, Hai-Dang Le

- Yas (#project2-dev): Blocked: the US1 PR had Miles's approval but Hai-Dang's review was still pending, so US2 could not start. Concerned about finishing US2, US3, and US8 by Sunday.
- Sam (#project2-dev, 9:16 AM): One tester's approval is enough to merge. Offered to help with US8 if needed. (Blocker resolved.)
- Yas (#project2-dev, 10:54 AM): About 80% done with US2.
- Yas (#daily-scrum, 8:11 PM): Yesterday: reviewed Sam's code to learn the setup. Today: finished US2, tested the food listing feature, and opened a PR to dev. Blockers: none.
- Esther (#project2-dev, 10:11 PM): Starting US3 tomorrow.
- Hai-Dang (#project2-dev, 11:05 PM): Finished manual testing for US2; all tested cases passed and are documented in PR #6. Server-side portion validation and the Docker Compose deployment still need to be verified.

# 10/30/26-13:05

Participants: Miles Porter

- Miles (#daily-scrum): Limited availability today. Will work on US1 test coverage tonight, then check what testing is needed tomorrow.

# 10/31/26-15:52

Participants: Esther Finotti

- Esther (#project2-dev): Was busy last night; working on US3 today.
- Esther (#daily-scrum, 5:42 PM): Yesterday: no project work. Today: update the Sprint 0 backlog and release plan with the optional stories, since the due date moved back a week, and share it for approval; then work on US3 so Yas can start US8. Blockers: none.

# 11/01/26-11:35

Participants: Hai-Dang Le, Esther Finotti, Yasemin Fekadu

- Hai-Dang (#daily-scrum): Yesterday: reviewed US3. Today: write the Selenium tests for US3. Blockers: none.
- Esther (#project2-dev, 3:36 PM): Updated the sprint-0 branch with the new sprint plan. The US3 implementation plan is ready. Blocked: US3 needs US2 merged into dev first.
- Hai-Dang (#project2-dev, 3:47 PM): Confirmed US2 was tested and approved. Asked for the US3 page URL and selectors so the Selenium tests match.
- Esther (#project2-dev, 3:56 PM): Shared the US3 URLs, selectors, and empty-state behavior with Hai-Dang.
- Yas (#project2-dev, 4:18 PM): Will merge the US2 PR. Can start US8 today but may not finish because of other homework.
- Esther (#project2-dev, 4:41 PM): Proposed a short meeting after Tuesday's class to assign Sprint 2 work. Hai-Dang agreed at 6:08 PM.

# 11/02/26-12:42

Participants: Hai-Dang Le, Miles Porter, Esther Finotti

- Hai-Dang (#project2-dev): Finished writing the US3 Selenium tests and is preparing test data; waiting for the US3 implementation.
- Miles (#project2-dev, 4:19 PM): Agreed to the Sprint 2 planning meeting.
- Esther (#project2-dev, 5:49 PM): Working on US3 now. At 7:44 PM: US3 is ready for testing (PR #9).
- Hai-Dang (#daily-scrum, 10:13 PM): Yesterday: worked on the US3 Selenium tests. Today: finished all 7 test cases and merged PR #10 into dev. All tests passed individually; TC07 needs a separate empty-data setup. Blockers: none.
