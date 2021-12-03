from datetime import date

class Student:
    def __init__(self, name: str, marks: int) -> None:
        self._name = name
        self._marks = marks

    def __str__(self) -> str:
        return f"{self._name} z oceną {self._marks}"


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._open_hours = open_hours
        self._phone = phone

    def __str__(self) -> str:
        return f"w mieście {self._city}, na ulicy {self._street}, " \
               f"kod pocztowy {self._zip_code}." \
               f" Jest otwarta w godzinach {self._open_hours}. W razie kontaktu," \
               f" nr telefonu to: {self._phone}"


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: date,
                 birth_date: date, city: str, street: str, zip_code: str,
                 phone: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._hire_date = hire_date
        self._birth_date = birth_date
        self._city = city
        self._street = street
        self._zip_code = zip_code
        self._phone = phone

    def __str__(self) -> str:
        return f"{self._first_name} {self._last_name} został zatrudniony " \
               f"{self._hire_date}, urodził się {self._birth_date}. " \
               f"Mieszka w  {self._city}ie, na ulicy {self._street}, " \
               f"kod pocztowy {self._zip_code},"


class Book:
    def __init__(self, library: Library, publication_date: date,
                 author_name: str, author_surname: str, number_of_pages: int) -> None:
        self._library = library
        self._publication_date = publication_date
        self._author_name = author_name
        self._author_surname = author_surname
        self._number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Książka dostępna w bibliotece {self._library}, " \
               f"napisana przez {self._author_name} {self._author_surname}, " \
               f"wydana {self._publication_date}, zawiera {self._number_of_pages} stron"


class Order:
    def __init__(self, employee: Employee, student: Student, books: list[Book], order_date: date) -> None:
        self._employee = employee
        self._student = student
        self._books = books
        self._order_date = order_date

    def __str__(self) -> str:
        return "Pracownik {} obsłużył studenta {}. Zamówienie z dnia " \
               "{} na {}.".format(self._employee, self._student, self._order_date, *self._books)


library1 = Library("Lublin", "Warszawska", "12345", "8-16", "123456789")
library2 = Library("Krakow", "Kasztanowa", "98765", "7-15", "987654321")

student1 = Student("Lusia", 60)
student2 = Student("Zosia", 10)
student3 = Student("Zbigniew", 77)

employee1 = Employee("Marian", "Lizak", date(2019, 12, 11),
                     date(1999, 1, 12), "Lublin", "Zosinska", "32145", "456987432")
employee2 = Employee("Magda", "Sasinska",
                     date(2018, 6, 4), date(1998, 12, 19), "Lublin", "Mariacka", "76523", "456987432")
employee3 = Employee("Lukasz", "Kisiel",
                     date(2010, 9, 8), date(1996, 5, 6), "Krakow", "Wislana", "43278", "456987432")

book1 = Book(library2, date(2021, 11, 13), "Rafael", "Miguel", 251)
book2 = Book(library1, date(2019, 10, 19), "Witold", "Marciniak", 53)
book3 = Book(library2, date(2016, 3, 26), "Wiola", "Bieniek", 396)
book4 = Book(library1, date(1996, 7, 1), "Katarzyna", "Kosciniec", 123)
book5 = Book(library2, date(2018, 9, 30), "Monika", "Wawrzacz", 543)

order1 = Order(employee1, student2, [book1, book3], date(2021, 11, 22))
order2 = Order(employee3, student1, [book2, book4, book5], date(2021, 11, 21))

print(order1)
print(order2)
