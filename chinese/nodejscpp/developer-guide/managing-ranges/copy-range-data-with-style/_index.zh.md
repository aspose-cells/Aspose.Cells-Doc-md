---  
title: 使用Node.js via C++复制带样式的范围数据  
linktitle: 仅复制范围数据和样式  
type: docs  
weight: 610  
url: /zh/nodejs-cpp/copy-range-data-with-style/  
description: 学习如何使用Aspose.Cells for Node.js via C++复制具有格式的单元格范围。  
---  

{{% alert color="primary" %}}  

[仅复制范围数据](/cells/zh/nodejs-cpp/copy-range-data-only/) 讲解了如何将单元格范围内的数据复制到另一区域，具体内容是对复制的单元格应用新样式。Aspose.Cells 也可以完整复制带格式的范围。本文将详细说明。  

{{% /alert %}}  

Aspose.Cells 提供了一套用于操作范围的类和方法，例如 [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) 和 [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-)。  

此示例：  

1. 创建一个工作簿。  
2. 在第一个工作表中填充多个单元格数据。  
3. 创建一个 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/)。  
4. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) 对象。  
5. 将样式应用到数据范围。  
6. 创建第二个单元格范围。  
7. 将第一个范围的带格式数据复制到第二个范围。  

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

