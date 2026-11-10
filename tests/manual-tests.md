| User story | Acceptance criterion | Tester | Date | Result | Notes |
|---|---|---|---|---|---|
| US2 | TC01: Vendor creates a valid food listing | Hai Dang Nguyen Le | 10/29/2026 | Passed | Listing saved in PostgreSQL |
| US2 | TC02: Student cannot access listing creation | Hai Dang Nguyen Le | 10/29/2026 | Passed | Access restriction verified |
| US2 | TC03: Required fields cannot be empty | Hai Dang Nguyen Le | 10/29/2026 | Passed | Required field validation |
| US2 | TC04: Pickup end must be after pickup start | Hai Dang Nguyen Le | 10/29/2026 | Passed | Pickup time validation |
| US2 | TC05: Pickup end must be in the future | Hai Dang Nguyen Le | 10/29/2026 | Passed | Pickup time validation |
| US2 | TC06: Portions cannot be less than 1 | Hai Dang Nguyen Le | 10/29/2026 | Passed | Browser validation only; server-side not verified |
| US2 | TC07: Portions cannot exceed 100 | Hai Dang Nguyen Le | 10/29/2026 | Passed | Browser validation only; server-side not verified |
| US2 | TC08: Portions = 1 | Hai Dang Nguyen Le | 10/29/2026 | Passed | Reported in original test results |
| US2 | TC09: Portions = 100 | Hai Dang Nguyen Le | 10/29/2026 | Passed | Reported in original test results |
| US4 | 1: Reservation is stored, portion decreases, and see a unique 6 number digit | Sam Haddad | 11/05/2026 | Passed | All criterion were satisfied, I was able to generate that code, save my listing and see portions decrease |
| US4 | 2: if reservation is > portion then I should see an error | Sam Haddad | 11/05/2026 | Passed | All criterion were satisfied, I wanted to reserve 2 but only 1 was remaining and I got an error message |
| US4 | 3: if I have active reservation for a listing when I try to reserve it again, then I am told I already have a reservation. | Sam Haddad | 11/05/2026 | Passed | All criterion were satisfied, I was not able to reserve it and got the message that I already have it |
| US4 | 3: if there's 1 portion left and 2 users click on it at the same time only one works the second shows an error and never goes below 0 | Sam Haddad | 11/05/2026 | Passed | All criterion were satisfied, I opened one browser in vscode the other in chrome and clicked reserve as fast as possible 1 reserved the other got no portions left error but never went negative |
| US6 | 1: View My Reservations | Miles Porter | 11/10/2026 | Passed | Environment: Local Flask application, port 5001. Logged in as a student and navigated to My Reservations. Verified that reservations displayed the correct listing title, vendor, pickup location, pickup window, portion count, pickup code, and status. |
| US6 | 2: Cancel an Eligible Reservation | Miles Porter | 11/10/2026 | Passed | Created a listing with 8 portions and reserved 2 as a student. Confirmed that 6 portions remained. Cancelled the reservation and received a success message. The reservation status changed to `cancelled`, and the listing's available portions returned to 8. |
| US6 | 3: Hide Cancel Button for Ineligible Reservations | Miles Porter | 11/10/2026 | Passed | Verified that the Cancel button appeared for the eligible active reservation and disappeared after cancellation. 
| US7 | 1 — Confirm an active reservation during its pickup window | Miles Porter | 2026-11-07 | Pass | Vendor 1 entered the code for a reservation on their listing. The app confirmed the pickup and displayed the student's name and portion count. |
| US7 | 2 — Reject an unknown pickup code | Miles Porter | 2026-11-07 | Pass | An unused code displayed “No reservation with that pickup code was found for your listings.” |
| US7 | 2 — Reject a code belonging to another vendor | Miles Porter | 2026-11-07 | Pass | Vendor 2 entered a valid code for Vendor 1's listing and saw the no-reservation message. Vendor 1 then confirmed the same code successfully. |
| US7 | 2 — Reject an already used code | Miles Porter | 2026-11-07 | Pass | Vendor 1 submitted the same code after confirming it and saw “This reservation is no longer active.” |
| US7 | 2 — Reject a cancelled reservation's code | Miles Porter | — | Pending | The current branch has no browser flow for cancelling a reservation. |
| US7 | 3 — Show all active reservations on an expired listing as no-shows | Miles Porter | 2026-11-07 | Pass | After the pickup window ended, both students who reserved from Food appeared under No-shows when the vendor opened Confirm Pickup with the code field empty. |
| US7 | 3 — Expired active reservations transition to no-show | Miles Porter | 2026-11-10 | Pass | Verified two expired reservations (pickup codes 599442 and 213586) changed from `active` to `no-show` when accessing My Reservations. |
| US7 | 3 — No-show status persists in PostgreSQL | Miles Porter | 2026-11-10 | Pass | Queried the database in a separate Python session. Both reservations returned `no-show`, confirming changes were committed. |
| US7 | 3 — Existing reservation statuses remain unchanged | Miles Porter | 2026-11-10 | Pass | Verified `picked_up` and `cancelled` reservations retained their statuses after the update. |
| US7 | 3 — Unexpired reservations remain active | Miles Porter | 2026-11-10 | Pass | Verified an active reservation with pickup window ending November 12 remained `active`. |
| US7 | 3 — Vendor can view no-show reservations | Miles Porter | 2026-11-10 | Pass | Logged in as the vendor and verified expired reservations appeared in the Confirm Pickup page's No-shows section with correct student names and portion counts. |
| US7 | 2 — Vendor cannot confirm pickup for a no-show | Miles Porter | 2026-11-10 | Pass | Submitted pickup code 599442. Application displayed "This reservation is no longer active." Reservation remained in the No-shows list. |
