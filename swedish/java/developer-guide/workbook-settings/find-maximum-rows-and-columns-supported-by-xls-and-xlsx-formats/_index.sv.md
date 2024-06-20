---
title: Hitta maxrader och maxkolumner som stöds av XLS och XLSX format
type: docs
weight: 60
url: /sv/java/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Möjliga användningsscenario**
Det finns olika antal rader och kolumner som stöds av Excel-format. Till exempel, XLS stöder 65536 rader och 256 kolumner medan XLSX stöder 1048576 rader och 16384 kolumner. Om du vill veta hur många rader och kolumner som stöds av det givna formatet kan du använda egenskaperna [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) och [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn).
## **Hitta maxrader och maxkolumner som stöds av XLS och XLSX-format**
Följande exempelkod skapar arbetsboken först i XLS och sedan i XLSX-format. Efter att ha skapats skrivs värdena av [Workbook.Settings.MaxRow](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxRow) och [Workbook.Settings.MaxColumn](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#MaxColumn) ut. Se konsoloutputen för den medföljande koden nedan för referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.java" >}}

Konsoloutput

{{< highlight java >}}

 Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
