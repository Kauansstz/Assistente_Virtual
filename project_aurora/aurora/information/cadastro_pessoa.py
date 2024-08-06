import json


class Pessoa:
    def __init__(self, name, idade, email, genero):
        self.name = name
        self.idade = idade
        self.email = email
        self.genero = genero

    def get_nome(self):
        self.name

    def get_email(self):
        self.email

    def get_genero(self):
        self.genero

    def get_idade(self):
        try:
            years = self.idade
            if years >= int("18"):
                self.get_email()
                self.show_data()

            else:
                print("Para se cadastrar, tem que haver acima ou igual a 18 anos.")

        except ValueError:
            print("Por Favor, digite uma idade válida.")

    def show_data(self):
        print(
            f"""
            Informações coletadas:
            Nome: {self.name},
            Idade: {self.idade},
            E-mail: {self.email},
            Genêro: {self.genero}
            """
        )
        response = input(
            "As informações acima estão corretas? Digite [S] para Sim e [N] para Não: "
        )

        match response.lower():
            case "s":
                print("Cadastro completado!")
            case "n":
                print("Por favor corrija os dados")
            case _:
                print("Não entendi o que digitou")

    def to_dict(self):
        """Converte a instância da classe Pessoa em um dicionário."""
        return {
            "name": self.name,
            "idade": self.idade,
            "email": self.email,
            "genero": self.genero,
        }

    @classmethod
    def from_dict(cls, data):
        """Cria uma instância da classe Pessoa a partir de um dicionário."""
        return cls(data["name"], data["idade"], data["email"], data["genero"])


def carregar_dados(arquivo):
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []
    return dados


def salvar_dados(arquivo, dados):
    with open(arquivo, "w") as f:
        json.dump(dados, f, indent=4)


def adicionar_pessoa(pessoa, arquivo="data.json"):
    dados = carregar_dados(arquivo)
    dados.append(pessoa.to_dict())
    salvar_dados(arquivo, dados)


def exibir_dados(arquivo="data.json"):
    """Exibe os dados do arquivo JSON."""
    dados = carregar_dados(arquivo)
    for data in dados:
        pessoa = Pessoa.from_dict(data)
        print(
            f"Nome: {pessoa.name}, Idade: {pessoa.idade}, Email: {pessoa.email}, Genero: {pessoa.genero}"
        )
