---
title: Finden Sie maximale Zeilen und Spalten, die von den Formaten XLS und XLSX unterstützt werden
type: docs
weight: 60
url: /de/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---
## **Mögliche Nutzungsszenarien**
Es gibt eine unterschiedliche Anzahl von Zeilen und Spalten, die von Excel-Formaten unterstützt werden. Beispielsweise unterstützt XLS 65536 Zeilen und 256 Spalten, während XLSX 1048576 Zeilen und 16384 Spalten unterstützt. Wenn Sie wissen möchten, wie viele Zeilen und Spalten von einem bestimmten Format unterstützt werden, können Sie verwenden[Arbeitsmappe.Einstellungen.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)und[Arbeitsmappe.Einstellungen.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)Eigenschaften.
## **Finden Sie maximale Zeilen und Spalten, die von den Formaten XLS und XLSX unterstützt werden**
Der folgende Beispielcode erstellt eine Arbeitsmappe zuerst im Format XLS und dann im Format XLSX. Nach der Erstellung werden die Werte von gedruckt[Arbeitsmappe.Einstellungen.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow)und[Arbeitsmappe.Einstellungen.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn)Eigenschaften. Bitte sehen Sie sich die Konsolenausgabe des unten angegebenen Codes als Referenz an.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Konsolenausgabe

{{< highlight "java" >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
