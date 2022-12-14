---
title: Parsar pivotcachade poster medan Excel-fil laddas
type: docs
weight: 100
url: /sv/java/parsing-pivot-cached-records-while-loading-excel-file/
---
## **Möjliga användningsscenarier**

När du skapar en pivottabell tar Microsoft Excel en kopia av källdata och lagrar den i pivotcachen. Pivot-cachen hålls i minnet i Microsoft Excel. Du kan inte se det, men det är de data som pivottabellen refererar till när du bygger din pivottabell eller ändrar ett Slicer-val eller flyttar runt rader/kolumner. Detta gör att Microsoft Excel kan vara mycket lyhörd för ändringar i pivottabellen men det kan också fördubbla storleken på din fil. När allt kommer omkring är Pivot-cachen bara en dubblett av dina källdata så det är vettigt att din filstorlek potentiellt kommer att vara dubbel.

När du laddar din Excel-fil i Workbook-objektet kan du bestämma om du också vill ladda posterna för Pivot Cache eller inte, med hjälp av[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)fast egendom. Standardvärdet för den här egenskapen är**falsk**. Om Pivot Cache är ganska stor kan det öka prestandan. Men om du också vill ladda posterna för Pivot Cache bör du ställa in den här egenskapen som**Sann**.

## **Parsar pivotcachade poster medan Excel-fil laddas**

Följande exempelkod förklarar användningen av[**LoadOptions.ParsingPivotCachedRecords**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#ParsingPivotCachedRecords)fast egendom. Den laddar[exempel på Excel-fil](61767786.xlsx)medan du analyserar de cachade pivotposterna. Sedan uppdaterar den pivottabellen och sparar den som[utdata Excel-fil](61767785.xlsx).

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-ParsingPivotCachedRecordsWhileLoadingExcelFile.java" >}}
