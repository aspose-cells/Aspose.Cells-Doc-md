---
title: Exportar certificado VBA a archivo o transmisión con Node.js a través de C++
linktitle: Exportar Certificado VBA a Archivo o Secuencia
type: docs
weight: 90
url: /es/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Aprenda cómo exportar el certificado digital VBA a un archivo o transmisión usando Aspose.Cells for Node.js via C++. Acceda a los datos en bruto de los certificados digitales VBA.
---

{{% alert color="primary" %}}

Aspose.Cells le permite exportar Certificado Digital VBA a una secuencia como un archivo o memoria. Puede acceder a los datos en bruto del certificado digital VBA utilizando la propiedad [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--).

{{% /alert %}}

## **Exportar certificado VBA a archivo o transmisión en Node.js**

Consulte el siguiente código de muestra que guarda los datos en bruto del Certificado VBA en un archivo. Puede descargar el [archivo de Excel de muestra utilizado en este código](5115031.xlsm) desde el enlace proporcionado.

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
