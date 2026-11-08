
# CampusEats - Manual Testing Results

## Test Environment
- Application: CampusEats
- Testing method: Manual testing

## US1 - User Registration
Status: Pending documentation

## US2 - Create Food Listing
Tester: Hai Dang Nguyen Le
Date: October 29, 2026
Branch tested: feature/us2-food-listing

### Test Results

| Test Case | Description | Result |
|---|---|---|
| TC01 | Vendor creates a valid food listing | PASS |
| TC02 | Student cannot access listing creation | PASS |
| TC03 | Required fields cannot be empty | PASS |
| TC04 | Pickup end must be after pickup start | PASS |
| TC05 | Pickup end must be in the future | PASS |
| TC06 | Portions cannot be less than 1 | PASS - browser validation |
| TC07 | Portions cannot exceed 100 | PASS - browser validation |
| TC08 | Portions = 1 | PASS - reported |
| TC09 | Portions = 100 | PASS - reported |

### Notes
- Valid listing was saved in PostgreSQL.
- Portion limits were checked in the browser; server-side rejection was not independently confirmed.
- Tests were run with Flask locally and PostgreSQL in Docker.
- Docker Compose deployment still needs verification.

## US3
Status: Pending documentation

## US4 - Food Reservation
Status: Pending documentation
