---
title: Node.jsとC++を使用したExcelワークシートの画面分割
linktitle: 画面分割
type: docs
weight: 190
url: /ja/nodejs-cpp/how-to-split-screen-of-excel-worksheet
description: この記事では、ワークシートを二つまたは四つに分割し、特定の行や列を別のペインに表示する方法を学びます。Node.js C++アドオンを使用してプログラム的に実行します。
keywords: 最上行の固定、最上行の固定
---

## **紹介**

この記事では、大規模なデータセットを操作する際に、同じワークシートの異なる部分を比較するために、2つまたは4つに分割して表示する方法を学びます。分割表示機能はあなたのニーズに応えます。

## **Excelで画面を分割する方法**
ワークシートを2つまたは4つの部分に分割するには、次のようにします:

1. 分割を配置したい行/列/セルを選択します。
2. [表示]タブの[ウィンドウ]グループで、[分割]ボタンをクリックします。

**![画面分割](Split-Screen.png)**

## **列単位でワークシートを分割**

スプレッドシートの2つの領域を垂直に分割するには、分割を表示したい列の右側の列を選択し、Excelの[分割]ボタンをクリックします。

Aspose.Cells for Node.js via C++を使用して垂直にワークシートを分割するのは簡単です。最初行のセルをアクティブセルとして選択し、[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)メソッドで分割します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets C1 cell in the top row as the active cell.
sheet.setActiveCell("C1");

// Split worksheet vertically on columns
sheet.split();
```

## **行単位でワークシートを分割**
Excelウィンドウを水平に分割するには、Excelで分割が発生する行の下の行を選択します。

Aspose.Cells for Node.js via C++を使った水平分割も簡単です。左列のセルをアクティブにして選択し、[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)メソッドで分割します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets A6 cell in the left column as the active cell.
sheet.setActiveCell("A6");

// Split worksheet horizontally on rows
sheet.split();

workbook.save("dest.xlsx");
```

## **ワークシートを4つの部分に分割する**
同じワークシートの4つの異なるセクションを同時に表示するには、Excelで画面を縦横に分割します。

Aspose.Cells for Node.js via C++を使えば、プログラム的にワークシートの列を垂直に分割するのは簡単です。アクティブセルは最初の行と列以外のセルを選択し、その後[**Worksheet.split()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#split--)メソッドで分割します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

const sheet = workbook.getWorksheets().get(0);

// Sets E6 cell as the active cell.
sheet.setActiveCell("E6");

// Split worksheet into four parts
sheet.split();
```

## **分割を削除する方法**
ワークシートの分割を解除するには、再び分割ボタンをクリックします。

Aspose.Cells for Node.js via C++は、分割設定を解除するための [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#removeSplit--) メソッドを提供します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Remove split.
sheet.removeSplit();

// Split worksheet into four parts
sheet.split();
```

{{< app/cells/assistant language="nodejs-cpp" >}}
