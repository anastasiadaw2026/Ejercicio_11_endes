from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.member import Member


class Loan:
    """
    Represents a loan entity in the system.

    The `Loan` class models a borrowing transaction between a member and a book.
    It contains details such as the book being loaned, the member who borrowed it,
    the loan's issue date, due date, and, optionally, the return date.

    Date constants (default system date and expiry date) are managed through
    the `ConstantsDates` inner class.

    :ivar _due_date: The due date for returning the loaned book.
    :vartype _due_date: str
    :ivar _return_date: The date when the book is returned (if set).
    :vartype _return_date: str
    :ivar _issue: The issue (loan) date.
    :vartype _issue: str
    :ivar book: The book being borrowed in the loan.
    :vartype book: Book
    :ivar member: The member borrowing the book.
    :vartype member: Member
    """

    class ConstantsDates:
        """
        Stores constants related to loan dates.

        :cvar SYSDATE: Default system date for the loan's creation.
        :vartype SYSDATE: str
        :cvar EXPIRE_DATE: Default due date for the loan.
        :vartype EXPIRE_DATE: str
        """
        SYSDATE: str = '15.03.2026'
        EXPIRE_DATE: str = '05.04.2026'

    def __init__(self):
        """
        Initializes a new `Loan` instance with default dates and entities.

        By default, the associated book and member are initialized with placeholder
        values (`Book(-1)` and `Member(-1)` respectively).

        The issue and due dates default to `ConstantsDates.SYSDATE` and
        `ConstantsDates.EXPIRE_DATE`.
        """
        self._due_date: str = Loan.ConstantsDates.EXPIRE_DATE
        self._return_date: str = ''
        self._issue: str = Loan.ConstantsDates.SYSDATE
        self.book: Book = Book(-1)
        self.member: Member = Member(-1)

    @property
    def return_date(self) -> str:
        """
        Gets the return date of the loaned book.

        :return: The return date.
        :rtype: str
        """
        return self._return_date

    @return_date.setter
    def return_date(self, value: str):
        """
        Sets the return date of the loaned book.

        :param value: The date when the book was returned.
        :type value: str
        """
        self._return_date = value

    @property
    def due_date(self) -> str:
        """
        Gets the due date for returning the loaned book.

        :return: The due date of the loan.
        :rtype: str
        """
        return self._due_date

    def __str__(self) -> str:
        """
        Provides a string representation of the loan details.

        :return: A string describing the loan.
        :rtype: str
        """
        return (f"Borrowed book: {self.book.book_id} - {self.book.title}\n"
                f"Borrower: {self.member.member_id} - {self.member.name}\n"
                f"Return before: {self._due_date}\n")

