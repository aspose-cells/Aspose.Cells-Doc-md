---  
title: 仅复制范围数据使用Node.js via C++  
linktitle: 仅复制范围的数据  
type: docs  
weight: 600  
url: /zh/nodejs-cpp/copy-range-data-only/  
description: 学习如何使用Aspose.Cells for Node.js via C++将一个单元格区域的数据复制到另一个区域。  
---  

{{% alert color="primary" %}}  
有时，您需要将数据从一个单元格范围复制到另一个范围，仅复制数据，而不是格式。Aspose.Cells提供了这一功能。  

本文提供了一个使用Aspose.Cells复制数据范围的示例代码。  
{{% /alert %}}  

此示例演示如何：  

1. 创建一个工作簿。  
1. 在第一个工作表中的单元格中添加数据。  
1. 创建[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range)。  
1. 使用指定的格式属性创建一个 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象。  
1. 将样式格式应用于范围。  
1. 创建另一个单元格范围。  
1. 将第一个范围的数据复制到这个第二个范围。  

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

