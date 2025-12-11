---
title: Export VBA Certificate to File or Stream with Node.js via C++
linktitle: Export VBA Certificate to File or Stream
type: docs
weight: 90
url: /nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Learn how to export a VBA digital certificate to a file or stream using Aspose.Cells for Node.js via C++. Access raw data of VBA digital certificates.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export a VBA digital certificate to a stream such as a file or memory stream. You can access the raw data of the VBA digital certificate using the [**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--) property.

{{% /alert %}}

## **Export VBA Certificate to File or Stream in Node.js**

Please see the following sample code that saves the raw data of the VBA certificate into a file. You can download the [sample Excel file used in this code](5115031.xlsm) from the provided link.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file into a Workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleVBAProjectSigned.xlsm"));

// Retrieve the byte data of the digital certificate of the VBA project
const certBytes = workbook.getVbaProject().getCertRawData();

// Save certificate data into a file stream
require("fs").writeFileSync(path.join(dataDir, "Cert_out_"), Uint8Array.from(certBytes));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
