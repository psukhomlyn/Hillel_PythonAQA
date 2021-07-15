"""
Написать функцию is_prime, принимающую 1 аргумент — число от 2 до 1000,
и возвращающую True, если оно простое, и False - иначе.
"""


def is_prime(x):
    if x < 2 or x > 1000:
        return f'Number is out of range from 2 to 1000'
    else:
        if x <= 1 or x % 1 > 0:
            return f'Entered number is not prime'
        for i in range(2, x):
            if x % i == 0:
                return f'Entered number is not prime'
        return f'Entered number is prime'


print(is_prime(71))
