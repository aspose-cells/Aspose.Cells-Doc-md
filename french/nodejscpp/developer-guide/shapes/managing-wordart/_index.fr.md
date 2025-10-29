---
title: Ajoutez un filigrane WordArt à la feuille avec Node.js via C++
linktitle: Gestion de WordArt
type: docs
weight: 180
url: /fr/nodejs-cpp/add-wordart-watermark-to-worksheet/
description: Apprenez comment ajouter un WordArt en tant que filigrane de fond à une feuille en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}} 

Utilisez WordArt pour ajouter des effets de texte spéciaux aux feuilles de calcul. Par exemple, étirez un titre sur le dessus du fichier, décorez du texte et faites en sorte que le texte s'adapte à une forme prédéfinie, ou appliquez du texte à une feuille Excel en tant que filigrane en arrière-plan. Le WordArt devient un objet que vous pouvez déplacer ou positionner dans les feuilles de calcul pour ajouter une décoration.

{{% /alert %}} 

L'exemple suivant montre comment ajouter une forme WordArt pour définir un filigrane en arrière-plan pour une feuille de calcul.

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

## **Sujets avancés**
- [Ajouter un texte Word Art avec des styles intégrés](/cells/fr/nodejs-cpp/add-word-art-text-with-built-in-styles/)
- [Verrouillage du filigrane WordArt](/cells/fr/nodejs-cpp/locking-wordart-watermark/)
- [Définir un style de WordArt prédéfini pour le texte de la forme](/cells/fr/nodejs-cpp/set-preset-wordart-style-to-the-text-of-the-shape/)
{{< app/cells/assistant language="nodejs-cpp" >}}
