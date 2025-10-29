---
title: 用C++创建成交量 开盘 最高 最低 收盘（VOHLC）股票图表
description: 学习如何用Aspose.Cells for C++创建成交量 开盘 最高 最低 收盘股票图表。该指南将演示如何绘制股票市场数据，包括成交量、开盘、最高、最低和收盘价，以便更好的分析与可视化。
keywords: Aspose.Cells for C++，成交量 开盘 最高 最低 收盘股票图表，股票市场数据，分析，可视化。
type: docs
weight: 184
url: /zh/cpp/create-volume-open-high-low-close-stock-chart/
---

## **可能的使用场景**
我们要看的第四个股票图表是成交量开盘最高最低收盘图表。同样，数据顺序必须正确。若需重新整理数据，应在设置图表前完成。该图表包括在第一（类别）列后立即的一列成交量，图表上有一个主轴显示成交量，价格移动到副轴。

![todo:image_alt_text](data.png)

## **成交量-开盘-最高-最低-收盘（VHLC）股票图表**

![todo:image_alt_text](sample.png)

## **示例代码**
以下示例代码加载了【示例Excel文件】(Volume-Open-High-Low-Close.xlsx)，并生成了【输出Excel文件】(out.xlsx)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
