"""
4 у вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"].
преобразовать его в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]
"""

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = []

for word in camel_case:
    for char in word:
        if char.isupper() is True:
            word = word.replace(char, '_' + char.lower())
            word = word.removeprefix('_')
    snake_case.append(word)
print(f'Converted CamelCase to snake_case is: {snake_case}')

# Interesting solution. As alternative could be solved with regular expression.
# some_list = ["FirstItem", "FriendsList", "MyTuple"]
# new_list = []

# for str_ in some_list:
#     new_list.append(re.sub('(?!^)([A-Z]+)', r'_\1', str_).lower())
