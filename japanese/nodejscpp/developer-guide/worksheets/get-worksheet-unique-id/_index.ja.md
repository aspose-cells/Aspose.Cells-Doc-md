---
title: Node.jsを通じてC++でワークシートのユニークIDを取得
linktitle: ワークシートの一意のIDを取得
type: docs
weight: 190
url: /ja/nodejs-cpp/get-worksheet-unique-id/
description: この記事では、Node.jsライブラリとC++ APIを使用してExcelワークシートのユニークIDをプログラム的に取得する方法を説明します。
keywords: Node.js経由のユニークID取得例（Excelワークシート用C++を使用）、Node.js経由のワークシートユニークID取得例（C++を使用）
---

## **ワークシートの一意のIDを取得**

Aspose.Cells for Node.js via C++は、[**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)プロパティを使用してワークシートのユニークIDを取得する機能を提供します。以下のコードスニペットは、[**Worksheet.getUniqueId()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getUniqueId--)プロパティを使ってワークシートのユニークIDを出力する例です。このコードスニペットは、この[サンプルExcelファイル](105480213.xlsx)を利用しています。

### ソースコード

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Print Unique Id
console.log("Unique Id: " + worksheet.getUniqueId());
```
{{< app/cells/assistant language="nodejs-cpp" >}}
