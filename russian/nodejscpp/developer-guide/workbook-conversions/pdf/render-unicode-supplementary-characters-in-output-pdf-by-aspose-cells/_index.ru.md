---
title: Отрисовывайте дополненные юникодные дополнительные символы в выходном PDF с помощью Aspose.Cells for Node.js via C++.
linktitle: Отображайте дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells
type: docs
weight: 350
url: /ru/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Узнайте, как отображать дополненные юникодные символы в выходном PDF с помощью Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells теперь поддерживает отображение этих дополнительных символов Юникода длиной 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}}

## Отрисовка дополненных юникодных символов в выходном PDF с помощью Aspose.Cells for Node.js via C++

Следующий скриншот показывает, как Aspose.Cells преобразовал [исходный excel-файл](5115563.xlsx) в [выходной PDF](5115564.pdf). Как видите, все три дополненных юникодных символа были отображены точно так же, как в Microsoft Excel.

![todo:image_alt_text](output.png)

## Образец кода

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5115563.xlsx) в [выходной PDF](5115564.pdf).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file containing Unicode Supplementary characters
const workbook = new AsposeCells.Workbook(path.join(dataDir, "unicode-supplementary-characters.xlsx"));

// Save the workbook
workbook.save(path.join(dataDir, "RenderUnicodeInOutput_out.pdf"));
```
