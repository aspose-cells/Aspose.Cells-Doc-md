---
title: 使用 C++ 管理Excel图表的轴线
description: 学习如何在Aspose.Cells for C++中配置图表轴。我们的指南将演示如何调整主轴和副轴、设置其范围以及修改其属性以增强您的图表效果。
keywords: Aspose.Cells for C++，图表轴，配置，主轴，副轴，范围，属性。
linktitle: 轴
type: docs
weight: 50
url: /zh/cpp/chart-axes/
---

{{% alert color="primary" %}}

在Excel图表中，有3种类型的轴：
1. 水平（类别）轴：X轴
1. 垂直（数值）轴：Y轴
1. 深度（系列）轴：Z轴

{{% /alert %}}

## **轴选项**
 Aspose.Cells 还允许你在运行时管理图表的轴线。使用 [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 对象，你可以像在Excel中一样更改轴线的所有选项。

|![todo:image_alt_text](chart_axes.png)|

## **管理X和Y轴**

 在Excel图表中，水平轴和垂直轴是最常用的两个轴线。

 以下代码片段演示了如何设置X轴和Y轴的选项。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [更改刻度标签方向](/cells/zh/cpp/change-tick-label-direction/)
- [确定图表中存在哪些轴](/cells/zh/cpp/determine-which-axis-exists-in-the-chart/)
- [处理Microsoft Excel的图表轴的自动单位](/cells/zh/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [计算图表后读取轴标签](/cells/zh/cpp/read-axis-labels-after-calculating-the-chart/)
- [如何在Excel图表中设置类别轴](/cells/zh/cpp/how-to-set-category-axis/)
