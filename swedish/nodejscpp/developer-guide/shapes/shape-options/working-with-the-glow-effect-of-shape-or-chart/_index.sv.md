---  
title: Arbeta med glödeffekten av shape eller diagram med Node.js via C++  
linktitle: Arbeta med glödeffekten av form eller diagram  
type: docs  
weight: 240  
url: /sv/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: Lär dig att arbeta med glödeffekten av former eller diagram i Node.js med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  
Aspose.Cells tillhandahåller egenskapen [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) tillsammans med klassen [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) för att arbeta med glödeffekten av form eller diagram. Klassen [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **Arbeta med glödeffekten av form eller diagram**  
Följande exempel laddar det [käll-Excel-filen](5115407.xlsx) och öppnar den första formen i det första arbetsbladet och ställer in sub-egenskaper för [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) egenskapen och sparar sedan arbetsboken i [utdata Excel-fil](5115414.xlsx).  

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
