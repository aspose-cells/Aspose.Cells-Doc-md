---
title: How to set Series invisible with C++
linktitle: How to set Series invisible
description: In Excel chart, you may need to set series invisible. This article describes how to use Aspose.Cells with C++ to do it.
keywords: Excel chart, Series, Invisible, IsFiltered.
type: docs
weight: 74
url: /cpp/how-to-set-series-invisible/
---

## How to set series invisible in Excel Chart

In Excel chart, you can right-click a chart, click "Select Data", and in the pop-up window, you can set whether a series is visible by checking or unchecking it. You can download the following [sample file](SeriesFiltered.xlsx) and operate it in Excel as shown in the figure to achieve this function. Next, we will tell you how to achieve this using the Aspose.Cells library.

![todo:image_alt_text](series-invisible.png)

## How to set series invisible using Aspose.Cells 

We use the following code to set series invisible using Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");
    
    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

You can get the following [Input file](SeriesFiltered.xlsx) and [output file](output.xlsx).

As shown in the figure below, the first two series which were originally visible, have become invisible in the output file.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}