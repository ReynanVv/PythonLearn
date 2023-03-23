import unittest
from atividades import comer, dormir


class AtividadesTeste(unittest.TestCase):

    def test_comer_bem(self):
        '''Testando o retorno com comida saudável.'''
        self.assertEqual(
            comer('salada', True),
            'Estou comendo salada porque quero manter a forma.'
        )

    def test_comer_mal(self):
        '''Testando o retorno com comida gostosa.'''
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        '''Testando o retorno dormindo pouco'''
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        '''Testando o retorno dormindo muito'''
        self.assertEqual(
            dormir(10),
            'Putz!, Dormi muito! Estou atrasado para o trabalho!'
        )


if __name__ == '__main__':
    unittest.main()
