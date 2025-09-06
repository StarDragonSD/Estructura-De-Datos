class Usuario:
    def __init__(self, nombre_de_usuario, contrasena):
        self.nombre_de_usuario = nombre_de_usuario
        self._contrasena = contrasena  # protegido, no público

    def iniciar_sesion(self, usuario_ingresado, contrasena_ingresada):
        if self.nombre_de_usuario == usuario_ingresado and self._contrasena == contrasena_ingresada:
            print(f"Inicio de sesión exitoso. Bienvenido, {self.nombre_de_usuario}.")
            return True
        else:
            print("Error: Nombre de usuario o contraseña incorrectos.")
            return False

    def __str__(self):
        return f"Usuario: {self.nombre_de_usuario}"


#Administrador
class Administrador(Usuario):
    def __init__(self, nombre_de_usuario, contrasena):
        super().__init__(nombre_de_usuario, contrasena)

    def gestionar_usuarios(self):
        print(f"{self.nombre_de_usuario} está gestionando usuarios...")

    def __str__(self):
        return f"Administrador: {self.nombre_de_usuario}"


#Cliente
class Cliente(Usuario):
    def __init__(self, nombre_de_usuario, contrasena):
        super().__init__(nombre_de_usuario, contrasena)

    def realizar_compra(self):
        print(f"{self.nombre_de_usuario} está realizando una compra...")

    def __str__(self):
        return f"Cliente: {self.nombre_de_usuario}"

#Instancias
admin = Administrador("admin123", "adminpass")
cliente = Cliente("juanito", "clave123")

#Inicio de sesión
print("\n→ Intento de inicio de sesión como administrador:")
if admin.iniciar_sesion("admin123", "adminpass"):
    admin.gestionar_usuarios()

print("\n→ Intento de inicio de sesión como cliente:")
if cliente.iniciar_sesion("juanito", "clave123"):
    cliente.realizar_compra()

print("\n→ Intento con credenciales incorrectas:")
cliente.iniciar_sesion("juanito", "clave_incorrecta")
