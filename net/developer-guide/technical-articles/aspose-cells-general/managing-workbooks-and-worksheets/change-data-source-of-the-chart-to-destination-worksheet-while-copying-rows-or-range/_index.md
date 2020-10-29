---
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range
type: docs
weight: 440
url: /net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possible Usage Scenarios**

When you copy rows or range which contains charts to a new worksheet, then the data source of the chart does not change. For example, if the data source of chart is =Sheet1!$A$1:$B$4, then after copying rows or range to new worksheet, the data source will remain the same i.e =Sheet1!$A$1:$B$4. It still refers to old worksheet i.e. Sheet1. This is also the behavior in Microsoft Excel. But if you want that it to refer to the new destination worksheet, then please use the [**CopyOptions.ReferToDestinationSheet**](https://apireference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) property and set it to **true** while calling the [**Cells.CopyRows()**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/copyrows/index) method. Now if your destination worksheet is DestSheet, then the data source of your chart will change from =Sheet1!$A$1:$B$4 to =DestSheet!$A$1:$B$4.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code explains the usage of [**CopyOptions.ReferToDestinationSheet**](https://apireference.aspose.com/cells/net/aspose.cells/copyoptions/properties/refertodestinationsheet) property while copying rows or range containing charts to a new worksheet. The code uses the [sample excel file](attachments/5013542/5113699.xlsx) and generates the [output excel file](attachments/5013542/5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ChangeChartDataSource-1.cs" >}}
