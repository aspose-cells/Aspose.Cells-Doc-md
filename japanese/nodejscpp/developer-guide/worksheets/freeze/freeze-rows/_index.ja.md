---
title: Node.jsとC++経由でExcelワークシートの上部行を固定します。
linktitle: 行を凍結
type: docs
weight: 190
url: /ja/nodejs-cpp/how-to-freeze-rows-of-excel-worksheet
description: この記事では、Node.jsライブラリとC++ APIを使用してExcelワークシートの上部行をプログラムで固定する方法を学びます。
keywords: 上部行を固定、C++経由のNode.jsで上部行を固定します。
---

## **紹介**

この記事では、上部行を固定する方法を学びます。共通の見出しの下に大量のデータがある場合、スクロールしても見出しが見えなくなります。上部行を固定すると、データのスクロール時でもその部分を確認できます。ヘッダーを簡単に確認できます。

## **Excelで行を凍結する**

**![Excelで行を凍結](Freeze-Rows.png)**

1. 上端の行を固定したい場合、その下の行を最初に選択します。
2. 表示 > ウィンドウ枠の固定をクリックします。
3. ドロップダウンメニューで「上部行を凍結」をクリックします。
4. 下にスクロールすると、常に最初の行が上部ビューに表示されます。

**![Frozen row](Frozen-Row.png)**

ご覧の通り、最初の行は固定されており、スクロールダウン時も常にビューの上部に残ります。

行の固定により、大量のデータを見やすくしつつ、行ラベルを気にせずに済みます。

## **Aspose.Cells for Node.js via C++を使った行の固定**
Aspose.Cells for Node.js via C++を使えば簡単に行（または列）を固定できます。 
[**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#freezePanes-number-number-number-number-) メソッドを使用し、選択した行に行の固定を行ってください。
1. ファイルを開くためにワークブックを作成します。または空のファイルを作成します。
2. Worksheet.freezePanes() メソッドを使用して最初の行を固定します。
3. ファイルを保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Freeze.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Freezing panes at the cell B2
workbook.getWorksheets().get(0).freezePanes("A2", 1, 0);

// Saving the file
workbook.save("frozen.xlsx");
```

添付の[サンプルソースExcelファイル](../Freeze.xlsx)。
{{< app/cells/assistant language="nodejs-cpp" >}}
