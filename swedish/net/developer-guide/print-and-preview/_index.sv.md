---
title: Skriv ut och förhandsgranska arbetsboken
linktitle: Skriv ut och förhandsgranska
type: docs
weight: 70
url: /sv/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells stödjer utskrift och förhandsgranskning av Excel filer utan Microsoft Excel installation.
---

{{% alert color="primary" %}}

Efter att ha skapat ett kalkylblad vill du ofta skriva ut en papperskopia av det. Den här artikeln förklarar hur man skriver ut kalkylblad med Aspose.Cells.

{{% /alert %}}

## **Introduktion till utskrift**

Microsoft Excel antar att du vill skriva ut hela kalkylbladsområdet om inte en markering anges. För att skriva ut med Aspose.Cells, importera först namnområdet Aspose.Cells.Rendering till programmet. Det har flera användbara klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) och [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Skriv ut med SheetRender**

Klassen [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) representerar ett kalkylblad och har metoden [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index) som kan skriva ut ett kalkylblad. Följande exempelkod visar hur du skriver ut ett kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Skriv ut med WorkbookRender**

För att skriva ut en hel arbetsbok, iterera genom bladen och skriv ut dem, eller använd [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) -klassen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells erbjuder också överbelastningar för [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) och [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) metoder, så det är möjligt att ange utskriftsjobbnamnet vid utskrift av Excel-kalkylblad. Som standard skapas alla utskriftsjobb med namnet "Dokument".

{{% /alert %}}

## **Förhandsgranska utskrift**

Det kan finnas fall där Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Bearbetning av sådana filer kommer att förbruka mycket tid och resurser. I sådana fall kan arbetsbokens och arbetsbladets förhandsgranskningsfunktion vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) -klasser för att ta reda på det totala antalet sidor.

Aspose.Cells erbjuder förhandsgranskningsfunktionen. För detta tillhandahåller API:et [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) klasser. För att skapa en förhandsgranskning av hela arbetsboken, skapa en instans av [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) -klassen genom att skicka [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objekt till konstruktören. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) -klassen tillhandahåller en [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) metod som returnerar antalet sidor i den genererade förhandsgranskningen. Liknande [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) -klass används [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) -klassen för att generera en förhandsgranskning för ett specifikt arbetsblad. För att skapa en förhandsgranskning av ett arbetsblad, skapa en instans av [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) -klassen genom att skicka [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) objekt till konstruktören. [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) -klassen tillhandahåller också en [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount) metod som returnerar antalet sidor i den genererade förhandsgranskningen.

Följande kodsnutt demonstrerar användningen av både [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) klasser genom att använda [exempel på excel-fil](94896177.xlsx).

### **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Följande är utdatan som genereras genom att köra ovanstående kod.

### **Konsoloutput**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Fortsatta ämnen**
- [Konfigurera typsnitt för att rendera kalkylblad](/cells/sv/net/configuring-fonts-for-rendering-spreadsheets/)
- [Konvertera arbetsblad till bild - Ta bort mellanrum runt data](/cells/sv/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Konvertera arbetsblad till bild med hjälp av ImageOrPrint Options](/cells/sv/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportera område av celler i en arbetsbok till bild](/cells/sv/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahera bilder från arbetsblad med hjälp av ImageOrPrintOptions](/cells/sv/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generera miniatyrbild av arbetsbladet](/cells/sv/net/generate-thumbnail-of-the-worksheet/)
- [Utdata tom sida när det inte finns något att skriva ut](/cells/sv/net/output-blank-page-when-there-is-nothing-to-print/)
- [Sidlayout- och utskriftsalternativ](/cells/sv/net/page-setup-and-printing-options/)
- [Utskrift av sidintervall med SheetRender och WorkbookRender](/cells/sv/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions](/cells/sv/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Rendera kalkylblad till grafiskt sammanhang](/cells/sv/net/render-worksheet-to-graphic-context/)
- [Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation](/cells/sv/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Ange jobb- eller dokumentnamn vid utskrift med Aspose.Cells](/cells/sv/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
