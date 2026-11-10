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


