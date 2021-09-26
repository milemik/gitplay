import dataclasses


@dataclasses.dataclass
class User:
    username: str
    email: str