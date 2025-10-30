---
title: Aggiungi linea di firma al foglio di lavoro con Node.js tramite C++
linktitle: Aggiungi linea di firma al foglio di lavoro
type: docs
weight: 200
url: /it/nodejs-cpp/add-signature-line/
description: Questo articolo descrive come aggiungere una linea di firma al foglio di lavoro usando il codice Node.js con Aspose.Cells for Node.js via C++.
keywords: Aggiungi linea di firma al foglio di lavoro Node.js tramite C++, come aggiungere una linea di firma al foglio di lavoro Node.js tramite C++, come aggiungere la linea di firma al foglio di lavoro Node.js tramite C++.
---

## **Introduzione**

Aspose.Cells fornisce la proprietà [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) per aggiungere la linea di firma del foglio di lavoro.

## **Come Aggiungere una Linea di Firma al Foglio di Lavoro**

Il codice di esempio seguente dimostra come usare la proprietà [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) per aggiungere la linea di firma del foglio di lavoro. La schermata mostra l'effetto del codice di esempio sul file Excel dopo l'esecuzione.

![todo:image_alt_text](add-signature-line.png)

## **Codice di Esempio**

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
{{< app/cells/assistant language="nodejs-cpp" >}}
