---
title: Filtrera objekt när du laddar arbetsbok eller kalkylblad
type: docs
weight: 1060
url: /sv/java/filter-objects-while-loading-workbook-or-worksheet/
---

## **Möjliga användningsscenario**
Vänligen använd egenskapen [LoadOptions.LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#LoadFilter) vid filtrering av data från arbetsboken. Men om du vill filtrera data från enskilda kalkylblad måste du åsidosätta metoden [LoadFilter.startSheet](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#startSheet-com.aspose.cells.Worksheet-). Ange rätt värde från uppradade [LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) medan du skapar eller arbetar med [LoadFilter](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter).

[LoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadDataFilterOptions) ramverket har följande värden.

- [INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#NONE)
- [ALLA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#ALL)
- [CELL_BLANK](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BLANK)
- [CELL_STRING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-STRING)
- [CELL_NUMERIC](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-NUMERIC)
- [CELL_ERROR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-ERROR)
- [CELL_BOOL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-BOOL)
- [CELL_VÄRDE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-VALUE)
- [FORMEL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#FORMULA)
- [CELL_DATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CELL-DATA)
- [DIAGRAM](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CHART)
- [FIGUR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE)
- [SAMMANSATT_OMRÅDE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#MERGED-AREA)
- [VILLKORSBASERAD_FORMATTERING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#CONDITIONAL-FORMATTING)
- [DATA_VALIDERING](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DATA-VALIDATION)
- [PIVOTTABELL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#PIVOT-TABLE)
- [TABELL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#TABLE)
- [HYPERLÄNKAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#HYPERLINKS)
- [ARKINSTÄLLNINGAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-SETTINGS)
- [ARKDATA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHEET-DATA)
- [BOKINSTÄLLNINGAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#BOOK-SETTINGS)
- [INSTÄLLNINGAR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SETTINGS)
- [XML-MAPP](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#XML-MAP)
- [STRUKTUR](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STRUCTURE)
- [DOKUMENTEGENSKAPER](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DOCUMENT-PROPERTIES)
- [DEFINIERADE_NAMN](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES)
- [VBA](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#VBA)
- [STIL](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#STYLE)
## **Filterobjekt vid inläsning av arbetsbok**
Följande exempelkod visar hur du filtrerar diagram från arbetsboken. Var god kontrollera den [provexelfil](5472489.xlsx) som används i denna kod och den [utdata PDF](5472488.pdf) som genererats av den. Som du kan se i utdata PDF:en har alla diagram filtrerats bort från arbetsboken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilterObjectsLoadingWorkbook-FilterObjectsLoadingWorkbook.java" >}}
## **Filterobjekt vid inläsning av arbetsblad**
Följande exempelkod laddar den [källa exelfilen](5472492.xlsx) och filtrerar följande data från dess arbetsblad med hjälp av ett anpassat filter.

- Det filtrerar diagram från kalkylbladet som heter NoCharts.
- Det filtrerar former från kalkylbladet som heter NoShapes.
- Det filtrerar villkorlig formatering från kalkylbladet som heter NoConditionalFormatting.

När den laddar den [källa exelfilen](5472492.xlsx) med ett anpassat filter, tar den bilderna av alla arbetsblad ett efter ett. Här är utdatbilderna för referens. Som du kan se har den första bilden inga diagram, den andra bilden har inga former och den tredje bilden har ingen villkorlig formatering.

- [NoCharts.png](5472493.png)
- [NoShapes.png](5472491.png)
- [NoConditionalFormatting.png](5472490.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterObjectsLoadingWorksheets-1.java" >}}
{{< app/cells/assistant language="java" >}}
