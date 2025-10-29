---  
title: Travailler avec l effet d ombre de la forme ou du graphique avec Node.js via C++  
linktitle: Travailler avec l effet d ombre de la forme ou du graphique  
type: docs  
weight: 220  
url: /fr/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Apprenez comment travailler avec l effet d ombre des formes ou des graphiques en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  
Aspose.Cells for Node.js via C++ fournit la propriété [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) ainsi que la classe [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) pour travailler avec l'effet d'ombre d'une forme ou d'un graphique. La classe [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) contient les propriétés suivantes qui peuvent être réglées pour obtenir différents résultats selon les besoins de l'application.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Travailler avec l'effet d'ombre de la forme ou du graphique**  
Le code exemple suivant charge le [fichier excel source](5115425.xlsx) et accède à la première forme dans la première feuille, en réglant les sous-propriétés de la propriété [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) puis enregistre le classeur dans le [fichier excel de sortie](5115411.xlsx).  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
