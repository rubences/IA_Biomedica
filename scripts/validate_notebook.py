#!/usr/bin/env python3
"""Validación estática del notebook de entrega."""

from __future__ import annotations

import ast
import json
from pathlib import Path

NOTEBOOK = Path("MUBIO07_Actividad3_IA_Python_Grupo.ipynb")

REQUIRED_TEXT = [
    "Meritxell Bastardas Pernil",
    "Rubén Juárez Cádiz",
    "Águeda Sobrino Martínez",
    "Yiling Teng Fang",
    "sns.load_dataset",
    "OneHotEncoder",
    "SVC",
    "RandomForestClassifier",
    "GaussianNB",
    "precision_score",
    "recall_score",
    "f1_score",
    "cv2.imread",
    "StratifiedGroupKFold",
    "Conv2D",
    "MaxPooling2D",
    "Dropout",
    "sigmoid",
    "binary_crossentropy",
    "confusion_matrix",
]


def main() -> None:
    if not NOTEBOOK.exists():
        raise SystemExit(f"No existe {NOTEBOOK}")

    data = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cells = data.get("cells", [])
    if not cells:
        raise SystemExit("El notebook no contiene celdas")

    all_text = "\n".join(
        "".join(cell.get("source", []))
        if isinstance(cell.get("source"), list)
        else str(cell.get("source", ""))
        for cell in cells
    )

    missing = [item for item in REQUIRED_TEXT if item not in all_text]
    if missing:
        raise SystemExit(f"Faltan elementos obligatorios: {missing}")

    code_cells = 0
    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue

        code_cells += 1
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)

        try:
            ast.parse(source)
        except SyntaxError as exc:
            raise SystemExit(
                f"Error de sintaxis en celda de código {i}: {exc}"
            ) from exc

    if code_cells < 10:
        raise SystemExit("Número inesperadamente bajo de celdas de código")

    print(
        f"OK: notebook válido, {len(cells)} celdas, "
        f"{code_cells} celdas de código y rúbrica cubierta."
    )


if __name__ == "__main__":
    main()
