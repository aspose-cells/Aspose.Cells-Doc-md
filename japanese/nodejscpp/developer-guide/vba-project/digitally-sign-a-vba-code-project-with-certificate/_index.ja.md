---
title: Node.js経由でC++を使用して、VBAコードプロジェクトにデジタル署名を付与する方法
linktitle: 証明書でVBAコードプロジェクトにデジタル署名する
type: docs
weight: 110
url: /ja/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for Node.js via C++を使用して、VBAコードプロジェクトに証明書でデジタル署名を付与する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsの[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)メソッドを使用して、VBAコードプロジェクトにデジタル署名を付与できます。Excelファイルが証明書でデジタル署名されているかどうかを確認する手順に従ってください。

- **開発**タブから**Visual Basic**をクリックして**Visual Basic for Applications IDE**を開きます
- **Visual Basic for Applications IDE**の**ツール** > **デジタル署名...**をクリック

そうすると**デジタル署名フォーム**が表示され、ドキュメントが証明書でデジタル署名されているかどうかが表示されます。

{{% /alert %}} 

## **Node.js経由で証明書を使ってVBAコードプロジェクトにデジタル署名を付与する**

以下のサンプルコードは、[**VbaProject.sign(DigitalSignature)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#sign-digitalsignature-)メソッドの使用例です。入力ファイルと出力ファイルの例も示します。任意のExcelファイルと任意の証明書を使用してテストできます。

- サンプルのExcelファイル（5115028.xlsm）
- [サンプルpfxファイル（5115039.pfx）](5115039.pfx)でデジタル署名を作成します。このコードを実行するためにこのファイルをコンピューターにインストールしてください。パスワードは1234です。
- サンプルコードによって生成された出力Excelファイル（5115029.xlsm）

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Set up paths
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const pfxPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.pfx");
const workbookPath = path.join(sourceDir, "sampleDigitallySignVbaProjectWithCertificate.xlsm");

// Set Digital Signature
const password = "1234";
const comment = "Signing Digital Signature using Aspose.Cells";
const digitalSignature = new AsposeCells.DigitalSignature(fs.readFileSync(pfxPath), password, comment, new Date());

// Create workbook object from excel file
const workbook = new AsposeCells.Workbook(workbookPath);

// Sign VBA Code Project with Digital Signature
workbook.getVbaProject().sign(digitalSignature);

// Save the workbook
workbook.save(path.join(outputDir, "outputDigitallySignVbaProjectWithCertificate.xlsm"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
