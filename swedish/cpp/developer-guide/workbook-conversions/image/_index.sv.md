---
title: Konvertera Excel till bild med C++
linktitle: Konvertera Excel till bild
type: docs
weight: 300
url: /sv/cpp/convert-excel-to-image/
description: Lär dig hur man konverterar Excel ark till bilder, inklusive TIFF och SVG format, med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig exportera ett kalkylblad från arbetsboken och konvertera det till olika format. Den här artikeln förklarar hur man konverterar ett kalkylblad till olika format.

{{% /alert %}}

## Konvertering av arbetsbok till TIFF

En Excel-fil kan innehålla flera blad med flera sidor. [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) låter dig konvertera Excel till TIFF med flera sidor. Du kan också styra flera alternativ för TIFF, som [komprimering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), upplösning ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Följande kodsnutt visar hur man konverterar Excel till TIFF med flera sidor. Den [källa Excel-filen](workbook-to-tiff-with-mulitiple-pages.xlsx) och [genererade TIFF-bilden](workbook-to-tiff-with-mulitiple-pages.tiff) är bifogade för din referens.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konvertera Kalkylblad till Bild**

Kalkylblad innehåller data som du vill analysera. Till exempel kan ett kalkylblad innehålla parametrar, totaler, procenttal, undantag och beräkningar.

Som utvecklare kan det hända att du behöver presentera kalkylblad som bilder. Till exempel kan det hända att du behöver använda en bild av ett kalkylblad i en applikation eller webbsida. Du kan vilja infoga en bild i ett Microsoft Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan dokumenttyp. Med andra ord vill du att ett kalkylblad ska renderas som en bild så att du kan använda det någon annanstans.

Aspose.Cells stödjer konvertering av Excel-ark till bilder. För att använda denna funktion behöver du importera [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)-namnutrymmet till ditt program eller projekt. Det har flera värdefulla klasser för rendering och utskrift, till exempel [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) och andra.

Klassen [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) representerar ett arbetsblad för rendering som bilder. Den har en överlagrad metod, [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), som kan konvertera ett arbetsblad till bildfiler med olika attribut eller alternativ. Den returnerar ett objekt av typen `System.Drawing.Bitmap` och du kan spara en bildfil till disk eller ström. Flera bildformat stöds, till exempel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Följande kodsnutt visar hur man konverterar ett kalkylblad i en Excel-fil till en bildfil.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

För närvarande stöder inte API:et för att konvertera kalkylblad till bilder 3D-bubble-diagram.

{{% /alert %}}

## **Konvertera Kalkylblad till SVG**

SVG står för Skalbara Vektorgrafik. SVG är en specifikation baserad på XML-standarder för tvådimensionell vektorgrafik. Det är en öppen standard som har varit under utveckling av World Wide Web Consortium (W3C) sedan 1999.

Aspose.Cells for C++ har kunnat konvertera arbetsblad till SVG-bild sedan version 7.1.0. Följande kodsnutt visar hur man konverterar ett arbetsblad i en Excel-fil till en SVG-bildfil.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Fortsatta ämnen**
- [Konvertera ett Excel-diagram till bild](/cells/sv/cpp/convert-an-excel-chart-to-image/)
- [Konvertera diagram till bild i SVG-format](/cells/sv/cpp/converting-chart-to-image-in-svg-format/)
- [Exportera diagram till SVG med viewBox-attribut](/cells/sv/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Spåra konverteringsframsteg för Excel till TIFF](/cells/sv/cpp/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="cpp" >}}
