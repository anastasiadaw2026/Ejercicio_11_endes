from ENDES.Ejercicio_11.lib.book import Book
from ENDES.Ejercicio_11.lib.loan import Loan
from ENDES.Ejercicio_11.lib.member import Member
from ENDES.Ejercicio_11.lib.publisher import Publisher


class App:
    """
    Main application class for managing a library system.

    The `App` class integrates the core system functionalities, such as handling
    publishers, books, members, and loans. It provides methods for registering
    new entities, managing loans, and defining the application's main workflow.

    :ivar counter_books: Counter for registered books.
    :vartype counter_books: int
    :ivar counter_publishers: Counter for registered publishers.
    :vartype counter_publishers: int
    :ivar counter_members: Counter for registered members.
    :vartype counter_members: int
    :ivar counter_loans: Counter for registered loans.
    :vartype counter_loans: int
    :ivar _publishers: List of all registered publishers.
    :vartype _publishers: list[Publisher]
    :ivar _books: List of all registered books.
    :vartype _books: list[Book]
    :ivar _members: List of all registered members.
    :vartype _members: list[Member]
    :ivar _loans: List of all registered loans.
    :vartype _loans: list[Loan]
    """

    class ConstantsDate:
        """
        Stores constant values related to dates.

        :cvar SYSDATE: System date representing the current date in the format DD.MM.YYYY.
        :vartype SYSDATE: str
        """
        SYSDATE: str = '30.03.2026'

    class ConstantsMenu:
        """
        Stores constant values for menu options.

        :cvar SALIDA: Option number for exiting the application.
        :vartype SALIDA: int
        :cvar OPCION_UNO: Menu option for registering a publisher.
        :vartype OPCION_UNO: int
        :cvar OPCION_DOS: Menu option for registering a book.
        :vartype OPCION_DOS: int
        :cvar OPCION_TRES: Menu option for registering a member.
        :vartype OPCION_TRES: int
        :cvar OPCION_CUATRO: Menu option for registering a loan.
        :vartype OPCION_CUATRO: int
        :cvar OPCION_CINCO: Menu option for registering a return.
        :vartype OPCION_CINCO: int
        :cvar OPCION_SEIS: Menu option for removing a member.
        :vartype OPCION_SEIS: int
        """
        SALIDA: int = 7
        OPCION_UNO: int = 1
        OPCION_DOS: int = 2
        OPCION_TRES: int = 3
        OPCION_CUATRO: int = 4
        OPCION_CINCO: int = 5
        OPCION_SEIS: int = 6

    def __init__(self):
        """
        Initializes the application.

        Initializes all counters and lists for managing publishers, books, members,
        and loans.
        """
        self.counter_books: int = -1
        self.counter_publishers: int = -1   
        self.counter_members: int = -1
        self.counter_loans: int = -1
        self._publishers: list[Publisher] = []
        self._books: list[Book] = []
        self._members: list[Member] = []
        self._loans: list[Loan] = []

    def run(self) -> None:
        """
        Runs the application's main loop.

        Continuously displays the main menu and processes user input
        until the exit option is selected.

        :return: None
        """
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

    def add_member(self) -> None:
        """
        Adds a new member to the system.

        The method increments the member counter, initializes a new `Member`
        object, appends it to the member list, and prompts the user to input
        member details.

        :return: None
        """
        self.counter_members += 1
        self._members.append(Member(self.counter_members + 1))
        self.register_member()

    def add_book(self) -> None:
        """
        Adds a new book to the system.

        Increments the book counter, initializes a new `Book` object, appends
        it to the book list, prompts the user to input book details, and assigns
        a publisher to the book.

        :return: None
        """
        self.counter_books += 1
        self._books.append(Book(self.counter_books + 1))
        self.register_book()
        self.print_publisher_menu()
        self.assign_publisher_book()

    def remove_member(self) -> None:
        """
        Removes a specific member from the system.

        Prompts the user to select a member from the list and removes the
        selected member.

        :return: None
        """
        option_member_remove: int = 0
        print("Choose the member you wanna remove:")
        self.print_list(self._members)
        option_member_remove = int(input(": "))
        self._members.pop(option_member_remove - 1)

    def register_return(self) -> None:
        """
        Registers the return of a borrowed book.

        When a book is returned, it updates the associated `Loan` object, sets
        the book's return date, and marks the book as available.

        :return: None
        """
        option_returned_book: int = 0
        print("Choose the book that is returned:")
        self.print_list(self._loans)
        option_returned_book = int(input(": "))
        self.check_return_date(option_returned_book)
        self._loans[option_returned_book - 1].return_date = App.ConstantsDate.SYSDATE
        self._books[option_returned_book - 1].available = True

    def check_return_date(self, option_returned_book: int) -> None:
        """
        Checks whether the returned book was overdue.

        If the book is overdue, removes the borrowing member as a penalty and
        informs the user.

        :param option_returned_book: Index of the returned book in the loan list.
        :type option_returned_book: int
        :return: None
        """
        date: list[str] = []
        expire_date: list[str] = []
        date = App.ConstantsDate.SYSDATE.split('.')
        expire_date = self._loans[option_returned_book - 1].due_date.split('.')
        if not (date[2] < expire_date[2] or (date[1] < expire_date[1]
                and date[2] == expire_date[2]) or (date[0] <= expire_date[0]
                and date[1] == expire_date[1] and date[2] == expire_date[2])):
            self.remove_unpunctual_member(option_returned_book)

    def remove_unpunctual_member(self, option_returned_book: int) -> None:
        """
        Removes a member from the members list if they have returned a book later
        than the due date. This action applies a penalty by removing their membership
        temporarily. The member can renew their subscription in two weeks.

        :param option_returned_book: The option number corresponding to the book
            that was returned late.
        :type option_returned_book: int
        :return: None
        """
        self._members.pop(self._members.index(self._loans[
                                            option_returned_book - 1].member))
        print("The return date is late. We removed this member from the "
              "members list. They will be able to renew their subscription "
              "in two weeks.")

    def create_loan(self) -> None:
        """
        Creates a loan entry by managing books and members registration
        and assigning loans.

        The method first checks if any existing books are available to
        register for a loan. If books are not pre-registered, it initiates
        a registration for new book loans. Subsequently, it handles members
        and loans assignment, depending on the prior registration statuses
        of books and members.

        :return: None
        """
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

    def register_existing_book_loan(self) -> None:
        """Registers a loan for an existing, available book by user selection.

        This method retrieves the list of books that are available for borrowing,
        displays them to the user, and then allows the user to select one for loan.
        The selected book is then processed for a loan assignment using another
        method call.

        :return: None
        """
        option_book: int = 0
        available_books = [x for x in self._books if x.available]
        print("Choose the book you want to borrow:")
        self.print_list(available_books)
        option_book = int(input(": "))
        self.assign_book_loan(option_book, available_books)

    def register_element(self, element_type: Member | Book) -> None:
        """
        Register an element based on the provided type.

        This method allows for registering an element of the specified type
        (Member or Book) into the system. Users have the option to cancel
        the loan or register a new element. If registering a new element, it
        handles the addition of either a Book or Member based on the provided
        `element_type`. Input validations are performed to ensure correct
        user interaction.

        :param element_type: The type of element to be registered; could be
            either Member or Book.
        :type element_type: Member | Book
        :return: None
        """
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

    def assign_book_loan(self, option_book: int, available_books: list) -> None:
        """
        Assigns a book for a loan and updates its availability.

        This method assigns a selected book from the available books to a loan.
        It retrieves the position of the selected book in the list of books,
        assigns it to the current loan, and then marks that book as
        unavailable.

        :param option_book: Index (1-based) representing the chosen book
            from the available books.
        :type option_book: int
        :param available_books: List of book objects currently available for loan.
        :type available_books: list
        :return: None
        """
        position = self._books.index(available_books[option_book - 1])
        self._loans[self.counter_loans].book = self._books[position]
        self._books[position].available = False

    def assign_member_loan(self) -> None:
        """
        Assigns a loan to a member from the members list.

        This function allows assigning a loan to a specific member from the list
        of available members. The user is prompted to choose a member by inputting
        the corresponding number from the displayed list. The selected member is
        then assigned to the loan corresponding to the current loan counter.

        :return: None
        """
        option_member: int = 0
        print("Choose who wants to borrow it:")
        self.print_list(self._members)
        option_member = int(input(": "))
        self._loans[self.counter_loans].member = self._members[option_member - 1]

    def assign_publisher_book(self) -> None:
        """
        Assigns a publisher to a book based on user input.

        This method prompts the user to select an option and performs one of the
        following actions:
        - Chooses an existing publisher if available.
        - Adds a new publisher and assigns it to the corresponding book.
        - Handles invalid inputs by recursively re-running the process.

        :return: None
        """
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

    def choose_publisher(self) -> None:
        """
        Allows the user to choose a publisher from a list, and assigns it to a book.

        The method displays a list of publishers for the user to choose from. Once
        the user selects a publisher by entering an option number, the chosen
        publisher is assigned to a specific book.

        :return: None
        """
        option_publisher: int = 0
        print("Choose a number:")
        self.print_list(self._publishers)
        option_publisher = int(input(": "))
        self._books[self.counter_books].publisher = (self._publishers[
            option_publisher - 1])

    def add_publisher(self) -> None:
        """
        Adds a new publisher to the list of publishers.

        This method increments the counter for publishers, adds a new Publisher
        instance to the internal list, and registers the new publisher.

        :return: None
        """
        self.counter_publishers += 1
        self._publishers.append(Publisher(self.counter_publishers + 1))
        self.register_publisher()

    def print_list(self, elements_list: list) -> None:
        """
        Prints each element in a given list along with its position.

        This function iterates through a list of elements provided as input,
        and prints each element prefixed with its 1-based index. If the list
        is empty, it outputs a message indicating no data is available.

        :param elements_list: A list of elements to be printed.
        :type elements_list: list
        """
        if elements_list:
            for index, element in enumerate(elements_list):
                print(index + 1, '-', element)
        else:
            print("No data found")

    def register_publisher(self) -> None:
        """
        Registers a new publisher with a name and address.

        This method allows for the input and storage of publisher details,
        such as name and address, which are stored in the respective fields.

        :return: None
        """
        self._publishers[self.counter_publishers].name = input("Enter the "
                                                    "name of the publisher: ")
        self._publishers[self.counter_publishers].address = input("Enter"
                                            "the address of the publisher: ")

    def register_book(self) -> None:
        """
        Registers a new book by accepting user input for title, author, and price.

        This method takes user input and sets the book's details, including title,
        author, and price, into the respective attributes of the book instance.

        :return: None
        """
        self._books[self.counter_books].title = input("Enter the title of the "
                                                "book: ")
        self._books[self.counter_books].author = input("Enter the author of the book: ")
        self._books[self.counter_books].price = float(input("Enter the price of the "
                                                "book: "))

    def register_member(self) -> None:
        """
        Registers a new member with their details.

        This method collects the name, address, and member type of a new member
        via user input and stores these details in the internal members' storage.

        :return: None
        """
        self._members[self.counter_members].name = input("Enter member's name: ")
        self._members[self.counter_members].address = input("Enter member's address: ")
        self._members[self.counter_members].member_type = input("Enter the member's type: ")

    def print_publisher_menu(self) -> None:
        """
        Prints the menu for assigning a publisher.

        This method displays options for assigning a publisher. If publishers are
        available, the user is allowed to either select an existing publisher or
        add a new one. If no publishers are currently registered, the method
        prompts the user to register a new publisher.

        :return: None
        """
        print(f"To assign the publisher: ")
        if self._publishers:
            print(f"{App.ConstantsMenu.OPCION_UNO}. Choose a existent one.\n"
                  f"{App.ConstantsMenu.OPCION_DOS}. Introduce another "
                  f"publisher.")
        else:
            print("     No publisher is registered at the moment. Press 2 to "
                  "register one.")

    def print_menu(self) -> None:
        """
        Display the main application menu.

        This method prints the list of available options for the user,
        including actions such as registering entities (publisher, book,
        member), managing loans and returns, and exiting the application.

        The menu options are dynamically generated using constants defined
        in ``App.ConstantsMenu``.

        :return: None
        """
        print(f"{App.ConstantsMenu.OPCION_UNO}. Register a publisher.\n"
              f"{App.ConstantsMenu.OPCION_DOS}. Register a book.\n"
              f"{App.ConstantsMenu.OPCION_TRES}. Register a member.\n"
              f"{App.ConstantsMenu.OPCION_CUATRO}. Register a loan.\n"
              f"{App.ConstantsMenu.OPCION_CINCO}. Register a return.\n"
              f"{App.ConstantsMenu.OPCION_SEIS}. Remove a member.\n"
              f"{App.ConstantsMenu.SALIDA}. Exit.")

App().run()