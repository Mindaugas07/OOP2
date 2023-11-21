# class Vehicle:

#     def meen_of_transport(self) -> str:
#         return "This is vehicle"
    
# class Car(Vehicle):
#     def __init__(self, brand: str) -> None:
#         self.brand = brand

#     def get_brand(self) -> str:
#         return self.brand
    
# class Plane:
#     def __init__(self, price: int) -> None:
#         self.price = price

#     def get_price(self) -> str:
#         return self.price
    
# car = Car(brand="Audi")

# print(car.get_brand())
# print(car.meen_of_transport())

# class Employee:

#     def __init__(self, name: str, surname: str, age: int) -> None:
#         self.name: str = name
#         self.surname: str = surname
#         self.age: int = age

#     def get_employee_info(self) -> str:
#         return f"{self.name} {self.surname} {self.age} years old"
    

# class Engineer(Employee):

#     def __init__(self, position: str, name: str, surname: str, age: int) -> None:
#         super().__init__(name=name, surname=surname, age=age)
#         self.position: str = position
        

#     def get_engineer_postition(self) -> str:
#         return self.position
    
# person = Engineer(position= "Specialist", name="Algirdas", surname="Kestutaitis", age=45)
# print(person.get_employee_info())

# class Author:

#     def __init__(self, name: str, surname: str, genre: str) -> None:
#         self.name: str = name
#         self.surname: str = surname
#         self.genre: int = genre

#     def get_author_info(self) -> str:
#         return f"{self.name} {self.surname} prefers to write {self.genre} books"
    

# class Book(Author):

#     def __init__(self, style: str, length: int, name: str, surname: str, genre: str) -> None:
#         super().__init__(name=name, surname=surname, genre=genre)
#         self.style: str = style
#         self.length: int = length
        
#     def get_book_length(self) -> str:
#         return self.length
    
# book_two = Book(style= "Novel", length=256, name="Algirdas", surname="Kestutaitis", genre="Horror")
# print(book_two.get_author_info())



# class Energy:

#     def __init__(self, source: str, polution: int, ) -> None:
#         self.source: str = source
#         self.polution: int = polution

#     def get_polution(self) -> int:
#         return f"{self.source} enegy produces {self.polution} polution"   


# class Renewable(Energy):

#     def __init__(self, structure: str,  source: str, polution: int) -> None:
#         super().__init__(source=source, polution=polution)
#         self.structure = structure
        
#     def get_structure_of_energy(self) -> str:
#         return self.structure
    
# solar_panel = Renewable(structure="Panel", source="Sun", polution=0)

# print(solar_panel.get_polution())


# Create a base class called Book with attributes like title, author, and publication_year.
# This class should have a method called display_info that prints basic information about the book.

# Create two subclasses of Book called Fiction and NonFiction. Add an additional attribute to each subclass,
# such as genre for Fiction and subject for NonFiction.

# Create two more subclasses, Mystery and History, that inherit from Fiction and NonFiction, respectively.
# Add specific attributes to each of these subclasses (e.g., detective for Mystery and time_period for History).

# Add in each sub class methods to retreive provided data.


class Book:
    def __init__(self, title: str, author: str, publication_year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.publication_year: int = publication_year

    def display_info(self) -> str:
        return f"{self.author} wrote a book '{self.title}' in {self.publication_year}"
    
class Fiction(Book):
    def __init__(self, genre: str, title: str, author: str, publication_year: int) -> None:
        super().__init__(title=title, author=author, publication_year=publication_year)
        self.genre = genre

    def get_genre(self) -> str:
        return self.genre

class NonFiction(Book):
    def __init__(self, subject: str, title: str, author: str, publication_year: int) -> None:
        super().__init__(title, author, publication_year)
        self.subject = subject

    def get_subject(self) -> str:
        return self.subject

class Mystery(Fiction):
    def __init__(self, detective: bool, genre: str, title: str, author: str, publication_year: int) -> None:
        super().__init__(genre=genre, title=title, author=author, publication_year=publication_year)
        self.detective: bool = detective

    def is_detective(self):
        return f"The book '{self.title}' is detective: {self.detective}"

class History(NonFiction):
    def __init__(self, time_period: int, subject: str, title: str, author: str, publication_year: int) -> None:
        super().__init__(subject=subject, title=title, author=author, publication_year=publication_year)
        self.time_period = time_period

    def get_time_period_of_the_book(self) -> str:
        return f"Book '{self.title}' wich was written by {self.author} is from {self.time_period} time period"


history_book = History(time_period=1939, subject="WW2", title="Winter is coming", author="Kestutis Jogailaitis", publication_year=2022)
mystery_book = Mystery(detective=False, genre="Docu", title="Chess for dummies", author="Jonas Jonsonas", publication_year=2014)
print(history_book.display_info())
print(mystery_book.get_genre())
print(mystery_book.is_detective())
print(history_book.get_time_period_of_the_book())
