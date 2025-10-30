---
title: Node.js経由でVBAコードのデジタル署名が有効かどうかを確認
linktitle: VBAコードのデジタル署名が有効かどうかを確認する
type: docs
weight: 120
url: /ja/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aspose.Cells for Node.js via C++を使用してVBAコードのデジタル署名の有効性を確認する方法を学ぶ
--- 

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAコードのデジタル署名が有効かどうかを確認することができます。[**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--)プロパティを使用すると、署名が有効であれば**true**を返し、それ以外の場合は**false**を返します。VBAコードを変更すると、そのデジタル署名は無効になります。

{{% /alert %}}

## ** Node.jsでVBAコードのデジタル署名が有効かどうかを確認**

提供されたリンクから[サンプルのExcelファイル](5115030.xlsm)をダウンロードし、このプロパティの使用方法を示すコードを実演しています。同じExcelファイルには有効な署名がありますが、VBAコードを変更してワークブックを保存した後、再チェックすると署名が無効になることが分かります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Signature is valid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());

// Modify the VBA Code, save the workbook then reload
// VBA Code Signature will now be invalid
let code = workbook.getVbaProject().getModules().get(1).getCodes();
code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
workbook.getVbaProject().getModules().get(1).setCodes(code);

// Save
workbook.save(path.join(dataDir, "output_out.xlsm"));

// Reload
workbook = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsm"));

// Now the signature is invalid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
