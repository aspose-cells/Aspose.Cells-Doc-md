---
title: Formato de tabla dinámica Cells
type: docs
weight: 20
url: /es/python-java/format-pivot-table-cells/
---
{{% alert color="primary" %}}

 A veces, desea dar formato a las celdas de la tabla dinámica. Por ejemplo, desea aplicar un color de fondo a las celdas de la tabla dinámica. Aspose.Cells proporciona dos métodos[**Tabla dinámica.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) y[**Tabla dinámica.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)), que puede utilizar para este fin.

[**Tabla dinámica.formatAll()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#formatAll(com.aspose.cells.Style) ) aplica el estilo a toda la tabla dinámica mientras[**Tabla dinámica.format()**](https://reference.aspose.com/cells/python-java/asposecells.api/pivottable#format(int,%20int,%20com.aspose.cells.Style)) aplica el estilo a una sola celda de la tabla dinámica.

{{% /alert %}}

El siguiente código de ejemplo formatea toda la tabla dinámica con un color azul claro y luego formatea la segunda fila de la tabla en amarillo.

**La tabla dinámica de entrada, antes de ejecutar el código.**

![todo:imagen_alternativa_texto](format-pivot-table-cells_1.png)

**La tabla dinámica de salida, después de ejecutar el código.**

![todo:imagen_alternativa_texto](format-pivot-table-cells_2.png)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "PivotTables-FormatCells.py" >}}
