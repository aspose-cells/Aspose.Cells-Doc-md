---  
title: Travailler avec l’effet de brillance de la forme ou du graphique avec Node.js via C++  
linktitle: Travailler avec l effet de lueur de la forme ou du graphique  
type: docs  
weight: 240  
url: /fr/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Apprenez comment travailler avec l’effet de brillance des formes ou des graphiques dans Node.js en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells fournit la propriété [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) ainsi que la classe [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) pour travailler avec l’effet de brillance des formes ou des graphiques. La classe [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) contient les propriétés suivantes qui peuvent être configurées pour obtenir des résultats différents selon les besoins de l’application.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Travailler avec l'effet de lueur de la forme ou du graphique**  
Le code d'exemple suivant charge le [fichier Excel source](5115407.xlsx) et accède à la première forme de la première feuille de calcul, puis configure les sous-propriétés de la propriété [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) et enregistre ensuite le classeur dans un [fichier Excel de sortie](5115414.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
