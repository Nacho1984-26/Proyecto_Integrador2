# ESTRUCTURA DE DATOS: 
# Utilizaremos un diccionario donde los contactos estarán organizados por categorías.

# Se importan funciones
from Funciones import  agregar_contacto, buscar_contacto, mostrar_contactos, mostrar_menu

# Se muestra el menú de opciones y se solicita una selección al usuario.
while True:
    mostrar_menu() # Se llama a la función que nos muestra el menú.

    opcion = input("Ingrese el número de la opción deseada: ") # Se almacena la selección en la variable "opcion"

    # Se evalúa y valida la la selección.
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
