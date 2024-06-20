---
title: Cortar y pegar celdas
type: docs
weight: 30
url: /es/python-java/cut-and-paste-cells/
---

## **Cortar y Pegar Celdas**
Aspose.Cells for Python via Java proporciona la capacidad de cortar y pegar celdas. Para esto, la API proporciona el método [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) de la colección [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells). El método [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) acepta los siguientes parámetros.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): El rango de celdas a cortar.
- Índice de Fila: El índice de la fila para insertar celdas.
- Índice de Columna: El índice de la columna para insertar celdas.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): La dirección de desplazamiento de las columnas.

El siguiente fragmento de código demuestra cómo cortar y pegar celdas dentro de una hoja de cálculo.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
