---
title: Eliminar la tabla dinámica de una hoja de cálculo
type: docs
weight: 60
url: /es/python-net/delete-pivot-table-from-a-worksheet/
description: Código Python via .NET para quitar PivotTable para hojas de Excel
keywords: Aspose.Cells for Python Excel, biblioteca de Python de Excel, Python via .NET eliminar tabla dinámica de la hoja de cálculo, Python via .NET eliminar tabla dinámica de Excel, cómo eliminar tabla dinámica con Python via .NET, eliminar tabla dinámica con Python via .NET, eliminar tabla dinámica de Excel con Python via .NET, Python via .NET eliminar tabla dinámica, Python via .NET quitar tabla dinámica, quitar tabla dinámica, eliminar tabla dinámica, cómo eliminar tabla dinámica
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET proporciona una función para eliminar o quitar la Tabla Dinámica de una Hoja de Cálculo. Puede eliminar la tabla dinámica usando el objeto de tabla dinámica o la posición de la tabla dinámica. Por favor, use el método [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) para eliminar la tabla dinámica usando el objeto de tabla dinámica y el método [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) para eliminar el objeto de tabla dinámica usando su posición dentro de la colección de tablas dinámicas.

{{% /alert %}}

## **Cómo Eliminar la Tabla Dinámica de la Hoja de Cálculo Usando la Biblioteca Aspose.Cells for Python de Excel**

El siguiente código de muestra elimina dos tablas dinámicas de la hoja de cálculo. Primero elimina la tabla dinámica usando el método [**Worksheet.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) y luego elimina la tabla dinámica usando el método [**Worksheet.pivot_tables.remove_at(index, keep_data)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
