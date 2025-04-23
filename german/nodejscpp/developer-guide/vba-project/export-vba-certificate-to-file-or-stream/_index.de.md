---
title: Exportieren Sie VBA Zertifikat nach Datei oder Stream mit Node.js via C++
linktitle: Exportieren Sie VBA Zertifikat in eine Datei oder einen Stream
type: docs
weight: 90
url: /de/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Erfahren Sie, wie man VBA Digitale Zertifikate mithilfe von Aspose.Cells for Node.js via C++ in eine Datei oder einen Stream exportiert. Zugriff auf Rohdaten von VBA Digitalzertifikaten.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, das VBA-Digitalzertifikat in einen Stream wie Datei oder Memory Stream zu exportieren. Sie können auf die Rohdaten des VBA-Digitalzertifikats über die [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--)-Eigenschaft zugreifen.

{{% /alert %}}

## **VBA-Zertifikat in Node.js nach Datei oder Stream exportieren**

Bitte sehen Sie sich den folgenden Beispielscode an, der die Rohdaten des VBA-Zertifikats in einer Datei speichert. Sie können die [Beispiel-Excel-Datei, die in diesem Code verwendet wird](5115031.xlsm) von dem bereitgestellten Link herunterladen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file into workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleVBAProjectSigned.xlsm"));

// Retrieve bytes data of Digital Certificate of VBA Project
const certBytes = workbook.getVbaProject().getCertRawData();

// Save Certificate Data into FileStream
require("fs").writeFileSync(path.join(dataDir, "Cert_out_"), Uint8Array.from(certBytes));
```
