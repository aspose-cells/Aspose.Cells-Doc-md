---
title: How to create waterfall chart with C++
linktitle: How to create waterfall chart
type: docs
weight: 160
url: /cpp/creating-waterfall-chart/
description: Create waterfall charts in Excel with C++ and Aspose.Cells for C++ API.
keywords: c++ create waterfall chart in excel, c++ creating waterfall chart in excel, creating waterfall chart in excel with c++, create waterfall chart in excel with c++, create waterfall chart in excel c++, create waterfall chart excel c++, create waterfall chart in excel programmatically, how to create waterfall chart in excel with c++
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

A waterfall chart is a special type of chart that is normally used to demonstrate how the starting position either increases or decreases. Microsoft Excel has many predefined chart types, including column, line, pie, bar, radar, etc., but the waterfall chart is beyond the basic graphs and can be created using the existing chart types with little or extensive customization.

{{% /alert %}}

Aspose.Cells API allows you to create a waterfall chart with the help of a line chart. The API also allows customizing the chart appearance to give it the shape of the waterfall by setting the [**Series.GetUpBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getupbars/) & [**Series.GetDownBars()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/getdownbars/) properties.

The code snippet below demonstrates the usage of the Aspose.Cells for C++ API to create a waterfall chart from scratch.

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

    // Add a chart of type Waterfall in the same worksheet as the data
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

    // Make both series lines invisible
    chart.GetNSeries().Get(0).GetBorder().SetIsVisible(false);
    chart.GetNSeries().Get(1).GetBorder().SetIsVisible(false);

    // Set the plot area formatting to Automatic
    chart.GetPlotArea().GetArea().SetFormatting(FormattingType::Automatic);

    // Delete the Legend
    chart.GetLegend().GetLegendEntries().Get(0).SetIsDeleted(true);
    chart.GetLegend().GetLegendEntries().Get(1).SetIsDeleted(true);

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## Related Articles

- [Creating Charts](/cells/cpp/creating-charts/)
- [Customizing Charts](/cells/cpp/customizing-charts/)
{{< app/cells/assistant language="cpp" >}}
