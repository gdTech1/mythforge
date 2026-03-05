#────────────────────────────────────────────────────
# - Validacao de entrada dos valores de escolha
#────────────────────────────────────────────────────

def pedirInteiro(mensagem: str, minimo: int, maximo: int):
    while True:
        try:
            valor = int(input(mensagem))

            if minimo <= valor <= maximo:
                return valor

            print(f'Digite um número entre {minimo} e {maximo}.')

        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')