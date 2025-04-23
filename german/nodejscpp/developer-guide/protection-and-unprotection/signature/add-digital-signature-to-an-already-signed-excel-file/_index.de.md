---
title: Digitales Signatur zu einer bereits signierten Excel Datei mit Node.js über C++ hinzufügen
linktitle: Fügen Sie eine digitale Signatur zu einer bereits signierten Excel Datei hinzu
type: docs
weight: 20
url: /de/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Dieser Artikel beschreibt, wie man mit Node.js und Aspose.Cells for Node.js via C++ eine digitale Signatur zu einer bereits signierten Excel Datei hinzufügt.
keywords: Fügen Sie einer bereits signierten Excel Datei eine digitale Signatur hinzu, wie man eine digitale Signatur zu einem bereits signierten Excel Dokument mit Node.js über C++ hinzufügt.
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Node.js via C++ bietet die [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) Methode, mit der Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzufügen können.

{{% alert color="primary" %}}

Bitte beachten Sie, dass beim Hinzufügen einer digitalen Signatur zu einem bereits signierten Excel-Dokument, falls das Originaldokument ein von Aspose.Cells generiertes Dokument ist, alles gut funktioniert. Wenn das Originaldokument jedoch von anderen Engines (z.B. Microsoft Excel usw.) generiert wurde, kann Aspose.Cells die Datei nach dem Laden und erneuten Speichern nicht unverändert halten, was die ursprüngliche Signatur ungültig macht.

{{% /alert %}}

## **Wie fügt man eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu**

Der folgende Beispielcode zeigt, wie die [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) Methode verwendet wird, um eine digitale Signatur zu einem bereits signierten Excel-Dokument hinzuzufügen. Überprüfen Sie die im Code verwendete [Beispiel-Excel-Datei](50528280.xlsx). Diese Datei ist bereits digital signiert. Überprüfen Sie die [Ausgabedatei Excel](50528281.xlsx), die vom Code generiert wurde. Für dieses Beispiel wurde das Demo-Zertifikat [AsposeDemo.pfx](50528279.pfx) mit einem Passwort **aspose** verwendet. Das Bild zeigt die Wirkung des Beispielcodes auf die Beispiel-Excel-Datei nach Ausführung.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Beispielcode**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
