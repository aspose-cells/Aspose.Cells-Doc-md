---  
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range with Golang via C++  
description: Learn how to change the data source of a chart to a destination worksheet while copying rows or a range in Aspose.Cells for C++. Our guide will show you how to update the chart's data range and link it to the destination worksheet, ensuring that the copied rows or range are accurately reflected in the chart.  
keywords: Aspose.Cells for C++, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.  
type: docs  
weight: 440  
url: /go-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **Possible Usage Scenarios**

When you copy rows or a range that contains charts to a new worksheet, the data source of the chart does not change. For example, if the data source of the chart is `=Sheet1!$A$1:$B$4`, then after copying rows or a range to a new worksheet, the data source will remain the same, i.e., `=Sheet1!$A$1:$B$4`. It still refers to the old worksheet, i.e., Sheet1. This is also the behavior in Microsoft Excel. But if you want it to refer to the new destination worksheet, use the [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) property and set it to **true** while calling the [**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/) method. Now, if your destination worksheet is **DestSheet**, the data source of your chart will change from `=Sheet1!$A$1:$B$4` to `=DestSheet!$A$1:$B$4`.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code explains the usage of the [**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/go-cpp/copyoptions/getrefertodestinationsheet/) property while copying rows or a range containing charts to a new worksheet. The code uses the [sample Excel file](5113699.xlsx) and generates the [output Excel file](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangeDataSourceOfTheChartToDestinationWorksheetWhileCopyingRowsOrRange.go" >}}