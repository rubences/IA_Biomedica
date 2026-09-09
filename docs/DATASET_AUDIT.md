# Auditoría del dataset suministrado

La información de este documento se ha recalculado directamente sobre el archivo `Malaria Data.zip` suministrado con la actividad. No procede de métricas copiadas de artículos ni de un dataset alternativo.

## Integridad y composición

| Métrica | Resultado |
|---|---:|
| SHA-256 de `Malaria Data.zip` | `6ec660693778afcbbb9294e3e2a6d6322fe5a6f20da586be79f19b8a3c443311` |
| Imágenes PNG totales | 27.558 |
| Parasitized | 13.779 |
| Uninfected | 13.779 |
| Balance global | 50 % / 50 % |
| Tamaño del ZIP | ~336 MB |
| Canales observados | 3 |
| Hashes SHA-256 de imagen únicos | 27.558 |
| Duplicados exactos | 0 |
| Duplicados exactos entre clases | 0 |

La comprobación de hashes se realizó sobre las **27.558 imágenes**, no sobre una muestra. Por tanto, no existen duplicados binarios exactos que puedan atravesar accidentalmente los subconjuntos de entrenamiento y evaluación.

Los tamaños originales de las imágenes son variables, por lo que el redimensionado a `100×100` solicitado por el enunciado es necesario. El pipeline conserva tres canales y transforma BGR → RGB antes de normalizar a `[0, 1]`.

## Agrupación por paciente

Los nombres de fichero codifican un prefijo asociado al paciente antes de la palabra `thin`, por ejemplo:

```text
C100P61ThinF_...
C37BP2_thinF_...
```

La extracción aplicada por el notebook identifica **200 grupos/pacientes**. De ellos, 150 contienen imágenes de ambas clases y 50 contienen una sola clase. El número de imágenes por grupo es heterogéneo (mínimo 65, mediana 85,5 y máximo 702), lo que refuerza la necesidad de realizar la partición a nivel de grupo y no a nivel de imagen.

## Split reproducible sin fuga por paciente

Con `StratifiedGroupKFold(n_splits=20, shuffle=True, random_state=42)` se obtiene el siguiente reparto real:

| Split | Imágenes | % total | Pacientes | Parasitized | % Parasitized |
|---|---:|---:|---:|---:|---:|
| Train | 19.491 | 70,73 % | 140 | 9.879 | 50,68 % |
| Validation | 4.092 | 14,85 % | 30 | 1.967 | 48,07 % |
| Test | 3.975 | 14,42 % | 30 | 1.933 | 48,63 % |
| **Total** | **27.558** | **100 %** | **200** | **13.779** | **50,00 %** |

Las intersecciones de `patient_id` son exactamente cero:

```text
train ∩ validation = 0
train ∩ test       = 0
validation ∩ test  = 0
```

Esto reduce el riesgo de que el modelo aprenda características específicas de preparación, tinción o adquisición de un mismo paciente y las encuentre después en el conjunto de prueba.

## Alcance

Esta auditoría valida integridad, balance, unicidad y diseño de la partición. Las métricas finales de la CNN deben proceder de la ejecución del notebook TensorFlow/Keras sobre estos mismos subconjuntos; no se sustituyen por resultados externos ni simulados.
