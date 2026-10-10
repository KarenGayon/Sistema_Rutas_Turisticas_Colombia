
# En este archivo voy a realizar pruebas del modelo
# de aprendizaje automático que entrené.

# Importo pandas para organizar los datos de prueba.
import pandas as pd

# Importo el modelo y las variables que utiliza.
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Leo el dataset con el que voy a trabajar.
datos = pd.read_csv("Actividad_3_supervisado/dataset_rutas.csv")

# Selecciono las características y la clasificación esperada.
caracteristicas = ["costo", "tiempo_minutos", "conexiones"]
X = datos[caracteristicas]
y = datos["recomendable"]

# Separo los datos para entrenar el modelo.
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = (
    train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )
)

# Creo y entreno el árbol de decisión.
modelo = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)
modelo.fit(X_entrenamiento, y_entrenamiento)

# Defino tres escenarios para comprobar las predicciones.
casos_prueba = pd.DataFrame(
    [
        [3, 150, 0],
        [12, 600, 1],
        [2, 60, 0]
    ],
    columns=caracteristicas
)

# Ejecuto las predicciones.
resultados = modelo.predict(casos_prueba)

# Muestro los resultados de cada escenario.
print("======================================")
print(" PRUEBAS DEL MODELO")
print("======================================")

for numero, (datos_caso, resultado) in enumerate(
    zip(casos_prueba.values, resultados), start=1
):
    clasificacion = (
        "Recomendable" if resultado == 1
        else "No recomendable"
    )

    print(f"\nPrueba {numero}")
    print(f"Costo: {datos_caso[0]}")
    print(f"Tiempo en minutos: {datos_caso[1]}")
    print(f"Conexiones: {datos_caso[2]}")
    print(f"Clasificación del modelo: {clasificacion}")

print("\nPruebas finalizadas.")
