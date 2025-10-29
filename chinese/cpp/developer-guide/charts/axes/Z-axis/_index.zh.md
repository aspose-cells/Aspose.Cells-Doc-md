---
title: 用C++实现Z轴
linktitle: Z轴
description: 学习如何操作Aspose.Cells for C++中的Z轴。我们的指南将帮助您了解如何配置和定制Z轴，包括其比例和标签，以增强您的图表效果。
keywords: Aspose.Cells for C++，Z轴，制图，配置，定制，比例，标签。
type: docs
weight: 210
url: /zh/cpp/z-axis/
---

## **可能的使用场景**
对于一些具有深度（系列）轴的3D图表，例如3D柱状图、3D圆锥体图或3D金字塔图，也称为Z轴，您可以进行更改。您可以指定刻度标记之间的间隔、轴标签和其他操作。

## **处理主轴和第二轴，就像处理Microsoft Excel一样**
请查看以下示例代码，它创建一个新的Excel文件，并将图表的值放在第一个工作表中。然后我们添加一个图表，将图表类型设置为柱状3D，然后可以看到深度轴也称为Z轴。 

![todo:image_alt_text](excel.png)

## **示例代码**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
