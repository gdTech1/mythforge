import json
from pathlib import Path
from Versao1.personagem import Personagem

#────────────────────────────────────────────────────
# - Responsável por salvar e carregar personagens.
#────────────────────────────────────────────────────

class armazenamentoJSON:
    def __init__(self, pasta_base: str = 'data/personagens'):
        self.pasta_base = Path(pasta_base)
        self.pasta_base.mkdir(parents=True, exist_ok=True)

    def salvar(self, personagem: Personagem):
        nome_arquivo = personagem.nome.lower().replace(' ', '_') + '.json'
        caminho = self.pasta_base / nome_arquivo

        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(personagem.para_dict(), arquivo, indent=4, ensure_ascii=False)

    def listar(self):
        return [arquivo.stem for arquivo in self.pasta_base.glob('*.json')]

    def carregar(self, nome: str):
        nome_arquivo = nome.lower().replace(' ', '_') + '.json'
        caminho = self.pasta_base / nome_arquivo

        if not caminho.exists():
            return None

        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        return Personagem.de_dict(dados)
    
