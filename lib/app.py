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

    def __init__(self):
        self.counter_books: int = -1
        self.counter_publishers: int = -1   
        self.counter_members: int = -1
        self.counter_loans: int = -1
        self._publishers: list[Publisher] = []
        self._books: list[Book] = []
        self._members: list[Member] = []
        self._loans: list[Loan] = []

    def run(self):
        option: int = 0
        print("Hi, choose the option you want to execute:")
        while option != App.ConstantsMenu.SALIDA:
            self.print_menu()
            option: int = int(input(": "))
            match option:
                case App.ConstantsMenu.OPCION_UNO:
                    self.add_publisher()
                    print(self._publishers[self.counter_publishers])
                case App.ConstantsMenu.OPCION_DOS:
                    self.add_book()
                    print(self._books[self.counter_books])
                case App.ConstantsMenu.OPCION_TRES:
                    self.add_member()
                    print(self._members[self.counter_members])
                case App.ConstantsMenu.OPCION_CUATRO:
                    self.counter_loans += 1
                    self._loans.append(Loan())
                    self.create_loan()
                case App.ConstantsMenu.OPCION_CINCO:
                    if self._loans:
                        self.register_return()
                    else:
                        print("No loan is registered at the moment.")
                case App.ConstantsMenu.OPCION_SEIS:
                    if self._members:
                        self.remove_member()
                    else:
                        print("No member is registered at the moment.")
                case App.ConstantsMenu.SALIDA:
                    print("¡Bye!")
                case _:
                    print("Incorrect number, try it again.")

    def add_member(self):
        self.counter_members += 1
        self._members.append(
            Member(self.counter_members + 1))
        self.register_member()

    def add_book(self):
        self.counter_books += 1
        self._books.append(Book(self.counter_books + 1))
        self.register_book()
        self.print_publisher_menu()
        self.assign_publisher_book()

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
        self.check_return_date(option_returned_book)
        self._loans[option_returned_book - 1].return_date = App.ConstantsDate.SYSDATE
        self._books[option_returned_book - 1].available = True

    def check_return_date(self, option_returned_book: int):
        date: list[str] = []
        expire_date: list[str] = []
        date = App.ConstantsDate.SYSDATE.split('.')
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
        print("Book:")
        if self._books:
            self.register_existing_book_loan()
        else:
            self.register_element(Book)
        print("Member:")
        if self._members and self._books:
            self.assign_member_loan()
            print(self._loans[self.counter_loans])
        elif self._books:
            self.register_element(Member)

    def register_existing_book_loan(self):
        option_book: int = 0
        available_books = [x for x in self._books if x.available]
        print("Choose the book you want to borrow:")
        self.print_list(available_books)
        option_book = int(input(": "))
        self.assign_book_loan(option_book, available_books)

    def register_element(self, element_type):
        print(f"No element is registered at the moment.\n"
              "Choose an option:\n"
              "1. Cancel the loan.\n"
              "2. Register a element.")
        option = int(input(": "))
        if option == 1:
            del self._loans[self.counter_loans]
            self.counter_loans -= 1
        elif option == 2:
            if element_type == Book:
                self.add_book()
                self._loans[self.counter_loans].book = self._books[
                    self.counter_books]
            else:
                self.add_member()
                self._loans[self.counter_loans].member = self._members[
                    self.counter_members]
                print(self._loans[self.counter_loans])
        else:
            print("Wrong number. Try it again.")
            self.register_element(element_type)

    def assign_book_loan(self, option_book: int, available_books):
        position = self._books.index(available_books[option_book - 1])
        self._loans[self.counter_loans].book = self._books[position]
        self._books[position].available = False

    def assign_member_loan(self):
        option_member: int = 0
        print("Choose who wants to borrow it:")
        self.print_list(self._members)
        option_member = int(input(": "))
        self._loans[self.counter_loans].member = self._members[
            option_member - 1]

    def assign_publisher_book(self):
        option_menu_2: int = 0
        option_menu_2 = int(input(": "))
        if option_menu_2 == App.ConstantsMenu.OPCION_UNO and self._publishers:
            self.choose_publisher()
        elif option_menu_2 == App.ConstantsMenu.OPCION_DOS:
            self.add_publisher()
            self._books[self.counter_books].publisher = (self._publishers[
                self.counter_publishers])
        else:
            print("The introduced number is incorrect. Try it again.")
            self.assign_publisher_book()

    def choose_publisher(self):
        option_publisher: int = 0
        print("Choose a number:")
        self.print_list(self._publishers)
        option_publisher = int(input(": "))
        self._books[self.counter_books].publisher = (self._publishers[
            option_publisher - 1])

    def add_publisher(self):
        self.counter_publishers += 1
        self._publishers.append(Publisher(self.counter_publishers + 1))
        self.register_publisher()

    def print_list(self, elements_list):
        if elements_list:
            for index, element in enumerate(elements_list):
                print(index + 1, '-', element)
        else:
            print("No data found")

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
        print(f"To assign the publisher: ")
        if self._publishers:
            print(f"{App.ConstantsMenu.OPCION_UNO}. Choose a existent one.\n"
                  f"{App.ConstantsMenu.OPCION_DOS}. Introduce another "
                  f"publisher.")
        else:
            print("     No publisher is registered at the moment. Press 2 to "
                  "register one.")

    def print_menu(self):
        print(f"{App.ConstantsMenu.OPCION_UNO}. Register a publisher.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Register a book.\n"
              f"{App.ConstantsMenu.OPCION_TRES}. Register a member.\n"
              f"{App.ConstantsMenu.OPCION_CUATRO}. Register a loan.\n"
              f"{App.ConstantsMenu.OPCION_CINCO}. Register a return.\n"
              f"{App.ConstantsMenu.OPCION_SEIS}. Remove a member.\n"
              f"{App.ConstantsMenu.SALIDA}. Exit.")

App().run()