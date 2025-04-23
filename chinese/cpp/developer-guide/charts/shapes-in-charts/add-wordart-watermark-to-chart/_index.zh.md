---
title: 用 C++ 在图表中添加 WordArt 水印
description: 学习如何使用 Aspose.Cells for C++ 向 Microsoft Excel 图表添加 WordArt 水印。我们的指南将演示如何创建和定位 WordArt 水印，以提升图表的视觉吸引力和独特性。
keywords: Aspose.Cells for C++，WordArt 水印，图表水印，Microsoft Excel，视觉吸引力，图表独特性。
type: docs
weight: 50
url: /zh/cpp/add-wordart-watermark-to-chart/
---

{{% alert color="primary" %}} 

您可以使用WordArt向电子表格添加特殊文本效果。例如，可以拉伸标题、装饰文本、使文本适应预设形状，或将受影响的文本应用到图表的绘图区作为水印。WordArt成为一个对象，您可以在电子表格中移动或定位以添加装饰。

以下示例显示如何向图表的绘图区添加WordArt形状作为水印。

{{% /alert %}} 

以下示例显示如何为现有图表的绘图区添加WordArt形状作为水印。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"sample.xlsx");

    // Get the chart in the first worksheet.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Add a WordArt watermark (shape) to the chart's plot area.
    Shape wordart = chart.GetShapes().AddTextEffectInChart(MsoPresetTextEffect::TextEffect2,
        u"CONFIDENTIAL", u"Arial Black", 66, false, false, 1200, 500, 2000, 3000);

    // Get the shape's fill format.
    FillFormat wordArtFormat = wordart.GetFill();

    // Set the transparency.
    wordArtFormat.SetTransparency(0.9);

    // Get the line format.
    LineFormat lineFormat = wordart.GetLine();

    // Set Line format to invisible.
    lineFormat.SetWeight(0.0);

    // Save the excel file.
    workbook.Save(outputDir + u"output_out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
