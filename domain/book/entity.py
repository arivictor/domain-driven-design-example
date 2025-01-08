from datetime import date
from typing import List
import uuid

import domain.book.value_object


class Book:
    def __init__(
        self,
        *,
        id: uuid.UUID = None,
        title: str,
        author: str,
        isbn: domain.book.value_object.ISBN,
        publication_date: date = None,
    ):
        self.id = id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_date = publication_date
        self.reviews: List[str] = []
