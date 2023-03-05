#Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe um objeto do tipo
#Triangulo como parâmetro e verifica se o triângulo atual é semelhante ao triângulo passado como parâmetro.
# Caso positivo, o método deve devolver True. Caso negativo, deve devolver False
#Um triângulo é semelhante a outro triângulo se a razão (divisão) entre os comprimentos dos seus lados 
#forem iguais

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
    
    def semelhantes(self, triangulo):
        razao1 = self.a / triangulo.a
        razao2 = self.b / triangulo.b
        razao3 = self.c / triangulo.c
        return razao1 == razao2 == razao3
