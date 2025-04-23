---
title: 使用C++将图表转换为SVG格式图像
linktitle: 将图表转换为SVG格式的图像
type: docs
weight: 240
url: /zh/cpp/converting-chart-to-image-in-svg-format/
description: 学习如何使用Aspose.Cells结合C++将图表转换为SVG图像。
---

{{% alert color="primary" %}}

可缩放矢量图形（SVG）是一种基于XML的二维图形格式，还支持交互和动画。SVG规范是由万维网联盟（W3C）自1999年以来制定的开放标准。

SVG图像及其行为是在XML文本文件中定义的。这意味着它们可以被搜索、索引、编写脚本和压缩。作为XML文件，SVG图像可以使用任何文本编辑器创建和编辑，但更常见的是使用绘图软件创建。

Aspose.Cells可以将图表保存为BMP、JPEG、PNG、GIF、SVG等多种格式的图像。本文介绍如何将图表保存为SVG格式。

{{% /alert %}}

以下示例代码解释了如何使用Aspose.Cells将图表转换为SVG格式图像。该代码加载源Microsoft Excel文件，然后将第一个工作表上找到的第一个图表保存为SVG。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleChartBook.xlsx";

    // Create workbook object from source file
    Workbook workbook(inputFilePath);

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set image or print options
    ImageOrPrintOptions opts;
    opts.SetImageType(Aspose::Cells::Drawing::ImageType::Svg);

    // Save the chart to svg format
    chart.ToImage(outDir + u"Image_out.svg", opts);

    std::cout << "Chart saved to SVG format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
