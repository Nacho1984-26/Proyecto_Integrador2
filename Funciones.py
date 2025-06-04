# FUNCIONES DE APLICACIÓN DE CONTACTO

# Diccionario donde los contactos estarán clasificados
# Cada categoría representa una clave con un valor ("contacto") a asignar.
contactos = {
    # El valor de cada categoría es un nuevo diccionario que amacenará los contactos y sus números.
    "familiares": {},
    "amigos": {},
    "compañeros de trabajo": {},
    "otros":{}
}


# Función de "Opción 1" que permite agregar un nuevo contacto a la lista.
def agregar_contacto():
    print("\nCategorías disponibles: Familiares, Amigos, Compañeros de trabajo, Otros")
    categoria = input("Ingrese la categoría donde desea guardar el contacto: ").strip().lower()

    if categoria in contactos: # Si la categoría seleccionada se encuentra dentro de los contactos:
        nombre = input("Ingrese el nombre del contacto: ").strip() # Se lolicita el nombre a agendar
        telefono = input("Ingrese el número de teléfono: ").strip() # Se solicita el número telefónico
        contactos[categoria][nombre] = telefono # Asignamos el número telefónico al nombre del contacto.
        print(f"Contacto '{nombre}' agregado a la categoría '{categoria}'.") # Se imprime confirmación.
    else:
        print("Categoría no válida. Intente nuevamente.")
    

# Función de "Opción 2" que permite buscar un contacto específico.
def buscar_contacto():
    # Se solicita la clave de la categoría requerida.
    categoria = input("Ingrese la categoría donde desea buscar el contacto: ").strip().lower()
    
    # Se evalúa si la categoría ingresada existe dentro de los contactos. De ser así se solicita el nombre.
    if categoria in contactos:
        nombre = input("Ingrese el nombre del contacto a buscar: ").strip()

        # Se evalúa si el nombre ingresado se encuentra dentro de "contactos"
        if nombre in contactos[categoria]: 
            # Si existe imprime su nombre y número de teléfono.
            print(f"Contacto encontrado: {nombre} - {contactos[categoria][nombre]}")
        else:
            print("El contacto no existe en esta categoría.")
    else:
        print("Categoría no válida.")

# Función de "Opción 3" que muestra todos los contactos.
def mostrar_contactos():
    print("\nLista de contactos:")

# Se implementa método de ordenamiento previo a mostrar la lista de contactos 
    contactos_ordenados = {categoria: dict(sorted(lista.items())) for categoria, lista in contactos.items()}
    
    for categoria, lista in contactos_ordenados.items():
        print(f"\n{categoria.capitalize()}:")  # Imprime la categoría.
        for nombre, telefono in lista.items():
            print(f"{nombre}: {telefono}")  # Se imprimen los contactos ordenados.


# Funsión que muestra el menú de opciones que puede elegir el usuario.
def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Salir")
