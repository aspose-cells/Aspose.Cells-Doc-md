---
title: Exportera arbetsblad CSS separat i utdata HTML
type: docs
weight: 80
url: /sv/net/export-worksheet-css-separately-in-output/
---
## **Möjliga användningsscenarier**

 Aspose.Cells tillhandahåller funktionen för att exportera kalkylblads-CSS separat när du konverterar din Excel-fil till HTML. Använd[**HtmlSaveOptions.ExportWorksheetCSSSeparat**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) egendom för detta ändamål och ställa den till**Sann** samtidigt som du sparar Excel-fil i formatet HTML.

## **Exportera arbetsblad CSS separat i utdata HTML**

Följande exempelkod skapar en Excel-fil, lägger till lite text i cellen**B5** i**Röd**färg och sparar den sedan i HTML-format med hjälp av[**HtmlSaveOptions.ExportWorksheetCSSSeparat**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) fast egendom. Vänligen se[utgång HTML](60489766.zip) genereras av koden för referens. Du kommer hitta**stilark.css**inuti den som ett resultat av exempelkoden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Exportera arbetsbok för ett ark till HTML**

När en arbetsbok med flera ark konverteras till HTML med Aspose.Cells, skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för en arbetsbok med enstaka kalkylblad när den konverteras till HTML. Tidigare skapades ingen separat mapp för enstaka arbetsböcker och endast HTML-filen skapades. Sådan HTML-fil visar inte flik när den öppnas i webbläsaren. MS Excel skapar en korrekt mapp och HTML för ett enda ark också, och därför implementeras samma beteende med Aspose.Cells API:er. Exempelfilen kan laddas ner från följande länk för användning i exempelkoden nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
