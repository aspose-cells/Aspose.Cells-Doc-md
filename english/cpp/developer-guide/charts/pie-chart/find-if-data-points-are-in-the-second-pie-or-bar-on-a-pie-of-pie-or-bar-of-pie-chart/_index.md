---
title: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart with C++
linktitle: Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart
description: Learn how to use Aspose.Cells for C++ to find if data points are in the second pie or bar on a pie of pie or bar of pie chart. Our guide will demonstrate how to identify and access the secondary pie or bar on a composite chart, allowing you to analyze and manipulate the data effectively.
keywords: Aspose.Cells for C++, Pie of Pie Chart, Bar of Pie Chart, Secondary Pie, Secondary Bar, Data Analysis, Data Manipulation.
type: docs
weight: 180
url: /cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/
---

## **Possible Usage Scenarios**
You can find if data points of series are in the second pie on *Pie of Pie* chart or in the bar of *Bar of Pie* chart using Aspose.Cells. Please use the [ChartPoint.IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) property to determine it.

Please download the [sample excel file](5115193.xlsx) used in the following sample code and see its console output. If you open the [sample excel file](5115193.xlsx), you will find, all the data points which are less than 10 are inside the bar of *Bar of Pie* chart as also shown by console output.

## **Find if Data Points are in the Second Pie or Bar on a Pie of Pie or Bar of Pie Chart**
The following sample code shows how to find if data points are in the second pie or bar on a *Pie of Pie* or *Bar of Pie* chart.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + u"PieBars.xlsx";
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Chart chart = worksheet.GetCharts().Get(0);
    chart.Calculate();

    Series series = chart.GetNSeries().Get(0);

    int pointCount = series.GetPoints().GetCount();
    for (int i = 0; i < pointCount; ++i)
    {
        ChartPoint chartPoint = series.GetPoints().Get(i);

        if (chartPoint.Get_YValue().IsNull())
            continue;

        std::cout << "Value: " << chartPoint.Get_YValue().ToDouble() << std::endl;
        std::cout << "IsInSecondaryPlot: " << (chartPoint.IsInSecondaryPlot() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**
Please see the following console output generated after the execution of the above sample code with the [sample excel file](5115193.xlsx). If [IsInSecondaryPlot](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/isinsecondaryplot/) is **false**, the data point is inside the Pie or if it is **true**, then the data point is inside the Bar.

{{< highlight java >}}

 Value: 15

IsInSecondaryPlot: False

Value: 9

IsInSecondaryPlot: True

Value: 2

IsInSecondaryPlot: True

Value: 40

IsInSecondaryPlot: False

Value: 5

IsInSecondaryPlot: True

Value: 4

IsInSecondaryPlot: True

Value: 25

IsInSecondaryPlot: False

{{< /highlight >}}