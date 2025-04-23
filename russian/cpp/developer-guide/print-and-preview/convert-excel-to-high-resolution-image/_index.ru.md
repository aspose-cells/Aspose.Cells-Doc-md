---
title: Конвертация Excel в изображение высокого разрешения с C++
linktitle: Конвертация Excel в изображение высокого разрешения
type: docs
weight: 100
url: /ru/cpp/convert-excel-to-high-resolution-image/
description: Создавайте изображения высокого разрешения из Excel файлов с помощью Aspose.Cells и C++.
---

С ростом популярности экранов высокого разрешения изображения, создаваемые по умолчанию с разрешением 96 DPI, выглядят размытыми и нечеткими. Чтобы обеспечить четкость на дисплеях высокого разрешения, важно генерировать изображения с более высоким DPI. Aspose.Cells позволяет устанавливать [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) и [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/), что дает возможность создавать изображения высокого качества из Excel-файлов, которые выглядят четко на дисплеях высокой четкости.

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
