---  
title: Node.jsとC++を使用してスタイル付きの範囲のコピー  
linktitle: スタイル付きの範囲のデータをコピーします。  
type: docs  
weight: 610  
url: /ja/nodejs-cpp/copy-range-data-with-style/  
description: Aspose.Cells for Node.js via C++を使用して書式設定とともにセル範囲をコピーする方法を学びます。  
---  

{{% alert color="primary" %}}  

[範囲のデータのみをコピー](/cells/ja/nodejs-cpp/copy-range-data-only/)は、セル範囲から別の範囲へのデータのコピー方法を説明します。特に、新しいスタイルセットをコピーされたセルに適用します。Aspose.Cellsは、書式設定を含む範囲全体のコピーも可能です。この記事ではその方法を解説します。  

{{% /alert %}}  

Aspose.Cellsは、範囲の操作に関するさまざまなクラスとメソッドを提供します。例：[**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-)、[**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/)、[**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-)。  

この例:  

1. ワークブックを作成します。  
2. 最初のシートの複数のセルにデータを入力します。  
3. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/)を作成します。  
4. 指定された書式属性を持つ[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/)オブジェクトを作成します。  
5. データ範囲にスタイルを適用します。  
6. 2つ目のセル範囲を作成します。  
7. 最初の範囲から2番目の範囲にデータと書式設定をコピーします。  

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
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
let style = workbook.createStyle();
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

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data with formatting.
range2.copy(range);

const outputFilePath = path.join(dataDir, "CopyRange.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
