---
title: تحويل إكسل إلى صورة عالية الدقة باستخدام C++
linktitle: تحويل إكسل إلى صورة عالية الدقة
type: docs
weight: 100
url: /ar/cpp/convert-excel-to-high-resolution-image/
description: إنشاء صور عالية الدقة من ملفات إكسل باستخدام Aspose.Cells مع C++.
---

مع تزايد انتشار الشاشات عالية الدقة، غالبًا ما تظهر الصور التي تنتج عند 96 DPI الافتراضية غير واضحة وغير حادة. لضمان الوضوح على الشاشات عالية الدقة، من الضروري إنشاء صور بدقة أعلى. تقدم Aspose.Cells ميزة لتعيين [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) و [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)، مما يسمح لك بإنشاء صور عالية الجودة من ملفات إكسل تظهر بشكل واضح على الشاشات عالية الدقة.

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
