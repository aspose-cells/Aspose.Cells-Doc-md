---
title: How to create Dynamic Rolling Chart with C++
linktitle: How to create Dynamic Rolling Chart
description: Learn how to create a dynamic rolling chart using Aspose.Cells for C++. Our guide will demonstrate how to implement smooth data transitions and rolling averages in your chart for a continuous and updated display.
keywords: Aspose.Cells for C++, Dynamic Rolling Chart, Data Transitions, Smooth Averages, Continuous Display, Updating Visualization.
type: docs
weight: 74
url: /cpp/create-dynamic-rolling-chart/
---

## **Possible Usage Scenarios**
A dynamic rolling chart refers to a graphical representation that displays data points constantly shifting and updating over time. It is a type of chart that continually updates itself, showcasing a rolling window of the most recent data points while discarding older data points as new ones come in.

Dynamic rolling charts are commonly used to visualize trends and patterns in real-time or streaming data. They are particularly useful in scenarios where temporal aspects and changes over time are critical, such as stock market analysis, weather monitoring, or live performance tracking.

These charts typically employ animation or auto-scrolling mechanisms to ensure the most up-to-date information is always presented. The length of the rolling window can be customized to show a specific time period, such as the last hour, day, or week.

In summary, a dynamic rolling chart is a continuously updated graphical representation that displays the latest data points while discarding older ones, allowing users to observe real-time trends and patterns.

## **Use Aspose Cells to create Dynamic Rolling Chart**
In the next paragraphs, we will show you how to create Dynamic Rolling Chart using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Rolling Chart File](DynamicRollingChart.xlsx).

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

## **Notes**
In the generated file, you can continue to add data in columns A and B, while the chart dynamically counts the latest 5 sets of data. This is done using the "OFFSET" formula in the sample code:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

You can try changing the number "-5" to "-10" in the formula, and the dynamic chart will count the latest 10 sets of data. Now we have created a dynamic rolling chart using Aspose.Cells successfully.
{{< app/cells/assistant language="cpp" >}}