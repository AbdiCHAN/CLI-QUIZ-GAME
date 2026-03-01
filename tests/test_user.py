from models.user import User


def test_user_creation():
    user = User("test", "1234")
    assert user.username == "test"


def test_password_check():
    user = User("test", "1234")
    assert user.check_password("1234") is True