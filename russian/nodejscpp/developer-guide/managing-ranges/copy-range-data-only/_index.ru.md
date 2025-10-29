---  
title: Копировать только данные диапазона с Node.js через C++  
linktitle: Копировать только данные диапазона  
type: docs  
weight: 600  
url: /ru/nodejs-cpp/copy-range-data-only/  
description: Узнайте, как копировать данные из одного диапазона ячеек в другой, используя Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, скопируя только данные, а не форматирование. Aspose.Cells предлагает эту функцию.  

Эта статья предоставляет пример кода, который использует Aspose.Cells для копирования диапазона данных.  
{{% /alert %}}  

Этот пример показывает, как:  

1. Создать книгу.  
1. Добавить данные в ячейки на первом листе.  
1. Создайте [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
1. Создайте объект [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) с указанными атрибутами форматирования.  
1. Применить форматирование стиля к диапазону.  
1. Создайте другой диапазон ячеек.  
1. Скопируйте данные из первого диапазона во второй диапазон.  

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
