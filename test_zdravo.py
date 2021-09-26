from common.common import get_first
from models.user import User


def test_get_first():
    values = [1, 2, 3]
    assert get_first(values=values) == 1


def test_get_first_empty_list():
    assert get_first(values=[]) is None


def test_user_info():
    mail = "someone@test.com"
    name = "someone123"
    user = User(username=name, email=mail)

    assert user.email == mail
    assert user.username == name
