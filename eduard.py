import datetime

saucao_bot = print("Seja Bem-Vindo!\nSou Eduard! Seu assistente virtual.")
saucao_user = input("Como posso te ajudar?\nR: ")

if saucao_user == 'pesquisa':
    print("Digite um palavra que seja precisa\nExemplo: 'clima', irá retorna como está o clima da sua região")

    lista = [
            "tempo",
            "clima", 
            "Horas", 
            "dia", 
            "calendario"
        ]
    while True:
        print("Digite o que deseja Pesquisar")
        print(f"Aqui estão uma lista de opções para pesquisar.", lista)
        response = input("O que seja pesquisar?\nR: ")
        
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
            if response == "clima" or saucao_user == "Clima":
                print(perguntas["clima"])
                
            if response == "dia" or saucao_user == "Dia":
                print(perguntas["dia"])
                
            if response == "tempo" or saucao_user == "Tempo":
                print(perguntas["tempo"])
                
            if response == "horas" or saucao_user =="Horas":
                print(perguntas["horas"])
                
            if response == "calendario" or saucao_user == "Calendario":
                print(perguntas["calendario"])
                
            continua = input("Deseja continuar?")
            if continua.lower() == "n":
                break
        