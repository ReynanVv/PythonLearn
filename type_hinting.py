def cabecalho(texto: str, alinhamento: bool = True) -> str:

    if alinhamento:
        return f"{texto}\n{'-' * len(texto)}"
    else:
        return f" {texto} ".center(50, '|')


print(cabecalho('inova'))

print(cabecalho('inova', alinhamento=False))
