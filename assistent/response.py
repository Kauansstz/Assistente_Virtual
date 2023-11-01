import datetime
import requests
import pyautogui
import pandas as pd


def calendary():
    HORA = datetime.datetime.now().strftime(
        "Horas: %H:%M"
    )  # Coletando as horas via console(Desktop/Mobile)
    DIA = datetime.datetime.now().strftime(
        "Data: %D - Dia da Semana: %A"
    )  # Coletando o dia, mes, ano e dia da semana via console(Desktop/Mobile)
    return DIA, HORA  # Juntando tudo para mostrar ao usuário as informações coletadas


def climate_of_the_region():
    api = "https://wttr.in/palhoça"  # Pegando uma api com clima, porcentagem de chuva nos 4 horarios(Manhã, começo/Fim da tarde e de Noite)
    response = requests.get(api)  # Variavel recebendo o requests da api
    CLIMA = response.text  # Convertendo a variavel acima em forma de texto
    return CLIMA


def calculator():
    operator = input("Digite qualquer sinal de operação\nR: ")

    number_1 = input("Digite um número\nR: ")
    number_2 = input("Digite um número\nR: ")

    number_1_float = float(number_1)
    number_2_float = float(number_2)

    def more(x, y):
        return print(x + y)

    def any_less(x, y):
        return print(x - y)

    def multiply(x, y):
        return print(x * y)

    def to_divide(x, y):
        return print(x / y)

    if operator == "+":
        return more(number_1_float, number_2_float)

    if operator == "-":
        return any_less(number_1_float, number_2_float)

    if operator == "*":
        return multiply(number_1_float, number_2_float)

    if operator == "/":
        return to_divide(number_1_float, number_2_float)


def open_app_and_browse(app_name, site_name):
    pyautogui.PAUSE = 2
    pyautogui.press("win")
    pyautogui.write(app_name)
    pyautogui.press("enter")
    pyautogui.click(x=500, y=50)
    pyautogui.write(site_name)
    pyautogui.press("enter")


def open_app(app_name):
    pyautogui.PAUSE = 2
    pyautogui.press("win")
    pyautogui.write(app_name)
    pyautogui.press("enter")


def open_dock_txt(dock_name):
    with open(
        f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\back-end\\Arquivo_txt\\{dock_name}.txt",
        "r",
    ) as arquivo:
        dados = arquivo.read()
        return print(dados)


def open_dock_xlsx(dock_name):
    open_xlsx = pd.read_excel(
        f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\{dock_name}.xlsx"
    )
    print(open_xlsx.head)
    print(open_xlsx.shape)


def dollar_exchange_rate():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["USDBRL"]["bid"]
    moeda_dolar_float = float(moeda_dolar)
    moeda_arren = round(moeda_dolar_float, 2)

    return print("Cotação do Dolar está $", moeda_arren)


def euro_value():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["EURBRL"]["bid"]
    moeda_dolar_float = float(moeda_dolar)
    moeda_arren = round(moeda_dolar_float, 2)

    return print("Cotação do Euro está $", moeda_arren)


def bitcon_quote():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["BTCBRL"]["bid"]
    moeda_dolar_float = float(moeda_dolar)
    moeda_arren = round(moeda_dolar_float, 2)

    return print("Cotação do Bitcoin está $", moeda_arren)
