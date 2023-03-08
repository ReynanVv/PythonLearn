my_list = (["1 4", "2 5", "3 6"])

saida = []

for elemento in my_list:
    # separa os elementos de exemplo - com a parte esperada em cada linha
    linhas_por_elemento = elemento.split(" ", 1)
    for j, linha_do_elemento in enumerate(linhas_por_elemento):
        if len(saida) <= j:
            # a linha onde essa informação vai entrar ainda não foi criada:
            saida.append([])
        saida[j].append(linha_do_elemento)
# nesse ponto, a variável saída é uma lista de listas - onde cada elemento da mesma é uma lista com as strings que vão em cada coluna

# O print abaixo concatena com "|" os elementos de uma mesma linha, e concatena cada linha de texto com "\n":

print("\n".join(
    "|".join(f"{elemento:>8s}" for elemento in linha) for linha in saida))
