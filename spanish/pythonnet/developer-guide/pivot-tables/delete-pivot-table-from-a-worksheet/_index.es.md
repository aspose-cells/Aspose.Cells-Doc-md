---
title: Eliminar tabla dinámica de una hoja de trabajo
type: docs
weight: 60
url: /es/python-net/delete-pivot-table-from-a-worksheet/
description: Python via .NET código para eliminar tabla dinámica para hojas de cálculo de Excel
keywords: Python via .NET remove pivot table from worksheet, Python via .NET remove pivot table from excel, how to delete pivot table with Python via .NET, delete pivot table with Python via .NET, delete pivot table from excel with Python via .NET, Python via .NET delete pivot table, Python via .NET remove pivot table, remove pivot table, delete pivot table, how to delete pivot table
---
{{% alert color="primary" %}}

 Aspose.Cells for Python via .NET proporciona una función para eliminar o eliminar la tabla dinámica de una hoja de trabajo. Puede eliminar la tabla dinámica utilizando el objeto de la tabla dinámica o la posición de la tabla dinámica. Por favor use el[**Hoja de trabajo.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) método para eliminar la tabla dinámica usando el objeto de tabla dinámica y[**Hoja de trabajo.pivot_tables.remove_at(índice, mantener_datos)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool)Método para eliminar el objeto de la tabla dinámica utilizando su posición dentro de la colección de la tabla dinámica.

{{% /alert %}}

 El siguiente código de muestra elimina dos tablas dinámicas de la hoja de trabajo. Primero elimina la tabla dinámica usando[**Hoja de trabajo.pivot_tables.remove(pivot_table)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/) método y luego elimina la tabla dinámica usando[**Hoja de trabajo.pivot_tables.remove_at(índice, mantener_datos)**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/remove_at/#int-bool) método

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTablesAndPivotCharts-RemovePivotTable-RemovePivotTableFromWorksheet.py" >}}
