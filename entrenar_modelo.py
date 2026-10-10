
# En este archivo voy a entrenar un modelo de
# aprendizaje automático para clasificar conexiones turísticas.

# Importo pandas para leer y organizar los datos.
import pandas as pd

# Importo las herramientas necesarias para crear
# y evaluar el árbol de decisión.
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# Leo los datos que guardé en el archivo CSV.
datos = pd.read_csv("dataset_rutas.csv")


# Muestro una parte de los datos para verificar
# que el archivo se haya leído correctamente.
print("======================================")
print(" DATASET DE RUTAS TURÍSTICAS")
print("======================================")
print(datos.head())


# Selecciono las variables que utilizará el modelo
# para aprender a clasificar las conexiones.
caracteristicas = [
    "costo",
    "tiempo_minutos",
    "conexiones"
]

X = datos[caracteristicas]

# Esta es la respuesta que quiero que aprenda
# a predecir el modelo.
y = datos["recomendable"]


# Divido los datos en dos grupos:
# uno para entrenar y otro para evaluar el modelo.
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
    train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )
)


# Creo el árbol de decisión.
# Limito su profundidad para evitar que memorice
# demasiados detalles de los ejemplos.
modelo = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)


# Entreno el modelo utilizando los datos de entrenamiento.
modelo.fit(X_entrenamiento, y_entrenamiento)


# Utilizo el modelo para predecir las clasificaciones
# de los datos que reservé para las pruebas.
predicciones = modelo.predict(X_prueba)


# Calculo la exactitud de las predicciones.
exactitud = accuracy_score(y_prueba, predicciones)


# Muestro los resultados de la evaluación.
print("\n======================================")
print(" RESULTADOS DEL MODELO")
print("======================================")

print(f"Cantidad de registros: {len(datos)}")
print(f"Registros para entrenamiento: {len(X_entrenamiento)}")
print(f"Registros para prueba: {len(X_prueba)}")
print(f"Exactitud del modelo: {exactitud:.2%}")

print("\nReporte de clasificación:")
print(
    classification_report(
        y_prueba,
        predicciones,
        labels=[0, 1],
        target_names=["No recomendable", "Recomendable"],
        zero_division=0
    )
)


# Pruebo el modelo con una conexión nueva.
# Este ejemplo utiliza valores simulados.
nueva_conexion = pd.DataFrame(
    [[3, 150, 0]],
    columns=caracteristicas
)

prediccion = modelo.predict(nueva_conexion)[0]

print("\n======================================")
print(" PREDICCIÓN DE UNA NUEVA CONEXIÓN")
print("======================================")

if prediccion == 1:
    print("El modelo clasifica la conexión como recomendable.")
else:
    print("El modelo clasifica la conexión como no recomendable.")

print("\nEvaluación finalizada.")
