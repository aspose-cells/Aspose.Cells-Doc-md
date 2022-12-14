---
title: Skriv ut och förhandsgranska arbetsbok
linktitle: Skriv ut och förhandsgranska
type: docs
weight: 70
url: /sv/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells stöder utskrift och förhandsgranskning av Excel-filer utan Microsoft Excel-installation.
---
{{% alert color="primary" %}}

När du har skapat ett kalkylblad vill du ofta skriva ut en papperskopia av det. Den här artikeln förklarar hur du skriver ut kalkylblad med Aspose.Cells.

{{% /alert %}}

## **Skriv ut introduktion**

Microsoft Excel förutsätter att du vill skriva ut hela kalkylbladsområdet om du inte anger ett urval. För att skriva ut med Aspose.Cells, importera först namnområdet Aspose.Cells.Rendering till programmet. Den har flera användbara klasser, t.ex.[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) och[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Skriv ut med SheetRender**

 De[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) klass representerar ett kalkylblad och har[**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)metod som kan skriva ut ett kalkylblad. Följande exempelkod visar hur man skriver ut ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Skriv ut med WorkbookRender**

 För att skriva ut en hel arbetsbok, iterera genom arken och skriv ut dem, eller använd[**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)klass.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells tillhandahåller också överbelastningar för[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) och[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) metoder, så det är möjligt att ställa in utskriftsjobbets namn när du skriver ut Excel-kalkylblad. Som standard skapas alla utskriftsjobb med namnet "Dokument".

{{% /alert %}}

## **Förhandsgranskning**

Det kan finnas fall där Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Att bearbeta sådana filer kommer att ta mycket tid och resurser. I sådana fall kan funktionen för förhandsgranskning av arbetsbok och arbetsblad visa sig vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Den här artikeln fokuserar på att använda[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)och[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)klasser för att ta reda på det totala antalet sidor.

 Aspose.Cells tillhandahåller förhandsgranskningsfunktionen. För detta tillhandahåller API[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) och[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) klasser. För att skapa förhandsvisningen av hela arbetsboken skapar du en instans av[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) klass genom att passera[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) och[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objekt till konstruktören. De[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) klass ger en[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) metod som returnerar antalet sidor i den genererade förhandsvisningen. Liknande[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)klass, den[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)klass används för att generera en förhandsgranskning för ett specifikt kalkylblad. För att skapa förhandsvisningen av ett kalkylblad, skapa en instans av[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)klass genom att passera[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)och[**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)objekt till konstruktören. De[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)klass ger också en[**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)metod som returnerar antalet sidor i den genererade förhandsvisningen.

Följande kodavsnitt visar användningen av båda[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)och[**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) klasser genom att använda[exempel på excel-fil](94896177.xlsx).

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Följande är utdata som genereras genom att exekvera ovanstående kod.

### **Konsolutgång**

Antal sidor i arbetsboken: 1
Antal sidor i arbetsbladet: 1


## **Förhandsämnen**
- [Konfigurera teckensnitt för rendering av kalkylblad](/cells/sv/net/configuring-fonts-for-rendering-spreadsheets/)
- [Konvertera kalkylblad till bild - Ta bort blanksteg runt data](/cells/sv/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Konvertera kalkylblad till bild och kalkylblad till bild för sida](/cells/sv/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Konvertera kalkylblad till bild med ImageOrPrint-alternativ](/cells/sv/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportera intervallet Cells i ett kalkylblad till bild](/cells/sv/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportera kalkylblad eller diagram till bild med önskad bredd och höjd](/cells/sv/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahera bilder från kalkylblad med ImageOrPrintOptions](/cells/sv/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Skapa miniatyrbild av arbetsbladet](/cells/sv/net/generate-thumbnail-of-the-worksheet/)
- [Skriv ut tom sida när det inte finns något att skriva ut](/cells/sv/net/output-blank-page-when-there-is-nothing-to-print/)
- [Sidinställningar och utskriftsalternativ](/cells/sv/net/page-setup-and-printing-options/)
- [Skriva ut omfång av sidor med SheetRender och WorkbookRender](/cells/sv/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Rendera sekvens av sidor med hjälp av PageIndex och PageCount Properties för ImageOrPrintOptions](/cells/sv/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Återge arbetsblad till grafisk kontext](/cells/sv/net/render-worksheet-to-graphic-context/)
- [Ange individuell eller privat uppsättning teckensnitt för arbetsbokrendering](/cells/sv/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Ange jobb- eller dokumentnamn vid utskrift med Aspose.Cells](/cells/sv/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
