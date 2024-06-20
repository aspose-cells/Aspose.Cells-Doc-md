---
title: Suchen Sie nach der maximal unterstützten Anzahl von Zeilen und Spalten in den Formaten XLS und XLSX
type: docs
weight: 60
url: /de/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Mögliche Verwendungsszenarien**
Excel-Formate unterstützen eine unterschiedliche Anzahl von Zeilen und Spalten. Zum Beispiel unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten von einem bestimmten Format unterstützt werden, können Sie die Eigenschaften [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) und [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) verwenden.
## **Suchen Sie die maximale Anzahl von Zeilen und Spalten, die von den XLS- und XLSX-Formaten unterstützt werden**
Der folgende Beispielcode erstellt zuerst eine Arbeitsmappe im XLS- und dann im XLSX-Format. Nach der Erstellung druckt er die Werte der Eigenschaften [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) und [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn). Bitte werfen Sie einen Blick auf die Konsolenausgabe des untenstehenden Codes als Referenz.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Konsolenausgabe

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
