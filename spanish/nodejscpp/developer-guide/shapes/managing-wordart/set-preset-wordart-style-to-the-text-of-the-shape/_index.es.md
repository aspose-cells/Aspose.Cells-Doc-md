---
title: Establecer estilo de WordArt predefinido en el texto de la forma con Node.js mediante C++
linktitle: Establecer estilo preestablecido de WordArt al texto de la forma
type: docs
weight: 280
url: /es/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Aprende cómo establecer un estilo de WordArt predefinido en el texto de una forma usando Aspose.Cells for Node.js via C++.
---

## **Escenarios de uso posibles**
 Puedes establecer un estilo de WordArt predefinido en el texto de la forma usando Aspose.Cells for Node.js via C++. Usa los métodos [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) o [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) para ello.

## **Establecer un estilo de WordArt preestablecido al texto de la forma**
El siguiente código de ejemplo crea un cuadro de texto con algo de texto y luego establece el estilo predefinido de WordArt en su texto usando el método [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). Así es como se ve el archivo de Excel de salida ([5115445.xlsx](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-)).

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
