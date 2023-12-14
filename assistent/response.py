import datetime
import requests
import pyautogui
import pandas as pd
from googletrans import Translator as tl
import subprocess


def calendary():
    HORA = datetime.datetime.now().strftime(
        "Horas: %H:%M"
    )  # Collecting hours via console (Desktop/Mobile)
    DIA = datetime.datetime.now().strftime(
        "Data: %D - Dia da Semana: %A"
    )  # Collecting the day, month, year and day of the week via console (Desktop/Mobile)
    return DIA, HORA


def climate_of_the_region():
    api = "https://wttr.in/palhoça"  # Getting an api with weather, percentage of rain at 4 times (Morning, beginning/Late afternoon and Night)
    response = requests.get(api)
    CLIMA = response.text
    return CLIMA


def calculator():
    # Inserted a calculator if possible the user wants to do an equation
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
    # If the user wants to open an app and browse a website
    nome_do_aplicativo = app_name
    comando = f"start {nome_do_aplicativo}"
    subprocess.run(comando, shell=True)
    pyautogui.click(x=500, y=50)
    pyautogui.write(site_name)
    pyautogui.press("enter")


def open_app(app_name):
    nome_do_aplicativo = app_name
    comando = f"start {nome_do_aplicativo}"
    subprocess.run(comando, shell=True)


def open_dock_txt(dock_name):
    # If the user wants to open a specific document
    try:
        with open(
            f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\back-end\\Arquivo_txt\\{dock_name}.txt",
            "r",
        ) as arquivo:
            dados = arquivo.read()
            return print(dados)
    except FileNotFoundError:
        print("Perdão, não consegui localizar o documento")


def open_dock_xlsx(dock_name):
    # If the user wants to open a specific document
    try:
        open_xlsx = pd.read_excel(
            f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\{dock_name}.xlsx"
        )
        print(open_xlsx.head)
        print(open_xlsx.shape)
    except FileNotFoundError:
        print("Perdão, não consegui localizar o documento")


def dollar_exchange_rate():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"  # Dollar, euro and bitcoin API
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["USDBRL"][
        "bid"
    ]  # Collecting the currency type and collecting the quote
    moeda_dolar_float = float(moeda_dolar)  # transforming the variable into float
    moeda_arren = round(
        moeda_dolar_float, 2
    )  # Rounding the variable and leaving two decimal places after the decimal point

    return print("Cotação do Dolar está $", moeda_arren)


def euro_value():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"  # Dollar, euro and bitcoin API
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["EURBRL"][
        "bid"
    ]  # Collecting the currency type and collecting the quote
    moeda_dolar_float = float(moeda_dolar)  # transforming the variable into float
    moeda_arren = round(
        moeda_dolar_float, 2
    )  # Rounding the variable and leaving two decimal places after the decimal point

    return print("Cotação do Euro está $", moeda_arren)


def bitcon_quote():
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"  # Dollar, euro and bitcoin API
    teste = requests.get(api)
    moeda = teste.json()
    moeda_dolar = moeda["BTCBRL"][
        "bid"
    ]  # Collecting the currency type and collecting the quote
    moeda_dolar_float = float(moeda_dolar)  # transforming the variable into float
    moeda_arren = round(
        moeda_dolar_float, 2
    )  # Rounding the variable and leaving two decimal places after the decimal point

    return print("Cotação do Bitcoin está $", moeda_arren)


def tradutor(text, language):
    try:
        # Create a translator instance
        translator = tl()

        language_distiny = language

        # Perform the translation
        traducao = translator.translate(text, dest=language_distiny)

        # Display the translated text
        print(f"Texto original ({traducao.src}): {text}")  # type: ignore
        print(f"Texto traduzido ({language_distiny}): {traducao.text}")  # type: ignore
    except ValueError:
        print("Perdão, não consegui identificar a língua/letra desejada ")
