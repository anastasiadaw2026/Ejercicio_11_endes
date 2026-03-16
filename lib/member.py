import random


class Member:
    class ConstantsDates:
        # como no sabemos como trabajar con fechas le asignamos una fecha por
        # defecto a todo. La idea es que después habrá una función que ponga la
        # fecha actual del sistema y otra que le sume un año.
        SYSDATE: str = '15.03.2026'
        EXPIRE_DATE: str = '15.03.2027'

    class ConstantsId:
        MAX_MEMBERS: int = 100

    def __init__(self, member_id):
        self._member_id: int = member_id
        self.name: str = ''
        self.address: str = ''
        self.member_type: str = ''
        self._member_date: str = Member.ConstantsDates.SYSDATE
        self._expiry_date: str = Member.ConstantsDates.EXPIRE_DATE

    @property
    def member_id(self):
        return self._member_id

    def __str__(self):
        return (f"Member id: {self._member_id}\n"
                f"Member name: {self.name}\n"
                f"Member type: {self.member_type}\n"
                f"Member address: {self.address}\n"
                f"Member register date: {self._member_date}\n"
                f"Member expiry date: {self._expiry_date}")
