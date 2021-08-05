"""
Создайте класс с описанием работника. Любого работника. Employee.
"""

class Employee:
    def __init__(self, name: str, age: int, male: bool, speciality: str):
        self.name = name
        self.age = age
        self.male = male # not sexism, just for use boolean type
        self.speciality = speciality


Worker: Employee = Employee("John Adams", 25, True, "Smith")


if __name__ == '__main__':
    print(Worker.name, Worker.age, Worker.male, Worker.speciality)
