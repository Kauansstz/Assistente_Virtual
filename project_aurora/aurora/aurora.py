import os
import json
from time import sleep
from importacao import (
    Pessoa,
    Money,
    Calculadora,
    Calendary,
    About,
    Solution,
    Climate,
    OpenDock,
    adicionar_pessoa,
    exibir_dados,
)


# Limpar a tela de forma portátil
def clear_screen():
    if os.name == "nt":  # Para Windows
        os.system("cls")
    else:  # Para Mac e Linux
        os.system("clear")


# Abrir o arquivo JSON
with open("project_aurora/aurora/dicionario/dici.json") as arquivo:
    base = json.load(arquivo)

day = Solution()
day.solution()


# Loop para tratar perguntas do usuário
while True:
    greetings_user = (
        input("R: ").lower().strip()
    )  # Converte a entrada para minúsculas e remove espaços extras

    found = False  # Flag para verificar se a entrada foi encontrada em alguma lista

    for key, phrases in base["dic"].items():
        if greetings_user in phrases:
            found = True
            match key:
                case "calendario":
                    sleep(1)
                    clear_screen()
                    response = Calendary()
                    for i in response.calendary():
                        print(i)

                case "about":
                    response = About()
                    response.about()

                case "clima":
                    sleep(1)
                    clear_screen()
                    response = Climate()
                    response.climate_of_the_region()

                case "calcular":
                    sleep(1)
                    clear_screen()
                    response = input(
                        "Digite uma das opções que deseja:\n[1] Soma;\n[2] Subtação;\n[3] Divisão;\n[4] Multiplicação;\n[5] Equação do Segundo Grau.\nR: "
                    )
                    match response:
                        case "1":
                            response = input("Quantos números tem a conta?\nR: ")
                            match response:
                                case "4":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = input("Digite o 4º número: ")
                                case "3":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                case "2":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                case _:
                                    print(
                                        "Por enquanto temos uma equação de somente com 4 números"
                                    )
                            calc = Calculadora(number_1, number_2, number_3, number_4)
                            print(calc.somar())
                        case "2":
                            response = input("Quantos números tem a conta?\nR: ")
                            match response:
                                case "4":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = input("Digite o 4º número: ")
                                case "3":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = None
                                case "2":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = None
                                    number_4 = None
                                case _:
                                    print(
                                        "Por enquanto temos uma equação de somente com 4 números"
                                    )
                            calc = Calculadora(number_1, number_2, number_3, number_4)
                            print(calc.subtacao())
                        case "3":
                            response = input("Quantos números tem a conta?\nR: ")
                            match response:
                                case "4":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = input("Digite o 4º número: ")
                                case "3":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = None
                                case "2":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = None
                                    number_4 = None
                                case _:
                                    print(
                                        "Por enquanto temos uma equação de somente com 4 números"
                                    )
                            calc = Calculadora(number_1, number_2, number_3, number_4)
                            print(calc.divisao())
                        case "4":
                            response = input("Quantos números tem a conta?\nR: ")
                            match response:
                                case "4":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = input("Digite o 4º número: ")
                                case "3":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = input("Digite o 3º número: ")
                                    number_4 = None
                                case "2":
                                    number_1 = input("Digite o 1º número: ")
                                    number_2 = input("Digite o 2º número:")
                                    number_3 = None
                                    number_4 = None
                                case _:
                                    print(
                                        "Por enquanto temos uma equação de somente com 4 números"
                                    )
                            calc = Calculadora(number_1, number_2, number_3, number_4)
                            print(calc.multiplicar())
                        case "5":
                            number_1 = input("Digite o 1º número: ")
                            number_2 = input("Digite o 2º número:")
                            number_3 = input("Digite o 3º número: ")
                            number_4 = None
                            calc = Calculadora(number_1, number_2, number_3, number_4)
                            print(calc.solve_quadratic())

                        case _:
                            print(
                                "Temos somente operações de somar, substração, multiplicação e divisão, em breve adicionaremos mais equações"
                            )

                case "open":
                    sleep(1)
                    clear_screen()
                    navigate = (
                        input("Deseja navegar em algum site?\nR: ").lower().strip()
                    )

                    if navigate == "sim":
                        sleep(1)
                        app_name = input(
                            "Digite o nome do aplicativo que deseja abrir\nR: "
                        ).strip()
                        site_name = input(
                            "Digite o nome do site que deseja abrir (Para melhorar sua experiência, coloque o nome do site 100% preciso)\nR: "
                        ).strip()
                        response = OpenDock()
                        response.open_app_and_browse(app_name, site_name)
                    else:
                        sleep(1)
                        app_name = input(
                            "Digite o nome do aplicativo que deseja abrir\nR: "
                        ).strip()
                        response = OpenDock()
                        response.open_app(app_name)

                case "dock":
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
                            response = OpenDock()
                            response.open_dock_txt(dock_name)
                        elif dock_type == "xlsx":
                            response = OpenDock()
                            response.open_dock_xlsx(dock_name)
                        # Adicione mais verificações se necessário

                case "cotacao":
                    sleep(1)
                    clear_screen()
                    print("Selecione uam das opções:")
                    sleep(1)
                    print("[1] Dólar;")
                    sleep(1)
                    print("[2] Euro;")
                    sleep(1)
                    print("[3] Bitcoin")
                    sleep(1)
                    type_money = input("R: ").lower().strip()
                    response = Money()
                    response.cote(type_money)

                case "esta":
                    sleep(1)
                    clear_screen()
                    print("Eu estou bem!")

                case "sair":
                    sleep(1)
                    print("\033[91m--A sessão foi Finalizada--\033[0m")
                    exit()

                case "cadastro":
                    nome = input("Digite seu nome completo: ")
                    idade = int(input("Digite sua idade: "))
                    email = input("Digite seu email: ")
                    pessoa = Pessoa(nome, idade, email)
                    adicionar_pessoa(pessoa)

                case "dados":
                    exibir_dados()
    if not found:
        sleep(1)
        print("Desculpe! Não consegui identificar o que disse")

    sleep(1)
    print(
        "\033[93mPara continuar a sessão, digite o que deseja...\nCaso deseje sair, digite 'sair'\033[0m"
    )
