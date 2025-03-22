---
title: Read and Manipulate Excel 2016 Charts with C++
linktitle: Read and Manipulate Excel 2016 Charts
description: Learn how to read and manipulate Excel 2016 charts using Aspose.Cells for C++. Our guide will show you how to access and modify various chart properties, including data labels, series colors, and layout.
keywords: Aspose.Cells for C++, Excel 2016 charts, read, manipulate, data labels, series colors, layout, hierarchical charting, circular charting.
type: docs
weight: 48
url: /cpp/read-and-manipulate-excel-2016-charts/
---

## **Possible Usage Scenarios**
Aspose.Cells now supports the reading and manipulation of Microsoft Excel 2016 charts which are not present in Microsoft Excel 2013 or earlier versions.

## **Read and Manipulate Excel 2016 Charts**
The following sample code loads the [source excel file](22774101.xlsx) which contains Excel 2016 charts in the first worksheet. It reads all charts one by one and changes its title as per its chart type. The following screenshot shows the source excel file before the execution of code. As you can see, the chart title is the same for all charts.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

The following screenshot shows the [output excel file](22774104.xlsx) after the execution of code. As you can see, the chart title is changed as per its chart type.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)

## **Sample Code**
```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"excel2016Charts.xlsx");

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    for (int i = 0; i < sheet.GetCharts().GetCount(); ++i)
    {
        Chart chart = sheet.GetCharts().Get(i);
        ChartType chartType = chart.GetType();
        chart.GetTitle().SetText(U16String(u"Chart Type is ") + U16String(std::to_string(static_cast<int>(chartType)).c_str()));
    }

    workbook.Save(outDir + u"out_excel2016Charts.xlsx");

    std::cout << "Charts processed successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**
Here is the console output of the above sample code when executed with the provided [source excel file](22774101.xlsx).

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}

## **Advance Topics**
- [Creating Waterfall Chart](/cells/cpp/creating-waterfall-chart/)
- [Creating TreeMap Chart](/cells/cpp/creating-treemap-chart/)
- [Creating Sunburst Chart](/cells/cpp/creating-sunburst-chart/)