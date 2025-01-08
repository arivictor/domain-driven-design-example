from abc import ABC, abstractmethod
from typing import List, Optional

import domain.book.entity


class UnitOfWork(ABC):
    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class BookRepository(UnitOfWork, ABC):
    @abstractmethod
    def save(self, book: domain.book.entity.Book):
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[domain.book.entity.Book]:
        pass

    @abstractmethod
    def find_by_author(self, author: str) -> Optional[List[domain.book.entity.Book]]:
        pass
