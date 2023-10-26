import datetime
import requests

HORA = datetime.datetime.now().strftime(
    "Horas: %H:%M"
)  # Coletando as horas via console(Desktop/Mobile)

DIA = datetime.datetime.now().strftime(
    "Data: %D - Dia da Semana: %A"
)  # Coletando o dia, mes, ano e dia da semana via console(Desktop/Mobile)

CALENDARIO = DIA, HORA  # Juntando tudo para mostrar ao usuário as informações coletadas

api = "https://wttr.in/palhoça"  # Pegando uma api com clima, porcentagem de chuva nos 4 horarios(Manhã, começo/Fim da tarde e de Noite)

response = requests.get(api)  # Variavel recebendo o requests da api
CLIMA = response.text  # Convertendo a variavel acima em forma de texto
