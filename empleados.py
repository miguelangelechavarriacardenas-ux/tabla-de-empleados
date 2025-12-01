import sqlite3

# Conectar (o crear) la base de datos
conexion = sqlite3.connect("cafeteria.db")
cursor = conexion.cursor()

# Crear tabla de empleados si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    puesto TEXT NOT NULL,
    salario REAL NOT NULL,
    fecha_ingreso TEXT NOT NULL
)
""")
conexion.commit()

# Funciones CRUD
def agregar_empleado(nombre, puesto, salario, fecha_ingreso):
    cursor.execute("INSERT INTO empleados (nombre, puesto, salario, fecha_ingreso) VALUES (?, ?, ?, ?)",
                   (nombre, puesto, salario, fecha_ingreso))
    conexion.commit()
    print("Empleado agregado correctamente.")

def mostrar_empleados():
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    print("\n Lista de empleados:")
    for e in empleados:
        print(f"ID: {e[0]} | Nombre: {e[1]} | Puesto: {e[2]} | Salario: {e[3]} | Fecha ingreso: {e[4]}")

def actualizar_salario(id_empleado, nuevo_salario):
    cursor.execute("UPDATE empleados SET salario = ? WHERE id = ?", (nuevo_salario, id_empleado))
    conexion.commit()
    print("Salario actualizado correctamente.")

def eliminar_empleado(id_empleado):
    cursor.execute("DELETE FROM empleados WHERE id = ?", (id_empleado,))
    conexion.commit()
    print("Empleado eliminado correctamente.")

# Menú interactivo
def menu():
    while True:
        print("\n--- Sistema de Gestión de Empleados ---")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Actualizar salario")
        print("4. Eliminar empleado")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            puesto = input("Puesto: ")
            salario = float(input("Salario: "))
            fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ")
            agregar_empleado(nombre, puesto, salario, fecha_ingreso)

        elif opcion == "2":
            mostrar_empleados()

        elif opcion == "3":
            id_empleado = int(input("ID del empleado: "))
            nuevo_salario = float(input("Nuevo salario: "))
            actualizar_salario(id_empleado, nuevo_salario)

        elif opcion == "4":
            id_empleado = int(input("ID del empleado: "))
            eliminar_empleado(id_empleado)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

menu()
conexion.close()
