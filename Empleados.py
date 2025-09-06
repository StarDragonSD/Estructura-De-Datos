class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

#Desarrolladores
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")

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

#Empleados
dev1 = Desarrollador("Ana", 50000, "Desarrollo", "Python")
dev2 = Desarrollador("Luis", 52000, "Desarrollo", "JavaScript")
gerente = Gerente("Carlos", 70000, "Desarrollo", equipo=[dev1, dev2])

dev1.trabajar()
dev2.trabajar()
gerente.trabajar()

