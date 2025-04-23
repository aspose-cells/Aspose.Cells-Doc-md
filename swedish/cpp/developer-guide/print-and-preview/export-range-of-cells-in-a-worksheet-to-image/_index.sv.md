---
title: Exportera område av celler i ett arbetsblad till bild med C++
linktitle: Exportera cellområde till bild
type: docs
weight: 60
url: /sv/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: Lär dig hur man exporterar ett specifikt cellområde i ett arbetsblad till en bild med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**

Du kan skapa en bild av en arbetsbok med hjälp av Aspose.Cells. Ibland behöver du dock exportera endast ett område av celler i en arbetsbok till en bild. Den här artikeln förklarar hur du åstadkommer detta.

## **Exportera område av celler i en arbetsbok till bild**

För att ta en bild av ett område, ange utskriftsområdet till det önskade området och ställ sedan in alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) till **true**. Följande kod tar en bild av området D8:G16. Nedan finns en skärmbild av den [exempelfil i Excel](47153160.xlsx) som används i koden. Du kan prova koden med vilken Excel-fil som helst.

## **Skärmbild av exempelfil i Excel och dess exporterade bild**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

Genom att köra koden skapas en bild av området D8:G16 endast.

**![todo:image_alt_text](Output-Image.png)**

## **Exempelkod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
