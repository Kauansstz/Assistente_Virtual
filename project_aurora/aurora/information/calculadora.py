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
