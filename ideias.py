import datetime

saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
saucao_user = input("Como posso te ajudar?\n")

hora =  datetime.datetime.now().strftime("Horas: %H:%M")
dia =  datetime.datetime.now().strftime("Data: %D - Dia da Semana: %A")
calendario = dia, hora, 
for i in calendario:
  perguntas = {
    'tempo': 'Está 26ºc',
    'clima': 'O clima se encontra nublado',
    'horas': hora,
    'dia': dia,
    'calendario': i
  }
  if saucao_user == "clima":
      print(perguntas["clima"])
  if saucao_user == "horas":
      print(perguntas["horas"])
  if saucao_user == "dia":
      print(perguntas["dia"])
  if saucao_user == "dia":
      print(perguntas["dia"])
  if saucao_user == "calendario":
      print(perguntas["calendario"])