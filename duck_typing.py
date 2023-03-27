"""
Duck Typing:
    - Objetos similares devem ter métodos e atributos similares.

O tipo ou a classe de um objeto é menos importante do que os
métodos que o definem e ao em vez de checar a classe ou o tipo
de dado é checada a presença ou não de métodos ou atributos
específicos.
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

nome = 'Reynan Vieira'
lista = [32, 13, 55, 12]
dic = {"carlos": 12, "vanessa": 22, "amanda": 20}

print(len(nome))
print(len(lista))
print(len(dic))
