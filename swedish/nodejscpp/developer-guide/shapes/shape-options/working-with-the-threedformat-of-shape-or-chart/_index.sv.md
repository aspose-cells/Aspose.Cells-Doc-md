---
title: Arbeta med ThreeDFormat av form eller diagram med Node.js via C++
linktitle: Att arbeta med ThreeDFormat av formen eller diagrammet
type: docs
weight: 250
url: /sv/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **Möjliga användningsscenario**
Aspose.Cells for Node.js via C++ tillhandahåller egenskapen [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) tillsammans med [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) klass för att arbeta med 3D-format av form eller diagram. Klassen [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) innehåller olika egenskaper som kan ställas in för att uppnå olika resultat enligt applikationskrav.

## **Att arbeta med ThreeDFormat av formen eller diagrammet**
Följande exempelkod laddar [källexcel-filen](5115419.xlsx) och hämtar den första formen i det första arbetsbladet, ställer in underegenskaper för [Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) och sparar sedan arbetsboken i [utdata excel-fil](5115410.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
