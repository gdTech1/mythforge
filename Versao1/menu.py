from Versao1.registro import registroSistemas
from Versao1.dnd5e import sistemaDnD5
from Versao1.armazenamentoJs import armazenamentoJSON
from Versao1.personagem import Personagem
from Versao1.validacao import pedirInteiro

#────────────────────────────────────────────────────
# - Registrando seu sistema
#────────────────────────────────────────────────────

def criar_registro():
    registro = registroSistemas()
    registro.registrar(sistemaDnD5())
    return registro

#────────────────────────────────────────────────────
# - Criando seu personagem 
#────────────────────────────────────────────────────

def criar_personagem(registro: registroSistemas, armazenamento: armazenamentoJSON):
    print('\n=== Criar Personagem ===')

    nome = input('Nome do personagem: ').strip()

    sistemas = registro.listar()
    print('\nSistemas disponíveis:')

    for indice, sistema_nome in enumerate(sistemas, start=1):
        print(f'{indice}. {sistema_nome}')

    escolha = pedirInteiro('\nEscolha o sistema: ', 1, len(sistemas))
    sistema_nome = sistemas[escolha - 1]
    sistema = registro.obter(sistema_nome)

    if sistema is None:
        print('Sistema inválido.')
        return

    print('\nDistribuição de atributos (1 a 20):')
    atributos = {}

    for atributo in sistema.atributos:
        atributos[atributo] = pedirInteiro(f'{atributo}: ', 1, 20)

    if not sistema.validar_atributos(atributos):
        print('Atributos inválidos.')
        return

    historia = input('\nHistória do personagem (opcional): ').strip()

    tracos_input = input('Traços de personalidade (separados por vírgula): ').strip()
    tracos = [t.strip() for t in tracos_input.split(',') if t.strip()]

    personagem = Personagem(
        nome=nome,
        sistema=sistema.nome,
        atributos=atributos,
        historia=historia,
        tracos_personalidade=tracos
    )

    armazenamento.salvar(personagem)
    print(f'\nPersonagem "{nome}" salvo com sucesso!')

#────────────────────────────────────────────────────
# - Lista seus personagens salvos 
#────────────────────────────────────────────────────

def listar_personagens(armazenamento: armazenamentoJSON):
    print('\n=== Personagens Salvos ===')

    personagens = armazenamento.listar()

    if not personagens:
        print('Nenhum personagem encontrado.')
        return

    for p in personagens:
        print(f'- {p}')

# - Carrega os personagens em que voce guardou
def carregar_personagem(armazenamento: armazenamentoJSON):
    print('\n=== Carregar Personagem ===')

    nome = input('Digite o nome do personagem: ').strip()
    personagem = armazenamento.carregar(nome)

    if personagem is None:
        print('Personagem não encontrado.')
        return

    print('\n=== FICHA DO PERSONAGEM ===')
    print(f'Nome: {personagem.nome}')
    print(f'Sistema: {personagem.sistema}')

    print('\nAtributos:')
    for atributo, valor in personagem.atributos.items():
        print(f'  {atributo}: {valor}')

    if personagem.historia:
        print('\nHistória:')
        print(f'  {personagem.historia}')

    if personagem.tracos_personalidade:
        print('\nTraços de Personalidade:')
        for traco in personagem.tracos_personalidade:
            print(f'  - {traco}')

#────────────────────────────────────────────────────
# - Menu principal
#────────────────────────────────────────────────────
def menu_principal():
    registro = criar_registro()
    armazenamento = armazenamentoJSON()

    while True:
        print('\n✦•┈๑⋅⋯ MythForge ⋯⋅๑┈•✦')
        print('┆ 1. Criar personagem')
        print('┆ 2. Listar personagens')
        print('┆ 3. Carregar personagem')
        print('┆ 4. Sair')

        escolha = pedirInteiro('\nEscolha uma opção: ', 1, 4)

        if escolha == 1:
            criar_personagem(registro, armazenamento)

        elif escolha == 2:
            listar_personagens(armazenamento)

        elif escolha == 3:
            carregar_personagem(armazenamento)

        elif escolha == 4:
            print('\nSaindo do MythForge... Até a próxima!')
            break
