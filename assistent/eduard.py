from respostas import CALENDARIO, CLIMA

while True:
    saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
    saucao_user = input("Como posso te ajudar?\nR: ")

    if saucao_user == "pesquisa":
        print(
            "Digite um palavra que seja precisa\nExemplo: 'clima', irá retorna como está o clima da sua região"
        )

        lista = ["tempo", "clima", "Horas", "dia", "calendario"]

        print("Digite o que deseja Pesquisar")
        print(f"Aqui estão uma lista de opções para pesquisar.", lista)
        response = input("O que seja pesquisar?\nR: ")

        for i in CALENDARIO:
            perguntas = i
            if response == "calendario" or saucao_user == "Calendario":
                print(i)

        if response == "clima" or saucao_user == "Clima":
            print(CLIMA)

        continua = input("Posso te ajudar algo a mais?\nR: ")
        if continua.lower() == "Nao" or continua.lower() == "nao":
            break
