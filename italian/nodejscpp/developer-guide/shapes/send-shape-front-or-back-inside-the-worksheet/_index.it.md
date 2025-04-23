---
title: Inoltra la forma davanti o dietro all interno del foglio di lavoro con Node.js tramite C++
linktitle: Invia la forma avanti o indietro all interno del foglio di lavoro
type: docs
weight: 3400
url: /it/nodejs-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Impara come inviare una forma in primo piano o in secondo piano in un foglio di lavoro usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Quando ci sono più forme nello stesso punto, la loro visibilità è determinata dalle posizioni z-order. Aspose.Cells fornisce il metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-), che cambia la posizione z-order della forma. Per inviare una forma in secondo piano, utilizza un numero negativo come -1, -2, -3, ecc., e per portare una forma in primo piano, utilizza un numero positivo come 1, 2, 3, ecc.

## **Invia la forma avanti o indietro all'interno del foglio di lavoro**

Il seguente esempio spiega l'uso del metodo [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#toFrontOrBack-number-). Guarda il [file Excel di esempio](50528330.xlsx) usato nel codice e il [file Excel di output](50528331.xlsx) generato. Lo screenshot mostra l'effetto del codice sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Codice di Esempio**

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
