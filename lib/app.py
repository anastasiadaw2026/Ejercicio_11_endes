"""
Dar de alta una editorial
Dar de alta un libro y dejar elegir editorial de las presentes,
crear nueva, o anónima
Dar de alta un miembro

Hacer una funcion que gestionara si el libro es available y gestionar
prestamos según lo es o no
Hacer un prestamo
Hacer una devolucion
Damos de baja editorial, libro, y/o miembro
Hacer una funcion que asgina un id

"""

from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.loan import Loan
from ENDES.Ejercicio_11.lib.member import Member
from ENDES.Ejercicio_11.lib.publisher import Publisher


class App:
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
        # despues meter to do esto en constantes
        self._publishers: list[Publisher] = [Publisher() for _ in range(50)]
        self._books: list[Book] = [Book() for _ in range(100)]
        self._members: list[Member] = [Member() for _ in range(100)]
        self._loans: list[Loan] = [Loan() for _ in range(200)]

    def run(self):
        counter_books: int = -1
        counter_publishers: int = -1
        counter_members: int = -1
        counter_loans: int = -1
        print("Hi, choose the option you want to execute: ")
        option: int = 0
        while option != App.ConstantsMenu.SALIDA:
            self.print_menu()
            option: int = int(input(": "))
            match option:
                case App.ConstantsMenu.OPCION_UNO:
                    counter_publishers += 1
                    self.register_publisher(counter_publishers)
                    print(self._publishers[counter_publishers])

                case App.ConstantsMenu.OPCION_DOS:
                    counter_books += 1
                    self.register_book(counter_books)
                    self.print_publisher_menu()
                    option_menu_2: int = int(input(": "))
                    match option_menu_2:
                        # poner constantes
                        case 1: # hay que dividirlo en funciones
                            print("Choose a number:")
                            self.print_list(self._publishers)
                            option_publisher: int = int(input(": "))
                            self._books[counter_books].publisher = (
                                self._publishers[option_publisher - 1])
                        case 2:
                            counter_publishers += 1
                            self.register_publisher(counter_publishers)
                            print(self._publishers[counter_publishers])
                            self._books[counter_books].publisher = (
                                self._publishers[counter_publishers])
                        case _:
                            pass #Todo
                    print(self._books[counter_books])

                case App.ConstantsMenu.OPCION_TRES:
                    counter_members += 1
                    self.register_member(counter_members)
                    print(self._members[counter_members])

                case App.ConstantsMenu.OPCION_CUATRO:
                    counter_loans += 1
                    print("Choose the book you want to borrow:")
                    self.print_list(self._books)
                    option_book: int = int(": ")
                    if self._books[option_book - 1].available:
                        self._loans[counter_loans].book = self._books[
                            option_book - 1]
                        print("Choose who wants to borrow it:")
                        self.print_list(self._members)
                        option_member: int = int(": ")
                        self._loans[counter_loans].member = self._members[
                            option_member - 1]
                        self._books[option_book - 1].available = False
                    else:
                        print("The book is not available.")

                case App.ConstantsMenu.OPCION_CINCO:
                    print("Choose the book that is returned:")
                    self.print_list(self._loans)
                    option_returned_book: int = int(input(": "))

                    date: list[str] = []
                    expire_date: list[str] = []
                    date = App.SYSDATE.split('.')
                    expire_date = self._loans[option_returned_book -
                                              1].due_date.split('.')
                    if not (date[2] < expire_date[2] or (
                            date[1] < expire_date[1] and date[
                        2] == expire_date[2]) or (
                            date[0] <= expire_date[0] and date[1]
                            == expire_date[1] and date[2] ==
                            expire_date[2])):
                        print("The return date is late. We will remove this "
                              "member from the members list. They will be "
                              "able to renew their subscription in two weeks.")
                        self._members.pop(self._members.index(self._loans[
                                                    option_returned_book -
                                                    1].member))

                    self._loans[option_returned_book].return_date = App.SYSDATE

                case App.ConstantsMenu.OPCION_SEIS:
                    print("Choose the member you wanna remove:")
                    self.print_list(self._members)
                    option_member_remove: int = int(input(": "))
                    self._members.pop(option_member_remove - 1)
                    self.print_list(self._members)

                case App.ConstantsMenu.SALIDA:
                    print("¡Adios!")
                case _:
                    print("Incorrect number, try it again.")

    def print_list(self, elements_list):
        for index, element in enumerate(elements_list):
            if isinstance(element, Book):
                if element.title:
                    print(index + 1, '-', element)
            else:
                if element.name:
                    print(index + 1, '-', element)

    def register_publisher(self, counter):
        self._publishers[counter].name = input("Enter the name of the publisher: ")
        self._publishers[counter].address = input("Enter the address of the "
                                                  "publisher: ")

    def register_book(self, counter):
        self._books[counter].title = input("Enter the title of the book: ")
        self._books[counter].author = input("Enter the author of the book: ")
        self._books[counter].price = float(input("Enter the price of the "
                                                "book: "))

    def print_publisher_menu(self):
        print(f"To assign the publisher you can choose between the next "
              f"options:\n"
              f"1. Choose a existent one.\n"
              f"2. Introduce another publisher.")

    def register_member(self, counter):
        self._members[counter].name = input("Enter member's name: ")
        self._members[counter].address = input("Enter member's address: ")
        self._members[counter].member_type = input("Enter the member's type: ")

    def print_menu(self):
        print(f"{App.ConstantsMenu.OPCION_UNO}. Register a publisher.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Register a book.\n"
              f"{App.ConstantsMenu.OPCION_TRES}. Register a member.\n"
              f"{App.ConstantsMenu.OPCION_CUATRO}. Register a loan.\n"
              f"{App.ConstantsMenu.OPCION_CINCO}. Register a return.\n"
              f"{App.ConstantsMenu.OPCION_SEIS}. Remove a member.\n"
              f"{App.ConstantsMenu.SALIDA}. Exit.")

App().run()