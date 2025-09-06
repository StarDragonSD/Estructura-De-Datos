class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energetico):
        self.marca = marca
        self.modelo = modelo
        self.consumo_energetico = consumo_energetico  # kWh

    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido.")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.marca} {self.modelo} (Consumo: {self.consumo_energetico} kWh)"


#Lavadora
class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, capacidad):
        super().__init__(marca, modelo, consumo_energetico)
        self.capacidad = capacidad  # en kilogramos

    def encender(self):
        print(f"Lavadora {self.marca} {self.modelo} encendida.")
        self.iniciar_ciclo_de_lavado()

    def iniciar_ciclo_de_lavado(self):
        print(f"Iniciando ciclo de lavado con capacidad de {self.capacidad} kg.")

    def __str__(self):
        return f"Lavadora - {self.marca} {self.modelo} (Capacidad: {self.capacidad} kg, Consumo: {self.consumo_energetico} kWh)"


#Refrigerador
class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, tiene_congelador):
        super().__init__(marca, modelo, consumo_energetico)
        self.tiene_congelador = tiene_congelador

    def encender(self):
        print(f"Refrigerador {self.marca} {self.modelo} encendido.")
        self.regular_temperatura()

    def regular_temperatura(self):
        if self.tiene_congelador:
            print("Regulando temperatura: refrigerador + congelador.")
        else:
            print("Regulando temperatura: solo refrigerador.")

    def __str__(self):
        congelador = "Sí" if self.tiene_congelador else "No"
        return f"Refrigerador - {self.marca} {self.modelo} (Congelador: {congelador}, Consumo: {self.consumo_energetico} kWh)"

#Objetos
lavadora = Lavadora("Samsung", "EcoBubble X1", 0.8, 9)
refrigerador = Refrigerador("LG", "CoolPlus 500", 1.2, True)
#Información
print(lavadora)
print(refrigerador)

#Encender Dispositivos
lavadora.encender()
refrigerador.encender()
