---
title: 通过C++在复制行或范围时将图表的数据源更改为目标工作表（Destination Worksheet）——适用于Aspose.Cells for Node.js via C++
linktitle: 在复制行或范围时将图表的数据源更改为目标工作表
description: 了解如何在Aspose.Cells for Node.js via C++中在复制行或区域的同时将图表的数据源更改为目标工作表。本指南演示了如何更新图表的数据范围并将其链接到目标工作表。
keywords: Aspose.Cells for Node.js via C++、图表、数据源、目标工作表、行、区域、复制、更新、数据范围、链接。
type: docs
weight: 440
url: /zh/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能的使用场景**

当你将包含图表的行或区域复制到新工作表时，图表的数据源不会变化。例如，如果图表的数据源是 `=Sheet1!$A$1:$B$4`，那么在复制到新工作表后，数据源仍然是相同的，即`=Sheet1!$A$1:$B$4`，仍指向旧工作表（即Sheet1）。这也是Microsoft Excel中的行为。但如果你希望它指向新的目标工作表，请在调用[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)方法时使用[**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)属性并设置为**true**。假设目标工作表为DestSheet，则你的图表数据源将从`=Sheet1!$A$1:$B$4`变为`=DestSheet!$A$1:$B$4`。

## **复制行或区域时更改图表的数据源到目标工作表**

以下示例代码解释了在复制包含图表的行或区域到新工作表时使用[**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)属性的方法。代码使用示例Excel文件（5113699.xlsx），并生成输出Excel文件（5113697.xlsx）。

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
{{< app/cells/assistant language="nodejs-cpp" >}}
