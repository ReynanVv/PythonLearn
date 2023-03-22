'''
Escrevendo em arquivos CSV

render() (leitor), writer() (escritor)
'''

from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != '0':
        filme = input('Informe o nome do filme: ')
        print('digite 0 para sair')
        if filme != 'sair':
            genero = input('Informe o gênero do filme: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
