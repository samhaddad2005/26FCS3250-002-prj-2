# Import tools for running concurrent requests.
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from threading import Barrier
from uuid import uuid4
import secrets

# Import pytest for automated testing.
import pytest

# Import the CampusEats Flask application and database.
from app import app, db
from app.models import User, FoodListing, Reservation


# Create two independent student accounts and one test listing.
@pytest.fixture
def reservation_setup():
    unique = uuid4().hex[:12]

    with app.app_context():
        # Create two student accounts with unique email addresses.
        student_a = User(
            name="US4 Test Student A",
            email=f"us4_a_{unique}@example.com",
            role="student",
        )
        student_a.set_password("TestPassword123!")

        student_b = User(
            name="US4 Test Student B",
            email=f"us4_b_{unique}@example.com",
            role="student",
        )
        student_b.set_password("TestPassword123!")

        # Create a vendor account to own the listing.
        vendor = User(
            name="US4 Test Vendor",
            email=f"us4_vendor_{unique}@example.com",
            role="vendor",
        )
        vendor.set_password("TestPassword123!")

        db.session.add_all([student_a, student_b, vendor])
        db.session.flush()

        # Create a listing with exactly one available portion.
        listing = FoodListing(
            vendor_id=vendor.id,
            title=f"US4 Concurrent Test {unique}",
            description="Temporary listing for concurrency testing",
            portions=1,
            portions_remaining=1,
            cancelled=False,
            pickup_location="Campus",
            pickup_start=datetime.now(),
            pickup_end=datetime.now() + timedelta(hours=2),
        )

        db.session.add(listing)
        db.session.commit()

        # Save identifiers for the test.
        data = {
            "student_ids": [student_a.id, student_b.id],
            "listing_id": listing.id,
        }

    yield data

    # Delete only records created by this test.
    with app.app_context():
        db.session.query(Reservation).filter(
            Reservation.listing_id == data["listing_id"]
        ).delete(synchronize_session=False)

        db.session.query(FoodListing).filter(
            FoodListing.id == data["listing_id"]
        ).delete(synchronize_session=False)

        db.session.query(User).filter(
            User.id.in_(data["student_ids"])
        ).delete(synchronize_session=False)

        db.session.query(User).filter(
            User.email == f"us4_vendor_{unique}@example.com"
        ).delete(synchronize_session=False)

        db.session.commit()


# Send a reservation request as one authenticated student.
def reserve_as_student(student_id, listing_id, barrier):
    # Each thread gets its own Flask test client.
    with app.test_client() as client:
        # Establish the authenticated Flask-Login session.
        with client.session_transaction() as session:
            session["_user_id"] = str(student_id)
            session["_fresh"] = True

        # Wait until both threads are ready.
        barrier.wait(timeout=10)

        # Send the reservation request.
        response = client.post(
            f"/reserve/{listing_id}",
            data={"portions": "1"},
        )

        return response.status_code


# Verify that two students cannot reserve the same last portion.
def test_concurrent_reservations(reservation_setup):
    student_a, student_b = reservation_setup["student_ids"]
    listing_id = reservation_setup["listing_id"]

    # Synchronize both requests before sending them.
    barrier = Barrier(2)

    # Execute two reservation requests concurrently.
    with ThreadPoolExecutor(max_workers=2) as executor:
        future_a = executor.submit(
            reserve_as_student, student_a, listing_id, barrier
        )
        future_b = executor.submit(
            reserve_as_student, student_b, listing_id, barrier
        )

        results = [
            future_a.result(timeout=20),
            future_b.result(timeout=20),
        ]

    # Exactly one request must succeed and one must fail.
    assert sorted(results) == [201, 409]

    # Verify the final database state.
    with app.app_context():
        listing = db.session.get(FoodListing, listing_id)

        reservations = db.session.query(Reservation).filter(
            Reservation.listing_id == listing_id,
            Reservation.status == "active",
        ).all()

        # Only one portion can be reserved.
        assert listing.portions_remaining == 0

        # Only one active reservation should exist.
        assert len(reservations) == 1
        assert reservations[0].portions == 1

        # Verify the generated pickup code.
        assert len(reservations[0].pickup_code) == 6
        assert reservations[0].pickup_code.isdigit()