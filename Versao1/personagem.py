from dataclasses import dataclass, field
from datetime import datetime

#────────────────────────────────────────────────────
# - "Atributos" da criação de seu personagem
#────────────────────────────────────────────────────

@dataclass
class Personagem:
    nome: str
    sistema: str
    atributos: dict[str, int]
    historia: str = ''
    tracos_personalidade: list[str] = field(default_factory=list)
    criado_em: str = field(default_factory=lambda: datetime.now().isoformat())

    def para_dict(self):
        return {
            'nome': self.nome,
            'sistema': self.sistema,
            'atributos': self.atributos,
            'historia': self.historia,
            'tracos_personalidade': self.tracos_personalidade,
            'criado_em': self.criado_em
        }

    @staticmethod
    def de_dict(dados: dict):
        return Personagem(
            nome=dados['nome'],
            sistema=dados['sistema'],
            atributos=dados['atributos'],
            historia=dados.get('historia', ''),
            tracos_personalidade=dados.get('tracos_personalidade', []),
            criado_em=dados.get('criado_em', '')
        )
