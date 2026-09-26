# Traemos la información de las rutas que se guardo en el archivo conocimiento.py.

from conocimiento import rutas
def destino_existe(destino):
    # Se revisa si el destino aparece dentro de la información que tenemos guardada en nuestra base de conocimiento.
    
    if destino in rutas:
        return True

    # Si no aparece, significa que el sistema no lo conoce.
    return False

def existe_conexion(origen, destino):
    # Primero se revisa las conexiones que tenemos registradas desde el lugar de origen.
    
    conexiones = rutas.get(origen, {})

    # Si el destino aparece entre esas conexiones,
    # significa que existe una ruta directa.
    if destino in conexiones:
        return True

    # Si no aparece, no existe una conexión directa.
    return False