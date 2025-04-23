---
title: 主轴和副轴练习用C++
linktitle: 主轴和次轴
description: 了解如何在Aspose.Cells for C++中理解和使用主轴和副轴。我们的指南将帮助您理解主轴和副轴的区别，以及如何有效地配置和使用它们的图表。
keywords: Aspose.Cells for C++，主轴，副轴，理解，差异，配置，使用。
type: docs
weight: 190
url: /zh/cpp/primary-and-second-axis/
---

## **可能的使用场景**
当图表中的数据系列之间的数值差异很大，或者当您有多种类型的数据（价格和成交量）时，请在次垂直（值）轴上绘制一个或多个数据系列。次垂直轴的刻度显示了相关数据系列的值。在显示柱形图和折线图的组合图中，次要轴效果很好。

## **处理主轴和第二轴，就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后我们添加一个图表并显示第二轴。

![todo:image_alt_text](excel.png)

## **示例代码**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
