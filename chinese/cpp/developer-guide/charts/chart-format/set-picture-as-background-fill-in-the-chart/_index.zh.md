---
title: 用C++在图表中设置图片为背景填充
linktitle: 在图表中设置图片作为背景填充
description: 学习如何使用Aspose.Cells for C++将图片设置为图表的背景填充。我们的指南将告诉您如何导入和调整图片位置、大小、颜色，以及应用格式化选项以增强图表外观。
keywords: Aspose.Cells for C++，制图，背景填充，图片，导入，定位，大小，颜色，格式化。
type: docs
weight: 30
url: /zh/cpp/set-picture-as-background-fill-in-the-chart/
---

{{% alert color="primary" %}}

Aspose.Cells允许您为不同对象如图表区域、图表区或图例框添加渐变、纹理、图案或图片作为填充效果。本文展示了如何向图表背景添加图像。

{{% /alert %}}

为实现该功能，Aspose.Cells提供了[**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/)属性。以下示例演示如何使用[**Chart.GetImageData()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/getimagedata/)属性将图片设置为图表背景填充。

## 使用C++在图表中设置图片作为背景填充的代码示例

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Region");
    cells.Get(u"A2").PutValue(u"France");
    cells.Get(u"A3").PutValue(u"Germany");
    cells.Get(u"A4").PutValue(u"England");
    cells.Get(u"A5").PutValue(u"Sweden");
    cells.Get(u"A6").PutValue(u"Italy");
    cells.Get(u"A7").PutValue(u"Spain");
    cells.Get(u"A8").PutValue(u"Portugal");
    cells.Get(u"B1").PutValue(u"Sale");
    cells.Get(u"B2").PutValue(70000);
    cells.Get(u"B3").PutValue(55000);
    cells.Get(u"B4").PutValue(30000);
    cells.Get(u"B5").PutValue(40000);
    cells.Get(u"B6").PutValue(35000);
    cells.Get(u"B7").PutValue(32000);
    cells.Get(u"B8").PutValue(10000);

    int sheetIndex = workbook.GetWorksheets().Add(SheetType::Chart);
    sheet = workbook.GetWorksheets().Get(sheetIndex);
    sheet.SetName(u"Chart");

    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 1, 1, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    std::ifstream fs((srcDir + u"aspose.png").ToUtf8(), std::ios::binary);
    std::vector<uint8_t> data((std::istreambuf_iterator<char>(fs)), std::istreambuf_iterator<char>());
    Aspose::Cells::Vector<uint8_t> asposeData(data.data(), data.size());

    chart.GetPlotArea().GetArea().GetFillFormat().SetImageData(asposeData);
    chart.GetPlotArea().GetBorder().SetIsVisible(false);

    chart.GetTitle().SetText(u"Sales By Region");
    chart.GetTitle().GetFont().SetColor(Color::Blue());
    chart.GetTitle().GetFont().SetIsBold(true);
    chart.GetTitle().GetFont().SetSize(12);

    chart.GetNSeries().Add(u"Data!B2:B8", true);
    chart.GetNSeries().SetCategoryData(u"Data!A2:A8");
    chart.GetNSeries().SetIsColorVaried(true);

    Legend legend = chart.GetLegend();
    legend.SetPosition(LegendPositionType::Top);

    workbook.Save(outDir + u"column_chart_out.xls");
    Aspose::Cells::Cleanup();
    return 0;
}
```
