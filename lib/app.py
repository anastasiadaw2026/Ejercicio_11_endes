from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.loan import Loan
from ENDES.Ejercicio_11.lib.member import Member
from ENDES.Ejercicio_11.lib.publisher import Publisher


class App:
    class ConstantsDate:
        SYSDATE: str = '30.03.2026'

    class ConstantsMenu:
        SALIDA: int = 7
        OPCION_UNO: int = 1
        OPCION_DOS: int = 2
        OPCION_TRES: int = 3
        OPCION_CUATRO: int = 4
        OPCION_CINCO: int = 5
        OPCION_SEIS: int = 6

    class ConstantsMaximums:
        MAX_ELEMENTS: int = 100

    def __init__(self):
        self.counter_books: int = -1
        self.counter_publishers: int = -1
        self.counter_members: int = -1
        self.counter_loans: int = -1
        self._publishers: list[Publisher] = self.create_list(Publisher)
        self._books: list[Book] = self.create_list(Book)
        self._members: list[Member] = self.create_list(Member)
        self._loans: list[Loan] = self.create_list(Loan())

    def create_list(self, element): #funciona
        list_elements: list = []
        if isinstance(element, Loan):
            list_elements = [element for _ in range(
                App.ConstantsMaximums.MAX_ELEMENTS)]
        else:
            list_elements = [element(auto_id + 1) for auto_id in range(
                App.ConstantsMaximums.MAX_ELEMENTS)]
        return list_elements

    def run(self):
        option: int = 0
        print("Hi, choose the option you want to execute: ")
        while option != App.ConstantsMenu.SALIDA:
            self.print_menu()
            option: int = int(input(": "))
            match option:
                case App.ConstantsMenu.OPCION_UNO:
                    self.add_publisher()
                case App.ConstantsMenu.OPCION_DOS:
                    self.counter_books += 1
                    self.register_book()
                    self.print_publisher_menu()
                    self.assign_publisher_book()
                    print(self._books[self.counter_books])
                case App.ConstantsMenu.OPCION_TRES:
                    self.counter_members += 1
                    self.register_member()
                    print(self._members[self.counter_members])
                case App.ConstantsMenu.OPCION_CUATRO:
                    self.counter_loans += 1
                    self.create_loan()
                case App.ConstantsMenu.OPCION_CINCO:
                    self.register_return()
                case App.ConstantsMenu.OPCION_SEIS:
                    self.remove_member()
                case App.ConstantsMenu.SALIDA:
                    print("¡Bye!")
                case _:
                    print("Incorrect number, try it again.")

    def remove_member(self):
        option_member_remove: int = 0
        print("Choose the member you wanna remove:")
        self.print_list(self._members)
        option_member_remove = int(input(": "))
        self._members.pop(option_member_remove - 1)

    def register_return(self):
        option_returned_book: int = 0
        print("Choose the book that is returned:")
        self.print_list(self._loans)
        option_returned_book = int(input(": "))
        self.chech_return_date(option_returned_book)
        self._loans[option_returned_book].return_date = (
            App.ConstantsDate.SYSDATE)
        self._books[option_returned_book - 1].available = True

    def chech_return_date(self, option_returned_book: int):
        date: list[str] = []
        expire_date: list[str] = []
        date = App.SYSDATE.split('.')
        expire_date = self._loans[option_returned_book - 1].due_date.split('.')
        if not (date[2] < expire_date[2] or (date[1] < expire_date[1]
                and date[2] == expire_date[2]) or (date[0] <= expire_date[0]
                and date[1] == expire_date[1] and date[2] == expire_date[2])):
            self.remove_unpunctual_member(option_returned_book)

    def remove_unpunctual_member(self, option_returned_book: int):
        self._members.pop(self._members.index(self._loans[
                                            option_returned_book - 1].member))
        print("The return date is late. We removed this member from the "
              "members list. They will be able to renew their subscription "
              "in two weeks.")

    def create_loan(self):
        option_book: int = 0
        print("Choose the book you want to borrow:")
        self.print_list(self._books)
        option_book = int(input(": "))
        if self._books[option_book - 1].available:
            self.assign_book_loan(option_book)
            self.assign_member_loan()
            print(self._loans[self.counter_loans])
        else:
            print("The book is not available.")

    def assign_book_loan(self, option_book: int):
        self._loans[self.counter_loans].book = self._books[
            option_book - 1]
        self._books[option_book - 1].available = False

    def assign_member_loan(self):
        # ver si la lista no esta vacía
        option_member: int = 0
        print("Choose who wants to borrow it:")
        self.print_list(self._members)
        option_member = int(input(": "))
        self._loans[self.counter_loans].member = self._members[
            option_member - 1]

    def assign_publisher_book(self):
        option_menu_2: int = 0
        option_menu_2 = int(input(": "))
        match option_menu_2:
            case App.ConstantsMenu.OPCION_UNO:
                self.choose_publisher()
            case App.ConstantsMenu.OPCION_DOS:
                self.add_publisher()
                self._books[self.counter_books].publisher = (
                    self._publishers[self.counter_publishers])
            case _:
                print("The introduced number is incorrect. Try it again.")
                self.assign_publisher_book()

    def choose_publisher(self):
        option_publisher: int = 0
        print("Choose a number:")
        self.print_list(self._publishers)
        option_publisher = int(input(": "))
        self._books[self.counter_books].publisher = (
            self._publishers[option_publisher - 1])

    def add_publisher(self):
        self.counter_publishers += 1
        self.register_publisher()
        print(self._publishers[self.counter_publishers])

    def print_list(self, elements_list):
        for index, element in enumerate(elements_list):
            if isinstance(element, Book):
                if element.title:
                    print(index + 1, '-', element)
            elif isinstance(element, Loan):
                if element.book.title:
                    print(index + 1, '-', element)
            else:
                if element.name:
                    print(index + 1, '-', element)

    def register_publisher(self):
        self._publishers[self.counter_publishers].name = input("Enter the "
                                                               "name of the publisher: ")
        self._publishers[self.counter_publishers].address = input("Enter the address of the publisher: ")

    def register_book(self):
        self._books[self.counter_books].title = input("Enter the title of the "
                                                "book: ")
        self._books[self.counter_books].author = input("Enter the author of the book: ")
        self._books[self.counter_books].price = float(input("Enter the price of the "
                                                "book: "))

    def register_member(self):
        self._members[self.counter_members].name = input("Enter member's name: ")
        self._members[self.counter_members].address = input("Enter member's address: ")
        self._members[self.counter_members].member_type = input("Enter the member's type: ")

    def print_publisher_menu(self):
        print(f"To assign the publisher you can choose between the next "
              f"options:\n"
              f"{App.ConstantsMenu.OPCION_UNO}. Choose a existent one.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Introduce another publisher.")

    def print_menu(self):
        print(f"{App.ConstantsMenu.OPCION_UNO}. Register a publisher.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Register a book.\n"
              f"{App.ConstantsMenu.OPCION_TRES}. Register a member.\n"
              f"{App.ConstantsMenu.OPCION_CUATRO}. Register a loan.\n"
              f"{App.ConstantsMenu.OPCION_CINCO}. Register a return.\n"
              f"{App.ConstantsMenu.OPCION_SEIS}. Remove a member.\n"
              f"{App.ConstantsMenu.SALIDA}. Exit.")

App().run()