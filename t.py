import json

# Carregar o JSON do arquivo
with open("project_aurora/aurora/dicionario/info.json") as data:
    info = json.load(data)

# Iterar sobre a lista de pessoas
for pessoa in info:
    if pessoa["genero"] == "masculino":
        tipo = "Senhor"
    elif pessoa["genero"] == "feminino":
        tipo = "Senhora"
    else:
        tipo = "Gênero não definido"

    print(f"{pessoa['name']}: {tipo}")
