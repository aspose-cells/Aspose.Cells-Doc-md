---
title: 仅复制范围样式使用Node.js via C++
linktitle: 仅复制范围样式
type: docs
weight: 620
url: /zh/nodejs-cpp/copy-range-style-only/
description: 学习如何在Aspose.Cells for Node.js via C++中在操作数据的同时只复制范围的样式。 
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/nodejs-cpp/copy-range-data-only/) 和 [复制范围数据与样式](/cells/zh/nodejs-cpp/copy-range-data-with-style/) 讲述了如何只复制范围到另一个范围，或者连同格式全部复制。也可以只复制格式。本文将详细介绍。

{{% /alert %}} 

此示例创建一个工作簿，填充数据并仅复制范围的样式。

1. 创建一个范围。
1. 创建一个带有指定格式属性的 `Style` 对象。
1. 将样式格式应用于范围。
1. 创建第二个单元格范围。
1. 将第一个范围的格式复制到第二个范围。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++)
{
for (let j = 0; j < 10; j++) 
{
cells.get(i, j).putValue(i.toString() + "," + j.toString());
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
const top = style.getBorders().get(AsposeCells.BorderType.TopBorder);
top.setLineStyle(AsposeCells.CellBorderType.Thin);
top.setColor(AsposeCells.Color.Blue);

const bottom = style.getBorders().get(AsposeCells.BorderType.BottomBorder);
bottom.setLineStyle(AsposeCells.CellBorderType.Thin);
bottom.setColor(AsposeCells.Color.Blue);

const left = style.getBorders().get(AsposeCells.BorderType.LeftBorder);
left.setLineStyle(AsposeCells.CellBorderType.Thin);
left.setColor(AsposeCells.Color.Blue);

const right = style.getBorders().get(AsposeCells.BorderType.RightBorder);
right.setLineStyle(AsposeCells.CellBorderType.Thin);
right.setColor(AsposeCells.Color.Blue);


// Create the styleflag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:E13).
const range2 = cells.createRange("C10", "E13");

// Copy the range style only.
range2.copyStyle(range);

const outputFilePath = path.join(dataDir, "copyrangestyle.out.xls");
// Save the excel file.
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
