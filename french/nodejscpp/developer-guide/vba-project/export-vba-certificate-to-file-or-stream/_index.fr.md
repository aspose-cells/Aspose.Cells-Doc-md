---
title: Exporter le certificat VBA vers un fichier ou un flux avec Node.js via C++
linktitle: Exporter le certificat VBA dans un fichier ou un flux
type: docs
weight: 90
url: /fr/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Découvrez comment exporter le certificat numérique VBA vers un fichier ou un flux en utilisant Aspose.Cells for Node.js via C++. Accédez aux données brutes des certificats numériques VBA.
---

{{% alert color="primary" %}}

Aspose.Cells vous permet d'exporter un certificat numérique VBA vers un flux tel qu'un fichier ou un flux de mémoire. Vous pouvez accéder aux données brutes du certificat numérique VBA en utilisant la propriété [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--).

{{% /alert %}}

## **Exporter le certificat VBA vers un fichier ou un flux dans Node.js**

Veuillez consulter le code d'exemple suivant qui enregistre les données brutes du certificat VBA dans un fichier. Vous pouvez télécharger le [fichier Excel d'exemple utilisé dans ce code](5115031.xlsm) à partir du lien fourni.

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
