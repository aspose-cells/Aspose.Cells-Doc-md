---
title: 用C++创建开盘 最高 最低 收盘（OHLC）股票图表
description: 学习如何用Aspose.Cells for C++创建开盘 最高 最低 收盘股票图表。该指南将展示如何绘制股票市场数据，包括开盘、最高、最低和收盘价，以便更好的分析和可视化。
keywords: Aspose.Cells for C++，开盘 最高 最低 收盘股票图表，股票市场数据，分析，可视化。
type: docs
weight: 182
url: /zh/cpp/create-open-high-low-close-stock-chart/
---

## **可能的使用场景**
开-高-低-收（OHLC）图表使用五列数据，分别是类别、开盘、最高、最低和收盘。每个类别的价格范围再次通过垂直线表示，开盘价格和收盘价格之间的范围由一个更宽的浮动条表示；如果该类别的价格上升（收盘价高于开盘价），则该条将填充一种颜色，而如果价格下降，则用另一种颜色填充。这种图表通常被称为蜡烛图。

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **图表的可见性改进**
我们通常用颜色而非黑白来表示价格的上涨与下降。在下面第一组蜡烛图中，红色表示上涨，绿色表示下降。

![todo:image_alt_text](sample2.png)

## **示例代码**
以下示例代码加载了【示例Excel文件】(Open-High-Low-Close.xlsx)，并生成了【输出Excel文件】(out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
