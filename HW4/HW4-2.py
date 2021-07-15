"""
2 есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"].
выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string.
Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
"""

friends = ["John", "Marta", "James", "Amanda", "Marianna"]

print("Names".center(20, '*'))
for name in friends:
    print(f'{name:>20}')

# Good but solve only using f string. Second solution also needed with
# str method
# -2 points