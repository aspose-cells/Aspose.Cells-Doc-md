---
title: 如何用C++创建动态滚动图表
linktitle: 创建动态滚动图表
description: 学习如何使用Aspose.Cells for C++创建动态滚动图表。我们的逐步指南将展示如何在您的图表中实现平滑数据过渡和自动滚动，提供连续更新的显示效果。
keywords: Aspose.Cells for C++，动态滚动图表，数据过渡，平滑滚动，连续显示，更新可视化。
type: docs
weight: 75
url: /zh/cpp/create-dynamic-scrolling-chart/
---

## **可能的使用场景**
动态滚动图表是一种用于显示随时间变化的数据的图形表示类型。它旨在实时显示数据，使用户能够追踪连续的更新和趋势。随着新增数据的加入，图表将持续更新并自动滚动，以显示最新的信息。

动态滚动图表通常在各个行业中被广泛使用，如金融、股市分析、天气跟踪和社交媒体分析。它们使用户能够可视化和分析数据模式，并基于实时信息做出明智的决策。

这些图表通常是交互式的，允许用户放大或缩小、滚动历史数据和调整时间间隔。它们通常支持多个数据系列，提供不同指标及其相关性的综合视图。

总的来说，动态滚动图表是用于监控和分析时间序列数据的有价值的工具，有助于实时决策和增强数据可视化能力。

## **使用Aspose Cells创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建动态滚动图表。我们会展示示例的代码，以及用该代码生成的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicScrollingChart.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **备注**
在生成的文件中，您可以操作滚动条，而图表会动态计算最新的10组数据。这是在示例代码中使用“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

您可以尝试将单元格“Sheet1!$H$20”中的数字“10”更改为“15”，动态图表将计算最新的15组数据。现在我们成功地使用Aspose.Cells创建了动态滚动图表。
