---
title: Convert Excel to High-Resolution Image with C++
linktitle: Convert Excel to High-Resolution Image
type: docs
weight: 100
url: /cpp/convert-excel-to-high-resolution-image/
description: Generate high-resolution images from Excel files using Aspose.Cells with C++.
---

With the increasing prevalence of high-resolution screens, images generated at the default 96 DPI often appear blurry and unclear. To ensure clarity on high-resolution screens, it's essential to generate images at a higher DPI. Aspose.Cells offers the functionality to set [**ImageOrPrintOptions.HorizontalResolution**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/horizontalresolution/) and [**ImageOrPrintOptions.VerticalResolution**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/verticalresolution/), allowing you to create high-quality images from Excel files that look sharp on high-resolution displays.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the Excel file
    Workbook workbook(u"input.xlsx");

    // Create an instance of ImageOrPrintOptions
    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300); // Set horizontal resolution to 300 DPI
    options.SetVerticalResolution(300);   // Set vertical resolution to 300 DPI
    options.SetImageType(ImageType::Png); // Set the image type

    // Get the worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Create a SheetRender instance
    SheetRender render(sheet, options);

    // Generate and save the image
    render.ToImage(0, u"output.png");

    std::cout << "Image generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
