Daily scrums were held asynchronously in Slack. Each weekday at noon a reminder in #daily-scrum asked: (1) what did you work on yesterday, (2) what are you working on today, (3) any blockers. Team members answered in #daily-scrum or posted status updates in #project2-dev; each note below says which channel it came from. Times are Mountain Time.

Sprint 3: Nov 9 - Nov 15.

# 11/09/26-05:52

Participants: Yasemin Fekadu, Hai-Dang Le, Miles Porter

- Yas (#project2-dev): Can start US9 now instead of waiting for US7. Agreed the team is short on time and needs to communicate more.
- Hai-Dang (#project2-dev, 9:00 PM; #daily-scrum, 9:01 PM): Yesterday: worked on US6. Today: finished implementing and manually testing US6 and opened a PR to dev. Blockers: no Sprint 3 tester or reviewer assigned yet.
- Hai-Dang (#project2-dev, 9:25 PM): Added the US2 manual test results to tests/manual-tests.md.
- Miles (#project2-dev, 11:51 PM): The US7 PR (with manual and Selenium tests) was posted Saturday and is awaiting review. Merged some PRs that had been sitting open. Added minor styling to make navigation easier during testing. Pointed out that updates were split between the CI bot channel and the dev channel.
- Miles (#daily-scrum, 11:53 PM): Yesterday: implemented US7 and its tests, plus minor styling. Today: not working. Blockers: none.

# 11/10/26-00:54

Participants: Miles Porter, Sam Haddad, Hai-Dang Le, Yasemin Fekadu, Esther Finotti

- Miles (#project2-dev): Manually tested US6; all passed. Updated the manual tests file and merged the US6 PR into dev. Found that no-show reservations were never updated in the database. At 2:09 AM: updated the US7 PR to persist no-show statuses, work with US6, add a reservation success page, and add the navigation bar to all pages.
- Sam (#project2-dev, 6:40 AM): Will review US7. Noted Selenium tests are only required for one story.
- Hai-Dang (#project2-dev, 7:47 AM): Agreed that posting quick updates in the dev channel will help coordination.
- Yas (#project2-dev, 9:13 AM): Finished US9 and opened a PR to dev; it builds on the US7 code. Offered to help with design once dev is updated.
- Sam (#project2-dev, 9:15-9:42 AM): Will test US7 and US9 together and merge them separately.
- Esther (#project2-dev, 9:25 AM): At KubeCon today; asked to be assigned US5 or US6. Agreed the team should @-mention each other in the dev channel instead of relying on the CI bot.
- Miles (#project2-dev, 9:34-9:41 AM): Wrote optional Selenium tests for US7. Warned that US9 may conflict with the updated US7.
- Sam (#project2-dev, 10:09-10:20 AM): Testing US9: the date range selection and the no-show percentage are missing.
- Yas (#project2-dev, 10:53 AM): Will fix the missing US9 criteria today.
- Sam (#project2-dev, 1:54 PM): Merged US7 into dev.
- Hai-Dang (#project2-dev, 8:18 PM): Posted the Sprint 3 assignments: Esther US5, Miles US10, Yas continues US9, Hai-Dang US6, Sam is the tester. Target for finishing stories is Nov 12, leaving time for testing and release before Nov 15.

# 11/11/26-15:07

Participants: Esther Finotti, Sam Haddad, Yasemin Fekadu

- Esther (#project2-dev): Will start US5 tonight.
- Sam (#project2-dev, 3:57 PM): Checking whether US9 is ready before retesting. At 5:24 PM: working on the login/register page UI.
- Yas (#project2-dev, 4:14 PM): Finishing the US9 fixes today. At 8:09 PM: US9 is ready for retesting.
- Sam (#project2-dev, 8:59 PM): US9 date range works; the local database had to be reset for the new column. At 10:09 PM: merged US9 into dev.

# 11/13/26-14:19

Participants: Hai-Dang Le, Yasemin Fekadu, Sam Haddad

- Hai-Dang (#project2-dev): Checked in on US5 and US10, which were targeted for Nov 12; offered help.
- Yas (#project2-dev, 3:33 PM): Working on the design implementation; will send it for review soon.
- Sam (#project2-dev, 6:41 PM): Opened a PR with the student-side UI and asked everyone to review it.

# 11/14/26-13:12

Participants: Esther Finotti

- Esther (#project2-dev): Back after being sick during the trip; starting US5. At 1:50 PM: asked Sam whether he will write the US5 tests. At 1:58 PM: flagged that the Dockerfile, docker-compose.yml, and seed script are missing from dev and need to be restored before the deadline.
- Esther (#project2-dev, 3:09 PM): US5 is implemented. Blocker: it cannot be tested in the Docker deployment until the Docker setup is restored.
- Esther (#daily-scrum, 3:13 PM): Yesterday: no project work (sick). Today: worked on US5 (manage listings) and UI features; plan to update the daily scrum logs.
