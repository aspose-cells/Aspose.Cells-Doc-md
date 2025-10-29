---
title: Lire la couleur de l’effet de brillance d’une forme avec Node.js via C++
linktitle: Lire la couleur de l effet de luminescence de la forme
type: docs
weight: 330
url: /fr/nodejs-cpp/read-color-of-shape-s-glow-effect/
description: Apprenez à lire la couleur de l’effet de brillance d’une forme en utilisant Aspose.Cells for Node.js via C++. 
---

## Scénarios d'utilisation possibles

Si vous souhaitez lire la couleur de l’effet de brillance d’une forme, utilisez la propriété [**Shape.getColor()**](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--). Cela vous aidera à trouver les différentes propriétés relatives à la couleur de l’effet de brillance.

## Lire la couleur de l'effet de luminescence de la forme

Veuillez consulter le code d'échantillon suivant et son [fichier Excel source](22774108.xlsx) ainsi que la sortie de la console pour votre référence. La capture d'écran suivante montre l'effet de luminescence de la forme à l'intérieur du fichier Excel source lorsqu'il est visualisé dans Microsoft Excel.

![todo:image_alt_text](read-color-of-shape-s-glow-effect_1.png)

## Code Node.js pour lire la couleur de l’effet de brillance d’une forme

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Read the source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sourceGlowEffectColor.xlsx"));

// Access the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Access the shape
const shape = sheet.getShapes().get(0);

// Read the glow effect color and its various properties
const effect = shape.getGlow();
const color = effect.getColor();
console.log("Color: " + color.getColor());
console.log("ColorIndex: " + color.getColorIndex());
console.log("IsShapeColor: " + color.isShapeColor());
console.log("Transparency: " + color.getTransparency());
console.log("Type: " + color.getType());
```

## Sortie de la console

Voici la sortie de la console du code d'échantillon ci-dessus lorsqu'il est exécuté avec le [fichier Excel source](22774108.xlsx) fourni.

{{< highlight javascript >}}

Color: Color [A=222, R=255, G=0, B=0]

ColorIndex: 16711672

IsShapeColor: True

Transparency: 0.13

Type: RGB

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
