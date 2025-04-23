---
title: Skriv ut och förhandsgranska arbetsboken
linktitle: Skriv ut och förhandsgranska
type: docs
weight: 70
url: /sv/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells för Python via .NET stöder utskrift och förhandsgranskning av Excel filer utan Microsoft Excel installation.
---

{{% alert color="primary" %}}

Efter att ha skapat ett kalkylblad vill du ofta skriva ut en hård kopia av det. Den här artikeln förklarar hur man skriver ut kalkylblad med Aspose.Cells för Python via .NET.

{{% /alert %}}

## **Introduktion till utskrift**

Microsoft Excel förutsätter att du vill skriva ut hela kalkylbladet om du inte specificerar ett urval. För att skriva ut med Aspose.Cells för Python via .NET, importera först namnrymden aspose.cells.rendering till programmet. Den har flera användbara klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) och [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Skriv ut med SheetRender**

Klassen [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) representerar ett kalkylblad och har metoden [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/) som kan skriva ut ett kalkylblad. Följande exempelkod visar hur du skriver ut ett kalkylblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Skriv ut med WorkbookRender**

För att skriva ut en hel arbetsbok, iterera genom bladen och skriv ut dem, eller använd [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) -klassen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET tillhandahåller också överbelastningar för metoderna [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) och [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), så att det är möjligt att ställa in namnet på utskriftsjobbet vid utskrift av Excel-kalkylblad. Som standard skapas alla utskriftsjobb med namnet "Dokument".

{{% /alert %}}

## **Förhandsgranska utskrift**

Det kan finnas fall där Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Bearbetning av sådana filer kommer att förbruka mycket tid och resurser. I sådana fall kan arbetsbokens och arbetsbladets förhandsgranskningsfunktion vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) -klasser för att ta reda på det totala antalet sidor.

Aspose.Cells för Python via .NET tillhandahåller funktionen för förhandsgranskning av utskrift. För detta tillhandahåller API:et [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)-klasser. För att skapa förhandsgranskning av hela arbetsboken, skapa en instans av [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview)-klassen genom att skicka [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)-objekt till konstruktorn. Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) tillhandahåller en [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/)-metod som returnerar antalet sidor i den genererade förhandsgranskningen. Liknande klass [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) används för att generera en förhandsgranskning för ett specifikt kalkylblad. För att skapa förhandsgranskning av ett kalkylblad, skapa en instans av [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview)-klassen genom att skicka [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions)-objekt till konstruktorn. Klassen [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) tillhandahåller också en [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/)-metod som returnerar antalet sidor i den genererade förhandsgranskningen.

Följande kodsnutt demonstrerar användningen av både [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) klasser genom att använda [exempel på excel-fil](94896177.xlsx).

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Följande är utdatan som genereras genom att köra ovanstående kod.

### **Konsoloutput**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

