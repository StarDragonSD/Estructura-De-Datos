import json
import os

class Usuario:
    def __init__(self, nombre_de_usuario, contrasena):
        self.nombre_de_usuario = nombre_de_usuario
        self._contrasena = contrasena

    def verificar_credenciales(self, nombre, contrasena):
        return self.nombre_de_usuario == nombre and self._contrasena == contrasena

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre_de_usuario,
            "contrasena": self._contrasena
        }

class Administrador(Usuario):
    def gestionar_usuarios(self):
        print(f"[Admin] {self.nombre_de_usuario} está gestionando usuarios...")

class Cliente(Usuario):
    def realizar_compra(self):
        print(f"[Cliente] {self.nombre_de_usuario} está realizando una compra...")

#FUNCIONES DE ARCHIVO

ARCHIVO = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, "r") as f:
        datos = json.load(f)
        usuarios = []
        for u in datos:
            if u["tipo"] == "Administrador":
                usuarios.append(Administrador(u["nombre"], u["contrasena"]))
            elif u["tipo"] == "Cliente":
                usuarios.append(Cliente(u["nombre"], u["contrasena"]))
        return usuarios

def guardar_usuarios(usuarios):
    with open(ARCHIVO, "w") as f:
        json.dump([u.to_dict() for u in usuarios], f, indent=4)

#FUNCIONES DE APLICACIÓN

def registrar_usuario(usuarios):
    nombre = input("Nombre de usuario: ")
    if any(u.nombre_de_usuario == nombre for u in usuarios):
        print("❌ Ese nombre ya está en uso.")
        return

    contrasena = input("Contraseña: ")
    tipo = input("Tipo de usuario (1 = Cliente, 2 = Administrador): ")

    if tipo == "1":
        nuevo = Cliente(nombre, contrasena)
    elif tipo == "2":
        nuevo = Administrador(nombre, contrasena)
    else:
        print("Tipo inválido.")
        return

    usuarios.append(nuevo)
    guardar_usuarios(usuarios)
    print(f"✅ Usuario {nombre} registrado exitosamente como {nuevo.__class__.__name__}.")

def iniciar_sesion(usuarios):
    nombre = input("Usuario: ")
    contrasena = input("Contraseña: ")

    for u in usuarios:
        if u.verificar_credenciales(nombre, contrasena):
            print(f"✅ Bienvenido, {u.nombre_de_usuario} ({u.__class__.__name__})")
            if isinstance(u, Administrador):
                u.gestionar_usuarios()
            elif isinstance(u, Cliente):
                u.realizar_compra()
            return
    print("❌ Credenciales incorrectas.")

#MENÚ

def menu():
    usuarios = cargar_usuarios()

    while True:
        print("\n==== MENÚ ====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            iniciar_sesion(usuarios)
        elif opcion == "3":
            print("Hasta luego 👋")
            break
        else:
            print("Opción inválida.")

#EJECUCIÓN PRINCIPAL

if __name__ == "__main__":
    menu()

[{"tipo": "Cliente",
        "nombre": "juanito",
        "contrasena": "clave123"},
    {"tipo": "Administrador",
        "nombre": "admin",
        "contrasena": "adminpass"}]
