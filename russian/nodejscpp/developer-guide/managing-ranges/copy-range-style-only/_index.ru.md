---
title: Копировать только стиль диапазона с Node.js через C++
linktitle: Копировать только стиль диапазона
type: docs
weight: 620
url: /ru/nodejs-cpp/copy-range-style-only/
description: Узнайте, как копировать только стиль диапазона при работе с данными в Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

[Копировать только данные диапазона](/cells/ru/nodejs-cpp/copy-range-data-only/) и [Копировать диапазон данных с стилем](/cells/ru/nodejs-cpp/copy-range-data-with-style/) объясняют, как копировать данные из диапазона в другой как отдельно, так и полностью с форматированием. Также возможно копировать только форматирование. В этой статье показано, как.

{{% /alert %}} 

Этот пример создает рабочую книгу, заполняет ее данными и копирует только стиль диапазона.

1. Создать диапазон.
1. Создайте объект `Style` с заданными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создать второй диапазон ячеек.
1. Скопируйте формат первого диапазона во второй диапазон.

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
