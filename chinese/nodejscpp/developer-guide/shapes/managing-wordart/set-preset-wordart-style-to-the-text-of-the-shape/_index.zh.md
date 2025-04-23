---
title: 用 Node.js 和 C++ 设置形状文本的预设 WordArt 样式
linktitle: 将文本形状的文字设置为预设的WordArt样式
type: docs
weight: 280
url: /zh/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: 学习如何用 Aspose.Cells for Node.js via C++ 为形状的文本设置预设 WordArt 样式
---

## **可能的使用场景**
你可以用 Aspose.Cells for Node.js via C++ 为形状的文本设置预设 WordArt 样式。请使用 [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) 或 [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) 方法。

## **将文本形状的文字设置为预设的WordArt样式**
以下示例代码创建一个带有文本的文本框，并使用 [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) 方法设置其文本的预设 WordArt 样式。如下的 [输出Excel文件](5115445.xlsx) 在 Microsoft Excel 中的显示效果。

![todo:image_alt_text](set-preset-wordart-style-to-the-text-of-the-shape_1.png)

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create a textbox with some text
const textbox = worksheet.getShapes().addTextBox(0, 0, 0, 0, 100, 700);
textbox.setText("Aspose File Format APIs");
textbox.getFont().setSize(44);

// Sets preset WordArt style to the text of the shape.
const fntSetting = textbox.getRichFormattings()[0];
fntSetting.setWordArtStyle(AsposeCells.PresetWordArtStyle.WordArtStyle3);

// Save the workbook in xlsx format
workbook.save(outputDir + "outputSetPresetWordArtStyle.xlsx");
```
