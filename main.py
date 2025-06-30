import os
from datetime import datetime

BASE_DIR = "./clientes"
os.makedirs(BASE_DIR, exist_ok=True)

# Tabla hash: nombre_cliente_normalizado -> ruta_archivo
clientes_dict = {}

def normalizar_nombre(nombre):
    return nombre.strip().lower()

def formatear_a_nombre_archivo(nombre):
    return nombre.strip().lower().replace(" ", "_") + ".txt"

def construir_diccionario_clientes():
    clientes = {}
    for archivo in os.listdir(BASE_DIR):
        if archivo.endswith(".txt"):
            nombre = archivo.replace("_", " ").replace(".txt", "").lower()
            ruta = os.path.join(BASE_DIR, archivo)
            clientes[nombre] = ruta
    return clientes

def crear_cliente():
    nombre = input("Nombre del cliente: ")
    clave = normalizar_nombre(nombre)

    if clave in clientes_dict:
        print("El cliente ya existe.")
        return

    email = input("Correo electrónico: ")
    telefono = input("Teléfono: ")
    descripcion = input("Descripción del servicio solicitado: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    archivo_nombre = formatear_a_nombre_archivo(nombre)
    ruta = os.path.join(BASE_DIR, archivo_nombre)

    with open(ruta, "w") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Email: {email}\n")
        archivo.write(f"Teléfono: {telefono}\n")
        archivo.write(f"Fecha de registro: {fecha}\n\n")
        archivo.write("Historial de servicios:\n")
        archivo.write(f"[{fecha}] {descripcion}\n")

    clientes_dict[clave] = ruta
    print("Cliente creado exitosamente.")

def consultar_cliente():
    nombre = input("Nombre del cliente: ")
    clave = normalizar_nombre(nombre)

    if clave in clientes_dict:
        with open(clientes_dict[clave], "r") as archivo:
            print(archivo.read())
    else:
        print("Cliente no encontrado.")

def modificar_cliente():
    nombre = input("Nombre del cliente a modificar: ")
    clave = normalizar_nombre(nombre)

    if clave not in clientes_dict:
        print("Cliente no encontrado.")
        return

    ruta = clientes_dict[clave]

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
    clave = normalizar_nombre(nombre)

    if clave in clientes_dict:
        os.remove(clientes_dict[clave])
        del clientes_dict[clave]
        print("Cliente eliminado.")
    else:
        print("Cliente no encontrado.")

def listar_clientes():
    print("Clientes registrados:")
    for nombre in clientes_dict:
        print(f"- {nombre.title()}")

def menu():
    global clientes_dict
    clientes_dict = construir_diccionario_clientes()

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
