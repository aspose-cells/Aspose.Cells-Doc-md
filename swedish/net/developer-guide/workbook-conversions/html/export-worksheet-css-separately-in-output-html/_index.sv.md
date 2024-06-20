---
title: Exportera arbetsbladets CSS separat i utdata HTML filen
type: docs
weight: 80
url: /sv/net/export-worksheet-css-separately-in-output/
---

## **Möjliga användningsscenario**

Aspose.Cells tillhandahåller funktionen att exportera arbetsblads-CSS separat när du konverterar din Excel-fil till HTML. Använd [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)-egenskapen för detta ändamål och ange den till **true** vid sparande av Excel-filen i HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cellan **B5** i **röd** färg och sparar sedan den i HTML-format med [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)-egenskapen. Se [utdata-HTML-filen](60489766.zip) genererad av koden för referens. Du hittar **stylesheet.css** i utdata som ett resultat av exempelkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportera arbetsbok med enkelt blad till HTML**

När en arbetsbok med flera blad konverteras till HTML med Aspose.Cells skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med enstaka arbetsblad när den konverteras till HTML. Tidigare skapades inget separat mapp för enkla bladarbetsböcker och endast en HTML-fil skapades. En sådan HTML-fil visar inte flik när den öppnas i webbläsaren. MS Excel skapar en korrekt mapp och HTML-fil för enkla blad också och därför har samma beteende implementerats med Aspose.Cells API:er. Exempelfilen kan laddas ned från följande länk för användning i den angivna koden nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
