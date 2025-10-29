---  
title: Копировать диапазон данных со стилями с помощью Node.js через C++  
linktitle: Копировать данные диапазона со стилем  
type: docs  
weight: 610  
url: /ru/nodejs-cpp/copy-range-data-with-style/  
description: Узнайте, как копировать диапазон ячеек с форматированием, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[Копировать только данные диапазона](/cells/ru/nodejs-cpp/copy-range-data-only/) объясняет, как копировать данные из диапазона ячеек в другой диапазон. В частности, он применяет новый набор стилей к скопированным ячейкам. Aspose.Cells также может копировать диапазон полностью с форматированием. В этой статье объясняется, как это сделать.  

{{% /alert %}}  

Aspose.Cells предоставляет набор классов и методов для работы с диапазонами, например, [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) и [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Этот пример:  

1. Создает рабочую книгу.  
2. Заполняет данные нескольких ячеек первого листа.  
3. Создает [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Создает объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) с указанными атрибутами форматирования.  
5. Применяет стиль к диапазону данных.  
6. Создает второй диапазон ячеек.  
7. Копирует данные с форматированием из первого диапазона во второй.  

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
