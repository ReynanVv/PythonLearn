def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'só se vive uma vez.'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 9:
        return 'Putz!, Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado após dormir por {num_horas} horas. :('
