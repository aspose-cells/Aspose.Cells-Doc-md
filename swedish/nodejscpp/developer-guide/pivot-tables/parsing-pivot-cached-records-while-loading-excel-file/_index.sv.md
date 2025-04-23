---
title: Dekodning Pivot Cache poster vid inläsning av Excel fil
type: docs
weight: 70
url: /sv/nodejs-cpp/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda Pivot Cache-poster eller inte med hjälp av [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-)-egenskapen. Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda Pivot Cache-poster bör du ställa in denna egenskap som **true**.

## **Dekodning Pivot Cache-poster vid inläsning av Excel-fil**

Följande exempelkod förklarar användningen av [**LoadOptions.setParsingPivotCachedRecords**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setParsingPivotCachedRecords-boolean-)-egenskapen. Den laddar den [provpå Excel-filen](61767773.xlsx) samtidigt som den dekoderar de pivot-cache-posterna. Därefter uppdaterar den pivotabell och sparar den som [utdata Excel-fil](61767774.xlsx).

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.js" >}}

