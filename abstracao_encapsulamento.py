class Conta:

    contador = 400
    mostra_valor = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('Valor deve ser positivo')

    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor

                conta_destino.__saldo += valor

                self.__valor_transferido = valor
                conta_destino = conta_destino.__titular
                print(
                    f'Valor de {self.__valor_transferido} do(a) Titular {self.__titular} para o(a) titular {conta_destino}')
            else:
                print('Saldo insuficiente')
        else:
            print('Valor deve ser positivo')
        
       

   
#Teste
conta1 = Conta('Rey', 3000.0, 5000)
conta1.extrato()

conta2 = Conta('Amanda', 2900.0, 6000)
conta2.extrato()

conta1.transferir(valor=400, conta_destino=conta2)

conta1.extrato()
conta2.extrato()
