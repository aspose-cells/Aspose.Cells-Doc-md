---
title: 如何用C++设置类别轴
linktitle: 如何设置类别轴
description: 了解如何在Aspose.Cells for C++中设置类别轴。我们的指南将帮助您理解如何定义类别轴范围、调整其属性和格式化标签。
keywords: Aspose.Cells for C++，类别轴，设置，范围，属性，格式化。
type: docs
weight: 205
url: /zh/cpp/how-to-set-category-axis/
---

## **可能的使用场景**
在工作表中创建图表后，您可以为它设置类别轴。本文将向您展示如何使用Aspose.Cells为Excel图表设置类别轴的示例代码。

## **示例代码中的步骤**

1. 创建一个新的工作簿。

2. 在第一个工作表中创建一个新的图表。

3. 在第一个工作表的单元格中添加一些值。

4. 现在您可以设置类别轴，有两种方法：使用单元格数据或直接使用字符串，示例代码都将演示这两种方法。

5. 设置数值轴，保存工作簿以查看结果。

## **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Your local test path
    U16String path = u"";

    // Create a new workbook
    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    worksheet.SetName(u"CHART");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 8, 0, 20, 10);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add some values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Sales");
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(130);
    worksheet.GetCells().Get(u"A5").PutValue(160);
    worksheet.GetCells().Get(u"A6").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Days");
    worksheet.GetCells().Get(u"B2").PutValue(1);
    worksheet.GetCells().Get(u"B3").PutValue(2);
    worksheet.GetCells().Get(u"B4").PutValue(3);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"B6").PutValue(5);

    // Some values in string
    U16String Sales = u"100,150,130,160,150";
    U16String Days = u"1,2,3,4,5";

    // Set Category Axis Data with string
    chart.GetNSeries().SetCategoryData(u"{" + Days + u"}");
    // Or you can set Category Axis Data with data in cells, try it!
    // chart.GetNSeries().SetCategoryData(u"B2:B6");

    // Add Series to the chart
    chart.GetNSeries().Add(u"Demand1", true);
    // Set value axis with string 
    chart.GetNSeries().Get(0).SetValues(u"{" + Sales + u"}");
    chart.GetNSeries().Add(u"Demand2", true);
    // Set value axis with data in cells
    chart.GetNSeries().Get(1).SetValues(u"A2:A6");

    // Set some Category Axis properties
    chart.GetCategoryAxis().GetTickLabels().SetRotationAngle(45);
    chart.GetCategoryAxis().GetTickLabels().GetFont().SetSize(8);
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Save the workbook to view the result file
    workbook.Save(path + u"Output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
