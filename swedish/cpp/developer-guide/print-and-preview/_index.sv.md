---
title: Skriv ut och förhandsgranska arbetsbok med C++
linktitle: Skriv ut och förhandsgranska
type: docs
weight: 70
url: /sv/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells stöder utskrift och förhandsgranskning av Excel filer utan Microsoft Excel installation med C++.
---

{{% alert color="primary" %}}

Efter att ha skapat ett kalkylblad vill du ofta skriva ut en papperskopia av det. Den här artikeln förklarar hur man skriver ut kalkylblad med Aspose.Cells.

{{% /alert %}}

## **Introduktion till utskrift**

Microsoft Excel antar att du vill skriva ut hela kalkylbladsområdet om inte en markering anges. För att skriva ut med Aspose.Cells, importera först namnområdet Aspose.Cells.Rendering till programmet. Det har flera användbara klasser, till exempel [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) och [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Förhandsgranska utskrift**

Det kan finnas fall där Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Bearbetning av sådana filer kommer att förbruka mycket tid och resurser. I sådana fall kan arbetsbokens och arbetsbladets förhandsgranskningsfunktion vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) -klasser för att ta reda på det totala antalet sidor.

Aspose.Cells erbjuder förhandsgranskningsfunktionen. För detta tillhandahåller API:et [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) klasser. För att skapa en förhandsgranskning av hela arbetsboken, skapa en instans av [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) -klassen genom att skicka [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) objekt till konstruktören. [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) -klassen tillhandahåller en [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/) metod som returnerar antalet sidor i den genererade förhandsgranskningen. Liknande [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) -klass används [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) -klassen för att generera en förhandsgranskning för ett specifikt arbetsblad. För att skapa en förhandsgranskning av ett arbetsblad, skapa en instans av [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) -klassen genom att skicka [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) objekt till konstruktören. [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) -klassen tillhandahåller också en [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/) metod som returnerar antalet sidor i den genererade förhandsgranskningen.

Följande kodsnutt demonstrerar användningen av både [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) klasser genom att använda [exempel på excel-fil](94896177.xlsx).

### **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Följande är utdatan som genereras genom att köra ovanstående kod.

### **Konsoloutput**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Fortsatta ämnen**
- [Konfigurera typsnitt för att rendera kalkylblad](/cells/sv/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Konvertera arbetsblad till bild - Ta bort mellanrum runt data](/cells/sv/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Konvertera kalkylblad till bild och kalkylblad till bild per sida](/cells/sv/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Konvertera arbetsblad till bild med hjälp av ImageOrPrint Options](/cells/sv/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Exportera område av celler i en arbetsbok till bild](/cells/sv/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Exportera Arbetsblad eller Diagram till Bild med önskad Bredd och Höjd](/cells/sv/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Extrahera bilder från arbetsblad med hjälp av ImageOrPrintOptions](/cells/sv/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Generera miniatyrbild av arbetsbladet](/cells/sv/cpp/generate-thumbnail-of-the-worksheet/)
- [Utdata tom sida när det inte finns något att skriva ut](/cells/sv/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Sidlayout- och utskriftsalternativ](/cells/sv/cpp/page-setup-and-printing-options/)
- [Rendera sekvens av sidor med hjälp av egenskaperna PageIndex och PageCount i ImageOrPrintOptions](/cells/sv/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Rendera kalkylblad till grafiskt sammanhang](/cells/sv/cpp/render-worksheet-to-graphic-context/)
- [Ange individuella eller privata uppsättningar typsnitt för arbetsbokpresentation](/cells/sv/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
