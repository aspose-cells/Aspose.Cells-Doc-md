---
title: Arbeta med reflektionseffekten av form eller diagram med Node.js via C++
linktitle: Att arbeta med reflektionseffekten i formen eller diagrammet
type: docs
weight: 210
url: /sv/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: Lär dig hur man arbetar med reflektionseffekten av former eller diagram med Aspose.Cells for Node.js via C++. Ställ in olika reflektionsegenskaper för att uppnå önskade resultat.
---

## **Möjliga användningsscenario**
Aspose.Cells for Node.js via C++ tillhandahåller egenskapen [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) tillsammans med klassen [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) för att arbeta med reflektionseffekten av form eller diagram. Klassen [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect) innehåller följande egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **Att arbeta med reflektionseffekten i formen eller diagrammet**
Följande exempelkod laddar [källexcel-filen](5115424.xlsx) och hämtar den första formen i standardarbetsbladet. Den ställer in olika egenskaper för [Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--) och sparar sedan arbetsboken i [utdata excel-fil](5115423.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
