import json
from project_aurora.aurora import response as rp

with open("project_aurora/dicionario/dici.json") as arquivo:
    base = json.load(arquivo)
greetings_user = input("R: ")
if greetings_user.lower() in base["dic"]["about"]:
    rp.about()
