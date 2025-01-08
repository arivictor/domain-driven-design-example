from dataclasses import dataclass
from datetime import date


@dataclass
class AddBook:
    title: str
    author: str
    isbn: str
    publication_date: date
