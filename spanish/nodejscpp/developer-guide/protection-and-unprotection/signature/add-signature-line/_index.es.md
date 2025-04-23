---
title: Agregar línea de firma a la hoja de trabajo con Node.js a través de C++
linktitle: Agregar línea de firma al documento de Excel
type: docs
weight: 200
url: /es/nodejs-cpp/add-signature-line/
description: Este artículo describe cómo agregar una línea de firma a la hoja de trabajo usando Node.js con Aspose.Cells for Node.js via C++.
keywords: Agregar línea de firma a la hoja de trabajo Node.js a través de C++, Cómo agregar línea de firma a la hoja de trabajo Node.js vía C++, Cómo agregar la línea de firma a la hoja de trabajo Node.js a través de C++.
---

## **Introducción**

Aspose.Cells proporciona la propiedad [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) para agregar la línea de firma al documento de Excel.

## **Cómo agregar una línea de firma a la hoja de cálculo**

El código de ejemplo siguiente demuestra cómo usar la propiedad [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) para agregar la línea de firma de la hoja de trabajo. La captura de pantalla muestra el efecto del código de ejemplo en el archivo Excel de muestra después de la ejecución.

![todo:image_alt_text](add-signature-line.png)

## **Código de muestra**

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
