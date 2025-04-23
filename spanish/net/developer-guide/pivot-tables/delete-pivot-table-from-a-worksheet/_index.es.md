---
title: Eliminar la tabla dinámica de una hoja de cálculo
type: docs
weight: 60
url: /es/net/delete-pivot-table-from-a-worksheet/
description: Código de C# para eliminar Tabla Dinámica de las hojas de cálculo de Excel
keywords: c# eliminar tabla dinámica de hoja de cálculo, c# eliminar tabla dinámica de Excel, cómo eliminar tabla dinámica con c#, eliminar tabla dinámica con c#, eliminar tabla dinámica de Excel con c#, c# eliminar tabla dinámica, c# quitar tabla dinámica, quitar tabla dinámica, eliminar tabla dinámica, cómo eliminar tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells proporciona una función para eliminar o quitar la Tabla Dinámica de una hoja de cálculo. Puede eliminar la tabla dinámica usando el objeto de tabla dinámica o la posición de la tabla dinámica. Utilice el método [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) para eliminar la tabla dinámica usando el objeto de tabla dinámica y el método [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat) para eliminar el objeto de tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

El siguiente código de muestra elimina dos tablas dinámicas de la hoja de cálculo. Primero elimina la tabla dinámica usando el método [**Worksheet.PivotTables.Remove()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/remove) y luego elimina la tabla dinámica usando el método [**Worksheet.PivotTables.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/removeat)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
