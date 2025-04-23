---
title: Skicka form fram eller bak i bladet med Node.js via C++
linktitle: Skicka form framåt eller bakåt inne i Arbetsbladet
type: docs
weight: 3400
url: /sv/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Lär dig hur du skickar en form till fronten eller baksidan i ett blad med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**

När flera former är placerade på samma plats bestäms deras synlighet av deras z-ordningspositioner. Aspose.Cells tillhandahåller [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)-metoden, som ändrar z-ordningspositionen för formen. För att skicka en form till bakgrunden använder du ett negativt nummer som -1, -2, -3 osv., och för att föra en form till fronten använder du ett positivt nummer som 1, 2, 3 osv.

## **Skicka form framåt eller bakåt inne i Arbetsbladet**

Följande exempel visar användningen av [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-)-metoden. Se [exempel-Excelfilen](50528330.xlsx) som används i koden och [utdata-Excelfilen](50528331.xlsx) som genereras. Skärmdumpen visar effekten av koden på exemplet när det körs.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

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
