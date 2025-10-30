---
title: Esporta il certificato VBA in file o stream con Node.js tramite C++
linktitle: Esporta il certificato VBA su File o Stream
type: docs
weight: 90
url: /it/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Impara come esportare il certificato digitale VBA in un file o stream usando Aspose.Cells for Node.js via C++. Accedi ai dati grezzi dei certificati digitali VBA.
---

{{% alert color="primary" %}}

Aspose.Cells ti consente di esportare il certificato digitale VBA su un flusso come file o memory stream. Puoi accedere ai dati grezzi del certificato digitale VBA utilizzando la proprietà [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--).

{{% /alert %}}

## **Esporta il certificato VBA in file o stream in Node.js**

Consulta il seguente codice di esempio che salva i dati grezzi del certificato VBA in un file. Puoi scaricare il [file di esempio di Excel utilizzato in questo codice](5115031.xlsm) dal link fornito.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
