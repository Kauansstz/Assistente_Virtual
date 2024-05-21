import json
from project_aurora.aurora import response as rp

with open("project_aurora/aurora/dicionario/dici.json") as arquivo:
    base = json.load(arquivo)

rp.about()
