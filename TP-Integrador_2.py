


# - Estructura de datos: Utilizaremos un diccionario donde los contactos estarán organizados por categoría.
# Diccionario donde los contactos estarán clasificados
contactos = {
    "familiares": {},
    "amigos": {},
    "compañeros de trabajo": {}
}


# Permitiremos al usuario elegir la categoría y agregar un contacto con su número.
def agregar_contacto():
    print("\nCategorías disponibles: Familiares, Amigos, Compañeros de trabajo")
    categoria = input("Ingrese la categoría donde desea guardar el contacto: ").strip().lower()

    if categoria in contactos:
        nombre = input("Ingrese el nombre del contacto: ").strip()
        telefono = input("Ingrese el número de teléfono: ").strip()
        contactos[categoria][nombre] = telefono
        print(f"Contacto '{nombre}' agregado a la categoría '{categoria}'.")
    else:
        print("Categoría no válida. Intente nuevamente.")
    
# El usuario puede buscar un nombre dentro de una categoría específica.
def buscar_contacto():
    categoria = input("Ingrese la categoría donde desea buscar el contacto: ").strip().lower()
    
    if categoria in contactos:
        nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
        if nombre in contactos[categoria]:
            print(f"Contacto encontrado: {nombre} - {contactos[categoria][nombre]}")
        else:
            print("El contacto no existe en esta categoría.")
    else:
        print("Categoría no válida.")

# Permite ver todos los contactos organizados por categoría
def mostrar_contactos():
    print("\nLista de contactos:")
    for categoria, lista in contactos.items():
        print(f"\n{categoria.capitalize()}:")
        for nombre, telefono in lista.items():
            print(f"  {nombre}: {telefono}")


# El usuario podrá elegir qué acción realizar.
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número de la opción deseada: ").strip()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida, intente nuevamente.")




