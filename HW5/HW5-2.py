"""
Используя созданный файл в задаче 1 прочитать файл и произвести математические операции над каждым элементом.
Результат операции вывести в консоль.
Использовать импорты для импортирования из модуля первой задачи нельзя.
"""
result = 0
with open("test/data/tuples_list.txt", mode="r") as file:
    file_data = file.read()
    #print(file_data.split('\n'))
rows_list = file_data.split('\n')
for row in rows_list:
    row_edited = row.replace('"', '').split("  ")
    for element in row_edited:
        if int(row_edited[2]) == 1:
           result = int(row_edited[0]) + int(row_edited[1])
        if int(row_edited[2]) == 2:
           result = int(row_edited[0]) - int(row_edited[1])
        if int(row_edited[2]) == 3:
           result = int(row_edited[0]) * int(row_edited[1])
    print(result)