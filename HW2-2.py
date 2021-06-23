"""
У вас есть 2 компании с людьми. Одна из компаний пусть будет это global_logic была поглощена компанией toshiba.
Отобразите это в коде. Учитывайте что люди с одинаковыми именами могут быть в обеих компаниях
"""

global_logic = ['John Dow', 'John Snow', 'Arya Stark']
toshiba = ['Robin Williams', 'John Snow', 'Taylor Swift']

toshiba.extend(global_logic)
global_logic.clear()   # all global_logic employees were moved into toshiba, global_logic has no employees anymore
print(toshiba)
print(global_logic)