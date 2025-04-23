---
title: 用 C++ 管理 Excel 图表的标题
linktitle: 标题
description: 学习如何使用 Aspose.Cells for C++ 在 Microsoft Excel 中添加和格式化图表及轴标题。我们的指南将演示如何设置不同类型的标题，调整其外观，并修改轴标题以更好地展示数据和提高清晰度。
keywords: Aspose.Cells for C++，图表标题，轴标题，Microsoft Excel，数据展示，外观优化。
type: docs
weight: 50
url: /zh/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

在Excel图表中，有两种标题：
1. 图表标题 
1. 轴标题

{{% /alert %}}

## **标题选项**
Aspose.Cells 还支持在运行时管理图表标题。使用 [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) 对象，您可以更改标题的文本、字体和填充格式。

|![todo:image_alt_text](chart_title.png)|

## **设置图表或坐标轴的标题**
您可以在 WYSIWYG 环境中使用 Microsoft Excel 设置图表及其轴的标题。Aspose.Cells 还允许开发者在运行时设置图表及其轴的标题。所有图表及其轴都包含一个 [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) 属性，可用于设置它们的标题，示例如下：

以下代码段演示了如何为图表和轴设置标题。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

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

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 高级主题**
- [从ODS文件中读取图表副标题](/cells/zh/cpp/read-chart-subtitle-from-ods-file/)
