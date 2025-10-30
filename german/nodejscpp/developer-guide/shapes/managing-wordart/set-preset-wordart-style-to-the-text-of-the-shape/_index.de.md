---
title: Voreingestellten WordArt Stil auf den Text der Form mit Node.js via C++ setzen
linktitle: Voreingestellten WordArt Stil auf den Text der Form setzen
type: docs
weight: 280
url: /de/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ einen voreingestellten WordArt Stil auf den Text einer Form anwenden.
---

## **Mögliche Verwendungsszenarien**
Sie können mit Aspose.Cells for Node.js via C++ einen voreingestellten WordArt-Stil auf den Text der Form anwenden. Verwenden Sie dazu die Methode [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) oder [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-)

## **Voreingestellten WordArt-Stil auf den Text der Form setzen**
Der folgende Beispielcode erstellt eine TextBox mit Text und setzt anschließend den voreingestellten WordArt-Stil seines Textes mit [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). So sieht die [Ausgabedatei Excel](5115445.xlsx) in Microsoft Excel aus.

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
