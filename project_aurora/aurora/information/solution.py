from time import sleep
import datetime


class Solution:
    def __init__(self):
        pass

    def solution(self):
        current_time = datetime.datetime.now().time()
        formatted_time = current_time.strftime("%H:%M")

        inicio_manha = datetime.datetime.strptime("06:00", "%H:%M").time()
        final_manha = datetime.datetime.strptime("11:59", "%H:%M").time()

        inicio_tarde = datetime.datetime.strptime("12:00", "%H:%M").time()
        final_tarde = datetime.datetime.strptime("17:59", "%H:%M").time()

        if inicio_manha <= current_time <= final_manha:
            response = "Bom dia!"

        elif inicio_tarde <= current_time <= final_tarde:
            response = "Boa Tarde!"

        else:
            response = "Boa Noite!"

        print(response)
        print("Sou Aurora!")
        sleep(2)
        print("Sua Assistente Pessoal.")
        sleep(2)
        print("Como posso te ajudar?")
