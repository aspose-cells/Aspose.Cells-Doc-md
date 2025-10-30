---
title: Node.jsを使用して各行に異なる横方向の配置を持つTextBoxを作成
linktitle: 各行が異なる水平方向の整列を持つテキストボックスを作成
type: docs
weight: 310
url: /ja/nodejs-cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/
description: Aspose.Cells for Node.js via C++を使用して、各行に異なる水平方向の配置を持つテキストボックスの作成方法を学ぶ
---

{{% alert color="primary" %}}
段落テキストの水平方向の配置を設定することができます。[**TextParagraph.getAlignmentType()**](https://reference.aspose.com/cells/nodejs-cpp/textparagraph/#getAlignmentType--)プロパティを使用します。
{{% /alert %}}

以下のサンプルコードは、三つの行を作成し、それぞれの水平方向の配置を設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const wb = new AsposeCells.Workbook();

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Add text box inside the sheet.
ws.getShapes().addTextBox(2, 0, 2, 0, 80, 400);

// Access first shape which is a text box and set its text.
const shape = ws.getShapes().get(0);
shape.setText("Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.");

// Access the first paragraph and set its horizontal alignment to left.
let p = shape.getTextBody().getTextParagraphs().get(0);
p.setAlignmentType(AsposeCells.TextAlignmentType.Left);

// Access the second paragraph and set its horizontal alignment to center.
p = shape.getTextBody().getTextParagraphs().get(1);
p.setAlignmentType(AsposeCells.TextAlignmentType.Center);

// Access the third paragraph and set its horizontal alignment to right.
p = shape.getTextBody().getTextParagraphs().get(2);
p.setAlignmentType(AsposeCells.TextAlignmentType.Right);

// Save the workbook in xlsx format.
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
