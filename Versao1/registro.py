from Versao1.sistema_base import sistemaRPG

#────────────────────────────────────────────────────
# - Guarda todos os sistemas disponiveis
# - E permite adicionar novos sistemas futuramente
#────────────────────────────────────────────────────

class registroSistemas:
    def __init__(self):
        self._sistemas: dict[str, sistemaRPG] = {}
    
    def registrar(self, sistema: sistemaRPG):
        self._sistemas[sistema.nome.lower()] = sistema
        
    def obter(self, nome: str):
        return self._sistemas.get(nome.lower())
    
    def listar(self):
        return list(self._sistemas.keys())
    
