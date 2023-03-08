class Produto:

    def __init__(self,nome, preco, quantidade):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco * quantidade

    
    def desconto(self):
        desconto_fixo = 20/100
        desconto = lambda x : x * desconto_fixo
        self.__preco = desconto(self.__preco)

    def __str__(self):
        return f'Produto: {self.__nome}, Preço: {str(self.__preco)}, Quantidade: {str(self.__quantidade)}'
    
produto1 = Produto('celular', 1000.0, 2)
print(f'Sem desconto: {produto1}')
produto1.desconto()
print(f'Com desconto: {produto1}')



        
