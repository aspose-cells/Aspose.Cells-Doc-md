---
title: 用C++创建成交量 最高 最低 收盘（VHLC）股票图表
linktitle: 创建成交量高低收（VHLC）股票图表
description: 学习如何用Aspose.Cells for C++创建成交量 最高 最低 收盘股票图表。该指南将展示如何绘制股票市场数据，包括成交量、最高、最低和收盘价，以便更好的分析与可视化。
keywords: Aspose.Cells for C++，成交量 最高 最低 收盘股票图表，股票市场数据，分析，可视化。
type: docs
weight: 183
url: /zh/cpp/create-volume-high-low-close-stock-chart/
---

## **可能的使用场景**
我们要看的第三个股票图表是成交量高低收（Volume High Low Close）图表。同样重要的是，要确保数据的顺序是正确的。如果需要重新排列数据表，应在设置图表之前完成。该图表包括在第一个（类别）列之后的成交量列，图表上的主轴显示成交量，而价格数据移动到副轴上。

![todo:image_alt_text](data.png)
## **成交量高低收（VHLC）股票图表**

![todo:image_alt_text](sample.png)
## **示例代码**
以下示例代码加载了 [样本Excel文件](Volume-High-Low-Close.xlsx) 并生成了 [输出Excel文件](out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

