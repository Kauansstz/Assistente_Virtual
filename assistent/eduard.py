from respostas import calendary, climate_of_the_region, calculator, open_app

while True:
    saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
    greetings_user = input("Como posso te ajudar?\nR: ")
    first_keyword = ["pesquisa", "calcular", "abrir", "acessar"]

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

        if greetings_user == "calcular":
            calculator()

        if greetings_user == "abrir":
            app_name = input("Digite o nome do aplicativo que deseja abrir\nR: ")
            site_name = input(
                "Digite o nome do site que deseja abrir(Para melhora a sua expêriencia, indico que coloque o nome do site 100% preciso)\nR: "
            )
            open_app(app_name, site_name)

    continua = input("Posso te ajudar algo a mais?\nR: ")
    if continua.lower() == "Nao" or continua.lower() == "nao":
        break
