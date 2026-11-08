from app.models import User


def test_password_is_hashed():
    user = User(name="Test Student", email="student@example.com", role="student")

    user.set_password("CampusEats123!")

    assert user.password_hash != "CampusEats123!"
    assert user.check_password("CampusEats123!") is True


def test_wrong_password_is_rejected():
    user = User(name="Test_Student", email="student@example.com", role="student")
    user.set_password("CampusEats123!")

    assert user.check_password("WrongPassword!") is False