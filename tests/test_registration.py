from app import app, db
from app.models import User


def test_registration_creates_user(client):
    response = client.post("/register", data={
        "name": "Test Student",
        "email": "student@example.com",
        "password": "CampusEats123!",
        "password_confirm": "CampusEats123!",
        "role": "student",
    })

    assert response.status_code == 302
    assert response.headers["Location"].endswith("/login")

    with app.app_context():
        user = db.session.scalar(
            db.select(User).filter_by(email="student@example.com")
        )
        assert user is not None
        assert user.name == "Test Student"
        assert user.role == "student"
        assert user.check_password("CampusEats123!")
        assert user.email == "student@example.com"


def test_mismatched_passwords_do_not_create_user(client):
    response = client.post("/register", data={
        "name": "Test Student",
        "email": "student@example.com",
        "password": "CampusEats123!",
        "password_confirm": "DifferentPassword!",
        "role": "student",
    })

    assert response.status_code == 200

    with app.app_context():
        user = db.session.scalar(
            db.select(User).filter_by(email="student@example.com")
        )
        assert user is None

def test_duplicate_email_is_rejected(client):
    data = {
        "name": "Test Student",
        "email": "student@example.com",
        "password": "CampusEats123!",
        "password_confirm": "CampusEats123!",
        "role": "student",
    }

    first_response = client.post("/register", data=data)
    assert first_response.status_code == 302

    data["name"] = "Another Student"
    second_response = client.post("/register", data=data)

    assert second_response.status_code == 200

    with app.app_context():
        users = db.session.scalars(
            db.select(User).filter_by(email="student@example.com")
        ).all()
        assert len(users) == 1
        assert users[0].name == "Test Student"

def register_user(client):
    response = client.post("/register", data={
        "name": "Test Student",
        "email": "student@example.com",
        "password": "CampusEats123!",
        "password_confirm": "CampusEats123!",
        "role": "student",
    })
    assert response.status_code == 302


def test_home_requires_login(client):
    response = client.get("/")

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_correct_password_logs_user_in(client):
    register_user(client)

    response = client.post("/login", data={
        "email": "student@example.com",
        "password": "CampusEats123!",
    })

    assert response.status_code == 302
    assert client.get("/").status_code == 200


def test_wrong_password_does_not_log_user_in(client):
    register_user(client)

    response = client.post("/login", data={
        "email": "student@example.com",
        "password": "WrongPassword!",
    })

    assert response.status_code == 200
    assert client.get("/").status_code == 302


def test_logout_ends_session(client):
    register_user(client)
    client.post("/login", data={
        "email": "student@example.com",
        "password": "CampusEats123!",
    })
    assert client.get("/").status_code == 200

    response = client.get("/logout")

    assert response.status_code == 302
    assert client.get("/").status_code == 302