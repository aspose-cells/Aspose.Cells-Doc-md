---
title: Export VBA Certificate to File or Stream with Node.js via C++
linktitle: Export VBA Certificate to File or Stream
type: docs
weight: 90
url: /nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Learn how to export VBA Digital Certificate to a file or stream using Aspose.Cells for Node.js via C++. Access raw data of VBA digital certificates.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export VBA Digital Certificate to stream such as file or memory stream. You can access the raw data of the VBA digital certificate using the [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--) property.

{{% /alert %}}

## **Export VBA Certificate to File or Stream in Node.js**

Please see the following sample code that saves the raw data of the VBA Certificate into a file. You can download the [sample excel file used in this code](5115031.xlsm) from the provided link.

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
