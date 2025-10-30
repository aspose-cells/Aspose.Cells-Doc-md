---
title: Node.jsとC++を使用したワークブックまたはシートの読み込み時にオブジェクトをフィルタ
linktitle: ワークブックまたはワークシートをロードする際にオブジェクトをフィルタリングする
type: docs
weight: 330
url: /ja/nodejs-cpp/filter-objects-while-loading-workbook-or-worksheet/
description: Aspose.Cells for Node.js via C++を利用して、ワークブックやシートのデータをフィルタする方法を学びます。
---

## **可能な使用シナリオ**
ワークブックからデータをフィルタリングするには、[LoadOptions.getLoadFilter()](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getLoadFilter--) プロパティを使用してください。ただし、個々のシートからデータをフィルタしたい場合は、[LoadFilter.startSheet(Worksheet)](https://reference.aspose.com/cells/nodejs-cpp/loadfilter/#startSheet-worksheet-) メソッドをオーバーライドする必要があります。[LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions)列挙体から適切な値を指定して、[LoadFilter](https://reference.aspose.com/cells/nodejs-cpp/loadfilter)を作成または操作してください。

[LoadDataFilterOptions](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions)の列挙値は次のとおりです。

- 全て
- ブック設定
- 空白セル
- ブールセル
- データセル
- エラーセル
- 数値セル
- 文字列セル
- 値セル
- Chart
- 条件付き書式
- データの検証
- 定義された名前
- ドキュメントのプロパティ
- 数式
- ハイパーリンク
- 結合エリア
- ピボットテーブル
- 設定
- 図形
- シートデータ
- シート設定
- 構造
- スタイル
- テーブル
- VBA
- XmlMap

## **ワークブックの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、ワークブックからグラフをフィルタリングする方法を示しています。このコードで使用されている[サンプルエクセルファイル](5115258.xlsx)とその生成された[出力PDF](5115257.pdf)を確認してください。出力PDFでは、すべてのグラフがワークブックからフィルタリングされていることが分かります。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Filter charts from the workbook.
const lOptions = new AsposeCells.LoadOptions();
lOptions.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart));

// Load the workbook with above filter.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleFilterCharts.xlsx"), lOptions);

// Save worksheet to a single PDF page.
const pOptions = new AsposeCells.PdfSaveOptions();
pOptions.setOnePagePerSheet(true);

// Save the workbook in PDF format.
workbook.save(path.join(dataDir, "sampleFilterCharts.pdf"), pOptions);
```

## **ワークシートの読み込み中にオブジェクトをフィルタリングする**
以下のサンプルコードは、[ソースエクセルファイル](5115255.xlsx)を読み込み、カスタムフィルタを使用してそのワークシートから以下のデータをフィルタリングする方法を説明しています。

- NoChartsという名前のワークシートからグラフをフィルタリングします。
- NoShapesという名前のワークシートから形状をフィルタリングします。
- NoConditionalFormattingという名前のワークシートから条件付き書式をフィルタリングします。

1つのカスタムフィルタで[ソースエクセルファイル](5115255.xlsx)を読み込むと、ワークシートを1つずつ画像化します。以下は参照用の出力画像です。最初の画像にはグラフがなく、2番目の画像には形状がなく、3番目の画像には条件付き書式がないことが分かります。

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```javascript
const AsposeCells = require("aspose.cells.node");

class CustomLoadFilter extends AsposeCells.LoadFilter {
startSheet(sheet) {
if (sheet.getName() === "NoCharts") {
// Load everything and filter charts
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Chart;
}

if (sheet.getName() === "NoShapes") {
// Load everything and filter shapes
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.Drawing;
}

if (sheet.getName() === "NoConditionalFormatting") {
// Load everything and filter conditional formatting
this.loadDataFilterOptions = AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.ConditionalFormatting;
}
}
}
```

ワークシート名に従ってCustomLoadFilterクラスを使用する方法

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function run() {
// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Filter worksheets using CustomLoadFilter class
const loadOpts = new AsposeCells.LoadOptions();
loadOpts.setLoadFilter(new CustomLoadFilter());

// Load the workbook with filter defined in CustomLoadFilter class
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleCustomFilteringPerWorksheet.xlsx"), loadOpts);

// Take the image of all worksheets one by one
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
// Access worksheet at index i
const worksheet = workbook.getWorksheets().get(i);

// Create an instance of ImageOrPrintOptions
// Render entire worksheet to image
const imageOpts = new AsposeCells.ImageOrPrintOptions();
imageOpts.setOnePagePerSheet(true);
imageOpts.setImageType(AsposeCells.ImageType.Png);

// Convert worksheet to image
const render = new AsposeCells.SheetRender(worksheet, imageOpts);
render.toImage(0, path.join(outputDir, `outputCustomFilteringPerWorksheet_${worksheet.getName()}.png`));
}
}

run();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
