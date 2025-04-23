---
title: Преобразование текста с фигурой внутри листа с помощью Node.js через C++
linktitle: Повернуть текст с фигурой внутри таблицы
type: docs
weight: 1300
url: /ru/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Узнайте, как вращать текст с фигурой внутри листа Excel, используя Aspose.Cells for Node.js via C++.
---

## **Возможные сценарии использования**

Вы можете добавлять текст внутри любой фигуры, используя Microsoft Excel. Если вы добавите фигуру с помощью очень старой версии Microsoft Excel 2003, текст не будет вращаться вместе с фигурой. Но если вы добавите фигуру с помощью более новых версий Microsoft Excel, например 2007, 2010, 2013 или 2016, текст будет вращаться вместе с фигурой. Вы можете управлять, вращается ли текст вместе с фигурой или нет, используя свойство [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--). Значение по умолчанию — **true**, что означает, что текст будет вращаться с фигурой, но если установить его как **false**, текст вращаться не будет.

## **Повернуть текст с фигурой внутри таблицы**

Следующий примерный код загружает [образец файла Excel](64716896.xlsx), в котором есть треугольная фигура, и его текст вращается вместе с фигурой. Если открыть этот файл в Microsoft Excel и повернуть треугольную фигуру, текст также повернется. Затем код устанавливает свойство [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) как **false** и сохраняет файл как [выходной файл Excel](64716897.xlsx). Если открыть выходной файл в Microsoft Excel и повернуть треугольник, текст не будет вращаться вместе с ним. Ознакомьтесь со скриншотом ниже, показывающим эффект работы кода на примере файла.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
