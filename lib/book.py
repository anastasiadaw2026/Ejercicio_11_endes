import random
from ENDES.Ejercicio_11.lib.publisher import Publisher


class Book:
    def __init__(self):
        self._book_id: int = self._create_id()
        self.author: str = ''
        self.title: str = ''
        self.price: float = 0.0
        self._available: bool = True
        self.publisher: Publisher = Publisher()

    def _create_id(self):
        id_1: int = 0
        id_1 = random.randint(1,100)
        return id_1

