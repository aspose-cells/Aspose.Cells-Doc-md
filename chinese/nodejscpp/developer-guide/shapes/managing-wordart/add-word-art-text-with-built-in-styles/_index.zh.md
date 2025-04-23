---
title: 使用 Node.js 和 C++ 添加带有内置样式的 Word Art 文字
linktitle: 添加具有内置样式的艺术字文本
type: docs
weight: 270
url: /zh/nodejs-cpp/add-word-art-text-with-built-in-styles/
description: 学习如何用 Aspose.Cells for Node.js via C++ 添加带有内置样式的 Word Art 文字。在Excel中使用内置样式创建具有视觉吸引力的文本。
---

## **可能的使用场景**
你可以用 Aspose.Cells for Node.js via C++ 添加带有内置样式的 Word Art 文字。请使用 [ShapeCollection.addWordArt()](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addWordArt-presetwordartstyle-string-number-number-number-number-number-number-) 方法实现。

## **添加具有内置样式的艺术字文本**
以下示例代码使用不同的内置样式添加Word Art文本。请使用[code]output excel file[/code]检查使用此代码生成的[输出excel文件](5115470.xlsx)。这是[输出excel文件](5115470.xlsx)在Microsoft Excel中的外观。

![todo:image_alt_text](add-word-art-text-with-built-in-styles_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add Word Art Text with Built-in Styles
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle1, "Aspose File Format APIs", 0, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle2, "Aspose File Format APIs", 10, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle3, "Aspose File Format APIs", 20, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle4, "Aspose File Format APIs", 30, 0, 0, 0, 100, 800);
ws.getShapes().addWordArt(AsposeCells.PresetWordArtStyle.WordArtStyle5, "Aspose File Format APIs", 40, 0, 0, 0, 100, 800);

// Save the workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
