import os
from datetime import datetime

BASE_DIR = "./clientes"

# Crear directorio si no existe
os.makedirs(BASE_DIR, exist_ok=True)

def obtener_ruta(nombre):
    nombre_archivo = nombre.lower().replace(" ", "_")
    return os.path.join(BASE_DIR, f"{nombre_archivo}.txt")

def crear_cliente():
    nombre = input("Nombre del cliente: ")
    ruta = obtener_ruta(nombre)
    if os.path.exists(ruta):
        print("El cliente ya existe.")
        return
    email = input("Correo electrónico: ")
    telefono = input("Teléfono: ")
    descripcion = input("Descripción del servicio solicitado: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ruta, "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Email: {email}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Fecha de registro: {fecha}\n\n")
        archivo.write("Historial de servicios:\n")
        archivo.write(f"[{fecha}] {descripcion}\n")

    print("Cliente creado exitosamente.")

def consultar_cliente():
    nombre = input("Nombre del cliente: ")
    ruta = obtener_ruta(nombre)
    if os.path.exists(ruta):
        with open(ruta, "r") as archivo:
            print(archivo.read())
    else:
        print("Cliente no encontrado.")

def modificar_cliente():
    nombre = input("Nombre del cliente a modificar: ")
    ruta = obtener_ruta(nombre)
    if not os.path.exists(ruta):
        print("Cliente no encontrado.")
        return

    print("¿Qué desea modificar?")
    print("1. Agregar nueva solicitud")
    print("2. Editar datos de contacto")
    opcion = input("Opción: ")

    if opcion == "1":
        descripcion = input("Descripción del nuevo servicio: ")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(ruta, "a") as archivo:
            archivo.write(f"[{fecha}] {descripcion}\n")
        print("Solicitud agregada.")
    elif opcion == "2":
        email = input("Nuevo correo electrónico: ")
        telefono = input("Nuevo teléfono: ")
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()

        for i, linea in enumerate(lineas):
            if linea.startswith("Email:"):
                lineas[i] = f"Email: {email}\n"
            elif linea.startswith("Teléfono:"):
                lineas[i] = f"Teléfono: {telefono}\n"

        with open(ruta, "w") as archivo:
            archivo.writelines(lineas)

        print("Datos de contacto actualizados.")
    else:
        print("Opción inválida.")

def eliminar_cliente():
    nombre = input("Nombre del cliente a eliminar: ")
    ruta = obtener_ruta(nombre)
    if os.path.exists(ruta):
        os.remove(ruta)
        print("Cliente eliminado.")
    else:
        print("Cliente no encontrado.")

def listar_clientes():
    print("Clientes registrados:")
    for archivo in os.listdir(BASE_DIR):
        if archivo.endswith(".txt"):
            nombre = archivo.replace("_", " ").replace(".txt", "")
            print(f"- {nombre}")

def menu():
    while True:
        print("\n=== Menú de Gestión de Clientes ===")
        print("1. Crear nuevo cliente")
        print("2. Consultar cliente")
        print("3. Modificar cliente")
        print("4. Eliminar cliente")
        print("5. Listar clientes")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_cliente()
        elif opcion == "2":
            consultar_cliente()
        elif opcion == "3":
            modificar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            listar_clientes()
        elif opcion == "6":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
