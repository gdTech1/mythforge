from MythforgeProjeto.sistema_base import sistemaRPG 

class Tormenta20(sistemaRPG):

    def __init__(self):
        super().__init__('Tormenta20')

    def atributos_padrao(self) -> dict:
        return {
            'FOR': 10,
            'DES': 10,
            'CON': 10,
            'INT': 10,
            'SAB': 10,
            'CAR': 10
        }

    def calcular_modificador(self, valor: int):
        return (valor - 10) // 2 if valor >= 10 else -((10 - valor) // 2)
    