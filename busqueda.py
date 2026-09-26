# Importamos la información de las rutas para que el algoritmo pueda saber que destinos están conectados.
from conocimiento import rutas

# Se importa heapq porque me permite organizar las opciones de búsqueda según su prioridad.
import heapq
# Para este proyecto vamos a darle una posición aproximada a cada destino dentro de nuestra red.
# Estos valores no representan kilómetros reales.
# Los usamos solamente para calcular una estimación.
posiciones = {
    "Bogotá": 0,
    "Villa de Leyva": 1,
    "Medellín": 2,
    "Eje Cafetero": 3,
    "Cartagena": 4,
    "Santa Marta": 5,
    "Parque Tayrona": 6
}

def heuristica(actual, destino):
    # Calculo una distancia estimada entre el destino en el que estoy y el destino al que quiero llegar.
    # Mientras menor sea el resultado, más cerca considero que estoy del destino.
    return abs(posiciones[actual] - posiciones[destino])



def buscar_ruta(origen, destino):
    # Esta función busca una ruta desde el origen hasta el destino utilizando el algoritmo A*.

    # Primero verificamos que los dos destinos estén registrados en nuestra base de conocimiento.
    if origen not in rutas or destino not in rutas:
        return None, None

    # Esta lista será utilizada por A* para guardar las opciones que todavía debe revisar.
    cola = []

    # Al comenzar todavía no hemos recorrido ningún tramo.
    costo_inicial = 0

    # Calculo la estimación inicial desde el origen hasta el destino que escogió el usuario.
    estimacion_inicial = heuristica(origen, destino)

    # La prioridad inicial es el costo recorrido más la estimación de lo que falta.
    prioridad_inicial = costo_inicial + estimacion_inicial

    # Guardamos en la cola la primera opción que vamos a revisar.
    heapq.heappush(
        cola,
        (
            prioridad_inicial,
            costo_inicial,
            origen,
            [origen]
        )
    )

    # Aquí voy guardando el menor costo conocido para llegar a cada destino.
    costos = {
        origen: 0
    }

    # Mientras todavía existan destinos por revisar, el algoritmo continúa buscando.
    while cola:

        # Saco de la cola la opción que tiene la prioridad más baja.
        prioridad, costo_actual, actual, ruta_actual = heapq.heappop(cola)

        # Si llego al destino solicitado, devuelvo la ruta encontrada y su costo.
        if actual == destino:
            return ruta_actual, costo_actual

        # Reviso todos los destinos conectados con el destino en el que me encuentro.
        for vecino, costo in rutas.get(actual, {}).items():

            # Sumo el costo de la nueva conexión al costo que ya llevaba acumulado.
            nuevo_costo = costo_actual + costo

            # Si es la primera vez que llegamos a ese destino o se encontro una opción más económica,
            # actualizo la información.
            if vecino not in costos or nuevo_costo < costos[vecino]:

                costos[vecino] = nuevo_costo

                # Calcula cuánto falta aproximadamente para llegar al destino final.
                h = heuristica(vecino, destino)

                # Calculo la prioridad que tendrá esta opción.
                f = nuevo_costo + h

                # Agregamos el nuevo destino a la ruta.
                nueva_ruta = ruta_actual + [vecino]

                # Guardo esta nueva opción para que A* pueda revisarla posteriormente.
                heapq.heappush(
                    cola,
                    (
                        f,
                        nuevo_costo,
                        vecino,
                        nueva_ruta
                    )
                )

    # Si se revisaron todas las posibilidades y no se llegó al destino, informo que no existe una ruta.
    return None, None