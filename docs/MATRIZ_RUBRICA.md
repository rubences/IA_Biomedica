# Matriz de trazabilidad de la rúbrica

| Apartado | Puntos | Evidencia en el notebook |
|---|---:|---|
| 1A. Crear Google Colab | 0,5 | Sección 1: procedimiento de creación, guardado y GPU |
| 1B. Acceso de integrantes | 1,5 | Sección 1: compartir con los cuatro integrantes como Editor y verificar permisos |
| 2A. One Hot Encoding | 1,0 | `OneHotEncoder` y tabla de clases codificadas |
| 2B. Train/test | 0,5 | Split 80/20 estratificado y justificado |
| 2C. SVM, Random Forest, Naive Bayes + métricas | 1,5 | Tres modelos, accuracy, precision, recall, F1, reports y matrices |
| 2D. Justificación del mejor | 1,5 | Ranking por F1 macro + validación cruzada de 5 folds + interpretación |
| 3A. OpenCV y preprocesamiento | 1,0 | `cv2.imread`, BGR→RGB, resize 100×100, normalización, split 70/15/15 |
| 3B. CNN | 1,5 | Conv2D, kernels 3×3/5×5, pooling, dropout, BN, sigmoid, BCE, 3 canales |
| 3C. Curvas y evaluación | 1,0 | loss/accuracy train-val, test, classification report, confusión y ejemplos |
| **Total** | **10,0** | Cobertura completa |

## Evidencia adicional

- Semilla reproducible.
- Separación por paciente para reducir fuga de información.
- Early stopping y reducción de learning rate.
- Checkpoint del mejor modelo.
- Pesos de clase calculados únicamente con training.
- Dataset no versionado por tamaño y privacidad/reproducibilidad.
