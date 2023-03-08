class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def __str__(self):
        return f'Nome: {self.__nome}, Sobrenome: {self.__sobrenome}, Email: {self.__email}, Senha: {self.__senha}'
        

u1 = Usuario('Reynan', 'Vieira', 'reynan2@gmail.com', '121323')
udict = u1.__dict__
print(udict.values())

print(u1)


class Cadastro:
    idCont = 0
    def __init__(self, nome, email, senha):
        self.__id = Cadastro.idCont + 1
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def __str__(self):
        return f'Nome: {self.__nome} Email: {self.__email} Senha: {self.__senha}'

    
listaC = []   
num = input('Quantos cadastros deseja fazer? ')
i=0

while i < int(num):
    i+=1
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    c = Cadastro(nome,email,senha)
    listaC.append(c)
    
for x in listaC:
    print(x)
  