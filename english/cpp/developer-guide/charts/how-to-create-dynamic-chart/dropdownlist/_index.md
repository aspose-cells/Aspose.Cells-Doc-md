---
title: How to Create Dynamic Chart with Dropdownlist with C++
linktitle: Create Dynamic Chart with Dropdownlist
description: Learn how to create a dynamic chart that updates based on a drop-down list selection using Aspose.Cells for C++. Our step-by-step guide will demonstrate how to integrate a drop-down list into your chart for flexible data visualization.
keywords: Aspose.Cells for C++, Dynamic Chart, Drop-Down List, Data Visualization, Integration, Flexible Visualization.
type: docs
weight: 76
url: /cpp/create-dynamic-chart-with-dropdownlist/
---

## **Possible Usage Scenarios**
A Dynamic Chart with Dropdownlist in Excel is a powerful tool that allows users to create interactive charts that can dynamically update based on the selected data. This feature is particularly useful in situations where there is a need to analyze multiple datasets or compare various scenarios.

One common application of a Dynamic Chart with Dropdownlist is in financial analysis. For example, a company may have multiple sets of financial data for different years or departments. By using a dropdown list, users can select the specific dataset they want to analyze, and the chart will automatically update to display the corresponding information. This allows for easy comparison and identification of trends or patterns.

Another application is in sales and marketing. A company may have sales data for different products or regions. With a Dynamic Chart with Dropdownlist, users can choose a specific product or region from the dropdown list, and the chart will dynamically update to show the sales performance for the selected option. This helps in identifying the top-performing areas or products and making data-driven decisions.

In summary, a Dynamic Chart with Dropdownlist in Excel provides a flexible and interactive way to visualize and analyze data. It is valuable in situations where there is a need to compare multiple datasets or explore different scenarios, making it a versatile tool for financial analysis, sales and marketing, and many other applications.

## **Use Aspose Cells to Create Dynamic Chart with Dropdownlist**
In the next paragraphs, we will show you how to create a Dynamic Chart with Dropdownlist using Aspose.Cells. We'll show you the code for the example, as well as the Excel file created with this code.

## **Sample Code**
The following sample code will generate the [Dynamic Chart with Dropdownlist File](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Notes**
In the generated file, the chart will dynamically count the data for the selected month. This is done using the "OFFSET" formula in the sample code:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

You can try changing the dropdown list value in cell "Sheet1!$A$10", and you will see the dynamic change of the chart. Now we have created a dynamic chart with dropdownlist using Aspose.Cells successfully.