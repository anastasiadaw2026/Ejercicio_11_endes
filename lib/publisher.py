import random


class Publisher:
    def __init__(self):
        self._pub_id: int = self._create_id()
        self.address: str = ''
        self.name: str = ''

    def _create_id(self):
        id_1: int = 0
        id_1 = random.randint(1,50) # poner después 50 como constante
        return id_1