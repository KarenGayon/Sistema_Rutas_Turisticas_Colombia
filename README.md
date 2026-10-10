# Sistema Inteligente de Rutas Turísticas en Colombia

## 1. Descripción del proyecto

Este proyecto académico desarrolla un sistema inteligente en Python para explorar conexiones entre destinos turísticos de Colombia e implementar técnicas de inteligencia artificial y aprendizaje automático.

El repositorio integra el algoritmo de búsqueda A*, un modelo de aprendizaje supervisado mediante árboles de decisión y una actividad de aprendizaje no supervisado mediante K-Means.

Los costos, tiempos y demás datos utilizados en los modelos son simulados y tienen fines exclusivamente académicos. No representan tarifas ni tiempos reales de transporte.

## 2. Objetivo general

Implementar técnicas de inteligencia artificial y aprendizaje automático para explorar rutas turísticas, clasificar conexiones e identificar patrones en los datos.

## 3. Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Git y GitHub
- Visual Studio Code

## 4. Estructura del repositorio

```text
Sistema_Rutas_Turisticas_Colombia/
├── Actividad_3_supervisado/
│   ├── dataset_rutas.csv
│   ├── entrenar_modelo.py
│   └── pruebas_modelo.py
├── Actividad_4_no_supervisado/
│   ├── dataset_rutas.csv
│   ├── agrupamiento_rutas.py
│   ├── pruebas_agrupamiento.py
│   ├── visualizar_agrupamiento.py
│   ├── resultados_agrupamiento.csv
│   └── grafica_agrupamiento.png
├── main.py
├── conocimiento.py
├── reglas.py
├── busqueda.py
├── pruebas.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 5. Componentes del sistema original

- `main.py`: permite interactuar con el sistema mediante un menú.
- `conocimiento.py`: contiene los destinos y las conexiones definidos para el proyecto.
- `reglas.py`: incluye las comprobaciones de destinos y conexiones.
- `busqueda.py`: implementa el algoritmo A* para explorar rutas.
- `pruebas.py`: permite verificar el funcionamiento del sistema de búsqueda.

## 6. Actividad 3. Aprendizaje automático supervisado

**Carpeta:** `Actividad_3_supervisado/`

Esta actividad utiliza un árbol de decisión mediante `DecisionTreeClassifier` de Scikit-learn para clasificar conexiones turísticas como recomendables o no recomendables.

Las características utilizadas son:

- `costo`: costo simulado de la conexión.
- `tiempo_minutos`: tiempo estimado simulado.
- `conexiones`: cantidad de conexiones adicionales.

La variable objetivo es `recomendable`, con valores de 1 para recomendable y 0 para no recomendable.

**Archivos principales:**

- `dataset_rutas.csv`: conjunto de datos.
- `entrenar_modelo.py`: entrenamiento y evaluación del modelo.
- `pruebas_modelo.py`: pruebas del clasificador.

**Resultado obtenido:** exactitud del 87,50 % en una ejecución con ocho registros de prueba. Debido al tamaño reducido y al carácter simulado de los datos, este resultado no garantiza el desempeño con información real.

## 7. Actividad 4. Aprendizaje automático no supervisado

**Carpeta:** `Actividad_4_no_supervisado/`

Esta actividad implementa K-Means para agrupar conexiones turísticas según sus características, sin utilizar la variable `recomendable` para formar los grupos.

Se utilizan las variables `costo`, `tiempo_minutos` y `conexiones`. Antes del agrupamiento, estas características se estandarizan mediante `StandardScaler`.

El modelo se configura para identificar tres grupos.

**Archivos principales:**

- `dataset_rutas.csv`: datos utilizados.
- `agrupamiento_rutas.py`: ejecución del agrupamiento.
- `pruebas_agrupamiento.py`: pruebas del modelo.
- `visualizar_agrupamiento.py`: generación de la gráfica.
- `resultados_agrupamiento.csv`: resultados con los grupos asignados.
- `grafica_agrupamiento.png`: representación gráfica de los grupos.

**Resultados obtenidos:**

- Tres grupos identificados.
- Coeficiente Silhouette de 0,520.
- Cuatro verificaciones automatizadas completadas correctamente.

Estos resultados corresponden al conjunto de datos utilizado y no demuestran que los grupos sean categorías óptimas para rutas reales.

## 8. Instalación y ejecución

Se recomienda ejecutar los siguientes comandos desde la raíz del repositorio.

### Preparar el entorno virtual

```bash
python -m venv .venv
```

En Windows PowerShell, activar el entorno:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

### Ejecutar el sistema de búsqueda

```bash
python main.py
```

Ejecutar sus pruebas:

```bash
python pruebas.py
```

### Ejecutar la actividad supervisada

```bash
python Actividad_3_supervisado/entrenar_modelo.py
```

Ejecutar sus pruebas:

```bash
python Actividad_3_supervisado/pruebas_modelo.py
```

### Ejecutar la actividad no supervisada

Entrenar el modelo y generar los resultados:

```bash
python Actividad_4_no_supervisado/agrupamiento_rutas.py
```

Ejecutar las pruebas:

```bash
python Actividad_4_no_supervisado/pruebas_agrupamiento.py
```

Generar la gráfica:

```bash
python Actividad_4_no_supervisado/visualizar_agrupamiento.py
```

## 9. Diferencias entre las actividades

| Característica | Supervisado | No supervisado |
|---|---|---|
| Algoritmo | Árbol de decisión | K-Means |
| Objetivo | Clasificar conexiones | Identificar grupos |
| Utiliza la etiqueta `recomendable` | Sí | No |
| Resultado | Predicción de categoría | Grupo asignado |
| Evaluación reportada | Exactitud del 87,50 % | Silhouette de 0,520 |

## 10. Limitaciones y mejoras futuras

El proyecto utiliza datos simulados y conjuntos de tamaño reducido. Por tanto, sus resultados tienen un alcance educativo y no deben interpretarse como recomendaciones validadas para viajes reales.

Como mejoras futuras se propone incorporar datos verificables de transporte, ampliar los conjuntos de datos y evaluar los modelos con información real.

## 11. Alcance académico

El proyecto permite explorar técnicas de búsqueda, clasificación supervisada y agrupamiento no supervisado, además de practicar la preparación de datos, el entrenamiento de modelos, las pruebas y la visualización de resultados.
