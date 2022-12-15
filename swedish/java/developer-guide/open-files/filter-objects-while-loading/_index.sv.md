---
title: Filtrera objekt när du laddar arbetsbok eller arbetsblad
type: docs
weight: 1060
url: /sv/java/filter-objects-while-loading-workbook-or-worksheet/
---
## **Möjliga användningsscenarier**
 Snälla använd[LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) egenskap medan du filtrerar data från arbetsboken. Men om du vill filtrera data från enskilda kalkylblad måste du åsidosätta[LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet\(com.aspose.cells.Worksheet\) ) metod. Ange lämpligt värde från[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) uppräkning medan du skapar eller arbetar med[LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

 De[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions)uppräkning har följande värden.

- [INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ALLT](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_BOOL)
- [CELL_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_VALUE)
- [FORMEL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL_DATA)
- [DIAGRAM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FORM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [MERGED_AREA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED_AREA)
- [VILLKORLIG FORMATERING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL_FORMATTING)
- [DATAVALIDERING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA_VALIDATION)
- [PIVOT_TABLE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT_TABLE)
- [TABELL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLÄNKAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [SHEET_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_SETTINGS)
- [SHEET_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET_DATA)
- [BOOK_SETTINGS](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK_SETTINGS)
- [INSTÄLLNINGAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML_MAP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML_MAP)
- [STRUKTURERA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DOKUMENT EGENSKAPER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT_PROPERTIES)
- [DEFINED_NAMES](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STIL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filtrera objekt medan arbetsbok läses in**
 Följande exempelkod illustrerar hur du filtrerar diagram från arbetsboken. Vänligen kontrollera[exempel på excel-fil](5472489.xlsx) används i den här koden och[mata ut PDF](5472488.pdf)genereras av det. Som du kan se i PDF-filen har alla diagram filtrerats bort från arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filtrera objekt medan kalkylblad laddas**
 Följande exempelkod laddar[källkod excel-fil](5472492.xlsx) och filtrerar följande data från sina kalkylblad med hjälp av ett anpassat filter.

- Det filtrerar diagram från kalkylblad som heter NoCharts.
- Det filtrerar former från kalkylblad som heter NoShapes.
- Det filtrerar villkorlig formatering från kalkylbladet som heter NoConditionalFormatting.

 En gång laddar den[källkod excel-fil](5472492.xlsx) med ett anpassat filter tar den bilderna av alla kalkylblad en efter en. Här är utdatabilderna för din referens. Som du kan se har den första bilden inga diagram, den andra bilden har inga former och den tredje bilden har inte villkorlig formatering.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
