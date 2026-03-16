import random
from ENDES.Ejercicio_11.lib.publisher import Publisher


class Book:
    class ConstantsId:
        MAX_BOOKS: int = 100

    def __init__(self):
        self._book_id: int = self._create_id()
        self.author: str = ''
        self.title: str = ''
        self.price: float = 0.0
        self.available: bool = True
        self.publisher: Publisher = Publisher(-1)

    @property
    def book_id(self):
        return self._book_id

    def __str__(self):
        return (f"Book id: {self._book_id}\n"
                f"Book title: {self.title}\n"
                f"Book author: {self.author}\n"
                f"Book price: {self.price}\n"
                f"Book publisher: {self.publisher.name}\n")

    def _create_id(self):
        id_1: int = 0
        id_1 = random.randint(1, Book.ConstantsId.MAX_BOOKS)
        return id_1

