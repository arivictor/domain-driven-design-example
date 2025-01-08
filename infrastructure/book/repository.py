from typing import Dict, List, Optional
import uuid
import domain.book.repository
import domain.book.entity


class InMemoryBookRepository(domain.book.repository.BookRepository):
    def __init__(self):
        self.books: Dict[uuid.UUID, domain.book.entity.Book] = {}
        self._transaction_active = False
        self._backup_books = {}

    def begin(self):
        self._transaction_active = True
        self._backup_books = self.books.copy()

    def commit(self):
        self._transaction_active = False
        self._backup_books = {}

    def rollback(self):
        if self._transaction_active:
            self.books = self._backup_books
            self._transaction_active = False
            self._backup_books = {}

    def save(self, book: domain.book.entity.Book):
        if book.id is None:
            book.id = uuid.uuid4()
        self.books[book.id] = book

    def find_by_id(self, book_id: int) -> Optional[domain.book.entity.Book]:
        return self.books.get(book_id)

    def find_by_author(self, author: str) -> Optional[List[domain.book.entity.Book]]:
        books: List[domain.book.entity.Book] = []
        for _, book in self.books.items():
            if book.author == author:
                books.append(book)

        return books


import sqlite3
from typing import List, Optional
import uuid
from domain.book.repository import BookRepository
from domain.book.entity import Book


class SQLiteBookRepository(BookRepository):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_database()
        self._transaction_active = False

    def _initialize_database(self):
        """Create the books table if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS books (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT NOT NULL,
                    publication_date TEXT
                )
            """
            )
            conn.commit()

    def begin(self):
        self._transaction_active = True
        self._conn = sqlite3.connect(self.db_path)
        self._cursor = self._conn.cursor()

    def commit(self):
        if self._transaction_active:
            self._conn.commit()
            self._conn.close()
            self._transaction_active = False

    def rollback(self):
        if self._transaction_active:
            self._conn.rollback()
            self._conn.close()
            self._transaction_active = False

    def save(self, book: Book):
        """Save a book to the database."""
        if self._transaction_active:
            cursor = self._cursor
        else:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

        if book.id is None:
            book.id = str(uuid.uuid4())  # Generate a new UUID if not set
            cursor.execute(
                """
                INSERT INTO books (id, title, author, isbn, publication_date)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    book.id,
                    book.title,
                    book.author,
                    book.isbn.value,
                    book.publication_date,
                ),
            )
        else:
            cursor.execute(
                """
                REPLACE INTO books (id, title, author, isbn, publication_date)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    book.id,
                    book.title,
                    book.author,
                    book.isbn.value,
                    book.publication_date,
                ),
            )

        if not self._transaction_active:
            conn.commit()

    def find_by_id(self, book_id: str) -> Optional[Book]:
        """Find a book by its ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, title, author, isbn, publication_date FROM books WHERE id = ?",
                (book_id,),
            )
            row = cursor.fetchone()
            if row:
                return Book(
                    id=row[0],
                    title=row[1],
                    author=row[2],
                    isbn=row[3],
                    publication_date=row[4],
                )
        return None

    def find_by_author(self, author: str) -> Optional[List[Book]]:
        """Find all books by an author."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, title, author, isbn, publication_date FROM books WHERE author = ?",
                (author,),
            )
            rows = cursor.fetchall()
            return (
                [
                    Book(
                        id=row[0],
                        title=row[1],
                        author=row[2],
                        isbn=row[3],
                        publication_date=row[4],
                    )
                    for row in rows
                ]
                if rows
                else None
            )
