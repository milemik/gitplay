import dataclasses


@dataclasses.dataclass
class User:
    username: str
    email: str

    @staticmethod
    def create_user(data):
        if not data.get("username"):
            raise ValueError("User must have username")
        if not data.get("email"):
            raise ValueError("User must have email")
        return User(username=data.get("username"), email=data.get("email"))


@dataclasses.dataclass
class Blog:
    title: str
    body: str
    number_of_likes: int
