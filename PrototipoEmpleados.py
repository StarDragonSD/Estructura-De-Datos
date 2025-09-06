class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

    def cambiar_departamento(self, nuevo_departamento):
        print(f"{self.nombre} ha sido transferido de {self.departamento} a {nuevo_departamento}.")
        self.departamento = nuevo_departamento

    def calcular_bonificacion(self):
        bonificacion = self.salario * 0.10
        print(f"Bonificación de {self.nombre}: ${bonificacion:.2f}")
        return bonificacion

#Desarrollador
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")

    def calcular_bonificacion(self):
        bonificacion = self.salario * 0.15
        print(f"Bonificación de {self.nombre} (Desarrollador): ${bonificacion:.2f}")
        return bonificacion

#Gerente
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo=None):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo if equipo else []

    def trabajar(self):
        print(f"{self.nombre} está supervisando al equipo en el departamento de {self.departamento}.")
        self.supervisarAEquipo()

    def supervisarAEquipo(self):
        if not self.equipo:
            print(f"{self.nombre} no tiene empleados a su cargo.")
        else:
            print(f"{self.nombre} está supervisando a:")
            for empleado in self.equipo:
                print(f" - {empleado.nombre} ({type(empleado).__name__})")

    def calcular_bonificacion(self):
        porcentaje_equipo = 0.05 * len(self.equipo)
        bonificacion = self.salario * (0.20 + porcentaje_equipo)
        print(f"Bonificación de {self.nombre} (Gerente): ${bonificacion:.2f}")
        return bonificacion

#Empleados
dev1 = Desarrollador("Ana", 50000, "Desarrollo", "Python")
dev2 = Desarrollador("Luis", 52000, "Desarrollo", "JavaScript")
gerente = Gerente("Carlos", 70000, "Desarrollo", equipo=[dev1, dev2])

#El Trabajar
dev1.trabajar()
dev2.trabajar()
gerente.trabajar()

# Cambio De Departamento
dev1.cambiar_departamento("Investigación")
gerente.cambiar_departamento("Dirección Técnica")

# Bonificaciones
dev1.calcular_bonificacion()
dev2.calcular_bonificacion()
gerente.calcular_bonificacion()
