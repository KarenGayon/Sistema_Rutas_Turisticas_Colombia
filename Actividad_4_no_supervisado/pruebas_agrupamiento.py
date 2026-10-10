
# Pruebas del modelo de aprendizaje no supervisado.
# Proyecto: Sistema Inteligente de Rutas Turísticas en Colombia.

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# 1. Cargar el dataset.
datos = pd.read_csv(
    "Actividad_4_no_supervisado/dataset_rutas.csv"
)

print("========================================")
print(" PRUEBAS DEL MODELO K-MEANS")
print("========================================")


# 2. Seleccionar las características.
caracteristicas = [
    "costo",
    "tiempo_minutos",
    "conexiones"
]

X = datos[caracteristicas]


# 3. Verificar que el dataset tenga datos suficientes.
assert len(datos) >= 3, "Se necesitan al menos 3 registros."
assert not X.isnull().any().any(), "Hay valores vacíos."
assert (X >= 0).all().all(), "Hay valores negativos inesperados."

print("Prueba 1: dataset válido. Correcta.")


# 4. Estandarizar las características.
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)


# 5. Entrenar K-Means.
modelo = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

grupos = modelo.fit_predict(X_escalado)


# 6. Verificar que se hayan creado tres grupos.
cantidad_grupos = len(set(grupos))

assert cantidad_grupos == 3, (
    "El modelo no generó los tres grupos esperados."
)

print("Prueba 2: generación de tres grupos. Correcta.")


# 7. Verificar que todos los registros tengan grupo.
assert len(grupos) == len(datos), (
    "No todos los registros fueron agrupados."
)

print("Prueba 3: asignación de grupos a todos los registros. Correcta.")


# 8. Evaluar la separación de los grupos.
puntuacion = silhouette_score(X_escalado, grupos)

assert -1 <= puntuacion <= 1, (
    "El coeficiente Silhouette está fuera del rango esperado."
)

print("Prueba 4: cálculo del coeficiente Silhouette. Correcta.")
print(f"Coeficiente Silhouette: {puntuacion:.3f}")


# 9. Mostrar el resultado de las pruebas.
print("\n========================================")
print(" RESUMEN DE LAS PRUEBAS")
print("========================================")
print("Pruebas completadas: 4")
print("Estado: todas las verificaciones finalizaron correctamente.")
