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
# el problema es que no me añade,
        # me sustituye, como hago que cada vez se cree otro objeto.

"""
        crear una lista de publishers y llevar un contador de cada uno,
        asi asignarle a tal posicion de la lista tal publisher y el id que
        sea el numero de contador.
"""

from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.member import Member
from ENDES.Ejercicio_11.lib.publisher import Publisher


class App:
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

    def run(self):
        pass

    def register_publisher(self, counter):
        self._publishers[counter].name = input("Enter the name of the publisher: ")
        self._publishers[counter].address = input("Enter the address of the "
                                                  "publisher: ")

    def register_book(self, counter):
        self._books[counter].title = input("Enter the title of the book: ")
        self._books[counter].author = input("Enter the author of the book: ")
        self._books[counter].price = input("Enter the price of the book: ")
        # publisher

    def register_member(self, counter):
        self._members[counter].name = input("Enter member's name: ")
        self._members[counter].address = input("Enter member's address: ")
        self._members[counter].member_type = input("Enter the price of the book: ")

    def print_menu(self):
        print(f"{App.ConstantsMenu.OPCION_UNO}. Register a publisher.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Register a book.\n"
              f"{App.ConstantsMenu.OPCION_TRES}. Register a member.\n"
              f"{App.ConstantsMenu.OPCION_CUATRO}. Register a load.\n"
              f"{App.ConstantsMenu.OPCION_CINCO}. Register a loan.\n"
              f"{App.ConstantsMenu.OPCION_SEIS}. Register a return.\n"
              f"{App.ConstantsMenu.SALIDA}. Exit.")
