"""
У вас есть 3 группы людей bigno_blacklist, poker_blacklist, majong_blacklist.
Имена людей в формате "John Dow" первое и второе имя. Найти тех кто состоит во всех черных списках.
"""

bingo_blacklist = {'John Smith', 'Adam Silver', 'Erik Dier', 'Marta Adams'}
poker_blacklist = {'George Washignton', 'Marta Adams', 'Frank Smith', 'John Smith'}
majong_blacklist = {'John Smith', 'Ben Aflek', 'Marta Adams', 'Marta Williams'}

blacklist_players = bingo_blacklist.intersection(poker_blacklist).intersection(majong_blacklist)
print(f'People who are in all blacklists are: {black_users}')
# Good. But you can move all set into the intersaction
# bingo_blacklist.intersection(poker_blacklist, majong_blacklist)