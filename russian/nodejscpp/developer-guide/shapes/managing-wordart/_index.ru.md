---
title: Добавьте водяной знак WordArt на лист с помощью Node.js через C++
linktitle: Управление WordArt
type: docs
weight: 180
url: /ru/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Узнайте, как добавить WordArt в качестве фонового водяного знака на лист с помощью Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Используйте WordArt для добавления специальных текстовых эффектов в электронные таблицы. Например, растяните заголовок сверху файла, украсьте текст или сделайте его соответствующим предварительно заданной форме или примените текст к листу Excel в качестве фонового водяного знака. WordArt становится объектом, который можно перемещать или позиционировать на листе, добавляя украшения.

{{% /alert %}} 

Приведенный ниже пример показывает, как добавить форму WordArt, чтобы установить водяной знак на фон для листа.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();            

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
const lineFormat = wordart.getLine();          

const outputFilePath = path.join(dataDir, "Watermark_Test.out.xls");
// Save the file
workbook.save(outputFilePath);
```

## **Продвинутые темы**
- [Добавление словесного искусства текста с встроенными стилями](/cells/ru/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Блокировка водяного знака WordArt](/cells/ru/nodejs-cpp/locking-wordart-watermark/)
- [Установить предварительный стиль WordArt для текста формы](/cells/ru/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
