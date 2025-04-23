---
title: Excelファイルの範囲の自動埋め（AutoFill）Node.js経由C++
linktitle: AutoFill 範囲
type: docs
weight: 105
url: /ja/nodejs-cpp/autofill-ranges/
description: Aspose.Cells for Node.js via C++を使ってExcelファイルの指定範囲でオートフィル操作を行う方法を学習します。
---

## **指定した範囲で Excel で自動入力を実行します**

Excelで範囲を選択し、右下にマウスを動かし、「プラス」アイコンをドラッグしてデータを自動入力（オートフィル）します。

## ** Aspose.Cells for Node.js via C++を使用した範囲のオートフィル**

 以下は範囲に対してオートフィル操作を行う例です。この機能のテスト用のサンプルファイルもダウンロードできます：

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

