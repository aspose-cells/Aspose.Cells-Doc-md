---
title: Ajouter une ligne de signature à la feuille de calcul avec Node.js via C++
linktitle: Ajouter une ligne de signature au classeur
type: docs
weight: 200
url: /fr/nodejs-cpp/add-signature-line/
description: Cet article explique comment ajouter une ligne de signature à la feuille de calcul en utilisant Node.js avec Aspose.Cells for Node.js via C++.
keywords: Ajouter une ligne de signature à la feuille de calcul avec Node.js via C++, Comment ajouter une ligne de signature à la feuille de calcul avec Node.js via C++, Comment ajouter la ligne de signature à la feuille de calcul avec Node.js via C++.
---

## **Introduction**

Aspose.Cells fournit la propriété [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) pour ajouter la ligne de signature de la feuille de calcul.

## **Comment ajouter une ligne de signature à la feuille de calcul**

Le code d'exemple suivant montre comment utiliser la propriété [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) pour ajouter la ligne de signature de la feuille de calcul. La capture d'écran montre l'effet du code d'exemple sur le fichier Excel après exécution.

![todo:image_alt_text](add-signature-line.png)

## **Code d'exemple**

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
