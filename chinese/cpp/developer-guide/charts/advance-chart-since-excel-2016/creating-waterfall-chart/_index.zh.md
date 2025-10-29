---
title: 如何用C++创建瀑布图
linktitle: 如何创建瀑布图表
type: docs
weight: 160
url: /zh/cpp/creating-waterfall-chart/
description: 用C++和Aspose.Cells for C++ API在Excel中创建瀑布图。
keywords: 用C++在Excel中创建瀑布图，C++在Excel中创建瀑布图，结合C++创建瀑布图，使用C++创建Excel瀑布图，代码实现瀑布图，程序中用C++创建瀑布图，如何用C++在Excel中创建瀑布图
---

{{% alert color="primary" %}}

瀑布图表是一种特殊的图表类型，通常用于演示起始位置是如何增加或减少的。Microsoft Excel 有许多预定义的图表类型，包括柱形图、线形图、饼图、条形图、雷达图等，但瀑布图表超出了基本图形范畴，可以使用现有的图表类型进行少量或大量的定制。

{{% /alert %}}

Aspose.Cells APIs 允许使用线图表创建瀑布图表。API 还允许自定义图表外观，使其呈现瀑布形状，通过设置 [**Series.GetUpBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getupbars/) 和 [**Series.GetDownBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getdownbars/) 属性。

以下代码演示了使用Aspose.Cells for C++ API从零开始创建瀑布图的过程。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an instance of Workbook
    Workbook workbook;

    // Retrieve the first Worksheet in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Retrieve the Cells of the first Worksheet
    Cells cells = worksheet.GetCells();

    // Input some data which chart will use as source
    cells.Get(U16String(u"A1")).PutValue(U16String(u"Previous Year"));
    cells.Get(U16String(u"A2")).PutValue(U16String(u"January"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"March"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"August"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"October"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Current Year"));

    cells.Get(U16String(u"B1")).PutValue(8.5);
    cells.Get(U16String(u"B2")).PutValue(1.5);
    cells.Get(U16String(u"B3")).PutValue(7.5);
    cells.Get(U16String(u"B4")).PutValue(7.5);
    cells.Get(U16String(u"B5")).PutValue(8.5);
    cells.Get(U16String(u"B6")).PutValue(3.5);

    cells.Get(U16String(u"C1")).PutValue(1.5);
    cells.Get(U16String(u"C2")).PutValue(4.5);
    cells.Get(U16String(u"C3")).PutValue(3.5);
    cells.Get(U16String(u"C4")).PutValue(9.5);
    cells.Get(U16String(u"C5")).PutValue(7.5);
    cells.Get(U16String(u"C6")).PutValue(9.5);

    // Add a Chart of type Waterfall in same worksheet as of data
    int idx = worksheet.GetCharts().Add(ChartType::Waterfall, 4, 4, 25, 13);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(idx);

    // Add Series
    chart.GetNSeries().Add(U16String(u"$B$1:$C$6"), true);

    // Add Category Data
    chart.GetNSeries().SetCategoryData(U16String(u"$A$1:$A$6"));

    // Series has Up Down Bars
    chart.GetNSeries().Get(0).SetHasUpDownBars(true);

    // Set the colors of Up and Down Bars
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Red());

    // Make both Series Lines invisible
    chart.GetNSeries().Get(0).GetBorder().SetIsVisible(false);
    chart.GetNSeries().Get(1).GetBorder().SetIsVisible(false);

    // Set the Plot Area Formatting Automatic
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::Automatic);

    // Delete the Legend
    chart.GetLegend().GetLegendEntries().Get(0).SetIsDeleted(true);
    chart.GetLegend().GetLegendEntries().Get(1).SetIsDeleted(true);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## 相关文章

- [创建图表](/cells/zh/cpp/creating-charts/)
- [自定义图表](/cells/zh/cpp/customizing-charts/)
{{< app/cells/assistant language="cpp" >}}
