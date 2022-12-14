---
title: Exportieren Sie sichtbare Zeilendaten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/net/export-visible-rows-data-from-worksheet/
---
{{% alert color="primary" %}}

 Mit Aspose.Cells können Sie Daten aus Arbeitsblättern in Datentabellen exportieren. Manchmal möchten Sie nur die Daten der sichtbaren Zeilen exportieren. Aspose.Cells bietet eine Möglichkeit, dies zu erreichen. Verwenden Sie die[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows) um anzugeben, dass nur sichtbare Zeilendaten exportiert werden sollen.

{{% /alert %}}

Dieses Beispiel zeigt, wie Daten aus dem folgenden Arbeitsblatt exportiert werden. Die Zeilen 5, 6 und 7 sind ausgeblendet.

|**Beispieldaten im Arbeitsblatt, Zeilen 5, 6 und 7 sind ausgeblendet**|
|:- |
|![todo: Bild_alt_Text](export-visible-rows-data-from-worksheet_1.png)|

Sobald die Daten mithilfe von in eine Datentabelle exportiert wurden[**Arbeitsblatt.Cells.ExportDataTable()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/exportdatatable/index) Methode mit der[**ExportTableOptions.PlotVisibleRows**](https://reference.aspose.com/cells/net/aspose.cells/exporttableoptions/properties/plotvisiblerows)Option, sieht es so aus. Ausgeblendete Zeilen werden als leere Zeilen gezeichnet

|**Ausgeblendete Zeilen werden als leere Zeilen in die Datentabelle exportiert**|
|:- |
|![todo: Bild_alt_Text](export-visible-rows-data-from-worksheet_2.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExportVisibleRowsData-1.cs" >}}
