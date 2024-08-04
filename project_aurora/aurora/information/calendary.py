import datetime
from time import sleep


class Calendary:
    def __init__(self):
        pass

    def calendary(self):
        sleep(1)
        HORA = datetime.datetime.now().strftime("Horas: %H:%M")
        DIA = datetime.datetime.now().strftime("Data: %D - Dia da Semana: %A")
        return DIA, HORA
