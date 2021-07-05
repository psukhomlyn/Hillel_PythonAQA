"""
2 есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"].
выведите в консоль имена каждое с новой строки выровняв по правой стороне используя метод строки и форматирование через f string.
Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное пространство заполнено скажем символом "*"
"""

friends = ["John", "Marta", "James", "Amanda", "Marianna"]

print("Names".center(25, '*'))
for name in friends:
    formatted_name = name.rjust(25, " ")
    print(f"{formatted_name}")
