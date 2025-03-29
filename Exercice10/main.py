class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        return f"Nom : {self.name}, Age : {self.age}"


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        return f"Nom : {self.name}, Age : {self.age}, Salaire : {self.salary}"
