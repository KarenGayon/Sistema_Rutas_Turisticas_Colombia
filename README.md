# Sistema Inteligente de Rutas Turísticas en Colombia

## 1. Descripción del proyecto

El **Sistema Inteligente de Rutas Turísticas en Colombia** es un proyecto académico desarrollado en Python que integra técnicas de inteligencia artificial para explorar rutas entre destinos turísticos y clasificar conexiones según su conveniencia.

El proyecto combina un algoritmo de búsqueda informada **A\*** con un modelo de **aprendizaje automático supervisado basado en árboles de decisión**.

Su propósito es demostrar cómo diferentes técnicas de inteligencia artificial pueden aplicarse a un sistema de exploración y análisis de rutas turísticas.

> **Nota:** Los costos, tiempos y datos utilizados en el modelo de aprendizaje automático son simulados y tienen fines exclusivamente académicos. No representan tarifas ni tiempos reales de transporte.

## 2. Objetivos

### Objetivo general

Desarrollar un prototipo en Python que integre algoritmos de búsqueda y aprendizaje automático supervisado para explorar rutas turísticas y clasificar conexiones entre destinos de Colombia.

### Objetivos específicos

- Representar destinos turísticos y sus conexiones mediante una base de conocimiento.
- Implementar el algoritmo A* para encontrar rutas dentro del grafo definido.
- Construir un conjunto de datos para entrenar un modelo supervisado.
- Entrenar un árbol de decisión para clasificar conexiones como recomendables o no recomendables.
- Evaluar el comportamiento del modelo mediante métricas y escenarios de prueba.
- Documentar el funcionamiento, los datos y las limitaciones del sistema.

## 3. Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Pandas:** lectura y organización del conjunto de datos.
- **Scikit-learn:** entrenamiento y evaluación del modelo de aprendizaje automático.
- **Algoritmo A\*:** búsqueda informada de rutas.
- **Git y GitHub:** control de versiones y alojamiento del código fuente.
- **Visual Studio Code:** entorno de desarrollo.

## 4. Estructura del proyecto

```text
Sistema_Rutas_Turisticas_Colombia/
│
├── main.py
├── conocimiento.py
├── reglas.py
├── busqueda.py
├── pruebas.py
│
├── dataset_rutas.csv
├── entrenar_modelo.py
├── pruebas_modelo.py
│
├── descripcion_datos.md
├── pruebas.md
├── README.md
├── requirements.txt
├── .gitignore
│
└── documentos/
    └── (documentos académicos y entregables)
```

La carpeta `documentos/` se utilizará para organizar los documentos finales del proyecto, como el mapa conceptual y el PDF de entrega.

## 5. Componentes del sistema

### 5.1. Base de conocimiento

El archivo `conocimiento.py` contiene los destinos turísticos y las conexiones definidas para el prototipo.

Entre los lugares representados se encuentran Bogotá, Villa de Leyva, Medellín, el Eje Cafetero, Cartagena, Santa Marta y el Parque Tayrona.

Las conexiones y sus costos son valores definidos para el ejercicio académico.

### 5.2. Reglas del sistema

El archivo `reglas.py` contiene las comprobaciones utilizadas para validar destinos y conexiones disponibles en la base de conocimiento.

### 5.3. Búsqueda de rutas con A*

El archivo `busqueda.py` implementa el algoritmo A*, que utiliza los costos de las conexiones y una función heurística para explorar posibles recorridos.

El archivo `main.py` permite interactuar con el sistema mediante un menú de opciones.

### 5.4. Aprendizaje automático supervisado

El archivo `entrenar_modelo.py` desarrolla el componente de aprendizaje automático mediante un árbol de decisión de Scikit-learn.

El modelo utiliza las siguientes características:

- `costo`: costo simulado de la conexión.
- `tiempo_minutos`: tiempo estimado simulado.
- `conexiones`: cantidad de conexiones adicionales.

La variable objetivo es `recomendable`, codificada de la siguiente manera:

- `1`: recomendable.
- `0`: no recomendable.

El archivo `pruebas_modelo.py` permite probar el modelo con distintos escenarios de entrada.

## 6. Conjunto de datos

El archivo `dataset_rutas.csv` contiene **30 registros simulados** de conexiones entre destinos turísticos.

El conjunto de datos incluye seis variables:

| Variable | Descripción |
|---|---|
| `origen` | Destino de partida. |
| `destino` | Destino de llegada. |
| `costo` | Costo simulado de la conexión. |
| `tiempo_minutos` | Tiempo simulado en minutos. |
| `conexiones` | Número de conexiones adicionales. |
| `recomendable` | Clasificación objetivo del modelo. |

Los datos se dividieron en un conjunto de entrenamiento del 75 % y uno de prueba del 25 %, utilizando una semilla fija para facilitar la reproducibilidad.

Para conocer más detalles, consulta `descripcion_datos.md`.

## 7. Instalación y ejecución

### Requisitos previos

Tener instalado Python y Git. Se recomienda utilizar una versión de Python compatible con las dependencias del proyecto.

### Instalar las dependencias

Desde la terminal, ubicada en la carpeta del proyecto, ejecuta:

```bash
python -m pip install -r requirements.txt
```

### Ejecutar el sistema de rutas

```bash
python main.py
```

Utiliza el menú para explorar las opciones disponibles.

### Entrenar y evaluar el modelo

```bash
python entrenar_modelo.py
```

Este comando carga el conjunto de datos, divide los registros, entrena el árbol de decisión y muestra las métricas de evaluación y una predicción de ejemplo.

### Ejecutar las pruebas del modelo

```bash
python pruebas_modelo.py
```

### Ejecutar las pruebas del algoritmo de búsqueda

```bash
python pruebas.py
```

## 8. Resultados obtenidos

En la ejecución documentada del modelo supervisado se obtuvieron los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Registros totales | 30 |
| Registros de entrenamiento | 22 |
| Registros de prueba | 8 |
| Exactitud observada | 87,50 % |

La exactitud corresponde a siete predicciones correctas de ocho registros de prueba en esa ejecución.

El modelo también produjo predicciones para tres escenarios adicionales de prueba.

**Interpretación:** estos resultados muestran el funcionamiento del prototipo, pero no demuestran que el sistema pueda recomendar rutas reales con precisión. El conjunto de datos es pequeño, simulado y sus etiquetas fueron definidas manualmente.

## 9. Pruebas y documentación

- `pruebas.py`: pruebas del sistema de búsqueda de rutas.
- `pruebas_modelo.py`: escenarios de prueba del clasificador.
- `pruebas.md`: documentación de las pruebas realizadas.
- `descripcion_datos.md`: descripción, preparación y limitaciones del dataset.

## 10. Limitaciones y mejoras futuras

El proyecto es un prototipo académico y presenta las siguientes limitaciones:

- No utiliza datos reales de tarifas o tiempos de transporte.
- El conjunto de datos es reducido y fue construido con fines educativos.
- Las clasificaciones fueron definidas manualmente.
- La heurística de búsqueda utiliza una representación simplificada y no debe interpretarse como una distancia geográfica real.
- La evaluación del modelo se realiza sobre una muestra pequeña.

Como mejoras futuras se propone incorporar fuentes verificables de información, ampliar el dataset, definir criterios de recomendación sustentados y desarrollar una interfaz que facilite la consulta de rutas.

## 11. Integrantes

Proyecto desarrollado de manera colaborativa en el marco de la asignatura **Inteligencia Artificial**.

- Integrante 1: [Nombre completo]
- Integrante 2: [Nombre completo]
- Integrante 3: [Nombre completo]
- Integrante 4: [Nombre completo, si aplica]

## 12. Entregables académicos

- Repositorio GitHub: [Agregar enlace del repositorio]
- Video de sustentación: [Agregar enlace del video]
- Mapa conceptual: [Agregar enlace o ubicación del archivo PDF]
- Documento de pruebas: `pruebas.md` y su versión PDF, cuando esté generada.

## 13. Licencia y uso

Este proyecto se desarrolló con fines académicos. Los datos simulados y los resultados deben interpretarse dentro del alcance educativo del prototipo.
