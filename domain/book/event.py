from dataclasses import dataclass


class DomainEvent:
    pass


@dataclass
class BookAdded(DomainEvent):
    title: str
    author: str
