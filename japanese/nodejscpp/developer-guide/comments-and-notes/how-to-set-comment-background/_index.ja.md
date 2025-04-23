---
title: Excel のコメントの背景を変更する方法（Node.js + C++）
linktitle: コメント背景
type: docs
weight: 190
url: /ja/nodejs-cpp/how-to-set-comment-background/
description: Aspose.Cells for Node.js via C++ を使用して、Excel のコメントの色を変更したり、コメントに画像や写真を挿入したりする方法。
keywords: セルのコメント背景色に inset 画像を追加する例（Node.js + C++）
---

{{% alert color="primary" %}}
セルにコメントを追加してメモやレビューの質問、値の由来など情報を記録します。複数人が異なる時間にドキュメントを議論やレビューを行う場合、コメントは非常に重要です。コメントごとに背景色を設定することは可能ですが、多数のドキュメントやコメントを処理する場合、手作業は大変です。幸い、[**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) はこれをコードで行うためのAPIを提供しています。
{{% /alert %}}

## **Excel でコメントの色を変更する方法**

コメントのデフォルト背景色が不要な場合は、お好きな色に置き換えることもできます。Excelのコメントボックスの背景色を変更するにはどうすればよいですか？

以下のコードは、[**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) を使用して自分の選択したコメントに好きな背景色を追加する方法を案内します。

こちらに[サンプルファイル](exmaple.xlsx)を用意しました。このファイルは、以下のコードでWorkbookオブジェクトを初期化するために使われます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Initialize a new workbook.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "example.xlsx"));

// Accessing the newly added comment
const comment = workbook.getWorksheets().get(0).getComments().get(0);

// change background color
const shape = comment.getCommentShape();
shape.getFill().getSolidFill().setColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "result.xlsx"));
```

上記のコードを実行すると、[出力ファイル](result.xlsx) が生成されます。

## **Excel でコメントに画像を挿入する方法**

Microsoft Excelは、スプレッドシートの外観と感触を大きくカスタマイズ可能です。コメントに背景画像を追加することも可能です。背景画像の追加は、見た目の工夫やブランディング強化に役立ちます。

以下のサンプルコードは、[**Aspose.Cells**](https://products.aspose.com/cells/nodejs-cpp/) APIを使用して、好きな背景色を持つコメントを作成し、セルA1に追加する方法を示しています。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
const workbook = new AsposeCells.Workbook();

// Get a reference of comments collection with the first sheet
const comments = workbook.getWorksheets().get(0).getComments();

// Add a comment to cell A1
const commentIndex = comments.add(0, 0);
const comment = comments.get(commentIndex);
comment.setNote("First note.");
comment.getFont().setName("Times New Roman");

// Load an image into stream
const fs = require("fs");
const bmp = fs.readFileSync(path.join(dataDir, "image2.jpg"));
const ms = Buffer.from(bmp);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(ms);

// Save the workbook
const outputFilePath = path.join(dataDir, "commentwithpicture1.out.xlsx");
workbook.save(outputFilePath, AsposeCells.SaveFormat.Xlsx);
```

