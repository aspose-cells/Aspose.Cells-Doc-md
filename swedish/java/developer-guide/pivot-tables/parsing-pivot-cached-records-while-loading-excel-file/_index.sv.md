---
title: Dekodning Pivot Cache poster vid inläsning av Excel fil
type: docs
weight: 100
url: /sv/java/parsing-pivot-cached-records-while-loading-excel-file/
---

## **Möjliga användningsscenario**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i Pivot Cache. Pivot Cache hålls i minnet i Microsoft Excel. Du kan inte se den, men det är datan som pivottabellen hänvisar till när du bygger din pivottabell eller ändrar en Slicer-val eller flyttar rader/kolumner. Detta gör att Microsoft Excel kan vara mycket reaktivt på förändringar i pivottabellen, men det kan också dubbla storleken på din fil. Trots allt är Pivot Cache bara en kopia av din källdata så det är logiskt att din filstorlek kommer att vara potentiellt dubblerad.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda in posterna från Pivot Cache eller inte, med hjälp av egenskapen [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Standardvärdet för denna egenskap är **false**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda in posterna från Pivot Cache bör du ange denna egenskap som **true**.

## **Dekodning Pivot Cache-poster vid inläsning av Excel-fil**

Följande kodexempel förklarar användningen av egenskapen [**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords). Den laddar in den [exempelvisk filen](61767786.xlsx) medan den analyserar pivotcachelagrade poster. Sedan uppdateras pivot-tabellen och sparas som den [utdataexempelviska filen](61767785.xlsx).

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
