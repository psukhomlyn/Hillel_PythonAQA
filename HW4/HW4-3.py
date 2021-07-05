"""
3 есть строка переданная в качестве квери параметров "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda......}
"""

query = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
query_list = []
query_dict = {}
query_pairs = query.strip().split('&')
for pair in query_pairs:
    pair.split('=', maxsplit=1)
    print(pair)
print(query_dict)
