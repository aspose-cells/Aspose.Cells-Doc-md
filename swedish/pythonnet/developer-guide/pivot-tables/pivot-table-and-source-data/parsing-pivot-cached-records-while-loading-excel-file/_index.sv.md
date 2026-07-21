---
title: Dekodning Pivot Cache poster vid inläsning av Excel fil
type: docs
weight: 70
url: /sv/python-net/parsing-pivot-cached-records-while-loading-excel-file/
description: Hur man analyserar cachade pivotposter vid inläsning av Excel fil med Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python bibliotek, Hur man analyserar cachade pivotposter vid inläsning av Excel fil med Aspose.Cells for Python Excel Library.
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda Pivot Cache-poster eller inte med hjälp av [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)-egenskapen. Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda Pivot Cache-poster bör du ställa in denna egenskap som **true**.

## **Hur man analyserar cachade pivotposter vid inläsning av Excel-fil**

Följande exempelkod förklarar användningen av [**LoadOptions.parsing_pivot_cached_records**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/parsing_pivot_cached_records/)-egenskapen. Den laddar den [provpå Excel-filen](61767773.xlsx) samtidigt som den dekoderar de pivot-cache-posterna. Därefter uppdaterar den pivotabell och sparar den som [utdata Excel-fil](61767774.xlsx).

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.py" >}}
{{< app/cells/assistant language="python-net" >}}
