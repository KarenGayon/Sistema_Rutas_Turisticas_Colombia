
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Cargar el conjunto de datos
ruta = "Actividad_4_no_supervisado/dataset_rutas.csv"
datos = pd.read_csv(ruta)

# Seleccionar las variables
caracteristicas = ["costo", "tiempo_minutos", "conexiones"]
X = datos[caracteristicas]

# Estandarizar las variables
escalador = StandardScaler()
X_escalado = escalador.fit_transform(X)

# Entrenar el modelo K-Means
modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
datos["cluster"] = modelo.fit_predict(X_escalado)

# Crear una gráfica de costo frente a tiempo
for grupo in sorted(datos["cluster"].unique()):
    subconjunto = datos[datos["cluster"] == grupo]
    plt.scatter(
        subconjunto["costo"],
        subconjunto["tiempo_minutos"],
        label=f"Grupo {grupo}"
    )

plt.title("Agrupamiento de rutas turísticas con K-Means")
plt.xlabel("Costo")
plt.ylabel("Tiempo (minutos)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar la gráfica en la carpeta de la actividad
plt.savefig(
    "Actividad_4_no_supervisado/grafica_agrupamiento.png",
    dpi=300
)
plt.show()

print("Gráfica guardada en grafica_agrupamiento.png")
