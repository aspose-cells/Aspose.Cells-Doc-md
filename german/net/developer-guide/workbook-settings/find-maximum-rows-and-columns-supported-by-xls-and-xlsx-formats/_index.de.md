---
title: Suchen Sie nach der maximal unterstützten Anzahl von Zeilen und Spalten in den Formaten XLS und XLSX
type: docs
weight: 20
url: /de/net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Mögliche Verwendungsszenarien**

Excel-Formate unterstützen unterschiedliche Anzahlen von Zeilen und Spalten. Zum Beispiel unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten von einem bestimmten Format unterstützt werden, können Sie die Eigenschaften [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) und [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) verwenden.

## **Suchen Sie die maximale Anzahl von Zeilen und Spalten, die von den XLS- und XLSX-Formaten unterstützt werden**

Der folgende Beispielcode erstellt zuerst eine Arbeitsmappe im XLS- und dann im XLSX-Format. Nach der Erstellung gibt er die Werte der Eigenschaften [**Workbook.Settings.MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxrow) und [**Workbook.Settings.MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/maxcolumn) aus. Bitte sehen Sie sich die Konsolenausgabe des unten angegebenen Codes zur Referenz an.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
