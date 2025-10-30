---
title: Node.js経由のC++を使用して既に署名済みのExcelファイルにデジタル署名を追加する
linktitle: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: この記事では、Aspose.Cells for Node.js via C++を使用して既に署名済みのExcelファイルにデジタル署名を追加する方法について説明します。
keywords: 既に署名済みのExcelファイルにデジタル署名を追加する方法、Node.js経由のC++を使用して既に署名済みのExcelドキュメントにデジタル署名を追加する方法。
---

## **可能な使用シナリオ**

Aspose.Cells for Node.js via C++は、既に署名済みのExcelファイルにデジタル署名を追加できる[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)メソッドを提供します。

{{% alert color="primary" %}}

既に署名されたExcelドキュメントにデジタル署名を追加する際、元のドキュメントがAspose.Cellsで生成されたものであれば正常に動作します。しかし、元のドキュメントが他のエンジン（例えばMicrosoft Excelなど）で生成された場合、Aspose.Cellsは読み込み後に保存し直すとファイルを同じ状態に保てず、元の署名が無効になります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する方法**

以下のサンプルコードは、[**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-)メソッドを使用して既に署名されたExcelファイルにデジタル署名を追加する方法を示しています。このコードで使用されている[サンプルExcelファイル](50528280.xlsx)はすでにデジタル署名が施されています。 このコードによって生成される[出力Excelファイル](50528281.xlsx)もご確認ください。デモ証明書として[name=AsposeDemo.pfx](50528279.pfx)を使用し、パスワードは**aspose**です。スクリーンショットは、コード実行後のサンプルExcelファイルの効果を示しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
