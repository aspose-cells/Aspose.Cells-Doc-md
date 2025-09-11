---
title: How to manage PivotChart with PivotOptions in C++
linktitle: Pivot Options
type: docs
weight: 10
url: /cpp/how-to-manage-pivotchart-with-pivotoptions/
description: How to manage PivotChart with PivotOptions using C++.
keywords: PivotChart
---

## What is PivotChart

A PivotChart in Excel is a graphical representation of data created from a PivotTable. It allows users to visualize and analyze data dynamically by summarizing and displaying information in chart form. PivotCharts are interactive and can be easily modified to show different perspectives of the data, making it a powerful tool for data analysis and presentation in Excel.

## How to manage PivotChart with PivotOptions

By using Aspose.Cells, you can use [**PivotOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/pivotoptions/) to manage PivotChart.

Sample file and code:  
[Sample File](Sample.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path for the sample Excel file
    U16String path = u"..\\Data\\01_SourceDirectory\\";
    
    // Create a Workbook object from the sample file
    Workbook book(path + u"Sample.xlsx");
    
    // Get the first chart from the first worksheet
    Chart chart = book.GetWorksheets().Get(0).GetCharts().Get(0);
    
    // Get the PivotOptions from the chart
    PivotOptions opt = chart.GetPivotOptions();
    
    // Hide ZoneFilter in PivotChart
    opt.SetDropZoneFilter(false); // HideZoneFilter

    // You can set more properties, try them!
    // opt.SetDropZoneCategories(false);  // HideZoneCategories
    // opt.SetDropZoneData(false);        // HideZoneData
    // opt.SetDropZoneSeries(false);      // HideZoneSeries
    // opt.SetDropZonesVisible(false);    // Hide All

    // Save the modified file to see the effect
    book.Save(path + u"HideZoneFilter.xlsx");

    std::cout << "Pivot chart updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

With the example code above, you can check the result file with the following effect, as shown in the figure:

**![Output](Output.png)**
{{< app/cells/assistant language="cpp" >}}