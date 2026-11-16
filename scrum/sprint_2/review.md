Date/Time: 11/10/26, after class (held together with the Sprint 2 retrospective)

Participants: Sam Haddad, Hai-Dang Le, Miles Porter, Yasemin Fekadu (Esther Finotti absent: school trip to KubeCon)

## Sprint 2 goal

Let students reserve portions (US4) and let vendors confirm pickups by code (US7). Optional: impact dashboard (US9). Carried over from Sprint 1: filter listings (US8).

## Completed by the end of Sprint 2 (Nov 8)

| Story | Points | Merged | Notes |
| --- | --- | --- | --- |
| US4: Reserve portions | 5 | Nov 5 (PR #12) | All four tests passed, including two students reserving the last portion at once; manual results in PR #14 |

Completed: 5 of 13 points (11 planned plus 2 carried over from US8).

## Not completed by the end of Sprint 2

| Story | Points | Status at sprint end | Outcome |
| --- | --- | --- | --- |
| US7: Confirm pickup | 3 | PR opened Nov 7 with manual and Selenium tests, awaiting review | Updated and merged Nov 10 (PR #15) |
| US8: Filter listings (optional) | 2 | PR opened Nov 4, awaiting review | Merged Nov 10 (PR #11) |
| US9: Impact dashboard (optional) | 3 | Not started; waiting on US7 | Merged Nov 11 (PR #17) |

US7, US8, and US9 were finished during Sprint 3, so their points count toward Sprint 3.

## Other work

- US2 manual test results moved into tests/manual-tests.md.
- Sprint 0 release plan update (optional stories) merged into dev (PR #7).
- Basic styling and navigation added while testing US7.
- No-show reservations found to never update in the database; fix added to the US7 PR.

## Product Owner feedback

- Dr. Mota reviewed the work after class (class starts at 2:00 PM). By then US7 had been merged into dev (1:54 PM), so both stories in the sprint goal, US4 and US7, were demonstrated.
- Dr. Mota: the work looked good and the sprint goals were met. No changes requested.

## Open items noted

- UML diagrams PR still open.
- v1 and v2 releases not yet tagged.
- Docker setup still missing from the repository.
