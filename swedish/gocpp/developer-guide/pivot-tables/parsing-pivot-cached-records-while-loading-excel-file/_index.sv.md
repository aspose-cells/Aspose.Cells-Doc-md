---
title: Parsning av pivotcache poster vid inläsning av Excel fil med Golang via C++
linktitle: Parsning av Pivot Cached Records
type: docs
weight: 70
url: /sv/go-cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Lär dig hur du parsar pivot cacheade poster vid laddning av Excel filer med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda Pivot Cache-poster eller inte med hjälp av [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/)-egenskapen. Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda Pivot Cache-poster bör du ställa in denna egenskap som **true**.

## **Dekodning Pivot Cache-poster vid inläsning av Excel-fil**

Följande exempelkod förklarar användningen av [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getparsingpivotcachedrecords/)-egenskapen. Den laddar den [provpå Excel-filen](61767773.xlsx) samtidigt som den dekoderar de pivot-cache-posterna. Därefter uppdaterar den pivotabell och sparar den som [utdata Excel-fil](61767774.xlsx).

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ParsingPivotCachedRecordsWhileLoadingExcelFile.go" >}}
