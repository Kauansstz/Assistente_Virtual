from time import sleep
import requests


class Money:
    def __init__(self):
        pass

    def cote(self, type_money):
        sleep(1)
        api = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"  # Dollar, euro and bitcoin API
        teste = requests.get(api)
        moeda = teste.json()
        money = type_money
        match money.lower():
            case "[1]":
                money_dollar = moeda["USDBRL"]["bid"]
                money_dollar_float = float(money_dollar)
                money_round = round(money_dollar_float, 2)
                return print("Cotação do Dolar está $", money_round)

            case "[2]":
                sleep(1)
                money_euro = moeda["EURBRL"]["bid"]
                money_euro_float = float(money_euro)
                money_round = round(money_euro_float, 2)
                return print("Cotação do Euro está $", money_round)

            case "[3]":
                sleep(1)
                money_btn = moeda["BTCBRL"]["bid"]
                money_btn_float = float(money_btn)
                money_round = round(money_btn_float, 2)
                return print("Cotação do Bitcoin está $", money_round)

            case _:
                print(
                    "Por favor, selecione somente as moedas citadas. Em breve a nossa equipe irá adicionar mais opções"
                )
