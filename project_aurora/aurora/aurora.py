import response as rp
import os
import json
from time import sleep


# open the JSON file
with open("project_aurora/dicionario/dici.json") as arquivo:
    base = json.load(arquivo)

rp.salution()

# debug loop in case the user has more questions
while True:
    greetings_user = input(
        "R: "
    )  # input for the user to enter what they want to insert
    if greetings_user in base["dic"]:

        # if greetings_user in base:  # checking what the user type contains in the list above
        if greetings_user.lower() in base["dic"]["calendario"]:
            sleep(1)
            os.system("cls")
            for i in rp.calendary():
                print(i)

        elif greetings_user.lower() in base["dic"]["clima"]:
            sleep(1)
            os.system("cls")
            print(rp.climate_of_the_region())

        if greetings_user.lower() in base["dic"]["calcular"]:
            sleep(1)
            os.system("cls")
            rp.calculator()

        if greetings_user.lower() in base["dic"]["open"]:
            sleep(1)
            os.system("cls")
            open = input("Deseja navegar em algum site?\nR: ")

            if open == "sim" or open == "Sim":
                sleep(1)
                app_name = input("Digite o nome do aplicativo que deseja abrir\nR: ")
                site_name = input(
                    "Digite o nome do site que deseja abrir(Para melhora a sua expêriencia, indico que coloque o nome do site 100% preciso)\nR: "
                )
                rp.open_app_and_browse(app_name, site_name)

            else:
                sleep(1)
                app_name = input("Digite o nome do aplicativo que deseja abrir\nR: ")
                rp.open_app(app_name)

        if greetings_user.lower() in base["dic"]["dock"]:
            sleep(1)
            os.system("cls")
            print(
                "Indicamos que agrupe em uma única pasta no dispositivo e coloque nomes simples nos documentos"
                "Para facilitar a localização do documento."
            )
            dock_type = input("Qual a formatação do documento?\nR: ")
            sleep(1)
            dock_formatting = ["txt", "xlsx", "pdf", "docx"]
            if dock_type in dock_formatting:
                if dock_type == "txt":
                    dock_name = input("Digite o documento que deseja abrir\nR: ")
                    rp.open_dock_txt(dock_name)

            if dock_type == "xlsx":
                sleep(1)
                dock_name = input("Digite o documento que deseja abrir\nR: ")
                rp.open_dock_xlsx(dock_name)

        if greetings_user.lower() in base["dic"]["cotacao"]:
            sleep(1)
            os.system("cls")
            print("Temos disponiveis:")
            sleep(1)
            print("Dólar;")
            sleep(1)
            print("Euro;")
            sleep(1)
            print("Bitcoin")
            sleep(1)
            type_money = input("Selecione a moeda desejada:")
            rp.cote(type_money)

        if greetings_user.lower() in base["dic"]["esta"]:
            sleep(1)
            os.system("cls")
            print("Eu estou bem!")
        if greetings_user.lower() in base["dic"]["about"]:
            rp.about()

        if greetings_user.lower() in base["dic"]["sair"]:
            sleep(1)
            print("\033[91m--A sessão foi Finalziada--\033[0m")
            break
    else:
        sleep(1)
        print("Desculpe! Não consegui identificar o que disse")
    sleep(1)
    print(
        "\033[93mPara continuar a sessão, só digitar o que deseja...\nCaso deseja sair, digite 'Sair'\033[0m"
    )
