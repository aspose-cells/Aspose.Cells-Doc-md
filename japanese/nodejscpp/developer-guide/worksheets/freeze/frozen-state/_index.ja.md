---
title: Excelを使わずにFrozen状態を確認する方法  C++を用いたNode.jsで
linktitle: 凍結状態
type: docs
weight: 190
url: /ja/nodejs-cpp/how-to-check-frozen-state-of-excel-worksheet
description: この記事では、Node.jsとC++ライブラリを使用してExcelワークシートの凍結状態をプログラムで確認する方法を学びます。

---

## **紹介**

このアーティクルでは、Excelワークシートの凍結状態をプログラム的に確認する方法を学びます。Excelではワークシートが凍結または分割されているかどうかを簡単に見つけられますが、Node.jsを使って凍結または分割されているかどうかを調べる方法はありますか？これもAspose.Cells for Node.js via C++で簡単にできます。

## **ウィンドウペインは凍っていますか**
Aspose.Cells for Node.js via C++を使えば、ウィンドウが凍結されているかどうか、またどれだけの行と列がロックされているかを確認できます。

ウインドウのペインの状態やロックされている行列を取得するには、[**Worksheet.getFreezedPanes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getFreezedPanes--)メソッドとともに[**Worksheet.getPaneState()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getPaneState--)プロパティを使用してください。
1. ファイルを開くためのワークブックを作成します。
2. ワークシートが凍結しているかどうかを確認します。
3. ロックされている行と列を取得します。

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Frozen.xlsx");

// Loads the workbook which contains frozen panes
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Check whether worksheet is frozen.
if (sheet.getPaneState() === AsposeCells.PaneStateType.Frozen || sheet.getPaneState() === AsposeCells.PaneStateType.FrozenSplit) {
let row, column, rows, columns;
// Gets locked rows and columns.
sheet.getFreezedPanes().forEach((value) => {
row = value[0];
column = value[1];
rows = value[2];
columns = value[3];
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
