---
title: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range with Node.js via C++
linktitle: Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range
description: Learn how to change the data source of a chart to a destination worksheet while copying rows or a range in Aspose.Cells for Node.js via C++. This guide demonstrates how to update the chart's data range and link it to the destination worksheet.
keywords: Aspose.Cells for Node.js via C++, charting, data source, destination worksheet, rows, range, copy, update, data range, linkage.
type: docs
weight: 440
url: /nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **Possible Usage Scenarios**

When you copy rows or range which contains charts to a new worksheet, then the data source of the chart does not change. For example, if the data source of the chart is `=Sheet1!$A$1:$B$4`, then after copying rows or range to a new worksheet, the data source will remain the same i.e., `=Sheet1!$A$1:$B$4`. It still refers to the old worksheet i.e., Sheet1. This is also the behavior in Microsoft Excel. But if you want it to refer to the new destination worksheet, then please use the [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#refertodestinationsheet-boolean) property and set it to **true** while calling the [**Cells.copyRows()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyrows-number-number-number-) method. Now if your destination worksheet is DestSheet, then the data source of your chart will change from `=Sheet1!$A$1:$B$4` to `=DestSheet!$A$1:$B$4`.

## **Change Data Source of the Chart to Destination Worksheet while Copying Rows or Range**

The following sample code explains the usage of [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#refertodestinationsheet-boolean) property while copying rows or range containing charts to a new worksheet. The code uses the [sample excel file](5113699.xlsx) and generates the [output excel file](5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
