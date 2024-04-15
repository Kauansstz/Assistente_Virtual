import datetime
import requests
import pyautogui
import pandas as pd
from googletrans import Translator as tl
import subprocess
from time import sleep


def salution():
    current_time = datetime.datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")

    inicio_manha = datetime.datetime.strptime("06:00", "%H:%M").time()
    final_manha = datetime.datetime.strptime("11:59", "%H:%M").time()

    inicio_tarde = datetime.datetime.strptime("12:00", "%H:%M").time()
    final_tarde = datetime.datetime.strptime("17:59", "%H:%M").time()

    if inicio_manha <= current_time <= final_manha:
        sleep(1)
        print("Bom dia!\nSeja Bem-Vindo!")
        sleep(2)
        print("Sou Eduard! Seu assistente virtual.\nComo posso te ajudar?")
    elif inicio_tarde <= current_time <= final_tarde:
        sleep(1)
        print("Boa Tarde!\nSeja Bem-Vindo!")
        sleep(2)
        print("Sou Eduard! Seu assistente virtual.\nComo posso te ajudar?")

    else:
        sleep(1)
        print("Boa Noite!\nSeja Bem-Vindo!")
        sleep(2)
        print("Sou Eduard! Seu assistente virtual.\nComo posso te ajudar?")


def calendary():
    sleep(1)
    HORA = datetime.datetime.now().strftime(
        "Horas: %H:%M"
    )  # Collecting hours via console (Desktop/Mobile)
    DIA = datetime.datetime.now().strftime(
        "Data: %D - Dia da Semana: %A"
    )  # Collecting the day, month, year and day of the week via console (Desktop/Mobile)
    return DIA, HORA


def climate_of_the_region():
    sleep(1)
    api = "https://wttr.in/palhoça"  # Getting an api with weather, percentage of rain at 4 times (Morning, beginning/Late afternoon and Night)
    response = requests.get(api)
    CLIMA = response.text
    return CLIMA


def calculator():
    sleep(1)
    # Inserted a calculator if possible the user wants to do an equation
    operator = input("Digite qualquer sinal de operação\nR: ")

    number_1 = input("Digite um número\nR: ")
    number_2 = input("Digite um número\nR: ")

    number_1_float = float(number_1)
    number_2_float = float(number_2)

    if operator == "+":
        sleep(1)
        more = lambda x, y: x + y
        result = more(number_1_float, number_2_float)
        print(result)

    elif operator == "-":
        sleep(1)
        any_less = lambda x, y: x - y
        result = any_less(number_1_float, number_2_float)
        print(result)

    elif operator == "*":
        sleep(1)
        multiply = lambda x, y: x * y
        result = multiply(number_1_float, number_2_float)
        print(result)

    elif operator == "/":
        sleep(1)
        to_divide = lambda x, y: x / y
        result = to_divide(number_1_float, number_2_float)
        print(result)

    else:
        sleep(1)
        print("Sinal de operator não reconhecido")


def open_app_and_browse(app_name, site_name):
    # If the user wants to open an app and browse a website
    sleep(1)
    nome_do_aplicativo = app_name
    comando = f"start {nome_do_aplicativo}"
    subprocess.run(comando, shell=True)
    pyautogui.click(x=500, y=50)
    pyautogui.write(site_name)
    pyautogui.press("enter")


def open_app(app_name):
    sleep(1)
    nome_do_aplicativo = app_name
    comando = f"start {nome_do_aplicativo}"
    subprocess.run(comando, shell=True)


def open_dock_txt(dock_name):
    sleep(1)
    # If the user wants to open a specific document
    try:
        with open(
            f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\back-end\\Arquivo_txt\\{dock_name}.txt",
            "r",
        ) as arquivo:
            dados = arquivo.read()
            return print(dados)
    except FileNotFoundError:
        sleep(1)
        print("Perdão, não consegui localizar o documento")


def open_dock_xlsx(dock_name):
    # If the user wants to open a specific document
    sleep(1)
    try:
        open_xlsx = pd.read_excel(
            f"C:\\Users\\Kauan\\OneDrive\\Área de Trabalho\\{dock_name}.xlsx"
        )
        opened_xlsx = pd.DataFrame(open_xlsx)
        print(opened_xlsx)
        print(open_xlsx.shape)
    except FileNotFoundError:
        sleep(1)
        print("Perdão, não consegui localizar o documento")


def cote(type_money):
    sleep(1)
    api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"  # Dollar, euro and bitcoin API
    teste = requests.get(api)
    moeda = teste.json()
    money = type_money
    if money.lower() == "dolar":
        sleep(1)
        money_dollar = moeda["USDBRL"]["bid"]
        money_dollar_float = float(money_dollar)
        money_round = round(money_dollar_float, 2)
        return print("Cotação do Dolar está $", money_round)

    elif money.lower() == "euro":
        sleep(1)
        money_euro = moeda["EURBRL"]["bid"]
        money_euro_float = float(money_euro)
        money_round = round(money_euro_float, 2)
        return print("Cotação do Euro está $", money_round)

    elif money.lower() == "bitcoin":
        sleep(1)
        money_btn = moeda["BTCBRL"]["bid"]
        money_btn_float = float(money_btn)
        money_round = round(money_btn_float, 2)
        return print("Cotação do Bitcoin está $", money_round)


def tradutor(text, language):
    sleep(1)
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
        sleep(1)
        print("Perdão, não consegui identificar a língua/letra desejada ")
