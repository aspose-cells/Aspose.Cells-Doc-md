---
title: Exportera VBA certifikat till fil eller ström med Node.js via C++
linktitle: Exportera VBA certifikat till fil eller ström
type: docs
weight: 90
url: /sv/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Lär dig hur man exporterar VBA digitalt certifikat till en fil eller ström med Aspose.Cells for Node.js via C++. Åtkomst till rådata för VBA digitala certifikat.
---

{{% alert color="primary" %}}

Aspose.Cells låter dig exportera VBA Digital Certificate till ström som fil eller minnesström. Du kan komma åt rådata för det VBA digitala certifikatet med hjälp av [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--) egenskapen.

{{% /alert %}}

## **Exportera VBA-certifikat till fil eller ström i Node.js**

Vänligen se följande exempelkod som sparar rådata för VBA-certifikatet i en fil. Du kan ladda ned [provexelfilen som används i denna kod](5115031.xlsm) från den angivna länken.

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
