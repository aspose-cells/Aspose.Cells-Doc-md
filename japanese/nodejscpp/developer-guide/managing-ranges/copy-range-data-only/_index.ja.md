---  
title: Node.jsとC++を使用して範囲のデータのみをコピー  
linktitle: 範囲のデータのみをコピーします。  
type: docs  
weight: 600  
url: /ja/nodejs-cpp/copy-range-data-only/  
description: Aspose.Cells for Node.js via C++を使用してセルの範囲から別の範囲へのデータのコピー方法を学びます。  
---  

{{% alert color="primary" %}}  
時には、セルの範囲からデータを別の範囲にコピーする必要があります。しかし、書式ではなくデータのみが必要なことがあります。Aspose.Cellsではこの機能が提供されます。  

この記事では、Aspose.Cellsを使用してデータの範囲をコピーするサンプルコードを提供します。  
{{% /alert %}}  

この例では、次のことができます:  

1. ワークブックを作成する。  
1. 最初のワークシートのセルにデータを追加する。  
1. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)を作成します。  
1. 指定した書式属性で[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)を作成します。  
1. 範囲にスタイルを適用します。  
1. 別のセルの範囲を作成します。  
1. 最初の範囲のデータを2番目の範囲にコピーします。  

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
for (let i = 0; i < 50; i++) {
for (let j = 0; j < 10; j++) {
cells.get(i, j).putValue(`${i},${j}`);
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
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
