---
title: Excel in hochauflösendes Bild mit C++ umwandeln
linktitle: Excel in hochauflösendes Bild umwandeln
type: docs
weight: 100
url: /de/cpp/convert-excel-to-high-resolution-image/
description: Hochauflösende Bilder aus Excel Dateien mit Aspose.Cells und C++ erstellen.
---

Mit der zunehmenden Verbreitung hochauflösender Bildschirme erscheinen Bilder, die mit den Standard-DPI von 96 erstellt wurden, oft unscharf und undeutlich. Um auf hochauflösenden Bildschirmen Klarheit zu gewährleisten, ist es wichtig, Bilder bei höherem DPI zu erstellen. Aspose.Cells bietet die Möglichkeit, [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) und [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/) zu setzen, um hochwertige Bilder aus Excel-Dateien zu erstellen, die auf hochauflösenden Displays scharf aussehen.

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
{{< app/cells/assistant language="cpp" >}}
