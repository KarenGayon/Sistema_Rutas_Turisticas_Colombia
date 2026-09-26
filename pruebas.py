# Importo las funciones que quiero probar
# desde el archivo reglas.py.
from reglas import destino_existe, existe_conexion


print("======================================")
print(" PRUEBAS DEL SISTEMA")
print("======================================")


# Prueba 1: comprobar que Bogotá existe.
print("\nPrueba 1 - ¿Existe Bogotá?")

if destino_existe("Bogotá"):
    print("Resultado: Bogotá sí está registrada.")
else:
    print("Resultado: Bogotá no está registrada.")


# Prueba 2: comprobar que Cali no existe.
print("\nPrueba 2 - ¿Existe Cali?")

if destino_existe("Cali"):
    print("Resultado: Cali sí está registrada.")
else:
    print("Resultado: Cali no está registrada.")


# Prueba 3: comprobar una conexión directa.
print("\nPrueba 3 - ¿Existe conexión entre Bogotá y Medellín?")

if existe_conexion("Bogotá", "Medellín"):
    print("Resultado: sí existe una conexión directa.")
else:
    print("Resultado: no existe una conexión directa.")


# Prueba 4: comprobar una conexión que no es directa.
print("\nPrueba 4 - ¿Existe conexión directa entre Bogotá y Cartagena?")

if existe_conexion("Bogotá", "Cartagena"):
    print("Resultado: sí existe una conexión directa.")
else:
    print("Resultado: no existe una conexión directa.")


print("\n======================================")
print(" PRUEBAS FINALIZADAS")
print("======================================")

# Importo la función que realiza la búsqueda
# de rutas utilizando el algoritmo A*.
from busqueda import buscar_ruta


# Prueba 5: buscar una ruta entre Bogotá y Villa de Leyva.
print("\nPrueba 5 - Buscar ruta Bogotá → Villa de Leyva")

ruta, costo = buscar_ruta("Bogotá", "Villa de Leyva")

if ruta:
    print("Ruta encontrada:", " → ".join(ruta))
    print("Costo:", costo)
else:
    print("No se encontró una ruta.")


# Prueba 6: buscar una ruta entre Medellín y Santa Marta.
print("\nPrueba 6 - Buscar ruta Medellín → Santa Marta")

ruta, costo = buscar_ruta("Medellín", "Santa Marta")

if ruta:
    print("Ruta encontrada:", " → ".join(ruta))
    print("Costo:", costo)
else:
    print("No se encontró una ruta.")