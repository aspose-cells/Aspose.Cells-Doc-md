---
title: Node.jsとC++を使用した範囲のスタイルのみコピー
linktitle: スタイルのみをコピーします。
type: docs
weight: 620
url: /ja/nodejs-cpp/copy-range-style-only/
description: Aspose.Cells for Node.js via C++を使ったデータ操作中に範囲のスタイルのみコピーする方法を学びます。 
---

{{% alert color="primary" %}}

[範囲のデータのみをコピー](/cells/ja/nodejs-cpp/copy-range-data-only/)と[スタイル付きでコピー](/cells/ja/nodejs-cpp/copy-range-data-with-style/)は、範囲から別の範囲へのデータまたは書式付きのコピー方法を解説します。書式だけをコピーすることも可能です。この記事はその方法を示します。

{{% /alert %}} 

この例では、ワークブックを作成し、データで埋め、範囲のスタイルのみをコピーします。

1. 範囲を作成します。
1. 指定された書式属性を持つ`Style`オブジェクトを作成します。
1. 範囲にスタイルを適用します。
1. 別のセルの範囲を作成します。
最初の範囲の書式を2番目の範囲にコピーします。

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
