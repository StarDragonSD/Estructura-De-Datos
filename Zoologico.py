class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Edad: {self.edad}"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, animal):
        """ Agrega un animal a la lista, asegurándose que no se repita. """
        if self.buscar_animal(animal.nombre, animal.tipo):
            print(f"El animal {animal.nombre} ({animal.tipo}) ya está registrado.")
            return
        
        nuevo_nodo = Nodo(animal)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Animal {animal.nombre} añadido correctamente.")

    def buscar_animal(self, nombre, tipo):
        """ Busca si ya existe un animal con el mismo nombre y tipo. """
        actual = self.cabeza
        while actual:
            if actual.animal.nombre == nombre and actual.animal.tipo == tipo:
                return True
            actual = actual.siguiente
        return False

    def mostrar_animales_iterativo(self):
        """ Muestra todos los animales usando un bucle iterativo. """
        actual = self.cabeza
        if not actual:
            print("No hay animales registrados.")
            return
        while actual:
            print(actual.animal)
            actual = actual.siguiente

    def mostrar_animales_recursivo(self, nodo=None):
        """ Muestra todos los animales de forma recursiva. """
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            print("No hay animales registrados.")
            return
        print(nodo.animal)
        if nodo.siguiente:  # Verifica que haya un siguiente nodo para evitar la recursión infinita
            self.mostrar_animales_recursivo(nodo.siguiente)

# Crear Animales
animal1 = Animal("Águila", 5, "Ave")
animal2 = Animal("Pantera", 3, "Mamífero")
animal3 = Animal("Vaca", 7, "Mamífero")
animal4 = Animal("Águila", 4, "Ave")  # Animal repetido

#Lista Enlazada Y Animales
zoologico = ListaEnlazada()
zoologico.agregar_animal(animal1)
zoologico.agregar_animal(animal2)
zoologico.agregar_animal(animal3)
zoologico.agregar_animal(animal4)  # Este animal no se añadirá

#Iterativo y Recursivo De Animales
print("\nMétodo Iterativo:")
zoologico.mostrar_animales_iterativo()

print("\nMétodo Recursivo:")
zoologico.mostrar_animales_recursivo()
