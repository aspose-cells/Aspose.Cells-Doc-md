---
title: 通过C++在Node.js中将VBA证书导出到文件或流
linktitle: 将VBA证书导出到文件或流
type: docs
weight: 90
url: /zh/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: 学习如何使用Aspose.Cells for Node.js via C++将VBA数字证书导出到文件或流。访问VBA数字证书的原始数据。
---

{{% alert color="primary" %}}

Aspose.Cells允许您将VBA数字证书导出到文件或内存流等流中。您可以使用[**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--)属性访问VBA数字证书的原始数据。

{{% /alert %}}

## **在Node.js中导出VBA证书到文件或流**

请参阅以下示例代码，将VBA证书的原始数据保存到文件中。您可以从提供的链接下载使用此代码的[示例excel文件](5115031.xlsm)。

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
