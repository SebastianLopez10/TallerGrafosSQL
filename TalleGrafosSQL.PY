import mysql.connector
from mysql.connector import Error

# Configuración de la conexión
db = mysql.connector.connect(user='root', password= 'S1ebastian1',
                              host='localhost', database= 'tallergrafosql',
                              auth_plugin='mysql_native_password')

# Llamar al procedimiento CrearNodo
def crear_nodo(id, nombre):
    try:
        cursor = db.cursor()
        cursor.callproc('CrearNodo', [id, nombre])
        db.commit()
        print(f"Nodo creado: {nombre}")
    except Error as e:
        print(f"Error al crear nodo: {e}")
    finally:
        cursor.close()

# Llamar al procedimiento LeerNodos
def leer_nodos():
    try:
        cursor = db.cursor()
        cursor.callproc('LeerNodos')
        for resultado in cursor.stored_results():
            print("Nodos:")
            for fila in resultado.fetchall():
                print(f"ID: {fila[0]}, Nombre: {fila[1]}")
    except Error as e:
        print(f"Error al leer nodos: {e}")
    finally:
        cursor.close()

# Llamar al procedimiento ActualizarNodo
def actualizar_nodo(id, nuevo_nombre):
    try:
        cursor = db.cursor()
        cursor.callproc('ActualizarNodo', [id, nuevo_nombre])
        db.commit()
        print(f"Nodo actualizado: ID {id} -> {nuevo_nombre}")
    except Error as e:
        print(f"Error al actualizar nodo: {e}")
    finally:
        cursor.close()

# Llamar al procedimiento EliminarNodo
def eliminar_nodo(id):
    try:
        cursor = db.cursor()
        cursor.callproc('EliminarNodo', [id])
        db.commit()
        print(f"Nodo eliminado: ID {id}")
    except Error as e:
        print(f"Error al eliminar nodo: {e}")
    finally:
        cursor.close()

# Llamar al procedimiento CrearArista
def crear_arista(origen, destino):
    try:
        cursor = db.cursor()
        cursor.callproc('CrearArista', [origen, destino])
        db.commit()
        print(f"Arista creada: {origen} -> {destino}")
    except Error as e:
        print(f"Error al crear arista: {e}")
    finally:
        cursor.close()

# Llamar al procedimiento EliminarArista
def eliminar_arista(origen, destino):
    try:
        cursor = db.cursor()
        cursor.callproc('EliminarArista', [origen, destino])
        db.commit()
        print(f"Arista eliminada: {origen} -> {destino}")
    except Error as e:
        print(f"Error al eliminar arista: {e}")
    finally:
        cursor.close()

# Función para leer y mostrar los nodos y aristas
def ver_nodos_y_aristas():
    try:
        cursor = db.cursor()

        # Leer nodos
        cursor.callproc('LeerNodos')
        print("\nNodos:")
        for resultado in cursor.stored_results():
            for fila in resultado.fetchall():
                print(f"ID: {fila[0]}, Nombre: {fila[1]}")

        # Leer aristas
        cursor.callproc('LeerAristas')
        print("\nAristas:")
        for resultado in cursor.stored_results():
            for fila in resultado.fetchall():
                print(f"Origen: {fila[0]} -> Destino: {fila[1]}")

    except Error as e:
        print(f"Error al leer nodos y aristas: {e}")
    finally:
        cursor.close()

# Menú interactivo
def mostrar_menu():
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Crear Nodo")
        print("2. Leer Nodos")
        print("3. Actualizar Nodo")
        print("4. Eliminar Nodo")
        print("5. Crear Arista")
        print("6. Eliminar Arista")
        print("7. Ver Nodos y Aristas")
        print("8. Salir")

        opcion = input("Elige una opción (1-8): ")

        if opcion == "1":
            id = int(input("Ingrese el ID del nodo: "))
            nombre = input("Ingrese el nombre del nodo: ")
            crear_nodo(id, nombre)
        elif opcion == "2":
            leer_nodos()
        elif opcion == "3":
            id = int(input("Ingrese el ID del nodo a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del nodo: ")
            actualizar_nodo(id, nuevo_nombre)
        elif opcion == "4":
            id = int(input("Ingrese el ID del nodo a eliminar: "))
            eliminar_nodo(id)
        elif opcion == "5":
            origen = int(input("Ingrese el ID del nodo de origen: "))
            destino = int(input("Ingrese el ID del nodo de destino: "))
            crear_arista(origen, destino)
        elif opcion == "6":
            origen = int(input("Ingrese el ID del nodo de origen de la arista a eliminar: "))
            destino = int(input("Ingrese el ID del nodo de destino de la arista a eliminar: "))
            eliminar_arista(origen, destino)
        elif opcion == "7":
            ver_nodos_y_aristas()  # Mostrar nodos y aristas
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor ingrese una opción del 1 al 8.")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
