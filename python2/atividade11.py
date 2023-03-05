#baseado na classe Triangulo que você deve ter criado
#Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, 
#e False caso contrário.

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "isósceles"
        else:
            return "escaleno"
    
    def retangulo(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        return lados[0]**2 + lados[1]**2 == lados[2]**2
