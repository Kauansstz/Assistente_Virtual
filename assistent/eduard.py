import response as rp
import os

rp.salution()

first_keyword = [
    "calendario",
    "clima",
    "calcular",
    "abrir",
    "documento",
    "cotaçao",
    "tradutor",
    "esta",
    "sair",
]  # list of items that will be used during the conversation

# debug loop in case the user has more questions
while True:
    greetings_user = input(
        "R: "
    )  # input for the user to enter what they want to insert

    if (
        greetings_user in first_keyword
    ):  # checking what the user type contains in the list above
        if greetings_user == "calendario":
            os.system("cls")
            for i in rp.calendary():
                print(i)

        elif greetings_user == "clima":
            os.system("cls")
            print(rp.climate_of_the_region())

        if greetings_user == "calcular":
            os.system("cls")
            rp.calculator()

        if greetings_user == "abrir":
            os.system("cls")
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
            os.system("cls")
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
            os.system("cls")
            type_money = input("Dólar\nEuro\nBitcoin\nSelecione a moeda:")
            rp.cote(type_money)

        if greetings_user == "tradutor":
            os.system("cls")
            print(
                "Antes de escolher a língua desejada, escreva corretamente para o álgoritimo identificar"
            )
            language = input("Qual língua deseja traduzir?\nR: ")
            langue_lower = language.lower()
            text = input("Traduzir\nR: ")
            rp.tradutor(text, langue_lower)

        if greetings_user == "esta":
            os.system("cls")
            print("Eu estou bem!")
    else:
        print("Desculpe! Não consegui identificar o que disse")

    print("\033[93mPara continuar a sessão, só digitar o que deseja...\033[0m")
    if greetings_user.lower() == "sair":
        print("\033[91m--A sessão foi Finalziada--\033[0m")
        break
