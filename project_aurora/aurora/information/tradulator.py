import json


class Tradulator:
    def __init__(self):
        pass

    def tradulator(self):
        with open("project_aurora/aurora/dicionario/languagem.json") as arquivo:
            base = json.load(arquivo)
        lingua = input("Escolha a língua (ex: ingles, portugues): ").lower()
        if lingua in base:
            # Solicitar a palavra que deseja traduzir
            palavra = input(
                "Digite a palavra: "
            ).lower()  # Usa capitalize para tratar a primeira letra maiúscula

            # Verificar se a palavra está na base de dados
            if palavra in base[lingua]:
                print(base[lingua][palavra])
            else:
                print(f"A palavra '{palavra.capitalize()}' não está no dicionário.")
        else:
            print(f"A língua '{lingua}' não está disponível.")
