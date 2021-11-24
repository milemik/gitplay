import dataclasses


@dataclasses.dataclass
class Blog:
    title: str
    body: str
    number_of_likes: int
