"""
Создать список кортежей длинной в 100 элементов где каждый кортеж состоит из 3 элементов:
1 элемент это целое число которое будет левым операндом выражения
2 элемент это целое число которое будет правым операндом выражения
3 элемент это целое число от 1 до 3 где:
1 идентифицирует операцию сложения
2 идентифицирует операцию вычитания
3 идентифицирует операцию умножения
Поместить данные в текстовый файл можно текстом можно через пикл модуль в двоичном виде.
Если поместили текстом тогда каждая строка должна содержать лишь элементы одного кортежа разделенные пробелом (например "100 2 3").
Файл необходимо создать скриптом в заранее созданное древо каталога \test\data.
Древо каталогов создавать скриптом. Пушить в репозиторий только код.
"""
import random

with open("test/data/tuples_list.txt", mode="w") as file:
    for item in range(100):
        my_tuple = ((random.randrange(1, 101), random.randrange(1, 101), random.randrange(1, 4)))
        file.write(str(my_tuple).replace(')', '"\n').replace(',', ' ').replace('(', '"'))


# Good but we don't know anything about comprehensions yet) -1 point
# Too complicated and value should be in next format in file in each line:
# left_operand right_operand operation\n
# -2 points - for not correct solution
# -1 point for dirty code
# -1 point for file in repository

# TODO: fix next warnings:
#   HW5-1.py:2:80: E501 line too long (89 > 79 characters)
#   HW5-1.py:9:80: E501 line too long (88 > 79 characters)
#   HW5-1.py:10:80: E501 line too long (131 > 79 characters)
#   HW5-1.py:18:80: E501 line too long (97 > 79 characters)
#   HW5-1.py:19:80: E501 line too long (89 > 79 characters)

