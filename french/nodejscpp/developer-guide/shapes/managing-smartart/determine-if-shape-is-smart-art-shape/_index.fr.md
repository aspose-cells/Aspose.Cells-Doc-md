---  
title: Déterminer si la forme est une forme d art intelligent avec Node.js via C++  
linktitle: Déterminer si la forme est une forme de l Art Smart  
type: docs  
weight: 400  
url: /fr/nodejs-cpp/determine-if-shape-is-smart-art-shape/  
description: Apprenez comment déterminer si une forme dans Excel est une forme d art intelligent en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Les formes d'art intelligent sont des formes spéciales dans Microsoft Excel qui permettent de créer automatiquement des diagrammes complexes. Vous pouvez vérifier si la forme est une forme d'art intelligent ou une forme normale en utilisant la propriété [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--).  

## **Déterminer si la forme est une forme de l'Art Smart**  

Le code d'exemple suivant charge le [fichier Excel d'exemple](55541792.xlsx) contenant une forme d'art intelligent comme illustré dans cette capture d'écran. Il affiche ensuite la valeur de la propriété [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) de la première forme. Veuillez voir la sortie de la console du code d'exemple ci-dessous.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");

// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```  

## **Sortie console**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}  

