"""
Escrevendo um iterador customizado
"""
#import print_mesma_linha

class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
          if self.menor < self.maior:
               numero = self.menor
               self.menor += 1
               return numero
          raise StopIteration

for n in Contador(1, 50):
    print(str(n) + " ", end="") 

#for n in range(1, 50):
#    print(n)
 