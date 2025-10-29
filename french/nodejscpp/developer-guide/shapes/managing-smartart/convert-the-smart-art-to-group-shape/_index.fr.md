---
title: Convertir l art intelligent en forme de groupe avec Node.js via C++
linktitle: Convertir l Art Smart en une Forme de Groupe
type: docs
weight: 200
url: /fr/nodejs-cpp/convert-the-smart-art-to-group-shape/
---

## **Scénarios d'utilisation possibles**

Vous pouvez convertir une forme d'art intelligent en forme de groupe en utilisant la méthode [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--). Cela vous permettra de traiter la forme d'art intelligent comme une forme de groupe. Par conséquent, vous aurez accès aux parties ou formes individuelles du groupe.

## **Convertir l'Art Smart en une Forme de Groupe**

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541793.xlsx) contenant une forme d'art intelligent comme illustré dans cette capture d'écran. Il convertit ensuite la forme d'art intelligent en forme de groupe et affiche la propriété Shape.isGroup. Veuillez voir la sortie de la console du code d'exemple ci-dessous.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load the sample smart art shape - Excel file
const filePath = path.join(__dirname, "data", "sampleSmartArtShape_GetResultOfSmartArt.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());

// Determine if shape is group shape
console.log("Is Group Shape: " + shape.isGroup());

// Convert smart art shape into group shape
console.log("Is Group Shape: " + shape.getResultOfSmartArt().isGroup());
```

## **Sortie console**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
