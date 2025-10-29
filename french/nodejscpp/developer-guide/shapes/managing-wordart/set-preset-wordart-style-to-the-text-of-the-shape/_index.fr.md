---
title: Définir le style WordArt prédéfini au texte de la forme avec Node.js via C++
linktitle: Définir un style de WordArt prédéfini pour le texte de la forme
type: docs
weight: 280
url: /fr/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/
description: Apprenez à définir un style WordArt prédéfini au texte d une forme en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**
Vous pouvez définir un style WordArt prédéfini au texte de la forme en utilisant Aspose.Cells for Node.js via C++. Veuillez utiliser la méthode [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-) ou [FontSettingCollection.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsettingcollection/#setWordArtStyle-presetwordartstyle-) pour cela.

## **Définir un style de WordArt prédéfini pour le texte de la forme**
Le code d'exemple suivant crée une zone de texte avec du texte, puis définit le style WordArt prédéfini de son texte en utilisant la méthode [FontSetting.setWordArtStyle(PresetWordArtStyle)](https://reference.aspose.com/cells/nodejs-cpp/fontsetting/#setWordArtStyle-presetwordartstyle-). Voici à quoi ressemble le fichier Excel en sortie dans Microsoft Excel :

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
