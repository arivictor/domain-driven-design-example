from dataclasses import dataclass
import uuid


@dataclass
class GetBookById:
    book_id: uuid.UUID


@dataclass
class FindBooksByAuthor:
    author: str
