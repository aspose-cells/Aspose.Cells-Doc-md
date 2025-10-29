---
title: Faire pivoter le texte avec la forme à l intérieur de la feuille de calcul en utilisant Node.js via C++
linktitle: Faire pivoter le texte avec la forme à l intérieur de la feuille de calcul
type: docs
weight: 1300
url: /fr/nodejs-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Apprenez à faire pivoter le texte avec la forme à l intérieur d une feuille Excel en utilisant Aspose.Cells for Node.js via C++.
---

## **Scénarios d'utilisation possibles**

Vous pouvez ajouter du texte à l'intérieur de n'importe quelle forme en utilisant Microsoft Excel. Si vous ajoutez une forme avec l'ancien Microsoft Excel 2003, le texte ne tournera pas avec la forme. Mais si vous utilisez des versions plus récentes de Microsoft Excel, par exemple 2007, 2010, 2013 ou 2016, le texte tournera avec la forme. Vous pouvez contrôler si le texte doit tourner avec la forme ou non en utilisant la propriété [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--). Sa valeur par défaut est **true**, ce qui signifie que le texte tournera avec la forme, mais si vous la définissez sur **false**, le texte ne tournera pas avec la forme.

## **Faire pivoter le texte avec la forme à l'intérieur de la feuille de calcul**

Le code exemple suivant charge le [fichier Excel d'exemple](64716896.xlsx) qui possède une forme triangulaire dont le texte tourne avec la forme. Si vous ouvrez le fichier Excel dans Microsoft Excel et que vous faites pivoter la forme triangulaire, le texte tournera également avec. Le code définit ensuite la propriété [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) sur **false** et l’enregistre sous le nom de [fichier Excel de sortie](64716897.xlsx). Si vous ouvrez maintenant le fichier Excel de sortie dans Microsoft Excel et faites pivoter la forme triangulaire, le texte ne tournera plus avec. Veuillez voir la capture d'écran suivante illustrant l'effet du code sur le fichier Excel d'exemple à titre de référence.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");

// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");

// Access first shape.
const shape = worksheet.getShapes().get(0);

// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();

// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);

// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
