---
title: Export Worksheet or Chart into Image with Desired Width and Height with C++
linktitle: Export Worksheet or Chart into Image with Desired Width and Height
type: docs
weight: 290
url: /cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: Use Aspose.Cells to export worksheet or chart into image with desired width and height in C++.
---

{{% alert color="primary" %}}

You can use Aspose.Cells to export your worksheet or chart into an image with the desired width and height. It provides [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) method to set the desired width and height of the exported image. The width and height are specified in the unit of pixels.

{{% /alert %}}

The following code exports the worksheet into an image with 400x400 size.

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