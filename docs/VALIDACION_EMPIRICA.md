# Validación empírica

Este documento separa de forma explícita los resultados realmente ejecutados de las comprobaciones metodológicas y de las métricas que deben producirse al ejecutar el notebook final en Google Colab.

## 1. Iris — ejecución completa

El bloque de machine learning se ejecutó con el split estratificado 80/20 definido en el notebook y con semilla `SEED = 42`.

### Hold-out 80/20

| Modelo | Accuracy | Precision macro | Recall macro | F1 macro |
|---|---:|---:|---:|---:|
| SVM | 0,967 | 0,970 | 0,967 | 0,967 |
| Random Forest | 0,900 | 0,902 | 0,900 | 0,900 |
| Naive Bayes | 0,967 | 0,970 | 0,967 | 0,967 |

SVM y Naive Bayes empatan en F1 macro en esta partición concreta.

### Validación cruzada estratificada, 5 folds

| Modelo | F1 macro medio aproximado |
|---|---:|
| SVM | 0,9599 |
| Random Forest | 0,9598 |
| Naive Bayes | 0,9465 |

La diferencia entre SVM y Random Forest es mínima, pero SVM queda ligeramente por encima y constituye la elección más defendible cuando se combinan hold-out y validación cruzada.

## 2. Dataset de malaria — auditoría completa

La auditoría se realizó sobre el archivo proporcionado con la actividad.

| Métrica | Resultado |
|---|---:|
| Imágenes PNG | 27.558 |
| Parasitized | 13.779 |
| Uninfected | 13.779 |
| Grupos/pacientes identificados | 200 |
| Duplicados exactos por SHA-256 | 0 |

### Split por paciente

| Split | Imágenes | Pacientes |
|---|---:|---:|
| Train | 19.491 | 140 |
| Validation | 4.092 | 30 |
| Test | 3.975 | 30 |

Se comprobó que:

```text
train ∩ validation = ∅
train ∩ test       = ∅
validation ∩ test  = ∅
```

Por tanto, ninguna célula de un mismo `patient_id` se utiliza simultáneamente para entrenar y evaluar el modelo.

## 3. CNN — comprobación independiente de viabilidad

Antes de la ejecución final en Google Colab se realizó una comprobación independiente sobre el dataset real para verificar que la arquitectura y el pipeline de datos son capaces de aprender una señal útil.

Resultados de validación observados:

| Época | Accuracy | F1 | AUC |
|---:|---:|---:|---:|
| 1 | 0,9357 | 0,9291 | 0,9911 |
| 2 | 0,9567 | 0,9540 | 0,9910 |
| 3 | 0,9611 | 0,9588 | 0,9922 |
| 4 | 0,9651 | 0,9634 | 0,99225 |

En la época 4 se observaron además aproximadamente:

- Precision: **0,9691**
- Recall: **0,9578**

### Alcance de esta comprobación

Estos valores sirven como **sanity check empírico** del pipeline, pero no se presentan como resultados oficiales de la CNN TensorFlow/Keras del cuaderno de entrega.

La actividad final utiliza TensorFlow/Keras en Google Colab y debe generar sus propias métricas a partir del conjunto de test reservado. El notebook incluye todas las celdas necesarias para producir:

- curvas de pérdida y accuracy;
- métricas finales sobre test;
- classification report;
- matriz de confusión;
- ejemplos de predicciones correctas e incorrectas.

No se han insertado valores CNN simulados ni pregrabados en el notebook.

## 4. Criterio de cierre

La solución se considera técnicamente cerrada cuando se cumplen simultáneamente estos puntos:

- un único notebook canónico;
- cobertura completa de la rúbrica;
- CI estática en verde;
- dataset excluido de GitHub;
- split por paciente sin leakage;
- resultados de Iris reproducibles;
- notebook preparado para ejecución final en Colab/GPU;
- separación explícita entre resultados ejecutados y resultados que dependen de la ejecución TensorFlow/Keras final.
