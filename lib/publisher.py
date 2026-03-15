import random


class Publisher:
    def __init__(self):
        self._pub_id: int = self._create_id()
        self.address: str = ''
        self.name: str = ''

    def __str__(self):
        return (f"Publisher id: {self._pub_id}\n"
                f"Publicher name: {self.name}\n"
                f"Publicher adress: {self.address}")

    def _create_id(self):
        id_1: int = 0
        id_1 = random.randint(1,50) # poner después 50 como constante
        return id_1
