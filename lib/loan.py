from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.member import Member


class Loan:
    class ConstantsDates:
        # como no sabemos como trabajar con fechas le asignamos una fecha por
        # defecto a todo. La idea es que después habrá una función que ponga la
        # fecha actual del sistema y otra que le sume 21 días.
        SYSDATE: str = '15.03.2026'
        EXPIRE_DATE: str = '05.04.2026'

    def __init__(self):
        self._due_date: str = Loan.ConstantsDates.EXPIRE_DATE
        self._return_date: str = ''
        self._issue: str = Loan.ConstantsDates.SYSDATE
        self.book: Book = Book()
        self.member: Member = Member()

    @property
    def return_date(self):
        return self._return_date

    @return_date.setter
    def return_date(self, value):
        return value

    @property
    def due_date(self):
        return self._due_date

    def __str__(self):
        return (f"Borrowed book: {self.book.book_id} - {self.book.title}\n"
                f"Borrower: {self.member.member_id} - {self.member.name}\n"
                f"Return before: {self._due_date}\n")

