import math

class FiguraGeometrica:
    def calcularArea(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def __str__(self):
        return "Figura geométrica genérica"

#Triángulo
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        return f"Triángulo (base={self.base}, altura={self.altura})"

#Cuadrado
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        if lado <= 0:
            raise ValueError("El lado debe ser mayor que cero.")
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

    def __str__(self):
        return f"Cuadrado (lado={self.lado})"

#Círculo
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que cero.")
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2

    def __str__(self):
        return f"Círculo (radio={self.radio})"

#Areas
def comparar_areas(fig1, fig2):
    area1 = fig1.calcularArea()
    area2 = fig2.calcularArea()

    print(f"\nComparando áreas:")
    print(f"{fig1} → área = {area1:.2f}")
    print(f"{fig2} → área = {area2:.2f}")

    if area1 > area2:
        print("→ La primera figura tiene mayor área.")
    elif area2 > area1:
        print("→ La segunda figura tiene mayor área.")
    else:
        print("→ Ambas figuras tienen la misma área.")

def menu():
    figuras = []

    while True:
        print("\nMenú:")
        print("1. Crear Triángulo")
        print("2. Crear Cuadrado")
        print("3. Crear Círculo")
        print("4. Ver todas las figuras")
        print("5. Comparar dos figuras")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == '1':
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                figura = Triangulo(base, altura)
                figuras.append(figura)
                print(f"Figura creada: {figura} (área = {figura.calcularArea():.2f})")

            elif opcion == '2':
                lado = float(input("Ingresa el lado del cuadrado: "))
                figura = Cuadrado(lado)
                figuras.append(figura)
                print(f"Figura creada: {figura} (área = {figura.calcularArea():.2f})")

            elif opcion == '3':
                radio = float(input("Ingresa el radio del círculo: "))
                figura = Circulo(radio)
                figuras.append(figura)
                print(f"Figura creada: {figura} (área = {figura.calcularArea():.2f})")

            elif opcion == '4':
                if not figuras:
                    print("No hay figuras creadas.")
                else:
                    print("\nFiguras creadas:")
                    for i, fig in enumerate(figuras):
                        print(f"{i + 1}. {fig} (área = {fig.calcularArea():.2f})")

            elif opcion == '5':
                if len(figuras) < 2:
                    print("Debes crear al menos dos figuras para comparar.")
                else:
                    print("Selecciona dos figuras por número:")
                    for i, fig in enumerate(figuras):
                        print(f"{i + 1}. {fig}")
                    idx1 = int(input("Figura 1: ")) - 1
                    idx2 = int(input("Figura 2: ")) - 1
                    comparar_areas(figuras[idx1], figuras[idx2])

            elif opcion == '6':
                print("¡Hasta luego!")
                break

            else:
                print("Opción inválida.")
        except ValueError as e:
            print(f"Error: {e}")
        except IndexError:
            print("Índice inválido.")

if __name__ == "__main__":
    menu()