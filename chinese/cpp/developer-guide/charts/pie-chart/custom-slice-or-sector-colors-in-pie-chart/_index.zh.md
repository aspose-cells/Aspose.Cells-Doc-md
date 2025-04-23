---
title: 在 C++ 中为饼图的切片或扇区自定义颜色
linktitle: 在饼图中自定义切片或扇区的颜色
description: 了解如何使用 Aspose.Cells for C++ 自定义饼图中切片和扇区的颜色。我们的指南将演示如何为每个切片、扇区或图例分配独特的颜色，以增强视觉吸引力和数据表现。
keywords: Aspose.Cells for C++，饼图，自定义切片颜色，自定义扇区颜色，视觉吸引力，数据表现。
type: docs
weight: 60
url: /zh/cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

本文解释了如何向饼图切片/扇区添加自定义颜色。默认情况下，饼图使用Microsoft Excel的默认模板。要使用其他颜色，需要重新定义图表中的颜色。

{{% /alert %}}

要为饼图的单独切片或扇区设置自定义颜色：

1. 访问 [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) 对象的 [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/)。
1. 使用[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/)属性分配您选择的颜色。

本文还解释了如何：

- 图表的类别数据。
- 与单元格相关联的图表标题。
- 图表标题字体设置。
- 图例的位置。

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/) 不仅适用于饼图，还可用于所有类型的图表。

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"C3").PutValue(u"India");
    worksheet.GetCells().Get(u"C4").PutValue(u"China");
    worksheet.GetCells().Get(u"C5").PutValue(u"United States");
    worksheet.GetCells().Get(u"C6").PutValue(u"Russia");
    worksheet.GetCells().Get(u"C7").PutValue(u"United Kingdom");
    worksheet.GetCells().Get(u"C8").PutValue(u"Others");

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"D2").PutValue(u"% of world population");
    worksheet.GetCells().Get(u"D3").PutValue(25);
    worksheet.GetCells().Get(u"D4").PutValue(30);
    worksheet.GetCells().Get(u"D5").PutValue(10);
    worksheet.GetCells().Get(u"D6").PutValue(13);
    worksheet.GetCells().Get(u"D7").PutValue(9);
    worksheet.GetCells().Get(u"D8").PutValue(13);

    // Create a pie chart with desired length and width
    int pieIdx = worksheet.GetCharts().Add(ChartType::Pie, 1, 6, 15, 14);

    // Access the pie chart
    Chart pie = worksheet.GetCharts().Get(pieIdx);

    // Set the pie chart series
    pie.GetNSeries().Add(u"D3:D8", true);

    // Set the category data
    pie.GetNSeries().SetCategoryData(u"=Sheet1!$C$3:$C$8");

    // Set the chart title that is linked to cell D2
    pie.GetTitle().SetLinkedSource(u"D2");

    // Set the legend position at the bottom
    pie.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set the chart title's font name and color
    pie.GetTitle().GetFont().SetName(u"Calibri");
    pie.GetTitle().GetFont().SetSize(18);

    // Access the chart series
    Series srs = pie.GetNSeries().Get(0);

    // Color the individual points with custom colors
    srs.GetPoints().Get(0).GetArea().SetForegroundColor(Color{0, 246, 22, 219});
    srs.GetPoints().Get(1).GetArea().SetForegroundColor(Color{0, 51, 34, 84});
    srs.GetPoints().Get(2).GetArea().SetForegroundColor(Color{0, 46, 74, 44});
    srs.GetPoints().Get(3).GetArea().SetForegroundColor(Color{0, 19, 99, 44});
    srs.GetPoints().Get(4).GetArea().SetForegroundColor(Color{0, 208, 223, 7});
    srs.GetPoints().Get(5).GetArea().SetForegroundColor(Color{0, 222, 69, 8});

    // Autofit all columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
