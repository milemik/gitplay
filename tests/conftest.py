import pytest


@pytest.fixture
def user_helper():
    mail = "someone@test.com"
    name = "someone123"
    return mail, name
