# MUBIO07 · Actividad 3 · Inteligencia artificial con Python

Resolución grupal reproducible de la actividad de **Programación en Python** dedicada a machine learning y deep learning.

## Equipo

- Meritxell Bastardas Pernil
- Rubén Juárez Cádiz
- Águeda Sobrino Martínez
- Yiling Teng Fang

El fichero principal y entregable académico es:

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

La auditoría del archivo entregado con la actividad muestra:

| Clase | Imágenes |
|---|---:|
| Parasitized | 13.779 |
| Uninfected | 13.779 |
| **Total** | **27.558** |

El archivo `Malaria Data.zip` ocupa aproximadamente 336 MB y **no debe versionarse en GitHub**.

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

1. Subir este repositorio a GitHub.
2. Abrir `MUBIO07_Actividad3_IA_Python_Grupo.ipynb` desde Colab.
3. Compartir el cuaderno con los cuatro miembros del equipo como **Editor**.
4. Seleccionar una GPU desde `Entorno de ejecución → Cambiar tipo de entorno de ejecución`.
5. Colocar `Malaria Data.zip` en Google Drive o subirlo temporalmente a `/content`.
6. Ejecutar todas las celdas en orden.

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
│   └── MATRIZ_RUBRICA.md
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

La CI no intenta entrenar la CNN en GitHub Actions. Valida que:

- el notebook es JSON válido;
- todas sus celdas de Python tienen sintaxis correcta;
- contiene los apartados y tecnologías obligatorias;
- no se ha añadido accidentalmente el dataset de 336 MB.

El entrenamiento completo debe ejecutarse en Colab con GPU.

## Privacidad y entrega

El repositorio contiene únicamente los nombres de los integrantes. No se publican correos electrónicos ni la hoja de control original.

Mientras la actividad esté siendo evaluada, se recomienda mantener el repositorio **privado**.
