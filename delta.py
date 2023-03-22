"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy hh:mm:ss:ms
data_final = dd/mm/yyyy hh:mm:ss:ms

delta = data_final - data_inicial

"""
import datetime

data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2023, 6, 17)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(
 f"Faltam {tempo_para_evento.days} dias,\
 {tempo_para_evento.seconds // 60 // 60} horas"
)

data_da_compra = datetime.datetime.now()

print(f'Data da Compra: {data_da_compra}')

regra_boleto = datetime.timedelta(days=3)

print(f'Prazo do boleto: {regra_boleto}')

vencimento_boleto = data_da_compra + regra_boleto

print(f'Data de Vencimento do Boleto: {vencimento_boleto}')
