from typing import Union


def get_first(values: list) -> Union[str, int]:
    if not values:
        return None
    return values[0]


def change_on_first():
    pass
