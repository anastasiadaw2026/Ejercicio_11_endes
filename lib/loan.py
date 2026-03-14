from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.member import Member


class Loan:
    def __init__(self):
        self.due_date: str = ''
        self.return_date: str = ''
        self.issue_date: str = ''
        self.book: Book = Book()
        self.member: Member = Member()