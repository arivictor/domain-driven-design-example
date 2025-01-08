from abc import ABC, abstractmethod
from typing import List, Optional

import domain.book.entity


class BookRepository(ABC):
    @abstractmethod
    def save(self, book: domain.book.entity.Book):
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[domain.book.entity.Book]:
        pass

    @abstractmethod
    def find_by_author(self, author: str) -> Optional[List[domain.book.entity.Book]]:
        pass
