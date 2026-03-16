import random


class Publisher:
    class ConstantsId:
        MAX_PUBLISHERS: int = 50

    def __init__(self, pub_id: int):
        self._pub_id: int = pub_id
        self.address: str = ''
        self.name: str = ''

    def __str__(self):
        return (f"Publisher id: {self._pub_id}\n"
                f"Publicher name: {self.name}\n"
                f"Publicher adress: {self.address}\n")

    # def _create_id(self):
    #     id_1: int = 0
    #     id_1 = random.randint(1,Publisher.ConstantsId.MAX_PUBLISHERS)
    #     return id_1
