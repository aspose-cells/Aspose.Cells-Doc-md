---
title: 如何用C++创建动态滚动图表
linktitle: 如何创建动态滚动图表
description: 学习如何使用Aspose.Cells for C++创建动态滚动图表。我们的指南将展示如何在您的图表中实现平滑数据过渡和滚动平均，提供连续更新的显示效果。
keywords: Aspose.Cells for C++，动态滚动图表，数据过渡，平滑平均，连续显示，更新可视化。
type: docs
weight: 74
url: /zh/cpp/create-dynamic-rolling-chart/
---

## **可能的使用场景**
动态滚动图表是指显示数据点不断变化和更新的图形表示。这是一种图表类型，会不断更新自己，展示最近数据点的滚动窗口，同时丢弃旧的数据点，因为新的数据点出现。

动态滚动图表通常用于可视化实时或流数据中的趋势和模式。在临时方面和随时间的变化至关重要的场景中特别有用，如股票市场分析、天气监测或实时性能跟踪。

这些图表通常采用动画或自动滚动机制，以确保始终呈现最新的信息。滚动窗口的长度可以自定义，以显示特定的时间段，如最近一小时、一天或一周。

总之，动态滚动图表是不断更新的图形表示，显示最新数据点，丢弃旧数据点，使用户能够观察实时趋势和模式。

## **使用Aspose Cells创建动态滚动图表**
在接下来的段落中，我们将向您展示如何使用Aspose.Cells创建动态滚动图表。我们将向您展示示例的代码以及使用该代码创建的Excel文件。

## **示例代码**
以下示例代码将生成[动态滚动图表文件](DynamicRollingChart.xlsx)。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **备注**
在生成的文件中，您可以继续在A列和B列中添加数据，同时图表动态计算最新的 5 组数据。这是通过示例代码中的“OFFSET”公式完成的：

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

您可以尝试在公式中将数字“-5”更改为“-10”，动态图表将计算最新的 10 组数据。现在，我们已成功使用Aspose.Cells创建了动态滚动图表。
{{< app/cells/assistant language="cpp" >}}
