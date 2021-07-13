"""
Используя созданный файл в задаче 1 прочитать файл и произвести математические операции над каждым элементом.
Результат операции вывести в консоль.
Использовать импорты для импортирования из модуля первой задачи нельзя.
"""
result = 0  # i am not really sure why this variable is needed
with open("test/data/tuples_list.txt", mode="r") as file:
    file_data = file.read()
    #print(file_data.split('\n'))
rows_list = file_data.split('\n')
for row in rows_list:
    row_edited = row.replace('"', '').split("  ")
    if len(row_edited) < 3:
        continue
    if int(row_edited[2]) == 1:
        result = int(row_edited[0]) + int(row_edited[1])
    if int(row_edited[2]) == 2:
        result = int(row_edited[0]) - int(row_edited[1])
    if int(row_edited[2]) == 3:
        result = int(row_edited[0]) * int(row_edited[1])
    print(result)

# not bad but it could be written easier. Take a look on pickle module which
# I have show on lesson 5
# -1 point fro dirty code
# TODO: rows_list - name is overheaded since we already know that it is list.
#        I suggest to rename it on lines or rows.
# TODO: this block could be simplefied
#     if int(row_edited[2]) == 1:
#         result = int(row_edited[0]) + int(row_edited[1])
#     if int(row_edited[2]) == 2:
#         result = int(row_edited[0]) - int(row_edited[1])
#     if int(row_edited[2]) == 3:
#         result = int(row_edited[0]) * int(row_edited[1])
#         ------------------------------------------
#     left, right, operator = row_edited
#     if operator == '1':
#         print(int(left_operand) + int(right_operand))
#     elif operator == '2':
#         print(int(left_operand) - int(right_operand))
#     elif operator == '3':
#         print(int(left_operand) * int(right_operand))
# It is look cleaner then before but better will be to use pickle module
# TODO: resolve warning below^
#  HW5-2.py:2:80: E501 line too long (109 > 79 characters)
#  HW5-2.py:9:5: E265 block comment should start with '# '
