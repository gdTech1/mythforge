from Versao1.sistema_base import sistemaRPG 

# - Importei o sistema base para estruturar o sistema de D&D5

#────────────────────────────────────────────────────
# - Caracteristicas base do sistema de DnDe5
#────────────────────────────────────────────────────
class sistemaDnD5(sistemaRPG):
    
    @property 
    def nome(self):
        return 'D&D 5e'

    @property # - transforma um método em atributo
    def atributos(self):
        return ['FORÇA', 'DESTREZA', 'CONSTITUIÇÃO', 'INTELIGÊNCIA', 'SABEDORIA', 'CARISMA']

    def atributos_padrao(self):
        return {atributo: 10 for atributo in self.atributos}

    def validar_atributos(self, atributos: dict[str, int]):
        for atributo in self.atributos:
            if atributo not in atributos:
                return False
            if not isinstance(atributos[atributo], int):
                return False
            if atributos[atributo] < 1 or atributos[atributo] > 20:
                return False
        return True

    def listar_atributos(self, atributos: dict[str, int]):
        for nome, valor in atributos.items():
            print(f'{nome}: {valor}')
