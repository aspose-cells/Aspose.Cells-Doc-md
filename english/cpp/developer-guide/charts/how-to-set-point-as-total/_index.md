---
title: How to set point as total with C++
linktitle: How to set point as total
description: In some Excel charts, for example a Waterfall chart, you may need to set a point as total. This article describes how to use Aspose.Cells with C++ to do it.
keywords: Waterfall Chart, Point, Set as total.
type: docs
weight: 72
url: /cpp/how-to-set-point-as-total/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## What is "Set point as total" in Excel Chart

In some Excel charts, for example a Waterfall chart, some point data are the sum of the previous points, so you may need to set a point as total. We will show sample code and an illustration below.

## A Waterfall Chart needs to "Set point as total"

![todo:image_alt_text](set-as-total1.png)

This picture shows a Waterfall chart in Excel. We can see that there are four data points starting with "Total", and they are used to count all the previous data points.  
In this picture, the settings are not exactly right. When we select the point "Total 2024", we can see that the "Set as total" option is not checked in Excel.  
Attached below is the [sample Excel file](SampleSheet.xlsx) that needs to be modified, and we will use Aspose.Cells to set it up correctly.

## Use Aspose.Cells to "Set point as total"

We use the following code to set up the file correctly:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize file path
    U16String filePath(u"");

    // Load the workbook
    Workbook wb(filePath + u"SampleSheet.xlsx");

    // Get the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Get the chart by name
    Chart chart = worksheet.GetCharts().Get(u"Graphiq5");

    // Set some points as total column
    // In this example, we set points 0, 4, 8, 12 as total
    Vector<int32_t> subtotals = {0, 4, 8, 12};
    chart.GetNSeries().Get(0).GetLayoutProperties().SetSubtotals(subtotals);

    // Save the workbook
    wb.Save(filePath + u"output.xlsx");

    std::cout << "Chart subtotals set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

You can obtain the following correct [output file](output.xlsx).

As shown in the figure below, the four "Total" data points are set correctly, and you can see the difference from the previous chart.

![todo:image_alt_text](set-as-total2.png)
{{< app/cells/assistant language="cpp" >}}
