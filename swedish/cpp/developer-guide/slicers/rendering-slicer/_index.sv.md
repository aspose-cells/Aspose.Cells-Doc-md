---
title: Rendera slicer med C++
type: docs
weight: 40
url: /sv/cpp/rendering-slicer/
description: Rendera slicers i Excel filer med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**
Aspose.Cells stöder rendering av slicerform. Om du konverterar ditt kalkylblad till en bild eller sparar din arbetsbok i PDF- eller HTML-format kommer du att se att slicers renderas korrekt.
## **Rendering slicer**
Följande exempel kod laddar filen [sample Excel](67338479.xlsx) som innehåller en existerande slicer. Den konverterar kalkylbladet till en bild genom att ställa in utskriftsområdet som endast täcker slicern. Den följande bilden visar [utdatabilden](67338480.png) som visar den renderade slicern. Som du kan se, har slicern renderats korrekt och ser likadan ut som i exempel Excel-filen.

![todo:image_alt_text](rendering-slicer_1)
## **Exempelkod**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleRenderingSlicer.xlsx");

    // Access first worksheet.
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Set the print area because we want to render slicer only.
    ws.GetPageSetup().SetPrintArea(u"B15:E25");

    // Specify image or print options, set one page per sheet and only area to true.
    ImageOrPrintOptions imgOpts;
    imgOpts.SetHorizontalResolution(200);
    imgOpts.SetVerticalResolution(200);
    imgOpts.SetImageType(ImageType::Png);
    imgOpts.SetOnePagePerSheet(true);
    imgOpts.SetOnlyArea(true);

    // Create sheet render object and render worksheet to image.
    SheetRender sr(ws, imgOpts);
    sr.ToImage(0, u"outputRenderingSlicer.png");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
