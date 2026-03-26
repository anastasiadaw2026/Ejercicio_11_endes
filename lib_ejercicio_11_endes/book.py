from ENDES.Ejercicio_11.lib_ejercicio_11_endes.publisher import Publisher


class Book:
    """
       Represents a book entity in the system.

       This class models the basic details of a book, including its unique
       identifier, title, author, price, availability status, and publisher.

       :ivar _book_id: Unique identifier for the book.
       :vartype _book_id: int
       :ivar author: Name of the author of the book.
       :vartype author: str
       :ivar title: Title of the book.
       :vartype title: str
       :ivar price: Price of the book.
       :vartype price: float
       :ivar available: Availability status of the book (True if available).
       :vartype available: bool
       :ivar publisher: Publisher that published the book.
       :vartype publisher: Publisher
       """

    def __init__(self, book_id):
        """
        Initializes a new `Book` instance.

        :param book_id: Unique identifier assigned to the book.
        :type book_id: int
        """
        self._book_id: int = book_id
        self.author: str = ''
        self.title: str = ''
        self.price: float = 0.0
        self.available: bool = True
        self.publisher: Publisher = Publisher(-1)

    @property
    def book_id(self) -> int:
        """
        Retrieves the unique identifier of the book.

        :return: The unique book ID.
        :rtype: int
        """
        return self._book_id

    def __str__(self) -> str:
        """
        Provides a string representation of the `Book` instance.

        :return: A string representing the book's details.
        :rtype: str
        """
        return (f"Book id: {self._book_id}\n"
                f"Book title: {self.title}\n"
                f"Book author: {self.author}\n"
                f"Book price: {self.price}\n"
                f"Book publisher: {self.publisher.name}\n")
