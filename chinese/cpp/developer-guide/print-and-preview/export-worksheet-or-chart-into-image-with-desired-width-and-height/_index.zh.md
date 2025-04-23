---
title: 使用C++将工作表或图表导出为具有所需宽度和高度的图像
linktitle: 导出工作表或图表为指定宽度和高度的图像
type: docs
weight: 290
url: /zh/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/
description: 使用Aspose.Cells在C++中将工作表或图表导出为所需宽度和高度的图像。
---

{{% alert color="primary" %}}

您可以使用 Aspose.Cells 将工作表或图表导出为具有指定宽度和高度的图像。它提供了 [**ImageOrPrintOptions.SetDesiredSize()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/setdesiredsize/) 方法，用于设置导出图像的期望宽度和高度。宽度和高度以像素为单位指定。

{{% /alert %}}

以下代码将工作表导出为一个 400x400 大小的图像。

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
