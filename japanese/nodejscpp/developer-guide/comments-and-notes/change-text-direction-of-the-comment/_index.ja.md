---
title: Node.js と C++ を使用したコメントのテキスト方向の変更
linktitle: コメントのテキスト方向を変更する
type: docs
weight: 10
url: /ja/nodejs-cpp/change-text-direction-of-the-comment/
description: Aspose.Cells for Node.js via C++ を使用してコメントのテキスト方向を変更する方法を学びましょう。コメントの整列設定を効果的にカスタマイズできます。
---

{{% alert color="primary" %}}

Microsoft Excel はセルにコメントを追加して、追加情報やデータをハイライトできます。開発者は、コメントの整列設定やテキスト方向を指定するためにカスタマイズが必要になる場合があります。Aspose.Cells for Node.js via C++ はこれを実現するAPIを提供します。

{{% /alert %}}

Aspose.Cells for Node.js via C++はコメントのテキスト方向を設定する [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) プロパティを提供します。以下のサンプルコードは、[**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) プロパティを使用してコメントのテキスト方向を設定する例です。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first worksheet
const sheet = wb.getWorksheets().get(0);

// Add a comment to A1 cell
const commentIndex = sheet.getComments().add("A1");
const comment = sheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set its horizontal alignment setting
comment.getCommentShape().setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Right);

// Set the Text Direction - Right-to-Left
comment.getCommentShape().setTextOrientationType(AsposeCells.TextDirectionType.RightToLeft);

// Set the Comment note
comment.setNote("This is my Comment Text. This is test");

const outputFilePath = path.join(dataDir, "OutCommentShape.out.xlsx");
// Save the Excel file
wb.save(outputFilePath);
```
