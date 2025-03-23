---  
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range with C++  
description: Learn how to change the data source of a chart to a destination worksheet while copying rows or a range in Aspose.Cells for C++. Our guide will show you how to update the chart's data range and link it to the destination worksheet, ensuring that the copied rows or range are accurately reflected in the chart.  
keywords: Aspose.Cells for C++, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.  
type: docs  
weight: 440  
url: /cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Possible Usage Scenarios**

When you copy rows or range which contains charts to a new worksheet, then the data source of the chart does not change. For example, if the data source of the chart is =Sheet1!$A$1:$B$4, then after copying rows or range to a new worksheet, the data source will remain the same i.e., =Sheet1!$A$1:$B$4. It still refers to the old worksheet i.e., Sheet1. This is also the behavior in Microsoft Excel. But if you want it to refer to the new destination worksheet, then please use the [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) property and set it to **true** while calling the [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) method. Now if your destination worksheet is DestSheet, then the data source of your chart will change from =Sheet1!$A$1:$B$4 to =DestSheet!$A$1:$B$4.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code explains the usage of [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/) property while copying rows or range containing charts to a new worksheet. The code uses the [sample excel file](5113699.xlsx) and generates the [output excel file](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
