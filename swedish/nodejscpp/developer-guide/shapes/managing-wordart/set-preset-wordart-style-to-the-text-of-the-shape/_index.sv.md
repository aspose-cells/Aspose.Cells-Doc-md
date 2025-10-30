---
title: Sätt förinställt WordArt stil till texten i formen med Node.js via C++
linktitle: Ange förvald WordArt stil för texten på formen
type: docs
weight: 280
url: /sv/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Lär dig att ställa in en förinställd WordArt stil till texten i en form med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**
Du kan ställa in en förinställd WordArt-stil till texten i formen med Aspose.Cells for Node.js via C++. Använd [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) eller [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) metoder för detta.

## **Ange förvald WordArt-stil för texten på formen**
 Följande exempel skapar en textruta med viss text och ställer in dess förinställda WordArt-stil med hjälp av [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). Så här ser den [utdata Excel-filen](5115445.xlsx) ut i Microsoft Excel.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
