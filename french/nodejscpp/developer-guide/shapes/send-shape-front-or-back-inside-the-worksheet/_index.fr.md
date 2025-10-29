---
title: Envoyer une forme en avant ou en arrière dans la feuille avec Node.js via C++
linktitle: Envoyer une forme vers l avant ou vers l arrière à l intérieur de la feuille de calcul
type: docs
weight: 3400
url: /fr/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Apprenez comment envoyer une forme à l avant ou à l arrière dans une feuille à l aide de Aspose.Cells for Node.js via C++. 
---

## **Scénarios d'utilisation possibles**

Lorsqu'il y a plusieurs formes au même endroit, leur visibilité est déterminée par leur position z-order. Aspose.Cells offre la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-), qui modifie la position z-order de la forme. Pour envoyer une forme à l'arrière, utilisez un nombre négatif comme -1, -2, -3, etc., et pour amener une forme en avant, utilisez un nombre positif comme 1, 2, 3, etc.

## **Envoyer la forme à l'avant ou à l'arrière dans la feuille de calcul**

Le code exemple suivant explique l'utilisation de la méthode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). Veuillez consulter le [fichier Excel d'exemple](50528330.xlsx) utilisé dans le code ainsi que le [fichier Excel de sortie](50528331.xlsx) généré. La capture d'écran montre l'effet du code sur le fichier Excel d'exemple lors de l'exécution.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleToFrontOrBack.xlsx");

// Load source Excel file
const workbook = new AsposeCells.Workbook(sourceFilePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first and fourth shape
const shape1 = worksheet.getShapes().get(0);
const shape4 = worksheet.getShapes().get(3);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 1: " + shape1.getZOrderPosition());

// Send this shape to front
shape1.toFrontOrBack(2);

// Print the Z-Order position of the shape
console.log("Z-Order Shape 4: " + shape4.getZOrderPosition());

// Send this shape to back
shape4.toFrontOrBack(-2);

// Save the output Excel file
const outputFilePath = path.join(dataDir, "outputToFrontOrBack.xlsx");
workbook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
