from respostas import calendary, climate_of_the_region, calculator

while True:
    saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
    greetings_user = input("Como posso te ajudar?\nR: ")
    keyword_search = "pesquisa"
    keyword_calculator = "calcular"
    first_keyword = ["pesquisa", "calcular"]
    if greetings_user in first_keyword:
        if greetings_user == "pesquisa":
            response = input("Digite o que deseja Pesquisar\nR: ")
            second_keyword = ["calendario", "clima"]

            if response in second_keyword:
                if response == "calendario":
                    for i in calendary():
                        if response in second_keyword:
                            print(i)

                elif response == "clima":
                    print(climate_of_the_region())
            else:
                print("Desculpe! Não consegui identificar o que disse")

        elif greetings_user == "calcular":
            calculator()

    continua = input("Posso te ajudar algo a mais?\nR: ")
    if continua.lower() == "Nao" or continua.lower() == "nao":
        break
