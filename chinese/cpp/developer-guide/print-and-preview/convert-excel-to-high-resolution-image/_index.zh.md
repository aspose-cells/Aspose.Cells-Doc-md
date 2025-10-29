---
title: 将Excel转换为高分辨率图像——使用C++
linktitle: 转换Excel到高分辨率图像
type: docs
weight: 100
url: /zh/cpp/convert-excel-to-high-resolution-image/
description: 使用Aspose.Cells与C++从Excel文件生成高分辨率图像。
---

随着高分辨率屏幕的普及，以默认96 DPI生成的图像往往显得模糊不清。为了确保在高分辨率屏幕上的清晰度，必须以更高的DPI生成图像。Aspose.Cells提供设置 [**ImageOrPrintOptions.GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/) 和 [**ImageOrPrintOptions.GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/) 的功能，从而可以从Excel文件创建在高分辨率显示器上清晰锐利的高质量图像。

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
