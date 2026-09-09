# Auditoría del dataset suministrado

La siguiente información se obtuvo directamente del archivo `Malaria Data.zip` suministrado con la actividad, antes de diseñar el pipeline.

| Métrica | Resultado |
|---|---:|
| Imágenes PNG totales | 27.558 |
| Parasitized | 13.779 |
| Uninfected | 13.779 |
| Balance global | 50 % / 50 % |
| Tamaño del ZIP | ~336 MB |
| Canales observados | 3 |

Una muestra aleatoria de 200 imágenes confirmó que los tamaños originales son variables, por lo que el redimensionado solicitado por el enunciado es necesario.

## Prevención de leakage

Los nombres de fichero codifican un prefijo asociado al paciente antes de la palabra `thin`, por ejemplo:

```text
C100P61ThinF_...
C37BP2_thinF_...
```

El notebook utiliza ese prefijo como `patient_id` y aplica `StratifiedGroupKFold`, evitando que el mismo paciente aparezca simultáneamente en train, validation y test.

La auditoría no sustituye a las comprobaciones del notebook: durante la ejecución se recalculan conteos, balance y disjunción de grupos.
