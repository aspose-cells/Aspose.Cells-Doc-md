---
title: ワークシートがパスワード保護されているかどうかをNode.jsをC++経由で検出
linktitle: ワークシートがパスワードで保護されているかどうかを検出する
type: docs
weight: 360
url: /ja/nodejs-cpp/detect-if-worksheet-is-password-protected/
description: Aspose.Cells for Node.js via C++を使用して、ワークシートがパスワード保護されているかどうかを検出する方法について学びます。 
keywords: ワークシートのパスワード保護ノード.jsの検出、C++経由でのチェック、Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

ワークブックとワークシートは別々に保護可能です。例えば、スプレッドシートには1つ以上のパスワード保護されたワークシートが含まれる場合がありますが、スプレッドシート自体は保護されている場合とそうでない場合があります。Aspose.Cells APIは、指定されたワークシートがパスワード保護されているかどうかを検出する手段を提供します。この記事は、そのためにAspose.Cells for Node.js via C++ APIの使用例を示しています。

{{% /alert %}}

Aspose.Cells for Node.js via C++は、ワークシートがパスワード保護されているかどうかを検出するための[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)プロパティを公開しています。Boolean型の[**Protection.isProtectedWithPassword()**](https://reference.aspose.com/cells/nodejs-cpp/protection/#isProtectedWithPassword--)プロパティは、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)がパスワード保護されている場合は**true**、そうでなければ**false**を返します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook and load a spreadsheet
const book = new AsposeCells.Workbook(filePath);

// Access the protected Worksheet
const sheet = book.getWorksheets().get(0);

// Check if Worksheet is password protected
if (sheet.getProtection().isProtectedWithPassword()) {
console.log("Worksheet is password protected");
} else {
console.log("Worksheet is not password protected");
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
