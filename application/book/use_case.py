from typing import List, Optional

import application.book.command
import application.book.query
import application.book.service
import domain.book.entity
import domain.book.value_object


class AddBook:
    def __init__(self, book_service: application.book.service.BookService):
        self.book_service = book_service

    def execute(
        self, command: application.book.command.AddBook
    ) -> domain.book.entity.Book:
        return self.book_service.add_book(
            command.title,
            command.author,
            domain.book.value_object.ISBN(command.isbn),
            command.publication_date,
        )


class FindBooksByAuthor:
    def __init__(self, book_service: application.book.service.BookService):
        self.book_service = book_service

    def execute(
        self, query: application.book.query.FindBooksByAuthor
    ) -> Optional[List[domain.book.entity.Book]]:
        return self.book_service.get_books_by_author(query.author)
