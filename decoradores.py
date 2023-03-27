def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer voce!')
        funcao()
        print('Tenha um exelente dia!')
    return sendo_mesmo


def apre(funcao):
    def apresentando():
        print('Meu nome eh Reynan')
        funcao()
    return apresentando


@apre
def dormir():
    print('Quero dormir...')


dormir()
