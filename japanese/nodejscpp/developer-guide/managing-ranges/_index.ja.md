---
title: Node.jsを通じて範囲を管理する方法
linktitle: 範囲
type: docs
weight: 105
url: /ja/nodejs-cpp/managing-ranges/
description: Aspose.Cells for Node.js via C++を使用してExcelの範囲を管理する方法を学びます。範囲の作成、値の設定、スタイルの適用、その他さまざまな操作を行います。
---

## **紹介**

Excelでは、マウスのボックス選択を使って複数のセルを選択でき、その選択範囲は「Range」と呼ばれます。

例として、Excelのセル「A1」で左クリックし、そのままセル「C4」までドラッグします。選択した矩形領域は、Aspose.Cells for Node.js via C++を使ってオブジェクトとして簡単に作成できます。

範囲を作成し、値を設定し、スタイルを適用し、その他さまざまな操作を行う方法です。

## **### Aspose.Cells for Node.js via C++を使った範囲の管理**

Aspose.Cellsは、Microsoft Excelファイルを表すクラス、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供しています。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)コレクションが含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスには[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションが提供されています。

### **範囲の作成**

A1:C4にまたがる長方形領域を作成する場合は、次のコードを使用できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **範囲のセルに値を入力する**

A1:C4にまたがるセルの範囲があるとします。行列は4*3=12セルを作ります。それぞれの範囲セルは順に配置されます: Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

次の例は、範囲のセルに値を入力する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **範囲のセルのスタイルを設定する**

次の例は、範囲内のセルのスタイルを設定する方法を示しています。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **範囲のCurrentRegionを取得する**

CurrentRegionは、現在の範囲を表すRangeオブジェクトを返すプロパティです。 

現在の領域は、空白の行と列の組み合わせによって囲まれた範囲です。読み取り専用です。

Excelでは、CurrentRegionエリアを次の方法で取得できます:
1. マウスボックスを使ってエリア（範囲1）を選択します。
2. 「ホーム - 編集 - 検索と選択 - 特定の場所に移動」をクリックするか、「Ctrl+Shift+*」を使用すると、Excelが自動的にエリア（範囲2）を選択します。これで範囲2は範囲1のCurrentRegionです。

以下のテストファイルをダウンロードし、Excelで開いて、マウスボックスを使ってエリア「A1:D7」を選択し、「Ctrl+Shift+*」をクリックすると、「A1:C3」エリアが選択されているのが見えます。

[current_region.xlsx](current_region.xlsx)

次に、以下の例を実行して、Aspose.Cellsでの動作を確認してください：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **高度なトピック**
- [ExcelファイルのAutoFill範囲](/cells/ja/nodejs-cpp/autofill-ranges/)
- [Excelの範囲をコピー](/cells/ja/nodejs-cpp/copy-ranges-of-Excel/)
- [Excelの範囲のデータをコピーする](/cells/ja/nodejs-cpp/copy-range-data-only/)
- [スタイルで範囲データをコピー](/cells/ja/nodejs-cpp/copy-range-data-with-style/)
- [ソースの範囲の行の高さのみをコピー](/cells/ja/nodejs-cpp/copy-range-style-only/)
- [ユニオン範囲の作成](/cells/ja/nodejs-cpp/create-union-range/)
- [範囲を切り取って貼り付ける](/cells/ja/nodejs-cpp/cut-and-paste-cells/)
- [範囲を削除する](/cells/ja/nodejs-cpp/delete-ranges-from-Excel/)
- [範囲のアドレス、セル数、オフセット、列全体、行全体を取得する](/cells/ja/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [範囲を挿入する](/cells/ja/nodejs-cpp/insert-ranges-to-Excel/)
- [セルの範囲を結合または結合解除する](/cells/ja/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [ワークシート内のセルの範囲を移動する](/cells/ja/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [ワークブックおよびワークシートスコープの名前付き範囲を作成する](/cells/ja/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [範囲内のデータを検索および置換する](/cells/ja/nodejs-cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="nodejs-cpp" >}}
