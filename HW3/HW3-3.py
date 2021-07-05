"""
У вас есть 2 списка имен friends = ["John", "Marta", "James"] и enamies = ["John", "Johnatan", "Artur"].
Перебрать имена друзей и написать сообщение f"{friend} we are the best friends" если друг не оказался в списке имен врагов.
И вывести сообщение f"{friend} we are not the friends anymore" если друг оказался в списке врагов.
Если имя друга James не проверяем его ибо он лучшый друг.
"""

friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for friend in friends:
    if friend == "James":
        continue  # for skip check for James. James should not be checked according to task description.
    elif friend not in enemies:
        print(f"{friend} we are the best friends")
    else:
        print(f"{friend} we are not the friends anymore")
