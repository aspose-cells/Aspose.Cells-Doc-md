---
title: Hitta maxrader och maxkolumner som stöds av XLS och XLSX format
type: docs
weight: 20
url: /sv/python-net/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **Möjliga användningsscenario**

Det finns olika antal rader och kolumner som stöds av Excel-format. Till exempel stöder XLS 65536 rader och 256 kolumner medan XLSX stöder 1048576 rader och 16384 kolumner. Om du vill veta hur många rader och kolumner som stöds av ett visst format kan du använda egenskaperna [**WorkbookSettings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) och [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column).

## **Hitta maxrader och maxkolumner som stöds av XLS och XLSX-format**

Följande exempelkod skapar först arbetsboken i XLS-format och sedan i XLSX-format. Efter skapandet skrivs värdena av egenskaperna [**Workbook.settings.max_row**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_row) och [**Workbook.settings.max_column**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_column) ut. Se konsoloutputen för koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
