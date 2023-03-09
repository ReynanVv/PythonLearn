""" 
A ideia de herança é reaproveitar código. Também extender classes.

Sobrescrita de método, ocorre quando reescrevemos um método na super classe em classes filhas.
"""
class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda
    
class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'

cliente1 = Cliente('Reynan', 'Vieira', '312.213.123-21', 5000)
funcionario1 = Funcionario('Amanda', 'Reis', '129.123.123-12', 1342)
print(f'{cliente1.nome_completo()}, \n{funcionario1.nome_completo()}')