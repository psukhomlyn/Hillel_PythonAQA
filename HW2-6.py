"""
У вас есть группа людей с неуникальными именами.
Сформируйте список не повторяющихся имен (для этой задачи нельзя использовать set.
Если в списке есть 2 джона нужно взять лишь одного из них.
"John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow")
"""

people = ["John Dow", "John Adams", "Marta Adams", "John Dow", "Marta Stuard", "Marta Stuard"]
unique_names = []

for name in people:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)
# Good. Interesting solution but it could be done with dicts
# print(list({}.fromkeys(people).keys()))
