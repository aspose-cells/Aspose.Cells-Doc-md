---
title: Extrahera text från Gear typen SmartArt form med Node.js via C++
linktitle: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 500
url: /sv/nodejs-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Lär dig hur du extraherar text från Gear typen SmartArt form med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Aspose.Cells kan extrahera text från Gear-typen Smart Art-form. För att göra detta bör du först konvertera Smart Art-form till Gruppform med hjälp av [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getResultOfSmartArt--) metoden. Sedan hämtar du arrayen av alla de enskilda former som bildar Gruppformen med hjälp av [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/nodejs-cpp/groupshape/#getGroupedShapes--) metoden. Slutligen kan du iterera över alla enskilda former en efter en i en loop och extrahera deras text med [**Shape.getText()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getText--) egenskapen.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande kodexempel laddar [exempel Excel-filen](67338483.xlsx) som innehåller Geartyp Smart Art Shape. Den extraherar sedan texten från dess individuella former enligt ovanstående. Se konsoloutputen från det angivna kodexemplet nedan för en referens.

## **Exempelkod**

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

## **Konsoloutput**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
