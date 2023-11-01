import response as rp


while True:
    saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
    greetings_user = input("Como posso te ajudar?\nR: ")
    first_keyword = ["pesquisa", "calcular", "abrir", "documento", "cotaçao"]

    if greetings_user in first_keyword:
        if greetings_user == "pesquisa":
            response = input("Digite o que deseja Pesquisar\nR: ")
            second_keyword = ["calendario", "clima"]

            if response in second_keyword:
                if response == "calendario":
                    for i in rp.calendary():
                        if response in second_keyword:
                            print(i)

                elif response == "clima":
                    print(rp.climate_of_the_region())
            else:
                print("Desculpe! Não consegui identificar o que disse")

        if greetings_user == "calcular":
            rp.calculator()

        if greetings_user == "abrir":
            open = input("Deseja navegar em algum site?\nR: ")
            if open == "sim" or open == "Sim":
                app_name = input("Digite o nome do aplicativo que deseja abrir\nR: ")
                site_name = input(
                    "Digite o nome do site que deseja abrir(Para melhora a sua expêriencia, indico que coloque o nome do site 100% preciso)\nR: "
                )
                rp.open_app_and_browse(app_name, site_name)
            else:
                app_name = input("Digite o nome do aplicativo que deseja abrir\nR: ")
                rp.open_app(app_name)
        if greetings_user == "documento":
            print(
                "Indicamos que agrupe em uma única pasta no dispositivo e coloque nomes simples nos documentos"
                "Para facilitar a localização do documento."
            )
            dock_type = input("Qual a formatação do documento?\nR: ")
            dock_formatting = ["txt", "xlsx", "pdf", "docx"]
            if dock_type in dock_formatting:
                if dock_type == "txt":
                    dock_name = input("Digite o documento que deseja abrir\nR: ")
                    rp.open_dock_txt(dock_name)
            if dock_type == "xlsx":
                dock_name = input("Digite o documento que deseja abrir\nR: ")
                rp.open_dock_xlsx(dock_name)
        if greetings_user == "cotaçao":
            type_coin = input("Dólar\nEuro\nBitcoin\nSelecione a moeda:")

            if type_coin == "dólar":
                rp.dollar_exchange_rate()

            if type_coin == "euro":
                rp.euro_value()

            if type_coin == "bitcoin":
                rp.bitcon_quote()

    continua = input("Posso te ajudar algo a mais?\nR: ")
    if continua.lower() == "Nao" or continua.lower() == "nao":
        break
