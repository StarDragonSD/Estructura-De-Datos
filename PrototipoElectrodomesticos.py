class Electrodomestico:
    def __init__(self, marca, modelo, consumo_energetico):
        if not marca or not modelo or consumo_energetico < 0:
            raise ValueError("Datos inválidos para el electrodoméstico.")
        
        self.marca = marca
        self.modelo = modelo
        self.consumo_energetico = consumo_energetico

    def encender(self):
        print(f"{self.marca} {self.modelo} está encendido.")

    def apagar(self):
        print(f"{self.marca} {self.modelo} está apagado.")

    def __str__(self):
        return f"{self.__class__.__name__} - {self.marca} {self.modelo} (Consumo: {self.consumo_energetico} kWh)"

class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, capacidad):
        super().__init__(marca, modelo, consumo_energetico)
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero.")
        self.capacidad = capacidad

    def encender(self):
        print(f"Lavadora {self.marca} {self.modelo} encendida.")
        self.elegir_ciclo()

    def elegir_ciclo(self):
        print("Selecciona un ciclo de lavado:")
        print("1. Rápido")
        print("2. Normal")
        print("3. Intensivo")
        opcion = input("→ Ingresa el número de opción: ")
        if opcion == "1":
            print("Ciclo rápido iniciado (30 min, baja temperatura).")
        elif opcion == "2":
            print("Ciclo normal iniciado (1 h, 40°C).")
        elif opcion == "3":
            print("Ciclo intensivo iniciado (2 h, 60°C).")
        else:
            print("Opción no válida. Se inicia ciclo normal por defecto.")
            print("Ciclo normal iniciado (1 h, 40°C).")

    def apagar(self):
        print(f"Lavadora {self.marca} {self.modelo} apagada.")

    def __str__(self):
        return f"Lavadora - {self.marca} {self.modelo} (Capacidad: {self.capacidad} kg, Consumo: {self.consumo_energetico} kWh)"

class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo_energetico, tiene_congelador):
        super().__init__(marca, modelo, consumo_energetico)
        self.tiene_congelador = tiene_congelador
        self.temperatura = 4  # temperatura por defecto (°C)

    def encender(self):
        print(f"Refrigerador {self.marca} {self.modelo} encendido.")
        self.regular_temperatura()

    def regular_temperatura(self):
        print(f"Temperatura actual: {self.temperatura}°C")
        cambiar = input("¿Deseas cambiar la temperatura? (s/n): ").lower()
        if cambiar == 's':
            try:
                nueva_temp = int(input("→ Ingresa nueva temperatura en °C (entre 1 y 8): "))
                if 1 <= nueva_temp <= 8:
                    self.temperatura = nueva_temp
                    print(f"Temperatura ajustada a {self.temperatura}°C.")
                else:
                    print("Temperatura fuera de rango. No se realizaron cambios.")
            except ValueError:
                print("Entrada inválida. No se realizaron cambios.")
        if self.tiene_congelador:
            print("Congelador activado.")
        else:
            print("Este modelo no tiene congelador.")

    def apagar(self):
        print(f"Refrigerador {self.marca} {self.modelo} apagado.")

    def __str__(self):
        congelador = "Sí" if self.tiene_congelador else "No"
        return f"Refrigerador - {self.marca} {self.modelo} (Congelador: {congelador}, Consumo: {self.consumo_energetico} kWh)"

#Dispositivos
lavadora = Lavadora("Samsung", "EcoBubble X1", 0.8, 9)
refrigerador = Refrigerador("LG", "CoolPlus 500", 1.2, True)

#Información
print(lavadora)
print(refrigerador)

#Encender
lavadora.encender()
refrigerador.encender()

#Apagar
lavadora.apagar()
refrigerador.apagar()
