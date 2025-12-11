---
title: How to Create Dynamic Scrolling Chart with C++
linktitle: Create Dynamic Scrolling Chart
description: Learn how to create a dynamic scrolling chart using Aspose.Cells for C++. Our step-by-step guide will demonstrate how to implement smooth data transitions and automatic scrolling in your chart for a continuous and updated display.
keywords: Aspose.Cells for C++, Dynamic Scrolling Chart, Data Transitions, Smooth Scrolling, Continuous Display, Updating Visualization.
type: docs
weight: 75
url: /cpp/create-dynamic-scrolling-chart/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A dynamic scrolling chart is a type of graphical representation used to display data that changes over time. It is designed to provide a real-time view of data, allowing users to track continuous updates and trends. The chart continuously updates itself as new data is added, and it automatically scrolls to show the most recent information.

Dynamic scrolling charts are commonly used in various industries, such as finance, stock market analysis, weather tracking, and social media analytics. They enable users to visualize and analyze data patterns and make informed decisions based on real-time information.

These charts are typically interactive, allowing the user to zoom in or out, scroll through historical data, and adjust time intervals. They often support multiple data series, providing a comprehensive view of different metrics and their correlations.

Overall, dynamic scrolling charts are valuable tools for monitoring and analyzing time-series data, facilitating real-time decision-making and enhancing data visualization capabilities.

## **Use Aspose Cells to Create Dynamic Scrolling Chart**
In the next paragraphs, we will show you how to create a Dynamic Scrolling Chart using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Scrolling Chart File](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notes**
In the generated file, you can operate on the scroll bar, while the chart dynamically displays the latest 10 sets of data. This is done using the "OFFSET" formula in the sample code:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

You can try changing the number "10" to "15" in cell "Sheet1!$H$20", and the dynamic chart will display the latest 15 sets of data. Now we have successfully created a dynamic scrolling chart using Aspose.Cells.

{{< app/cells/assistant language="cpp" >}}
