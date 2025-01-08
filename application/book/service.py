from datetime import date
from typing import List, Optional
import uuid

import application.book.event
import application.book.event_bus
import domain.book.repository
import domain.book.entity
import domain.book.event
import domain.book.value_object


class BookService:
    def __init__(
        self,
        book_repository: domain.book.repository.BookRepository,
        event_bus: application.book.event_bus.EventBus,
    ):
        self.book_repository = book_repository
        self.event_bus = event_bus

    def add_book(
        self,
        title: str,
        author: str,
        isbn: domain.book.value_object.ISBN,
        publication_date: date,
    ) -> domain.book.entity.Book:
        book = domain.book.entity.Book(
            title=title,
            author=author,
            isbn=isbn,
            publication_date=publication_date,
        )
        self.book_repository.save(book)

        event = application.book.event.BookAdded(title=book.title, author=book.author)
        self.event_bus.publish(event)

        return book

    def get_book_by_id(self, book_id: uuid.UUID) -> Optional[domain.book.entity.Book]:
        return self.book_repository.find_by_id(book_id=book_id)

    def get_books_by_author(
        self, author: str
    ) -> Optional[List[domain.book.entity.Book]]:
        return self.book_repository.find_by_author(author=author)
