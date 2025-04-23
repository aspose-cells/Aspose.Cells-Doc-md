---
title: Node.js経由でC++を使用してVBAデジタル証明書をファイルまたはストリームにエクスポートする
linktitle: ファイルまたはストリームにVBAデジタル証明書をエクスポート
type: docs
weight: 90
url: /ja/nodejs-cpp/export-vba-certificate-to-file-or-stream/
description: Aspose.Cells for Node.js via C++を使って、VBAデジタル証明書をファイルまたはストリームにエクスポートする方法を学びます。VBAデジタル証明書の生データにアクセスします。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAデジタル証明書をファイルまたはメモリストリームにエクスポートできます。VBAデジタル証明書の生データには[**VbaProject.getCertRawData()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#getCertRawData--)プロパティを使用できます。

{{% /alert %}}

## **Node.jsでVBA証明書をファイルまたはストリームにエクスポートする**

以下のサンプルコードを参照してください。このコードで使用される[サンプルExcelファイル](5115031.xlsm)を提供リンクからダウンロードできます。

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
