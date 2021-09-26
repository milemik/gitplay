import pytest

from common.common import get_first
from models.user import User


def test_get_first():
    values = [1, 2, 3]
    assert get_first(values=values) == 1


def test_get_first_empty_list():
    assert get_first(values=[]) is None


class TestUser:

    def test_user_info(self, user_helper):
        mail, name = user_helper
        user = User(username=name, email=mail)

        assert user.email == mail
        assert user.username == name

    def test_create_user(self, user_helper):
        mail, name = user_helper
        data = {"username": name, "email": mail}
        new_user = User.create_user(data)

        assert new_user.username == name
        assert new_user.email == mail

    def test_create_user_no_username(self, user_helper):
        mail, _ = user_helper
        with pytest.raises(ValueError) as err:
            User.create_user(data={"username": "", "mail": mail})

        assert err.value.args[0] == "User must have username"

    def test_create_user_no_email(self, user_helper):
        _, username = user_helper
        with pytest.raises(ValueError) as err:
            User.create_user(data={"username": username, "mail": ""})

        assert err.value.args[0] == "User must have email"
