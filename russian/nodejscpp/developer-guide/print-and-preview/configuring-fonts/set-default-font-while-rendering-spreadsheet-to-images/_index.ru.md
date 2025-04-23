---
title: Установить шрифт по умолчанию при рендеринге электронной таблицы в изображение с помощью Node.js через C++
linktitle: Установить шрифт по умолчанию при преобразовании электронной таблицы в изображения
type: docs
weight: 360
url: /ru/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Узнайте, как установить шрифт по умолчанию при рендеринге таблиц в изображения с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Используйте свойство [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), чтобы установить шрифт по умолчанию при рендеринге электронных таблиц в изображения. Это свойство будет действительным только в том случае, если шрифт по умолчанию книги не может отобразить ваши символы. Шрифт по умолчанию, указанный с помощью свойства [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), используется для всех тех ячеек, которые имеют недопустимые или отсутствующие шрифты.

{{% /alert %}}

## Установка шрифта по умолчанию при рендеринге электронных таблиц в изображения

Следующий пример кода создает рабочую книгу, добавляет текст в ячейку A4 первого листа и устанавливает шрифт на недопустимый или несуществующий. Затем он создает два изображения этого листа. Первое изображение сделано, установив свойство [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в *Courier New*, второе — установив свойство [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в *Times New Roman*.

Это изображение после установки свойства [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Это изображение после установки свойства [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) в *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Образец кода

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
