---
title: 用Node.js通过C++设置图表系列的数值格式代码
description: 了解如何在Aspose.Cells for Node.js via C++中设置图表系列的数值格式代码。本指南将帮助您理解如何使用适当的格式代码格式化图表系列数据，从而专业、准确地展示您的数据。
keywords: Aspose.Cells for Node.js，图表系列，数值格式代码，格式化，数据显示，准确性，专业性。
linktitle: 数字格式
type: docs
weight: 100
url: /zh/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **可能的使用场景**
你可以使用[Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--)属性设置图表系列的数值格式代码。此属性不仅适用于基于工作表范围的系列，也适用于使用值数组创建的系列。

## **设置图表系列的值格式代码**
以下示例代码在空的无系列图表中添加一个系列，使用数组值添加系列。添加后，使用[Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--)属性将其格式化为$#,##0，数字10000变成$10,000。截图显示执行后对示例Excel文件（51740712.xlsx）和输出Excel文件（51740713.xlsx）的效果。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **示例代码**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
