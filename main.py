# Importo la información de las rutas para poder
# mostrar los destinos que tiene nuestro sistema.
from conocimiento import rutas

# Importo la función que busca la ruta utilizando A*.
from busqueda import buscar_ruta


def mostrar_destinos():
    # Esta función muestra los destinos que tenemos
    # registrados en nuestra base de conocimiento.
    print("\nDESTINOS TURÍSTICOS DISPONIBLES")
    print("--------------------------------")

    for destino in rutas:
        print("-", destino)


def buscar():
    # Esta función permite que el usuario seleccione
    # un origen y un destino final.

    print("\nBUSCAR RUTA TURÍSTICA")
    print("---------------------")

    mostrar_destinos()

    origen = input("\nIngrese el destino de origen: ")
    destino = input("Ingrese el destino final: ")

    # Verifico que el origen esté registrado.
    if origen not in rutas:
        print("\nEl destino de origen no está registrado.")
        return

    # Verifico que el destino esté registrado.
    if destino not in rutas:
        print("\nEl destino final no está registrado.")
        return

    # Envío el origen y el destino al algoritmo A*
    # para que encuentre una ruta.
    ruta, costo = buscar_ruta(origen, destino)

    # Si se encontró una ruta, la muestro.
    if ruta:
        print("\nRuta encontrada:")
        print(" → ".join(ruta))

        print(f"\nCosto de la ruta: {costo}")

    else:
        print("\nNo se encontró una ruta entre los destinos.")


def menu():
    # Esta función muestra el menú principal
    # del sistema y permite seleccionar una opción.

    while True:

        print("\n======================================")
        print(" SISTEMA INTELIGENTE DE RUTAS TURÍSTICAS")
        print("======================================")
        print("1. Buscar una ruta")
        print("2. Ver destinos disponibles")
        print("3. Salir")
        print("======================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            buscar()

        elif opcion == "2":
            mostrar_destinos()

        elif opcion == "3":
            print("\nMuchas gracias por su visita. Chat finalizado.")
            break

        else:
            print("\nLa opción seleccionada no es válida.")


# Esta condición hace que el menú se ejecute
# cuando abrimos directamente este archivo.
if __name__ == "__main__":
    menu()