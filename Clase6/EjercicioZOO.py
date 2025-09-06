from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Nodo:
    valor: Any
    siguiente: Optional[Nodo] = None

class ListaEnlazada:
    def __init__(self) -> None:
        self.cabeza: Optional[Nodo] = None

    def esta_vacia(self) -> bool:
        return self.cabeza is None

    def agregar_al_final(self, valor: Any) -> None:
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def buscar(self, valor: Any) -> bool:
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def eliminar(self, valor: Any) -> bool:
        actual = self.cabeza
        previo: Optional[Nodo] = None
        while actual:
            if actual.valor == valor:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente    				
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def __str__(self) -> str:
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(valores) if valores else "Lista vacía"

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar_al_inicio(3)
    lista.agregar_al_inicio(2)
    lista.agregar_al_final(4)
    print(lista)  # 2 -> 3 -> 4
    print(lista.buscar(3))  # True
    lista.eliminar(3)
    print(lista)  # 2 -> 4
    
    
    
    
    


from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Any

@dataclass
class Animal:
    nombre: str
    tipo: str
    edad: int

    def __init__(self, nombre: str, edad: int, tipo: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def setNombre(self, nombre: str) -> None:
        self.nombre = nombre
    
    def getNombre(self) -> str:
        return self.nombre
    
    def setTipo(self, tipo: str) -> None:
        self.tipo = tipo

    def getTipo(self) -> str:
        return self.tipo
    
    def setEdad(self, edad: int) -> None:
        self.edad = edad
    
    def getEdad(self) -> int:
        return self.edad
    
@dataclass
class Nodo:
    valor: Animal
    siguiente: Optional[Nodo] = None

    def __init__(self, valor: Animal, siguiente: Optional[Nodo] = None) -> None:
        self.valor = valor