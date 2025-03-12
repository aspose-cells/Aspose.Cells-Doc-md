---
title: Set preset WordArt style to the text of the shape with Node.js via C++
linktitle: Set preset WordArt style to the text of the shape
type: docs
weight: 280
url: /nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Learn how to set a preset WordArt style to the text of a shape using Aspose.Cells for Node.js via C++.
---

## **Possible Usage Scenarios**
You can set a preset WordArt style to the text of the shape using Aspose.Cells for Node.js via C++. Please use [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) or [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) methods for this purpose.

## **Set preset WordArt style to the text of the shape**
The following sample code creates a text box with some text and then sets the preset WordArt style of its text using [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) method. This is how the [output excel file](5115445.xlsx) looks in Microsoft Excel.

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
const fntSetting = textbox.getEquationParagraph().getFont();
fntSetting.setWordArtStyle(AsposeCells.PresetWordArtStyle.WordArtStyle3);

// Save the workbook in xlsx format
workbook.save(path.join(outputDir, "outputSetPresetWordArtStyle.xlsx"));
```
