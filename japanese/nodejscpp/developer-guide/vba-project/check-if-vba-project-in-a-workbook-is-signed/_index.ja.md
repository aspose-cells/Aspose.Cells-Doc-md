---
title: Node.js経由でブック内のVBAプロジェクトが署名されているかどうかを確認（C++利用）
linktitle: ブックのVBAプロジェクトが署名されているかどうかを確認
type: docs
weight: 70
url: /ja/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.Cells for Node.js via C++を用いて、ブック内のVBAプロジェクトが署名されているかどうかを確認する方法を学ぶ
---

{{% alert color="primary" %}}

Microsoft Excelでは、**ツール > デジタル署名...**メニューコマンドを使用してVBAプロジェクトが署名されているかどうかを確認できます。同様に、Aspose.Cellsの[**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)プロパティを使用してプログラムで確認することも可能です。

{{% /alert %}}

## **Node.jsでワークブックのVBAプロジェクトが署名されているかどうかを確認**

以下のコードは、ワークブックをロードし、そのVBAプロジェクトが署名されているかどうかを [**Workbook.getVbaProject()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getVbaProject--)プロパティを使用して判定します。署名されている場合は **true** を返し、そうでなければ**false**を返します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
console.log("VBA Project is Signed: " + workbook.getVbaProject().isSigned());
```
