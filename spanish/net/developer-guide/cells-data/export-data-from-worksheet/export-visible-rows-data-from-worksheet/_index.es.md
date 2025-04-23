---
title: Exportar datos de filas visibles de la hoja de trabajo
type: docs
weight: 10
url: /es/net/export-visible-rows-data-from-worksheet/
description: Aprenda cómo exportar datos de filas visibles de la hoja de trabajo a través de la API Aspose.Cells for .NET.
keywords: Exportar datos de filas visibles a DataTable, exportar datos de filas no ocultas a DataTable, exportar datos de filas a DataTable y excluir filas ocultas, ignorar filas ocultas al exportar datos de hoja de cálculo a tabla de datos
---

{{% alert color="primary" %}}

Puede exportar datos de hojas de cálculo a tablas de datos utilizando Aspose.Cells. A veces desea exportar solo los datos de filas visibles. Aspose.Cells proporciona una forma de lograr esto. Utilice el [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) para especificar que desea exportar solo los datos de filas visibles.

{{% /alert %}}

Este ejemplo muestra cómo exportar datos de la siguiente hoja de cálculo. Las filas 5, 6 y 7 están ocultas.

|**Datos de ejemplo en la hoja de cálculo, las filas 5, 6 y 7 están ocultas**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Una vez que los datos se exportan a una tabla de datos utilizando el método [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) con la opción [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), se verá así. Las filas ocultas se representan como filas en blanco

|**Las filas ocultas se exportan a la tabla de datos como filas en blanco**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
