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

# class Country:
#     def __init__(self, country_name: str, population: int, area: int) -> None:
#         self.country_name: str = country_name
#         self.population: int = population
#         self.area: int = area
#         if self.population > 20000000 or self.area > 3000000:
#             self.is_big: bool = True
#         else:
#             self.is_big: bool = False

#     # def is_big_or_not(self) -> bool:
#     #     if self.population > 20000000 or self.area > 3000000:
#     #         self.is_big = True
#     def compare_pd(self, other_country: "Country") -> str:
#         country_density = self.population / self.area 
#         other_country_density = other_country.population / other_country.area
#         if country_density > other_country_density:
#             return f"{self.country_name} has a larger population density than {other_country.country_name}"
#         else:
#             return f"{self.country_name} has a smaller population density than {other_country.country_name}"


# if __name__ == "__main__":
#     australia = Country("Australia", 23545500, 7692024)
#     andorra = Country("Andorra", 76098, 468)
#     print(australia.is_big)
#     print(andorra.is_big)
#     print(andorra.compare_pd(australia))

# Create a Python class named Fraudster with the following attributes:
# email_domain: A string representing the email domain associated with fraudulent activities (e.g., "@gmail.com").
# amount: An integer representing the total amount fraudulently approved.
# number_of_users: An integer representing the number of users associated with the specified email domain.
# Implement two methods within the class:
# fraud_amount_by_domain(): This method should return a string indicating the amount that was fraudulently received with the specified email domain.
# users_by_domain(): This method should return a string indicating the number of users using the specified email domain.
# initiate three classes:
# Spain_fraud -> email_domain="@gmail.com", amount=100000, number_of_users=5
# French_fraud -> email_domain="@yahoo.com", amount=453295, number_of_users=19
# Latin_america_fraud = "@yandex.ru", amount=1036594, number_of_users=2
 
# implement methods created in the class to return various information about these fraud rings

# class Fraudster:
#     def __init__(self, email_domain: str, amount: int, number_of_users: int) -> None:
#         self.email_domain = email_domain
#         self.amount = amount
#         self.number_of_users = number_of_users

#     def fraud_amount_by_domain(self) -> str:
#         return f"{self.amount} times {self.email_domain} was used fraudulently"
    
#     def users_by_domain(self) -> str:
#         return f"{self.number_of_users} users using the {self.email_domain} email domain"

    
# if __name__ == "__main__":
#     spain_fraud = Fraudster(email_domain="@gmail.com", amount=100000, number_of_users=5)
#     french_fraud = Fraudster(email_domain="@yahoo.com", amount=453295, number_of_users=19)
#     latin_america_fraud = Fraudster(email_domain="@yandex.ru", amount=1036594, number_of_users=2)
#     print(spain_fraud.fraud_amount_by_domain())
#     print(french_fraud.users_by_domain())

# 1. Create class Country which takes 2 arguments (country_name, population).
#   Create methods to return:
#   1) country name
#   2) Population
#   3) How many letters are in country name 
#   4) Get population status: (if population is less than 5 million that mean low, more or equal to 5 millions and less than 10 millions means average, else high.

# class Country:
#     def __init__(self, country_name: str, population: int) -> None:
#         self.country_name = country_name
#         self.population = population

#     def get_country(self) -> str:
#         return self.country_name
    
#     def get_population(self) -> str:
#         return self.population
    
#     def get_country_name_letter_number(self) -> str:
#         return len(self.country_name)
    
#     def population_status(self) -> str:
#         if self.population < 5000000:
#             return f"Population of {self.country_name} is low"
#         elif self.population < 10000000:
#             return f"Population of {self.country_name} is laverage"
#         else:
#             return f"Population of {self.country_name} is high"
        
# if __name__ == "__main__":
#     lietuva = Country("Lithuania", 3000000)
#     print(lietuva.get_country())
#     print(lietuva.get_population())
#     print(lietuva.get_country_name_letter_number())
#     print(lietuva.population_status())




#2. Create a program that user enters name, surname, email_provider, age (example: Thom, Nelson, gmail, 12 )
# Program should list options to choose:
#  - Generate some email variants from all data provided
#  - Get year of birth 
#  - Return all personal info (including generic email and year of birth)


# Must use class for dealing with data. Error handling, types. Input should be invoked as a script (if __name__ ....)


# class People:
#     CURRENT_YEAR = 2023

#     def __init__(self, person_ditc=None) -> None:
#         if person_ditc is not None:
#             for key, value in person_ditc.items():
#                 setattr(self, key, value)

#     def generate_email(self) -> str:
#         return f"{self.name.lower()}{self.surname.lower()}@{self.email_provider.lower()}.com"




    
# if __name__ == "__main__":

#     def user_input_to_dict():
#         person_string = input("Please enter your name, surname, email_provider, age (example: Thom, Nelson, gmail, 12): ")
#         person_dict = {"name": "", "surname": "", "email_provider": "", "age": ""}
#         for index, key in enumerate(person_dict):
#             person_dict[key] = person_string.replace(" ", "").split(",")[index]
#         return person_dict

# person = People(user_input_to_dict())
# print(person.generate_email())
  

# class Person:
#     CURRENT_YEAR: int = 2023

#     def __init__(self, name: str, surname: str, email_provider: str, age: int) -> None:
#         self.name = name
#         self.surname = surname
#         self.email_provider = email_provider
#         self.age = age

#     def email_generator(self) -> str:
#         return f"Some email variants for you:\n{self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\n{self.surname.lower()}.{self.age}.{self.name.lower()}@{self.email_provider.lower()}"

#     def get_year_of_birth(self) -> int:
#         return self.CURRENT_YEAR - self.age

#     def get_personal_info(self) -> str:
#         return f"Name: {self.name}\nSurname: {self.surname}\nEmail: {self.name.lower()}.{self.surname.lower()}@{self.email_provider.lower()}\nAge: {self.age}"


# def main_menu(person_info: str) -> None:
#     person_info_list = person_info.replace(" ", "").split(",")
#     name = person_info_list[0]
#     surname = person_info_list[1]
#     email_provider = person_info_list[2]
#     age = int(person_info_list[3])

#     person = Person(
#         name=name,
#         surname=surname,
#         email_provider=email_provider,
#         age=age,
#     )
#     menu_entries: str = "\n1. Generate some email variants\n2. Get year of birth\n3. Return all personal info\n4. End program.\nPlease enter number of your selection: "

#     while True:
#         menu_select: str = input(menu_entries)
#         print()

#         if menu_select.isnumeric() == True:
#             if menu_select == "1":
#                 print(person.email_generator())
#             elif menu_select == "2":
#                 print(person.get_year_of_birth())
#             elif menu_select == "3":
#                 print(person.get_personal_info())
#             elif menu_select == "4":
#                 print("Bye")
#                 break
#             else:
#                 print("There is no such selection.")
#         else:
#             print(
#                 "Please enter number from list provided without any symbols and spaces."
#             )


# if __name__ == "__main__":
#     person_info: str = input(
#         "Enter name, surname, email_provider, age (example: Thom, Nelson, gmail, 12 ): "
#     )

#     try:
#         main_menu(person_info)
#     except Exception as err:
#         print(f"You've got an {err} error.")    

# class Person:
#     def __init__(self, name: str, surname: str) -> None:
#         self.name = name
#         self.surname = surname

# human = Person(name="Kestutis", surname="Algirdaitis")
# human.name = "Jogaila"
# print(human.name)
