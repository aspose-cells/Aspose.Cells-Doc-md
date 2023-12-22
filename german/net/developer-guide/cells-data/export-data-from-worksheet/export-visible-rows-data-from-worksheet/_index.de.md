---
title: Exportieren Sie sichtbare Zeilendaten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/net/export-visible-rows-data-from-worksheet/
description: Erfahren Sie, wie Sie sichtbare Zeilendaten aus einem Arbeitsblatt über Aspose.Cells for .NET API exportieren.
keywords: Export Visible Rows Data to DataTable, Export unhidden Rows Data to DataTable, Export Rows Data to DataTable and Exclude hidden rows, Ignore Hidden Rows while Exporting Worksheet Data to Data Table
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Daten aus Arbeitsblättern in Datentabellen exportieren. Manchmal möchten Sie nur die Daten sichtbarer Zeilen exportieren. Aspose.Cells bietet eine Möglichkeit, dies zu erreichen. Benutzen Sie die[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)um anzugeben, dass Sie nur sichtbare Zeilendaten exportieren möchten.

{{% /alert %}}

Dieses Beispiel zeigt, wie Daten aus dem folgenden Arbeitsblatt exportiert werden. Die Zeilen 5, 6 und 7 sind ausgeblendet.

|**Beispieldaten im Arbeitsblatt, Zeilen 5, 6 und 7 sind ausgeblendet**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

 Sobald die Daten mithilfe von in eine Datentabelle exportiert wurden[**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Methode mit der[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)Option, es wird so aussehen. Ausgeblendete Zeilen werden als leere Zeilen dargestellt

|**Ausgeblendete Zeilen werden als leere Zeilen in die Datentabelle exportiert**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
