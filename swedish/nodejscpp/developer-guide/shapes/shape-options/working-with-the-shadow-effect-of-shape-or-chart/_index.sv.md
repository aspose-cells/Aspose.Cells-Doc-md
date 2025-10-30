---  
title: Arbeta med skuggeffekten av form eller diagram med Node.js via C++  
linktitle: Att arbeta med skuggeffekten i formen eller diagrammet  
type: docs  
weight: 220  
url: /sv/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: Lär dig hur man arbetar med skuggeffekten av former eller diagram med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  
Aspose.Cells for Node.js via C++ tillhandahåller egenskapen [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) tillsammans med klassen [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) för att arbeta med skuggeffekten av form eller diagram. Klassen [ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **Att arbeta med skuggeffekten i formen eller diagrammet**  
Följande exempelkod laddar [källexcel-filen](5115425.xlsx) och hämtar det första formen i det första arbetsbladet, ställer in underegenskaper för egenskapen [Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--) och sparar sedan arbetsboken i [utdata excel-fil](5115411.xlsx).  

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
