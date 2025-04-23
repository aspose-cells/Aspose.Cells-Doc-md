---
title: Отправить фигуру вперед или назад внутри листа с помощью Node.js через C++
linktitle: Отправить форму вперед или назад внутри листа
type: docs
weight: 3400
url: /ru/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Узнайте, как отправить фигуру на передний или задний план в листе с помощью Aspose.Cells for Node.js via C++. 
---

## **Возможные сценарии использования**

Когда на одном месте расположено несколько фигур, их видимость определяется по их z-порядку. Aspose.Cells предоставляет метод [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-), который изменяет z-положение фигуры. Чтобы отправить фигуру на задний план, используйте отрицательное число, например -1, -2, -3, ..., а чтобы поднять фигуру на передний план — положительное число, например 1, 2, 3, ...

## **Отправить форму вперед или назад внутри листа**

Следующий пример кода объясняет использование метода [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). Посмотрите [пример файла Excel](50528330.xlsx), использованный внутри кода, и [выходной файл Excel](50528331.xlsx), созданный им. Скриншот показывает эффект работы кода на образце Excel после выполнения.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Образец кода**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
