
# Actividad 2: Aprendizaje automatico no supervisado
# Proyecto: Sistema Inteligente de Rutas Turisticas en Colombia

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# 1. Cargar los datos de la actividad.
datos = pd.read_csv("Actividad_4_no_supervisado/dataset_rutas.csv")

print("========================================")
print(" AGRUPAMIENTO DE RUTAS TURISTICAS")
print("========================================")
print(f"Cantidad de registros: {len(datos)}")


# 2. Seleccionar las variables para el agrupamiento.
# No usamos la columna 'recomendable' porque
# el aprendizaje no supervisado no necesita etiquetas.
caracteristicas = [
    "costo",
    "tiempo_minutos",
    "conexiones"
]

X = datos[caracteristicas]


# 3. Estandarizar las variables para ponerlas
# en escalas comparables.
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)


# 4. Crear y entrenar el modelo K-Means.
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

grupos = modelo.fit_predict(X_escalado)


# 5. Crear una tabla con los grupos asignados.
resultados = datos[
    ["origen", "destino", "costo",
     "tiempo_minutos", "conexiones"]
].copy()

resultados["cluster"] = grupos


# 6. Guardar los resultados en un archivo CSV.
resultados.to_csv(
    "Actividad_4_no_supervisado/resultados_agrupamiento.csv",
    index=False
)


# 7. Mostrar algunos registros agrupados.
print("\nPrimeros registros agrupados:")
print(resultados.head(10).to_string(index=False))


# 8. Mostrar la cantidad de registros de cada grupo.
print("\nCantidad de conexiones por grupo:")
print(resultados["cluster"].value_counts().sort_index())


# 9. Calcular los promedios de cada grupo.
print("\nPromedios de las caracteristicas por grupo:")

resumen = resultados.groupby("cluster")[
    caracteristicas
].mean().round(2)

print(resumen)


# 10. Evaluar la separación entre los grupos.
puntuacion = silhouette_score(X_escalado, grupos)

print("\n========================================")
print(" EVALUACION DEL AGRUPAMIENTO")
print("========================================")
print(f"Coeficiente Silhouette: {puntuacion:.3f}")

print("\nArchivo generado:")
print("resultados_agrupamiento.csv")
print("Proceso finalizado.")
