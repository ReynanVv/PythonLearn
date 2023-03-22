"""
Propiedades substituem os getters e setters em python e metodos 
para serem usados sem a chamada de função
"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo {self.__saldo} do cliente {self.__titular}'
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

c1 = Conta('Rey', 3000, 5000)
c2 = Conta('Amanda', 2000, 4000)

print(c1.extrato())
print(c2.extrato())

soma = c1.saldo + c2.saldo
print(f'Soma dos saldos {soma}')

print(c1.__dict__)
c1.limite = 70002
print(c1.__dict__)
    
