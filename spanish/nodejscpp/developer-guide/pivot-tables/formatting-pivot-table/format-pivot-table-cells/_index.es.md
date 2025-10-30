---
title: Formato de celdas de tabla dinámica
type: docs
weight: 30
url: /es/nodejs-cpp/format-pivot-table-cells/
description: Cómo formatear celdas de tablas dinámicas con Aspose.Cells for Node.js via C++.
keywords: Formato de celdas de tabla dinámica.
---

{{% alert color="primary" %}}

A veces, quieres formatear celdas de tablas dinámicas. Por ejemplo, deseas aplicar color de fondo a las celdas de la tabla dinámica. Aspose.Cells for Node.js via C++ proporciona dos métodos [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) y [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-), que puedes usar para este propósito.

[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#formatAll-style-) aplica el estilo a toda la tabla dinámica mientras que [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#format-number-number-style-) aplica el estilo a una sola celda de la tabla dinámica.

{{% /alert %}}
El siguiente código de muestra carga el [archivo de Excel de ejemplo](pivot_format.xlsx) que contiene dos tablas dinámicas y logra la operación de dar formato a toda la tabla dinámica y dar formato a las celdas individuales en la tabla dinámica.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-FormatPivotTableCells-1.js" >}}

## Artículos relacionados

- [Dar formato a la tabla dinámica](/cells/es/nodejs-cpp/formatting-pivot-table/)
- [Trabajar con formatos de visualización de datos del Campo de Datos en la Tabla Dinámica](/cells/es/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="nodejs-cpp" >}}
