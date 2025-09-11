---
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range
description: Learn how to change the data source of a chart to a destination worksheet while copying rows or a range in Aspose.Cells for Python via .NET. Our guide will show you how to update the chart's data range and link it to the destination worksheet, ensuring that the copied rows or range are accurately reflected in the chart.
keywords: Aspose.Cells for Python via .NET, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /python-net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possible Usage Scenarios**

When you copy rows or range which contains charts to a new worksheet, then the data source of the chart does not change. For example, if the data source of chart is =Sheet1!$A$1:$B$4, then after copying rows or range to new worksheet, the data source will remain the same i.e =Sheet1!$A$1:$B$4. It still refers to old worksheet i.e. Sheet1. This is also the behavior in Microsoft Excel. But if you want that it to refer to the new destination worksheet, then please use the [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) property and set it to **true** while calling the [**Cells.copy_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/copy_rows) method. Now if your destination worksheet is DestSheet, then the data source of your chart will change from =Sheet1!$A$1:$B$4 to =DestSheet!$A$1:$B$4.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code explains the usage of [**CopyOptions.refer_to_destination_sheet**](https://reference.aspose.com/cells/python-net/aspose.cells/copyoptions/refer_to_destination_sheet) property while copying rows or range containing charts to a new worksheet. The code uses the [sample excel file](5113699.xlsx) and generates the [output excel file](5113697.xlsx).

![todo:image_alt_text](1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartDataSource-1.py" >}}
{{< app/cells/assistant language="python-net" >}}