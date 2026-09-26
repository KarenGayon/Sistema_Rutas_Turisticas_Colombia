# En este archivo vamos a guardar la información que el sistema
# se necesita conocer sobre los destinos turísticos y sus conexiones.

rutas = {

    # Desde Bogotá podemos viajar hacia estos destinos.
    "Bogotá": {
        "Villa de Leyva": 3,
        "Medellín": 8,
        "Eje Cafetero": 7
    },

    # Villa de Leyva tiene una conexión con Bogotá.
    "Villa de Leyva": {
        "Bogotá": 3
    },

    # Medellín tiene conexiones con Bogotá, Eje Cafetero y Cartagena.
    "Medellín": {
        "Bogotá": 8,
        "Eje Cafetero": 5,
        "Cartagena": 10
    },

    # El Eje Cafetero tiene conexiones con Bogotá y Medellín.
    "Eje Cafetero": {
        "Bogotá": 7,
        "Medellín": 5
    },

    # Cartagena está conectada con Medellín y Santa Marta.
    "Cartagena": {
        "Medellín": 10,
        "Santa Marta": 3
    },

    # Desde Santa Marta se puede continuar hacia el Parque Tayrona.
    "Santa Marta": {
        "Cartagena": 3,
        "Parque Tayrona": 2
    },

    # El Parque Tayrona tiene conexión de regreso con Santa Marta.
    "Parque Tayrona": {
        "Santa Marta": 2
    }
}