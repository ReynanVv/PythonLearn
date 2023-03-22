'''
Testando funções do datetime
'''

import datetime


evento = datetime.datetime.now()
evento.today()
evento.__format__
evento.__add__
evento.fromisoformat(str(evento))
print(evento)

# print(dir(evento))
