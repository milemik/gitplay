from common.common import get_first


def test_get_first():
    values = [1, 2, 3]
    assert get_first(values=values) == 1
