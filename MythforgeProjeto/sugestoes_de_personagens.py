# faikeando uma iakkk

import random


class motor_de_sugestoes:

    classes_por_atributo = {
        'FOR': 'Guerreiro',
        'DES': 'Ladino',
        'INT': 'Mago',
        'SAB': 'Clérigo',
        'CAR': 'Bardo'
    }

    @classmethod
    def sugerir_classe(cls, atributos: dict):
        melhor_atributo = max(atributos, key=atributos.get)
        return cls.classes_por_atributo.get(melhor_atributo, 'Aventureiro')

    @staticmethod
    def sugerir_historia():
        historias = [
            'Nobre exilado',
            'Sobrevivente das sombras',
            'Aprendiz de arquimago',
            'Mercenário veterano'
        ]
        return random.choice(historias)