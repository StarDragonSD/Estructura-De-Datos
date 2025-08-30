class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} de edad"
    
    @staticmethod
    def esMayor():
        return None


    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
class Estudiante(Persona):
    __promedio: float

    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)    
        self.carrera = carrera
    
    def estudiar(self) -> str:
        return f"{self.nombre} esta estudiando {self.carrera}."
    
    def __str__(self) -> str:
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, carrera={self.carrera})"
    
    def getPromedio(self) -> float:
        return self.__promedio
    
    def setPromedio(self, promedio: float) -> None:
        self.__promedio = promedio
        
Orión = Persona("Orión", 30)
Lucas = Estudiante("Lucas", 22, "Ingenieria")
print(Orión.saludar)
print(Lucas.saludar)
Orión.altura = 1.75
print(Orión)
print(Lucas.__promedio) # Esto generara un error porque .__promedio es privado