"""
У вас есть группа гостей для вип ложи. Места в вип ложе все заняты этими гостями.
Есть группа гостей в общем зале и места в нем все еще есть. Отобразите 2 группы гостей в коде.
"""

vip = ("John Snow", "Dina Watsons", "", "Karl Edwards")
common = ["Din Ambrose", "", "Oleg Vasin", "", "Anna Smith"]

guest_name = input("What is your name? ")

if guest_name == '':
    raise(ValueError)
elif guest_name in vip:
    vip_seat = vip.index(guest_name) + 1  # becaues index start from 0, seats start from 1
    print(f"{guest_name}, your seat is {vip_seat} in VIP zone")
else:
    common.insert(common.index(""), guest_name)
    common.remove("")
    common_seat = common.index(guest_name) + 1
    print(f"{guest_name}, your seat is {common_seat} in common zone")

print(f'Guests list in vip zone is: {vip}')
print(f'Guests list in common zone is: {common}')