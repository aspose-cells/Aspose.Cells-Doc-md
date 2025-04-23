---
title: Node.js経由でVBAコードに署名されているかどうかを確認（C++利用）
linktitle: VBAコードが署名されているかどうかをチェック
type: docs
weight: 100
url: /ja/nodejs-cpp/check-if-vba-code-is-signed/
description: Aspose.Cells for Node.js via C++を使用して、VBAコードプロジェクトに署名されているかどうかを確認する方法を学ぶ 
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、VBAコードプロジェクトが署名されているかどうかを確認できます。VBAコードプロジェクトが署名されているかどうかを確認するには、[**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)プロパティを使用してください。

{{% /alert %}}

以下のコードは、[**VbaProject.isSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isSigned--)プロパティを使用してVBAコードに署名されているかどうかを確認する方法を示しています。このコードは任意のExcelファイルでテストできます。テスト用に、このコードで使用されているExcelファイル（[このExcelファイル](5115032.xlsm)）を使用可能です。

## ** Node.jsでVBAコードに署名されているかどうかを確認**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

console.log("Is VBA Code Project Signed: " + workbook.getVbaProject().isSigned());
```

## コンソール出力

上記のコードのコンソール出力は、提供された[サンプルExcelファイル](5115032.xlsm)を使用して以下のようになります。

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
