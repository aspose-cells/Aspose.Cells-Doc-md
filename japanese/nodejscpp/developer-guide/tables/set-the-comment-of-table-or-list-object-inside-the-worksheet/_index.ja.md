---
title: Node.jsをC++経由で使用して、ワークシート内のテーブルまたはリストオブジェクトのコメントを設定する
linktitle: ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください
type: docs
weight: 40
url: /ja/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/
description: Aspose.Cells for Node.js via C++を使用して、ワークシート内のテーブルまたはリストオブジェクトのコメントを設定する方法を学びます。 
---

{{% alert color="primary" %}}

Worksheet内のテーブルまたはリストオブジェクトのコメントは、[**ListObject.getComment()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getComment--)プロパティを使用して設定できます。コメントはxl/tables/tableName.xmlファイル内に表示されます。

{{% /alert %}}

## **ワークシート内のテーブルまたはリストオブジェクトのコメントを設定してください**

以下のサンプルコードは、[ソースエクセルファイル](5115514.xlsx)を読み込み、ワークシート内の最初のテーブルまたはリストオブジェクトのコメントを設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "table_comment.xlsx"));
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access first list object or table.
const lstObj = worksheet.getListObjects().get(0);
// Set the comment of the list object
lstObj.setComment("This is Aspose.Cells comment.");
// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "SetCommentOfTableOrListObject_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
