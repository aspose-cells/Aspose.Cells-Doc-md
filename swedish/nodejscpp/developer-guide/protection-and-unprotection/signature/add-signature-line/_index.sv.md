---
title: Lägg till underskriftslinje i arbetsbladet med Node.js via C++
linktitle: Lägg till signaturlinje i kalkylarket
type: docs
weight: 200
url: /sv/nodejs-cpp/add-signature-line/
description: Denna artikel beskriver hur man lägger till en underskriftslinje i arbetsbladet med Node.js kod med Aspose.Cells for Node.js via C++.
keywords: Lägg till underskriftslinje i arbetsbladet Node.js via C++, Hur man lägger till underskriftslinje i arbetsbladet Node.js via C++, Hur man lägger till underskriftslinje i arbetsbladet Node.js via C++.
---

## **Introduktion**

Aspose.Cells tillhandahåller egenskapen [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) för att lägga till signaturlinjen i kalkylarket.

## **Hur man lägger till signeringsrad i arket**

 Följande exempel visar hur man använder [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--)-egenskapen för att lägga till underskriftslinjen i arbetsbladet. Skärmbilden visar effekten av exempel-koden på exempel-Excel-filen efter körning.

![todo:image_alt_text](add-signature-line.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiating a Workbook object
const wb = new AsposeCells.Workbook();

const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("Aspose.Cells");
signatureLine.setTitle("signed by Aspose.Cells");
wb.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

const certificatePath = path.join(dataDir, "AsposeDemo.pfx");
const signature = new AsposeCells.DigitalSignature(certificatePath, "aspose", "test Microsoft Office signature line", new Date());


const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);
wb.setDigitalSignature(dsCollection);
wb.save(path.join(dataDir, "signatureLine.xlsx"));
```
