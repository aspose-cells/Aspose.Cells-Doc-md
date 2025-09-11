---
title: Add WordArt Watermark to Worksheet with Node.js via C++
linktitle: Managing WordArt
type: docs
weight: 180
url: /nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Learn how to add WordArt as a background watermark to a worksheet using Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Use WordArt to add special text effects to spreadsheets. For example, stretch a title across the top of the file, decorate text, and make text fit a preset shape, or apply text to an Excel sheet as a background watermark. The WordArt becomes an object that you can move or position in spreadsheets to add decoration.

{{% /alert %}} 

The following example shows how to add a WordArt shape to set a background watermark for a worksheet.

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

## **Advance topics**
- [Add Word Art Text with Built-in Styles](/cells/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Locking WordArt Watermark](/cells/nodejs-cpp/locking-wordart-watermark/)
- [Set preset WordArt style to the text of the shape](/cells/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}