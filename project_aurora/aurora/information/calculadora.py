class Calculadora:
    def __init__(self, a, b, c=None, d=None):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c) if c is not None else None
        self.d = float(d) if d is not None else None

    def multiplicar(self):
        if self.c and self.d is not None:
            response = self.a * self.b * self.c * self.d
        elif self.c is not None:
            response = self.a * self.b * self.c
        else:
            response = self.a * self.b
        return response

    def somar(self):
        if self.c and self.d is not None:
            response = self.a + self.b + self.c + self.d
        elif self.c is not None:
            response = self.a + self.b + self.c
        else:
            response = self.a + self.b
        return response

    def divisao(self):
        if self.c and self.d is not None:
            response = self.a / self.b / self.c / self.d
        elif self.c is not None:
            response = self.a / self.b / self.c
        else:
            response = self.a / self.b
        return response

    def subtacao(self):
        if self.c and self.d is not None:
            response = self.a - self.b - self.c - self.d
        elif self.c is not None:
            response = self.a - self.b - self.c
        else:
            response = self.a - self.b
        return response

    def solve_quadratic(self):
        # Calculando o discriminante
        if self.c is not None:
            discriminant = self.b**2 - 4 * self.a * self.c

            # Calculando as duas raízes
            root1 = (self.b + discriminant) / (2 * self.a)
            root2 = (self.b - discriminant) / (2 * self.a)

            return root1, root2

    def porcentagem_de_relação(self):
        if self.c is not None:
            self.a = int(input("Digite o valor base: "))
            self.b = int(input("Digite o valor da relação: "))
            self.c = 100
            p1 = self.a / self.b * self.c
            print(f"a porcentagem de {self.a} em relação com {self.b} é: {p1}%")

    def porcentagem_de_base(self):
        if self.c is not None:
            self.a = int(input("Digite o valor da parte a ser encontrada: "))
            self.b = 100
            self.c = int(input("Digite o valor da base: "))
            p1 = self.a / self.b * self.c
            print(f"a porcentagem de {self.a} em relação com {self.b} é: {p1}%")

    def porcentagem_de_total(self):
        if self.c is not None:
            self.a = int(input("Digite o valor da parte: "))
            self.b = int(input("Digite a porcentagem da parte: "))
            self.c = 100
            p1 = self.b / self.c
            p2 = self.a / p1
            print(f"a porcentagem de {self.a} em relação com {self.b} é: {p2}%")
