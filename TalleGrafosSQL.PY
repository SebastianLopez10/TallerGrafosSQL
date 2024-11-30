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

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Crear un nodo")
    print("2. Leer nodos")
    print("3. Actualizar un nodo")
    print("4. Eliminar un nodo")
    print("5. Crear una arista")
    print("6. Eliminar una arista")
    print("7. Salir")

def ejecutar_opcion(opcion):
    if opcion == 1:
        id_nodo = int(input("Ingrese el ID del nodo: "))
        nombre = input("Ingrese el nombre del nodo: ")
        crear_nodo(id_nodo, nombre)
    elif opcion == 2:
        leer_nodos()
    elif opcion == 3:
        id_nodo = int(input("Ingrese el ID del nodo: "))
        nombre = input("Ingrese el nuevo nombre del nodo: ")
        actualizar_nodo(id_nodo, nombre)
    elif opcion == 4:
        id_nodo = int(input("Ingrese el ID del nodo a eliminar: "))
        eliminar_nodo(id_nodo)
    elif opcion == 5:
        id_origen = int(input("Ingrese el ID del nodo origen: "))
        id_destino = int(input("Ingrese el ID del nodo destino: "))
        crear_arista(id_origen, id_destino)
    elif opcion == 6:
        id_origen = int(input("Ingrese el ID del nodo origen: "))
        id_destino = int(input("Ingrese el ID del nodo destino: "))
        eliminar_arista(id_origen, id_destino)
    elif opcion == 7:
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        ejecutar_opcion(opcion)
