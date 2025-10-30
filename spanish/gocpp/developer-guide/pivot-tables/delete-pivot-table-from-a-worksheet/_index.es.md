---
title: Eliminar tabla dinámica de una hoja de cálculo con Golang vía C++
linktitle: Eliminar tabla dinámica
type: docs
weight: 60
url: /es/go-cpp/delete-pivot-table-from-a-worksheet/
description: Código C++ para eliminar la tabla dinámica en hojas de Excel usando Aspose.Cells.
keywords: c++ elimina la tabla dinámica de la hoja de trabajo, c++ elimina la tabla dinámica de Excel, cómo eliminar la tabla dinámica con c++, elimina la tabla dinámica con c++, elimina la tabla dinámica de Excel con c++, c++ eliminar tabla dinámica, c++ eliminar tabla dinámica, elimina tabla dinámica, elimina la tabla dinámica, cómo eliminar la tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una función para eliminar o quitar la Tabla Dinámica de una hoja de cálculo. Puede eliminar la tabla dinámica usando el objeto de tabla dinámica o la posición de la tabla dinámica. Utilice el método [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) para eliminar la tabla dinámica usando el objeto de tabla dinámica y el método [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) para eliminar el objeto de tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

El siguiente código de ejemplo elimina dos tablas dinámicas de la hoja de trabajo. Primero elimina la tabla dinámica usando [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/go-cpp/pivottablecollection/remove_pivottable/) método y luego elimina otra usando [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/removeat/) método.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeletePivotTableFromAWorksheet.go" >}}
