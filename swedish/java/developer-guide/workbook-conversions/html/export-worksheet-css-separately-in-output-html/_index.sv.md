---
title: Exportera arbetsbladets CSS separat i utdata HTML filen
type: docs
weight: 80
url: /sv/java/export-worksheet-css-separately-in-output-html/
---

## **Möjliga användningsscenario**

Aspose.Cells erbjuder funktionen att exportera arbetsbladets CSS separat när du konverterar din Excel-fil till HTML. Använd HtmlSaveOptions.ExportWorksheetCSSSeparately egenskapen för detta ändamål och ställ in den som true när du sparar Excel-filen i HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande provkod skapar en Excel-fil, lägger till lite text i cell B5 i röd färg och sparar sedan den i HTML-format med HtmlSaveOptions.ExportWorksheetCSSSeparately egenskapen. Se den [utdata-HTML](60489780.zip) som genererats av koden för referens. Du kommer att hitta stylesheet.css i det som ett resultat av provkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Exportera arbetsbok med enkelt blad till HTML**

När en arbetsbok med flera blad konverteras till HTML med hjälp av Aspose.Cells skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med endast ett arbetsblad när den konverteras till HTML. Tidigare skapades inte en separat mapp för arbetsböcker med endast ett blad och endast en HTML-fil skapades. En sådan HTML-fil visar inte fliken när den öppnas i webbläsaren. Excel skapar en lämplig mapp och HTML för singelblads också och därför implementeras samma beteende med användning av Aspose.Cells. En provfil kan laddas ner från följande länk för att användas i den följande provkoden:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
