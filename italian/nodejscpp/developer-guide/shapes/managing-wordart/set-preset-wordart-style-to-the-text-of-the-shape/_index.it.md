---
title: Imposta stile WordArt predefinito al testo della forma con Node.js tramite C++
linktitle: Imposta lo stile predefinito di WordArt al testo della forma
type: docs
weight: 280
url: /it/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Impara come impostare uno stile WordArt predefinito al testo di una forma usando Aspose.Cells for Node.js via C++.
---

## **Possibili Scenari di Utilizzo**
Puoi impostare uno stile WordArt predefinito al testo della forma usando Aspose.Cells for Node.js via C++. Si prega di usare i metodi [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) o [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) per questo scopo.

## **Imposta lo stile predefinito di WordArt al testo della forma**
Il codice di esempio seguente crea una casella di testo con del testo e quindi imposta lo stile WordArt predefinito del testo usando il metodo [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). Ecco come appare il file Excel di output in Microsoft Excel.

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
