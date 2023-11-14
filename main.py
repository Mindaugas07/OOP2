# class Calculator:

#     def __init__(self) -> None:
#         print("Hello instance!")
    
#     def add_two_numbers(self, numb_a: int, numb_b: int) -> int:
#         return numb_a + numb_b
    
#     def divide_two_numbers(self, numb_a: int, numb_b: int) -> int:
#         return numb_a / numb_b

#     def multiply_two_numbers(self, numb_a: int, numb_b: int) -> int:
#         return numb_a * numb_b

# calc = Calculator()
# print(calc.add_two_numbers(5, 2))

# print(calc.multiply_two_numbers(5, 2))

# class People:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

#     def get_name_and_surname(self):
#         return self.name + " " + self.surname


# if __name__ == "__main__":

#     person = People("Mindaugas", " Pavarde")
#     print(person.name)
#     print(person.get_name_and_surname())



# create a class which represents a car.

# class Car:

#     def __init__(self, model: str, made_date: int, engine: float) -> None:
#         self.model = model
#         self.made_date = made_date
#         self.engine = engine

#     def get_car_model(self) -> str:
#         return self.model

# car = Car(model = "Audi", made_date = 2023, engine = 2.0)

# print(car.get_car_model())
# print(car.model, car.made_date, car.engine)

# Create a class which represents your family. Class should take your mom,dad,sister ,broters names and ages.
# Create instance methods that would return :
#  - All names and ages as dict data structure
#  - The sum of all ages
#  - Would print the names depending on your relatives(sister,brother etc)
#  - Would list all family members from youngest to oldest (Choose return type by yourself.)


# class Family:

#     def __init__(self, mom_name: str, dad_name: str, sister_name: str, brother_name: str, mom_age: int, dad_age: int, sister_age: int, brother_age: int,) -> None:
#         self.mom_name = mom_name
#         self.dad_name = dad_name
#         self.sister_name = sister_name
#         self.brother_name = brother_name
#         self.mom_age = mom_age
#         self.dad_age = dad_age
#         self.sister_age = sister_age
#         self.brother_age = brother_age
    
#     def data_to_dict(self) -> dict:
#         try:
#             data_dict = {self.mom_name: self.mom_age, self.dad_name: self.dad_age, self.sister_name: self.sister_age , self.brother_name: self.brother_age}
#             return data_dict
#         except TypeError:
#             print("Dictionary key must be imutable!")
    
#     def sum_of_all_ages(self) -> int:
#         sum_ages = self.mom_age + self.dad_age + self.sister_age + self.brother_age
#         return sum_ages

#     def get_mom_name(self) -> str:
#         return self.mom_name

#     def get_dad_name(self) -> str:
#         return self.dad_name

#     def get_sister_name(self) -> str:
#         return self.sister_name

#     def get_brother_name(self) -> str:
#         return self.brother_name

#     def sorted_ages(self) -> list:
#         for item in sorted(self.data_to_dict(), key=self.data_to_dict().get):
#             print(item, self.data_to_dict()[item])
        

# if __name__ == "__main__":
#     family = Family(mom_name = "Ana", dad_name = "Jhon", sister_name = "Ona", brother_name = "Neo", mom_age = 39, dad_age = 38, sister_age = 18, brother_age = 40)
#     print(family.data_to_dict())
#     print(family.sum_of_all_ages())
#     family.sorted_ages()
#     print(family.get_mom_name())



# class Calculator:

#     def __init__(self, numb_a: [int, float], numb_b: [int, float]) -> None:
#         self.numb_a = numb_a
#         self.numb_b = numb_b
    
#     def add_two_numbers(self) -> [int, float]:
#         return self.numb_a + self.numb_b
    
#     def divide_two_numbers(self) -> [int, float]:
#         try:
#             return self.numb_a / self.numb_b
#         except ZeroDivisionError:
#             print("You cannot divide by 0!")

#     def multiply_two_numbers(self) -> [int, float]:
#         return self.numb_a * self.numb_b

#     def substract_two_numbers(self) -> [int, float]:
#         return self.numb_a - self.numb_b
    
# if __name__ == "__main__":
#     calc = Calculator(5.5, 0)
#     print(calc.add_two_numbers())

#     print(calc.divide_two_numbers())
#     print(calc.substract_two_numbers())


# class Employee:

#     def __init__(self, name: str, surname: str) -> None:
#         self.name: str = name
#         self.surname: str = surname
#         self.full_name: str = self.name + " " + self.surname
#         self.email: str = self.name.lower() + "." + self.surname.lower() + "@company.com"

# #     def get_full_name(self) -> str:
# #         return self.name + " " + self.surname
    
# #     def get_email(self) -> str:
# #         return self.name.lower() + "." + self.surname.lower() + "@company.com"
    
# if __name__ == "__main__":
#     employee_one = Employee("Algirdas", "Jogailaitis")
#     print(employee_one.full_name)
#     print(employee_one.email)


# class Book:

#     def __init__(self, title: str, author: str) -> None:
#         self.title: str = title
#         self.author: str = author

#     def get_title(self) -> str:
#         return "Title: " + self.title
    
#     def get_author(self) -> str:
#         return "Author: " + self.author

# if __name__ == "__main__":
#     PP = Book(title="Pride and Prejudice", author="Jane Austen (PP)")
#     H = Book(title="Hamlet", author="William Shakespeare (H)")
#     WP = Book(title="War and Peace", author="Leo Tolstoy (WP)")
#     print(PP.get_title())
#     print(PP.get_author())
#     print(PP.title)
#     print(PP.author)

class Country:
    def __init__(self, country_name: str, population: int, area: int) -> None:
        self.country_name: str = country_name
        self.population: int = population
        self.area: int = area
        if self.population > 20000000 or self.area > 3000000:
            self.is_big: bool = True
        else:
            self.is_big: bool = False

    # def is_big_or_not(self) -> bool:
    #     if self.population > 20000000 or self.area > 3000000:
    #         self.is_big = True
    def compare_pd(self, other_country: "Country") -> str:
        country_density = self.population / self.area 
        other_country_density = other_country.population / other_country.area
        if country_density > other_country_density:
            return f"{self.country_name} has a larger population density than {other_country.country_name}"
        else:
            return f"{self.country_name} has a smaller population density than {other_country.country_name}"


if __name__ == "__main__":
    australia = Country("Australia", 23545500, 7692024)
    andorra = Country("Andorra", 76098, 468)
    print(australia.is_big)
    print(andorra.is_big)
    print(andorra.compare_pd(australia))