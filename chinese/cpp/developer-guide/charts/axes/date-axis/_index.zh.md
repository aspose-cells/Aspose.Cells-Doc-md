---
title: 带有C++的日期轴
linktitle: 日期轴
description: 了解如何管理Aspose.Cells for C++中的日期轴。我们的指南将帮助您理解如何处理各种日期格式、时间刻度和刻度标签频率。
keywords: Aspose.Cells for C++，日期轴，管理，日期格式，时间尺度，刻度标签频率。
type: docs
weight: 200
url: /zh/cpp/date-axis/
---

## **可能的使用场景**
当您从工作表数据创建图表，并在图表中将日期沿水平（类别）轴绘制时，Aspose.Cells 会自动将类别轴转换为日期（时间尺度）轴。
日期轴以特定间隔或基本单位（例如天数、月份或年份）按年代顺序显示日期，即使工作表上的日期不是按顺序或基本单位相同。
默认情况下，Aspose.Cells 根据工作表数据中任何两个日期之间的最小差异，确定日期轴的基本单位。例如，如果您的数据是股票价格，并且日期之间的最小差异是七天，Aspose.Cells 将基本单位设为天，但如果您希望观察股票在更长时间内的表现，也可以将基本单位改为月或年。

## **处理日期轴就像处理Microsoft Excel一样**
请参阅以下示例代码，此代码创建一个新的Excel文件并将图表的值放在第一个工作表中。 
然后，我们添加一个图表并设置[**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/)的类型 
到[**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/)，然后将基本单位设置为天数。

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

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
