"""
1 есть строка с именами разделенная пробелами "john marta james Morgan Adam Maria huang".
Преобразовать строку таким образом что бы каждое имя однозначно начиналось с большой буквы.
"""
names = "john marta james Morgan Adam Maria huang"
title_names = []

names_list = names.split(" ")
for name in names_list:
    name = name.title()
    title_names.append(name)
title_names_str = ' '.join(title_names)
print(f"Converted names string is: {title_names_str}")