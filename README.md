# MUBIO07 · Actividad 3 · Inteligencia artificial con Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rubences/IA_Biomedica/blob/main/MUBIO07_Actividad3_IA_Python_Grupo.ipynb)

Resolución grupal reproducible de la actividad de **Programación en Python** dedicada a machine learning y deep learning.

## Equipo

- Meritxell Bastardas Pernil
- Rubén Juárez Cádiz
- Águeda Sobrino Martínez
- Yiling Teng Fang

El fichero principal y único entregable académico es:

```text
MUBIO07_Actividad3_IA_Python_Grupo.ipynb
```

## Cobertura de la actividad

### 1. Google Colab — 2 puntos

El notebook contiene un bloque de texto que documenta:

- creación del cuaderno;
- guardado en Google Drive;
- habilitación de GPU;
- compartición con los cuatro integrantes con rol Editor;
- comprobación de permisos e historial de versiones.

### 2. Machine learning con Iris — 4,5 puntos

Se implementan:

- `sns.load_dataset("iris")`;
- One Hot Encoding de las clases;
- partición estratificada 80/20;
- Support Vector Machine;
- Random Forest;
- Gaussian Naive Bayes;
- accuracy, precision, recall y F1 macro;
- classification reports;
- matrices de confusión;
- validación cruzada estratificada para reforzar la selección del mejor modelo.

La ejecución de referencia del bloque Iris obtuvo en el hold-out 80/20 un F1 macro de **0,967** para SVM y Naive Bayes, y **0,900** para Random Forest. La validación cruzada de 5 folds favorece ligeramente a **SVM** (F1 macro medio ≈ 0,9599), prácticamente empatada con Random Forest (≈ 0,9598). Los detalles y la interpretación se documentan en `docs/VALIDACION_EMPIRICA.md`.

### 3. CNN para malaria — 3,5 puntos

Se implementan:

- lectura de imágenes mediante OpenCV;
- redimensionado a 100×100;
- conversión BGR → RGB;
- normalización a `[0,1]`;
- separación train/validation/test;
- partición **estratificada por clase y agrupada por paciente** para evitar fuga de información;
- CNN TensorFlow/Keras con kernels 3×3 y 5×5;
- pooling, batch normalization, data augmentation y dropout;
- salida sigmoid y binary cross-entropy;
- early stopping, reducción de learning rate y checkpoint;
- curvas de pérdida/accuracy;
- classification report;
- matriz de confusión;
- ejemplos de aciertos y errores.

## Dataset suministrado

La auditoría real del archivo entregado con la actividad muestra:

| Métrica | Resultado |
|---|---:|
| Imágenes PNG totales | 27.558 |
| Parasitized | 13.779 |
| Uninfected | 13.779 |
| Pacientes/grupos identificados | 200 |
| Duplicados exactos por SHA-256 | 0 |
| Train | 19.491 imágenes / 140 pacientes |
| Validation | 4.092 imágenes / 30 pacientes |
| Test | 3.975 imágenes / 30 pacientes |

Los tres subconjuntos son disjuntos por `patient_id`, evitando que células del mismo paciente aparezcan simultáneamente en entrenamiento y evaluación.

El archivo `Malaria Data.zip` ocupa aproximadamente 336 MB y **no se versiona en GitHub**.

Para Colab se recomienda guardarlo en:

```text
MyDrive/MUBIO07/Malaria Data.zip
```

El notebook también busca:

```text
/content/Malaria Data.zip
data/Malaria Data.zip
```

## Ejecución en Google Colab

1. Pulsar el badge **Open in Colab** situado al inicio de este README.
2. Guardar una copia del notebook en Google Drive si se desea conservar la ejecución.
3. Compartir el cuaderno con los cuatro miembros del equipo como **Editor**.
4. Seleccionar una GPU desde `Entorno de ejecución → Cambiar tipo de entorno de ejecución`.
5. Colocar `Malaria Data.zip` en Google Drive o subirlo temporalmente a `/content`.
6. Ejecutar todas las celdas en orden.
7. Conservar las métricas generadas por el propio notebook; no se incluyen resultados CNN inventados o pregrabados.

## Validación empírica

El repositorio diferencia tres niveles de evidencia:

1. **Iris:** ejecución completa de SVM, Random Forest y Naive Bayes con métricas reales y validación cruzada.
2. **Malaria / datos:** auditoría completa de las 27.558 imágenes, comprobación SHA-256 y partición por 200 grupos de paciente sin intersecciones.
3. **CNN:** se realizó una comprobación independiente de viabilidad sobre el dataset real que alcanzó, en validación, aproximadamente **96,5 % de accuracy**, **0,963 de F1** y **0,992 de AUC** en la cuarta época. Esta comprobación no se presenta como la ejecución oficial TensorFlow/Keras de la entrega; las métricas finales oficiales deben ser las generadas al ejecutar el notebook en Colab.

Véase `docs/VALIDACION_EMPIRICA.md` para la trazabilidad completa.

## Entorno local

Google Colab es el entorno recomendado. Para una ejecución local:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

pip install -r requirements.txt
jupyter lab
```

## Estructura

```text
.
├── MUBIO07_Actividad3_IA_Python_Grupo.ipynb
├── README.md
├── CONTRIBUTORS.md
├── requirements.txt
├── .gitignore
├── data/
│   └── README.md
├── docs/
│   ├── DATASET_AUDIT.md
│   ├── MATRIZ_RUBRICA.md
│   └── VALIDACION_EMPIRICA.md
├── scripts/
│   └── validate_notebook.py
├── outputs/
│   └── .gitkeep
└── .github/
    └── workflows/
        └── ci.yml
```

## Decisiones metodológicas

### Por qué 80/20 en Iris

Iris contiene solo 150 muestras. Un split 80/20 conserva 120 observaciones para aprender y 30 para evaluar. La estratificación mantiene diez observaciones de cada especie en test.

### Por qué el split de malaria es por paciente

Los nombres de las imágenes contienen un prefijo de paciente. Si células del mismo paciente apareciesen en entrenamiento y test, el modelo podría explotar patrones específicos de preparación/tinción y producir una estimación demasiado optimista.

Por ello se emplea `StratifiedGroupKFold` y se asignan 14 de 20 folds a entrenamiento, 3 a validación y 3 a test, conservando los grupos de paciente disjuntos.

### Por qué RGB

Las imágenes suministradas son de tres canales. La información cromática de la tinción puede ser discriminativa, por lo que se conservan los tres canales RGB.

### Por qué sigmoid + binary cross-entropy

El problema tiene dos clases y el modelo devuelve una probabilidad `P(Parasitized)`. Una neurona sigmoid junto con `binary_crossentropy` es la formulación natural de este problema binario.

## CI

GitHub Actions valida automáticamente que:

- el notebook es JSON válido;
- todas sus celdas de Python tienen sintaxis correcta;
- contiene los apartados y tecnologías obligatorias;
- el dataset no está versionado;
- la hoja de control grupal no se publica en el árbol actual;
- existe exactamente un notebook de entrega y es el canónico.

El entrenamiento completo de la CNN se reserva para Colab/GPU, evitando convertir la CI en una prueba costosa y dependiente de hardware.

## Repositorio público y protección de datos

El repositorio se mantiene **público** por decisión del equipo. En el árbol actual solo se publican los nombres de los integrantes necesarios para documentar la autoría; no se versionan correos electrónicos, el dataset ni la hoja de control grupal. La hoja de control debe entregarse por el canal académico correspondiente.
