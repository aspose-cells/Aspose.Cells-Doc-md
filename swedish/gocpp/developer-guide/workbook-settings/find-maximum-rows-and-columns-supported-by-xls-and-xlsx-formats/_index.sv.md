---
title: Hitta maximalt antal rader och kolumner som stöds av XLS och XLSX format med Golang via C++
linktitle: Hitta maximala rader och kolumner
type: docs
weight: 20
url: /sv/go-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
description: Lär dig hur man hittar de maximala raderna och kolumnerna som stöds av XLS och XLSX format med hjälp av Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Det finns olika antal rader och kolumner som stöds av Excel-format. Till exempel stöder XLS 65536 rader och 256 kolumner, medan XLSX stöder 1048576 rader och 16384 kolumner. Om du vill veta hur många rader och kolumner som stöds av ett givet format kan du använda [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) och [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) egenskaper.

## **Hitta maxrader och maxkolumner som stöds av XLS och XLSX-format**

Följande exempel skapar först en arbetsbok i XLS-format och sedan i XLSX-format. Efter skapandet skriver den ut värdena för [**GetMaxRow()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getmaxrow/) och [**GetMaxColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getmaxcolumn/) egenskaperna. Vänligen se konsolutmatningen av koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindMaximumRowsAndColumnsSupportedByXlsAndXlsxFormats.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Maximum Rows and Columns supported by XLS format.

Maximum Rows: 65536

Maximum Columns: 256

Maximum Rows and Columns supported by XLSX format.

Maximum Rows: 1048576

Maximum Columns: 16384

{{< /highlight >}}
