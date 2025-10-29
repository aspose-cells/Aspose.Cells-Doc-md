---
title: 使用C++管理Excel图表的数据标签
linktitle: 数据标签
type: docs
weight: 50
url: /zh/cpp/insert-datalabels-to-chart/
description: 学习如何使用Aspose.Cells for C++有效管理Excel图表中的数据标签。我们的全面指南涵盖了添加、删除和修改标签等各种管理任务，以增强图表的可读性和易用性。
keywords: Aspose.Cells for C++、Excel图表、数据标签、管理、可读性、易用性、添加、删除、修改。
---

{{% alert color="primary" %}}

数据标签是图表的重要组成部分。我们可以轻松了解每个系列的值、百分比等信息。

{{% /alert %}}

## **数据标签选项**
Aspose.Cells还允许使用[DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/)对象在运行时管理图表的数据标签。移动、更新和格式化图表的数据标签都很简单。

|![todo:image_alt_text](chart_datalabels.png)|

## **管理图表的数据标签**
用Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/) 管理图表数据标签非常简单。

以下代码片段演示了如何管理DataLabels：

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [向图表系列的数据点添加自定义标签](/cells/zh/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [禁用图表的数据标签文本换行](/cells/zh/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [调整图表数据标签形状以适应文本](/cells/zh/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [图表点的富文本自定义数据标签](/cells/zh/cpp/rich-text-custom-data-label-of-chart-point/)
- [设置图表数据标签的形状类型](/cells/zh/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [将单元格范围显示为数据标签](/cells/zh/cpp/showing-cell-range-as-the-data-labels/)
{{< app/cells/assistant language="cpp" >}}
