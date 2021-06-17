"""
1. Создать переменные john_salary и marta_salary вещественного типа (с плавающей точкой).
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_salary = 1234.5
marta_salary = 9876.5
print(john_salary)
print(marta_salary)

"""
2. Создать переменные john_age и marta_age целочисленного типа.
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_age = 25
marta_age = 23
print(john_age)
print(marta_age)

"""
3. Создать переменные john_name и marta_name строкового типа.
Присвоить созданным переменным значения по своему усмотрению. Вывести в консоль методом print значения обеих переменных.
"""
john_name = "John Smith"
marta_name = "Marta Adams"
print(john_name)
print(marta_name)

"""
4. Создать переменные john_gender и marta_gender булевого типа.
Пусть john будет принимать истинное значение а marta ложное. Вывести в консоль методом print значения обеих переменных.
"""
john_gender = True
marta_gender = False
print(john_gender)
print(marta_gender)

"""
5. Создать переменные john_friends и marta_friends. Присвоить переменным списки.
Каждый список должен содержать имена друзей. У джона свой список друзей а у Марты свой.
Друзья (имя друга) могут быть обычные строки “James”, “Peter” и т. Д.
"""
john_friends = ["Peter", "Max", "Erik"]
marta_friends = ["Viktoria", "Dina", "Maria"]

"""
6. Создать список с именами людей, в нем должны повторяться некоторые имена.
Превратите список с повторяющимися именами в список уникальных имен используя множества.
"""
names_list = ["Max", "Ben", "Dirk", "Olga", "Stefan", "Ben", "Olga"]
names_set = set(names_list)
print(names_list)
print(names_set)

"""
7. Создайте 2 переменные типа кортеж. Кортеж должен состоять из 2 чисел с плавающей точкой.
Первое значение кортежа это широта в которой вы проживаете, а второе это долгота в которой вы проживаете.
"""
john_location = (50.01, 36.16)
marta_location = (39.55, 48.78)

"""
8. Создайте 2 переменные john, marta.
Переменные должны быть словарями с ключами: full_name, age, salary, gender, friends, coordinates. 
"""
john_dict = {'full_name': john_name, 'age': john_age, 'salary': john_salary, 'gender': john_gender, 'friends': john_friends, 'coordinates': john_location}
marta_dict = {'full_name': marta_name, 'age': marta_age, 'salary': marta_salary, 'gender': marta_gender, 'friends': marta_friends, 'coordinates': marta_location}
print(f"There is John's dict - {john_dict}")
print(f"There is Marta's dict - {marta_dict}")
