---
title: 使用C++管理Excel图表的图例
linktitle: 图例
description: 学习如何利用 Aspose.Cells for C++ 高效利用和定制Microsoft Excel中的图表图例。我们的全面指南介绍了图例的功能、访问和修改方法，以及如何利用图例改善可视化和数据理解。
keywords: Aspose.Cells for C++，图例，Microsoft Excel，可视化，数据理解。
type: docs
weight: 50
url: /zh/cpp/chart-legend/
---

## **图例选项**
Aspose.Cells 还允许你在运行时管理图表的图例。通过[图例](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/)对象，图例可以被移动、更新和格式化。

|![todo:image_alt_text](chart_legend.png)|

## **设置图表的图例**
使用Aspose.Cells的[图例](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/)管理图表的图例非常简单。

以下代码片段演示如何管理图例：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ** 高级主题**
- [使用Aspose.Cells将图例条目填充的文本设置为无](/cells/zh/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="cpp" >}}
