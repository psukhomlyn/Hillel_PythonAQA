"""
3 есть строка переданная в качестве квери параметров "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             ".
Преобразовать эту строку в словарь где ключем должно быть значение перед = а значение пары значение после равно {name: Amanda......}
"""

query = "     name=Amanda=sssss&age=32&&salary=1500&currency=quro                             "
params = []
param_values = []
query_dict = {}
query_pairs = query.strip().split('&')
for pair in query_pairs:
    if pair == '':
        continue
    else:
        param, param_value = pair.split('=', maxsplit=1)
        params.append(param)
        param_values.append(param_value)

query_dict = dict(zip(params, param_values))
print(f'Query string converted to dict is: {query_dict}')