from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")  # Convirtiendo la fecha a un objeto datetime

    def __str__(self):
        return f"Descripción: {self.descripcion}, Prioridad: {self.prioridad}, Vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class Nodo:
    def __init__(self, tarea):
        self.tarea = tarea
        self.siguiente = None

class ListaEnlazadaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        """ Agrega una nueva tarea al final de la lista. """
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        print(f"Tarea '{tarea.descripcion}' añadida correctamente.")

    def eliminar_tarea(self, descripcion=None, posicion=None):
        """ Elimina una tarea por descripción o por posición en la lista. """
        if descripcion:
            actual = self.cabeza
            previo = None
            while actual:
                if actual.tarea.descripcion == descripcion:
                    if previo:
                        previo.siguiente = actual.siguiente
                    else:
                        self.cabeza = actual.siguiente
                    print(f"Tarea '{descripcion}' eliminada.")
                    return
                previo = actual
                actual = actual.siguiente
            print(f"Tarea '{descripcion}' no encontrada.")
        elif posicion:
            actual = self.cabeza
            index = 0
            previo = None
            while actual:
                if index == posicion:
                    if previo:
                        previo.siguiente = actual.siguiente
                    else:
                        self.cabeza = actual.siguiente
                    print(f"Tarea en posición {posicion} eliminada.")
                    return
                index += 1
                previo = actual
                actual = actual.siguiente
            print("Posición no válida.")

    def mostrar_tareas(self):
        """ Muestra todas las tareas ordenadas por prioridad y fecha de vencimiento. """
        if not self.cabeza:
            print("No hay tareas registradas.")
            return
        
        #lista de tareas para ordenarlas
        tareas = []
        actual = self.cabeza
        while actual:
            tareas.append(actual.tarea)
            actual = actual.siguiente

        # Ordenar por prioridad (de alta a baja), luego por fecha de vencimiento
        tareas.sort(key=lambda tarea: (tarea.prioridad, tarea.fecha_vencimiento))

        # Mostrar tareas
        for tarea in tareas:
            print(tarea)

    def buscar_tarea(self, descripcion):
        """ Busca una tarea por descripción. """
        actual = self.cabeza
        while actual:
            if actual.tarea.descripcion == descripcion:
                print("Tarea encontrada:", actual.tarea)
                return
            actual = actual.siguiente
        print(f"Tarea con descripción '{descripcion}' no encontrada.")

    def marcar_completada(self, descripcion):
        """ Marca una tarea como completada (eliminándola de la lista). """
        self.eliminar_tarea(descripcion=descripcion)


#lista enlazada de tareas
gestor_tareas = ListaEnlazadaTareas()

# Agregar tareas
gestor_tareas.agregar_tarea(Tarea("Comprar comida", 1, "2025-09-15"))
gestor_tareas.agregar_tarea(Tarea("Estudiar programación", 2, "2025-09-20"))
gestor_tareas.agregar_tarea(Tarea("Hacer ejercicio", 3, "2025-09-12"))
gestor_tareas.agregar_tarea(Tarea("Revisar correos", 1, "2025-09-13"))

# Mostrar las tareas
print("\nTareas ordenadas por prioridad y fecha de vencimiento:")
gestor_tareas.mostrar_tareas()

# Buscar una tarea
print("\nBuscar tarea 'Estudiar programación':")
gestor_tareas.buscar_tarea("Estudiar programación")

# Marcar una tarea como completada (eliminarla)
print("\nMarcar tarea 'Hacer ejercicio' como completada:")
gestor_tareas.marcar_completada("Hacer ejercicio")

# Mostrar las tareas después de eliminar una
print("\nTareas después de completar una:")
gestor_tareas.mostrar_tareas()

# Eliminar una tarea por posición
print("\nEliminar tarea en posición 1:")
gestor_tareas.eliminar_tarea(posicion=1)

# Mostrar las tareas después de eliminar una por posición
print("\nTareas después de eliminar por posición:")
gestor_tareas.mostrar_tareas()
