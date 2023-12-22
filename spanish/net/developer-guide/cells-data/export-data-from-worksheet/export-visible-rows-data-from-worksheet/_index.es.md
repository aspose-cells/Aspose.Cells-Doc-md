---
title: Exportar datos de filas visibles desde la hoja de trabajo
type: docs
weight: 10
url: /es/net/export-visible-rows-data-from-worksheet/
description: Aprenda a exportar datos de filas visibles desde la hoja de trabajo a través de Aspose.Cells for .NET API.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Puede exportar datos de hojas de trabajo a tablas de datos usando Aspose.Cells. A veces desea exportar solo los datos de las filas visibles. Aspose.Cells proporciona una manera de lograrlo. Utilizar el[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)para especificar que desea exportar solo datos de filas visibles.

{{% /alert %}}

Este ejemplo muestra cómo exportar datos de la siguiente hoja de trabajo. Las filas 5, 6 y 7 están ocultas.

|**Datos de muestra en la hoja de trabajo, las filas 5, 6 y 7 están ocultas**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 Una vez que los datos se exportan a una tabla de datos usando el[**Hoja de trabajo.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) método con el[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)opción, se verá así. Las filas ocultas se trazan como filas en blanco.

|**Las filas ocultas se exportan a la tabla de datos como filas en blanco.**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
