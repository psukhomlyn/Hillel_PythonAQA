"""
у вас есть список элементов [1, 2, 3, 4, 5, 6, 7, 8]. Перебрать список используя foreach цыкл.
Элемент с нечетным индексом поместить в новый список кортежей где первый элемент это индекс а второй это значение. [(index, value)].
соответственно элементы с четным индексом поместить в другой список кортежей с тем же форматом что и в случае с нечетными индексами.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_index = []
odd_index = []

# for digit in numbers:  #for each loop
#     if numbers.index(digit) % 2 == 0:
#         even_index.append((numbers.index(digit), digit))
#     else:
#         odd_index.append((numbers.index(digit), digit))
#
# print(f'Elements on even indexes are: {even_index}')
# print(f'Elements on odd indexes are: {odd_index}')

for index in range(len(numbers)):  #for loop
    if index % 2 == 0:
        even_index.append((index, numbers[index]))
    else:
        odd_index.append((index, numbers[index]))

print(f'Elements on even indexes are: {even_index}')
print(f'Elements on odd indexes are: {odd_index}')






