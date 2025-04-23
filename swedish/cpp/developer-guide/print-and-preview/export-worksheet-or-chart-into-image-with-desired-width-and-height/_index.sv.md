---
title: Exportera arbetsblad eller diagram till bild med önskad bredd och höjd med C++
linktitle: Exportera arbetsbok eller diagram till bild med önskad bredd och höjd
type: docs
weight: 290
url: /sv/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Använd Aspose.Cells för att exportera arbetsblad eller diagram till bild med önskad bredd och höjd i C++.
---

{{% alert color="primary" %}}

Du kan använda Aspose.Cells för att exportera din arbetsbok eller diagram till en bild med önskad bredd och höjd. Det finns en [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/)-metod för att ange den önskade bredden och höjden på den exporterade bilden. Bredden och höjden anges i pixelenheter.

{{% /alert %}}

Följande kod exporterar arbetsboken till en bild med storleken 400x400.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleWorksheetToImageDesiredSize.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetOnePagePerSheet(true);
    opts.SetImageType(Drawing::ImageType::Png);
    opts.SetDesiredSize(400, 400, false);

    // Render sheet into image
    SheetRender sr(worksheet, opts);
    sr.ToImage(0, outputDir + u"outputWorksheetToImageDesiredSize.png");

    std::cout << "Worksheet rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
