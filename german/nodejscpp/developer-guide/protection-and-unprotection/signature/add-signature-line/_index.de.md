---
title: Signaturzeile zum Arbeitsblatt mit Node.js über C++ hinzufügen
linktitle: Fügen Sie eine Signaturlinie zum Arbeitsblatt hinzu
type: docs
weight: 200
url: /de/nodejs-cpp/add-signature-line/
description: Dieser Artikel beschreibt, wie man mit Node.js Code und Aspose.Cells for Node.js via C++ eine Signaturzeile zum Arbeitsblatt hinzufügt.
keywords: Signaturzeile zum Arbeitsblatt hinzufügen mit Node.js über C++, Wie man eine Signaturzeile zum Arbeitsblatt hinzufügt mit Node.js über C++, Wie man eine Signaturzeile zum Arbeitsblatt mit Node.js über C++ hinzufügt.
---

## **Einführung**

Aspose.Cells stellt die Eigenschaft [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) bereit, um die Signaturlinie des Arbeitsblatts hinzuzufügen.

## **Wie fügt man eine Signaturlinie zum Arbeitsblatt hinzu**

Der folgende Beispielcode zeigt, wie man die [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) Eigenschaft verwendet, um die Signaturzeile des Arbeitsblatts hinzuzufügen. Das Bild zeigt die Wirkung des Beispielcodes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](add-signature-line.png)

## **Beispielcode**

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
