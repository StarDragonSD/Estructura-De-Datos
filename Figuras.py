class FiguraGeometrica:
    def calcularArea(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

#Triángulo
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = (self.base * self.altura) / 2
        print(f"Área del triángulo: {area}")
        return area

#Cuadrado
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        area = self.lado ** 2
        print(f"Área del cuadrado: {area}")
        return area

#Figuras
triangulo = Triangulo(base=10, altura=5)
cuadrado = Cuadrado(lado=4)

#Areas
triangulo.calcularArea()
cuadrado.calcularArea()
