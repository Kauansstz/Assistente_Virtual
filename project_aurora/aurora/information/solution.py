from time import sleep
import datetime
import json


class Solution:
    def __init__(self):
        pass

    def solution(self):
        with open("info.json") as data:
            info = json.load(data)

        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime("%H:%M")

        inicio_manha = datetime.datetime.strptime("06:00", "%H:%M").time()
        final_manha = datetime.datetime.strptime("11:59", "%H:%M").time()

        inicio_tarde = datetime.datetime.strptime("12:00", "%H:%M").time()
        final_tarde = datetime.datetime.strptime("17:59", "%H:%M").time()
        for pessoa in info:
            if pessoa["genero"] == "masculino":
                tipo = "Senhor"
            elif pessoa["genero"] == "feminino":
                tipo = "Senhora"
            elif pessoa["genero"] == "nao quero selecionar":
                tipo = " "
        if inicio_manha <= current_time <= final_manha:
            response = "Bom dia"
        elif inicio_tarde <= current_time <= final_tarde:
            response = "Boa Tarde"
        else:
            response = "Boa Noite"
        print(response)
        sleep(1)
        print(f"Como posso ajudar o(a) {tipo}?")
