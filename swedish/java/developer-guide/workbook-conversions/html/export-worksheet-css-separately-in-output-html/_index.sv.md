---
title: Exportera arbetsblad CSS separat i utdata HTML
type: docs
weight: 80
url: /sv/java/export-worksheet-css-separately-in-output-html/
---
## **Möjliga användningsscenarier**

Aspose.Cells tillhandahåller funktionen för att exportera kalkylblads-CSS separat när du konverterar din Excel-fil till HTML. Använd egenskapen HtmlSaveOptions.ExportWorksheetCSSSeparat för detta ändamål och ställ in den som sann medan du sparar Excel-fil i HTML-format.

## **Exportera arbetsblad CSS separat i utdata HTML**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cell B5 i röd färg och sparar den sedan i HTML-format med hjälp av egenskapen HtmlSaveOptions.ExportWorksheetCSSSeparately. Vänligen se[mata ut HTML](60489780.zip)genereras av koden för en referens. Du hittar stylesheet.css i den som ett resultat av exempelkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exportera en arbetsbok till HTML**

När en arbetsbok med flera ark konverteras till HTML med Aspose.Cells, skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med ett enda kalkylblad när den konverteras till HTML. Tidigare skapades ingen separat mapp för arbetsböcker med enstaka ark och endast HTML-fil skapades. Sådan HTML-fil visar inte flik när den öppnas i webbläsaren. Excel skapar också rätt mapp och HTML för enstaka ark och därför implementeras samma beteende med Aspose.Cells. Exempelfil kan laddas ner från följande länk för användning i exempelkoden nedan:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
