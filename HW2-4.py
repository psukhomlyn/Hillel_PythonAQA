"""
У вас есть две группы людей. В одной группе состоят всеядные люди в другой лишь вегетарианцы.
Всеядный является вегетарианцем но вегетарианец не является всеядным.
Вывести список гостей которые могут есть овощи и зелень.
"""

vegetarians = ["John Dow", "Frank White", "Viky Benky"]
omnivores = ["Ernie May", "Charlie Black", "Peter Waters"]
guests = []

# как я понял задачу нам нужно создать новый список, а не модифицировать уже данные.
# т.к. люди от этого не перестают быть всеядными и вегетариацами.

for veg in vegetarians:
    guests.append(veg)  # add vegetarians to guests list
for omn in omnivores:
    guests.append(omn)  # add omnivores to guests list

print(f'The list of guests who eat vegetables are: {guests}')
# Good it is also will work but lets look on solution with syntax sugar^
# print(vegetarians + omnivores)
