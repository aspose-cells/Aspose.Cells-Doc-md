---
title: 用 Node.js via C++ 插入折线图
linktitle: 迷你图
type: docs
weight: 160
url: /zh/nodejs-cpp/creating-sparklines/
description: 使用Aspose.Cells for Node.js via C++为Excel创建迷你图。
---

## **插入火花线**
{{% alert color="primary" %}} 

折线图是在工作表单元格中的一个微型图表，提供数据的直观表现。使用折线图可以显示一系列值的趋势，如季节性变动、经济周期，或突出最大最小值。为了达到最大效果，建议将折线图放在数据附近。折线图有三种类型：线型、柱状和堆叠。

{{% /alert %}} 

使用Aspose.Cells for Node.js via C++创建迷你图非常简单，示例代码如下：



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **高级主题**
- [使用迷你图和设置3D格式](/cells/zh/nodejs-cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
