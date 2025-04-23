---
title: Node.jsとC++を使用したコメントとメモの管理
linktitle: コメントとノート
type: docs
weight: 128
url: /ja/nodejs-cpp/comments-and-notes/
description: Aspose.Cells for Node.js via C++を使用してコメントやメモを挿入・管理します。
keywords: コメントやメモの挿入 Node.jsとC++
---

## **紹介**

コメントはセルに追加情報を付加するために使用されます。Aspose.Cells for Node.js via C++はセルにコメントを追加する二つの方法を提供します。一つはデザイナーファイルで手動でコメントを作成し、それをAspose.Cellsでインポートする方法です。もう一つは、実行時にAspose.Cells APIを使用してコメントを追加する方法です。このトピックでは、Aspose.Cells APIを使ったセルへのコメント追加方法について説明します。コメントの書式設定も解説します。

## **コメントの追加**

[**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)コレクションの[**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#add-number-number-)メソッドを呼び出してセルにコメントを追加します（[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)オブジェクトにカプセル化されています）。新しい[**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)オブジェクトには、コメントのインデックスを渡して[**Comments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection)コレクションからアクセスします。[**Comment**](https://reference.aspose.com/cells/nodejs-cpp/comment)オブジェクトにアクセスした後、[**getNote()**](https://reference.aspose.com/cells/nodejs-cpp/comment/#getNote--)プロパティを使ってコメントメモをカスタマイズします。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **コメントの書式設定**

コメントの高さ、幅、フォント設定を構成することで、コメントの外観を書式設定することも可能です。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding a comment to "F5" cell
const commentIndex = worksheet.getComments().add("F5");

// Accessing the newly added comment
const comment = worksheet.getComments().get(commentIndex);

// Setting the comment note
comment.setNote("Hello Aspose!");

// Setting the font size of a comment to 14
comment.getFont().setSize(14);

// Setting the font of a comment to bold
comment.getFont().setIsBold(true);

// Setting the height of the font to 10
comment.setHeightCM(10);

// Setting the width of the font to 2
comment.setWidthCM(2);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **コメントに画像を追加する**

Microsoft Excel 2007では、セルコメントの背景として画像を使用することもできます。Excel 2007では、次の手順を実行することでこれが実現されます。（すでにセルにコメントを追加していることを前提とします。）

1. コメントを含むセルを右クリックします。
1. **表示/非表示**を選択し、コメント内のテキストをクリアします。
1. コメントの境界線をクリックして選択します。
1. **書式**、次に**コメント**を選択します。
1. **色と線**タブで、**色**リストを展開します。
1. **塗りつぶしの効果**をクリックします。
1. **図**タブで、**ピクチャを選択**をクリックします。
1. 画像を探し、選択します。
1. すべてのダイアログが閉じるまで**OK**をクリックします。

Aspose.Cellsもこの機能を提供します。以下は、セル"A1"に画像を背景として設定したコメントを追加し、からXLSXファイルをスクラッチから作成するコードサンプルです。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

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
const bmpPath = path.join(dataDir, "logo.jpg");
const bmpData = fs.readFileSync(bmpPath);

// Set image data to the shape associated with the comment
comment.getCommentShape().getFill().setImageData(bmpData);

// Save the workbook
workbook.save(path.join(dataDir, "book1.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **高度なトピック**
- [コメントのテキスト方向を変更する](/cells/ja/nodejs-cpp/change-text-direction-of-the-comment/)
- [コメントのフォント色を変更する方法](/cells/ja/nodejs-cpp/how-to-change-the-comment-font-color/)
- [コメントの背景を設定する方法](/cells/ja/nodejs-cpp/how-to-set-comment-background/)
- [スレッド化されたコメント](/cells/ja/nodejs-cpp/threaded-comments/)

