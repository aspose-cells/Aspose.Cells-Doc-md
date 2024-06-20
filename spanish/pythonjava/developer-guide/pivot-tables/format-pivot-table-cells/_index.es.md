---
title: Formato de celdas de tabla dinámica
type: docs
weight: 20
url: /es/python-java/format-pivot-table-cells/
---

{{% alert color="primary" %}}

A veces desearás dar formato a las celdas de una tabla dinámica. Por ejemplo, aplicar un color de fondo a las celdas de una tabla dinámica. Aspose.Cells proporciona dos métodos [**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) y [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), que puedes utilizar para este propósito.

[**PivotTable.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style)) aplica el estilo a toda la tabla dinámica, mientras que [**PivotTable.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) aplica el estilo a una única celda de la tabla dinámica.

{{% /alert %}}

El siguiente código de ejemplo da formato a toda la tabla dinámica con un color azul claro y luego formatea la segunda fila de la tabla con color amarillo.

**La tabla dinámica de entrada, antes de ejecutar el código**

![todo:image_alt_text](format-pivot-table-cells_1.png)

**La tabla dinámica de salida, después de ejecutar el código**

![todo:image_alt_text](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
