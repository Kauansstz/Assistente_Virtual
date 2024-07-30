import response as rp
import os
import json
from time import sleep


# Limpar a tela de forma portátil
def clear_screen():
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Mac e Linux
        os.system("clear")


# Abrir o arquivo JSON
with open("project_aurora/aurora/dicionario/dici.json") as arquivo:
    base = json.load(arquivo)

rp.salution()

# Loop para tratar perguntas do usuário
while True:
    greetings_user = (
        input("R: ").lower().strip()
    )  # Converte a entrada para minúsculas e remove espaços extras

    found = False  # Flag para verificar se a entrada foi encontrada em alguma lista

    for key, phrases in base["dic"].items():
        if greetings_user in phrases:
            found = True

            if key == "calendario":
                sleep(1)
                clear_screen()
                for i in rp.calendary():
                    print(i)

            elif key == "about":
                rp.about()

            elif key == "clima":
                sleep(1)
                clear_screen()
                print(rp.climate_of_the_region())

            elif key == "calcular":
                sleep(1)
                clear_screen()
                rp.calculator()

            elif key == "open":
                sleep(1)
                clear_screen()
                navigate = input("Deseja navegar em algum site?\nR: ").lower().strip()

                if navigate == "sim":
                    sleep(1)
                    app_name = input(
                        "Digite o nome do aplicativo que deseja abrir\nR: "
                    ).strip()
                    site_name = input(
                        "Digite o nome do site que deseja abrir (Para melhorar sua experiência, coloque o nome do site 100% preciso)\nR: "
                    ).strip()
                    rp.open_app_and_browse(app_name, site_name)
                else:
                    sleep(1)
                    app_name = input(
                        "Digite o nome do aplicativo que deseja abrir\nR: "
                    ).strip()
                    rp.open_app(app_name)

            elif key == "dock":
                sleep(1)
                clear_screen()
                print(
                    "Indicamos que agrupe em uma única pasta no dispositivo e coloque nomes simples nos documentos "
                    "para facilitar a localização do documento."
                )
                dock_type = (
                    input("Qual a formatação do documento?\nR: ").lower().strip()
                )
                sleep(1)
                dock_formatting = ["txt", "xlsx", "pdf", "docx"]
                if dock_type in dock_formatting:
                    dock_name = input(
                        "Digite o nome do documento que deseja abrir\nR: "
                    ).strip()
                    if dock_type == "txt":
                        rp.open_dock_txt(dock_name)
                    elif dock_type == "xlsx":
                        rp.open_dock_xlsx(dock_name)
                    # Adicione mais verificações se necessário

            elif key == "cotacao":
                sleep(1)
                clear_screen()
                print("Temos disponíveis:")
                sleep(1)
                print("Dólar;")
                sleep(1)
                print("Euro;")
                sleep(1)
                print("Bitcoin")
                sleep(1)
                type_money = input("Selecione a moeda desejada:\nR: ").lower().strip()
                rp.cote(type_money)

            elif key == "esta":
                sleep(1)
                clear_screen()
                print("Eu estou bem!")

            elif key == "sair":
                sleep(1)
                print("\033[91m--A sessão foi Finalizada--\033[0m")
                exit()

    if not found:
        sleep(1)
        print("Desculpe! Não consegui identificar o que disse")

    sleep(1)
    print(
        "\033[93mPara continuar a sessão, digite o que deseja...\nCaso deseje sair, digite 'sair'\033[0m"
    )
