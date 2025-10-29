---
title: Extraire le texte de la forme d art intelligent de type engrenage avec Node.js via C++
linktitle: Extraire du texte de la forme SmartArt de type équipement
type: docs
weight: 500
url: /fr/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Apprenez comment extraire le texte de la forme d art intelligent de type engrenage en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells peut extraire le texte de la forme d'art intelligent de type engrenage. Pour ce faire, vous devez d'abord convertir la forme d'art intelligent en forme de groupe en utilisant la méthode [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Ensuite, vous devez obtenir le tableau de toutes les formes individuelles constituant la forme de groupe en utilisant la méthode [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--). Enfin, vous pouvez parcourir toutes les formes individuelles une par une dans une boucle et extraire leur texte en utilisant la propriété [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--).

## **Extraire du texte de la forme SmartArt de type équipement**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338483.xlsx) qui contient une forme SmartArt de type équipement. Ensuite, il extrait le texte de ses formes individuelles comme discuté ci-dessus. Veuillez consulter la sortie de console du code ci-dessous à titre de référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx");

// Load sample Excel file containing gear type smart art shape.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Get the result of gear type smart art shape in the form of group shape.
const groupShape = shape.getResultOfSmartArt();

// Get the list of individual shapes consisting of group shape.
const shapes = groupShape.getGroupedShapes();

// Extract the text of gear type shapes and print them on console.
for (let i = 0; i < shapes.length; i++) {
const s = shapes[i];

if (s.getType() === AsposeCells.AutoShapeType.Gear9 || s.getType() === AsposeCells.AutoShapeType.Gear6) {
console.log("Gear Type Shape Text: " + s.getText());
}
}
```

## **Sortie console**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
