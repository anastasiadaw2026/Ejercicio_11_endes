import random


class Member:
    # como no sabemos como trabajar con fechas le asignamos una fecha por
    # defecto a todo. La idea es que después habrá una función que ponga la
    # fecha actual del sistema y otra que le sume un año.
    SYSDATE: str = '15.02.2026'
    EXPIRE_DATE: str = '16.02.2026'

    def __init__(self):
        self._member_id: int = 0
        self.name: str = ''
        self.address: str = ''
        self.member_type: str = ''
        self._member_date: str = Member.SYSDATE
        self._expiry_date: str = Member.EXPIRE_DATE

    # ver como puedo hacer que compartan este metodo
    def _create_id(self):
        id_1: int = 0
        id_1 = random.randint(1,100) # poner después 50 como constante
        return id_1
