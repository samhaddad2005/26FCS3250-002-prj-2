Date/Time: 11/15/26, evening (held asynchronously in Slack on the final day, while the team finished the release)

Participants: Esther Finotti (Scrum Master, recorded the review). Sam Haddad, Yasemin Fekadu, and Hai-Dang Le took part in the #project2-dev threads that evening (reviews, merges, and fixes); Miles Porter was asked about US10.

## Sprint 3 goal

Let students view and cancel their reservations (US6) and let vendors manage their listings (US5). Optional: rate a pickup (US10). Carried over from Sprint 2: US7, US8, and US9.

## Completed (merged into dev)

| Story | Points | Merged | Notes |
| --- | --- | --- | --- |
| US8: Filter listings (optional, carried over) | 2 | Nov 10 (PR #11) | Multiple tags combined with AND logic |
| US6: View and cancel my reservations | 3 | Nov 10 (PR #16) | Manually tested by Miles, all passed |
| US7: Confirm pickup (carried over) | 3 | Nov 10 (PR #15) | Includes no-show status updates and a reservation success page |
| US9: Impact dashboard (optional, carried over) | 3 | Nov 11 (PR #17) | Date range and no-show rate added after first test |
| US5: Manage listings | 5 | Nov 15 (PR #19) | My Listings, edit, cancel, and reserved-by list; manually tested by Sam (PR #25) |

Completed: 16 points (US5, US6, US7, US8, US9). Of the 11 new points planned for Sprint 3, 8 were completed (US5 and US6); the other 8 points were US7, US8, and US9 carried over from Sprint 2.

## Not completed

- US10: Rate a pickup (optional, 3 points). Not started; dropped so the final day could go to testing and deployment.

## Team feedback

- Hai-Dang Le: the team made good progress, completing important features like US5 and US6, improving the UI, and working on testing and deployment.

## Product Owner feedback

- No Product Owner review was held before the Nov 15 deadline. The final release is submitted for grading.

## Other work

- Student-side UI redesign (PR #18, merged Nov 13).
- UML class and US4 sequence diagrams updated to match the final code (PR #8, merged Nov 15).
- Full manual test pass on Nov 15 against the Docker Compose deployment (PR #29): all US1 and US3 criteria, US8 criteria 1-2, and the US7 cancelled-code case passed.
- That test pass found three deployment problems, all fixed the same day (PR #26): the app would not start without a .env file, forms and login needed a SECRET_KEY default, and the container ran in UTC, so pickup times entered in Denver time were rejected. It also found that US8 had no Clear filters button; Yasemin added one (PR #21).
- Vendor-side UI redesign (PR #21) and the US5 manual test table fix (PR #28).
- Task board evidence: #project2-ci screenshots and a Task tracking section in each sprint's planning file (PR #20).
