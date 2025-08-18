---
title: Node.js経由のC++を使ったワークシートの重複行の削除
linktitle: ワークシート内の重複行を削除する
type: docs
weight: 370
url: /ja/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Aspose.Cells for Node.js via C++を使ったワークシートの重複行の削除方法と、特定の列を選択して重複チェックを行う方法を学びます。
---


重複行の削除は、Microsoft Excelの多くの便利な機能の一つです。これにより、ワークシート内の重複行を削除でき、重複情報を検出する列を選択できます。

Aspose.Cells for Node.js via C++は、この目的のために`Cells.removeDuplicates()`メソッドを提供します。`startRow`、`startColumn`、`endRow`、`endColumn`を設定して、重複を確認する範囲の列を指定することも可能です。

これがこの機能のテストにダウンロードできるサンプルファイルです。

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
