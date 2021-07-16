"""
2. Написать функцию square, принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа): периметр квадрата,
площадь квадрата и диагональ квадрата.
"""


def square(a):
    return (f'perimeter = {a * 4},'
            f'square = {a **2},'
            f'diagonal = {a * pow(2, 1/2)}'
            )

print(square(10))
print(type(square(10)))

# Interesting solution. It would be nice declare which arguments you expect
# and what will be returned
# For now function returns string but should tuple
# -2 points
