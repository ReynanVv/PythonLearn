"""
Herança múltipla é a possibilidade de uma classe herdar de multiplas classes 

Pode ser feita de duas maneiras:
    - Multiderivação Direta
    - Multiderivação Indireta

# Exemplo Direta:

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass
    
class MultiDer(Base1, Base2, Base3):
    pass
    
# Exemplo Indireta:

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass
    
class MultiDer(Base3):
    pass
"""

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    
class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def nadar(self):
        return f'{self._Animal__nome} está nadando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'
    
class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está andando'
    
    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'
    
class Pinguim(Aquatico, Terrestre): # ordem Terrestre como primeiro, o metodo cumprimentar será o terrestre

    def __init__(self, nome):
        super().__init__(nome)

p1 = Pinguim('Happy')
print(p1.andar())
print(p1.nadar())
print(p1.cumprimentar()) # MRO - Method Resolution Order. A ordem em que a a Herança é passada altera no comportamento do objeto