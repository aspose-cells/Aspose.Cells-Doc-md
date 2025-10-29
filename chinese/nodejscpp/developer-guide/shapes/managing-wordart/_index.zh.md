---
title: 用Node.js通过C++在工作表中添加WordArt水印
linktitle: 管理文字艺术
type: docs
weight: 180
url: /zh/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: 学习如何使用Aspose.Cells for Node.js via C++向工作表添加WordArt作为背景水印。
---

{{% alert color="primary" %}} 

使用WordArt为电子表格添加特殊文本效果，例如，将标题横跨文件顶部，装饰文本，并使文本适应预设形状，或将文本应用于Excel工作表作为背景水印。 WordArt成为您可以在电子表格中移动或定位以添加装饰的对象。

{{% /alert %}} 

以下示例显示如何添加文字艺术形状以设置工作表的背景水印。

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

## **高级主题**
- [添加具有内置样式的艺术字文本](/cells/zh/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [锁定WordArt水印](/cells/zh/nodejs-cpp/locking-wordart-watermark/)
- [将文本形状的文字设置为预设的WordArt样式](/cells/zh/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}
