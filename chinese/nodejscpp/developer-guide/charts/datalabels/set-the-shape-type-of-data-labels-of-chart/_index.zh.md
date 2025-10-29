---
title: 用 Node.js via C++ 设置图表数据标签的形状类型
linktitle: 设置图表数据标签的形状类型
description: 学习如何使用 Aspose.Cells for Node.js via C++ 设置图表中数据标签的形状类型。此指南将介绍不同的形状类型以及如何选择合适的形状以增强展示效果和实用性。
keywords: Aspose.Cells for Node.js via C++，制图，数据标签，形状类型，展示，实用性。
type: docs
weight: 110
url: /zh/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **可能的使用场景**
您可以使用 `DataLabels.shapeType` 属性更改图表中的数据标签的形状类型。它采用 `DataLabelShapeType` 枚举值，并相应地更改数据标签的形状类型。部分值包括

{{< highlight javascript >}}
 DataLabelShapeType.BentLineCallout
DataLabelShapeType.DownArrowCallout
DataLabelShapeType.Ellipse
DataLabelShapeType.LineCallout
DataLabelShapeType.Rect
etc.
{{< /highlight >}}

## **设置图表数据标签的形状类型**
以下示例代码将图表数据标签的形状类型更改为`DataLabelShapeType.WedgeEllipseCallout`。请参阅此代码使用的[示例Excel文件](60489778.xlsx)和由其生成的[输出Excel文件](60489779.xlsx)。截屏展示了代码在示例Excel文件上的效果。

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **示例代码**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Access first series
const series = chart.getNSeries().get(0);

// Set the shape type of data labels i.e. Speech Bubble Oval
series.getDataLabels().setShapeType(AsposeCells.DataLabelShapeType.WedgeEllipseCallout);

// Save the output Excel file
workbook.save(path.join(dataDir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
