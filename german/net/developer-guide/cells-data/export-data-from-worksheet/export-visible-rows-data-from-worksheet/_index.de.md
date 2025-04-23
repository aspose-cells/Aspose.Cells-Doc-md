---
title: Exportieren von sichtbaren Zeilendaten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/net/export-visible-rows-data-from-worksheet/
description: Erfahren Sie, wie Sie sichtbare Zeilendaten aus dem Arbeitsblatt durch die Aspose.Cells for .NET API exportieren können.
keywords: Exportieren Sie sichtbare Zeilendaten in eine DataTable, exportieren Sie nicht ausgeblendene Zeilendaten in eine DataTable, exportieren Sie Zeilendaten in eine DataTable und schließen Sie ausgeblendene Zeilen aus, ignorieren Sie ausgeblendete Zeilen beim Exportieren von Arbeitsblattdaten in eine Daten Tabelle
---

{{% alert color="primary" %}}

Sie können Daten aus Arbeitsblättern mithilfe von Aspose.Cells in Daten Tabellen exportieren. Manchmal möchten Sie nur die Daten sichtbarer Zeilen exportieren. Aspose.Cells bietet eine Möglichkeit, dies zu erreichen. Verwenden Sie [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows), um anzugeben, dass Sie nur sichtbare Zeilendaten exportieren möchten.

{{% /alert %}}

Dieses Beispiel zeigt, wie Daten aus dem folgenden Arbeitsblatt exportiert werden. Die Reihen 5, 6 und 7 sind ausgeblendet.

|**Beispiel Daten im Arbeitsblatt, Reihen 5, 6 und 7 sind ausgeblendet**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_1.png)|

Nachdem die Daten mithilfe der Methode [**Worksheet.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) und der Option [**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) in eine Datentabelle exportiert wurden, sieht es so aus. Ausgeblendete Reihen werden als leere Reihen dargestellt.

|**Ausgeblendete Reihen werden als leere Reihen in die Datentabelle exportiert**|
| :- |
|![todo:image_alt_text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
