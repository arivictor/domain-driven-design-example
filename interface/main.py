from datetime import date

import application.book.event
import application.book.service
import application.book.command
import application.book.query
import application.book.use_case
import application.book.event_bus

import infrastructure.book.repository
import infrastructure.book.event_handler


# Initialize components
event_bus = application.book.event_bus.EventBus()
# book_repository = infrastructure.book.repository.InMemoryBookRepository()
book_repository = infrastructure.book.repository.SQLiteBookRepository("test.db")
book_service = application.book.service.BookService(book_repository, event_bus)

# Subscribe handlers via the application layer
event_bus.subscribe(
    event_type=application.book.event.BookAdded,
    handler=infrastructure.book.event_handler.notify_customers_new_book_added,
)

# Example usage - Adding a Book
command = application.book.command.AddBook(
    title="Harry Potter",
    author="J.K. Rowling",
    isbn="1234567890",
    publication_date=date.today(),
)
usecase = application.book.use_case.AddBook(book_service)
book = usecase.execute(command)  # triggers event

# Example usage - Query for Books by Author
command = application.book.query.FindBooksByAuthor(author="J.K. Rowling")
usecase = application.book.use_case.FindBooksByAuthor(book_service)
books = usecase.execute(command)

for book in books:
    print(book.title)
