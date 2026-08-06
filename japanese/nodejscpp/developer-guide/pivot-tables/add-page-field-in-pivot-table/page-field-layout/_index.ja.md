---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Node.js via C++ を使用して、ピボットテーブル内のページフィールド領域のレイアウト（表示順、折り返し数、ページフィールドのフィールド順）を制御する方法を学びます。
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールド順, ページフィールド折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
このドキュメントは、**ピボットテーブルにページフィールドを追加する** トピックの続きです。ページフィールド領域のレイアウト、つまりピボットテーブル上部にあるフィルターコントロールの帯の表示順、折り返し数、フィールドの並び替えを制御する方法を説明します。
{{% /alert %}}
## **概要**
Microsoft Excel のピボットテーブルには、表の行/列/データ本体の上部に位置する専用の **ページフィールド領域** があります。この領域は、ドロップダウンフィルターコントロールの帯（ページフィールドごとに1つ）として描画され、エンドユーザーが年や地域などの基準でピボットをスライスするためにクリックする場所です。Aspose.Cells for Node.js via C++ はこの領域を `pivotTable.pageFields` コレクションでモデル化し、この帯の視覚的なレイアウトを制御する3つのプロパティを公開しています。
- `pivotTable.pageFieldOrder`（`Aspose.Cells.PrintOrderType` 値）は、追加のページフィールドを既存のフィールドの *隣* に配置するか、*下* に配置するかを決定します。
- `pivotTable.pageFieldWrapCount` は、折り返し前に1行または1列に配置されるページフィールドの数を設定します。
- `pivotTable.pageFields.move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドを並べ替えます。
このドキュメントでは、共有データセットに対してこれらの各操作を実演する3つのコード例を示し、結果として得られるレイアウトを並べて比較できるようにします。
## **ソースデータ**
以下の3つの例では、次の8行の売上データを `PivotData` という名前のワークシートに読み込みます。データには、2つのページフィールド候補（`Year`、`Region`）、1つの行フィールド候補（`Fruit`）、および1つのメジャー（`Amount`）が含まれており、ページフィールドの帯を検査する意味があります。
8行すべてがすべてのコード例で同じ順序で入力されるため、ソースデータはシナリオ間で異なることはありません。ページフィールドのレイアウトプロパティのみが異なります。
## **例1: Over Then Down（横優先）**
最初のシナリオでは、2つのページフィールド（`Year`、`Region`）をピボットテーブルの上部に **1行に横並びで** 表示するように設定します。`Fruit` を行軸に割り当て、`Year` をページ軸の最初に、`Region` を2番目に配置し（`addFieldToArea` の呼び出し順序が開始インデックスを決定します）、`Amount`（Sum）をデータフィールドとして追加し、`pageFieldOrder` を `PrintOrderType.OverThenDown` に、`pageFieldWrapCount` を `2` に設定します。`OverThenDown` と折り返し数2を使用すると、2つのページフィールドはピボットテーブルの上部で1行に横並びで配置され、帯は幅2の1行を占めます。
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// ヘッダー (行0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// 行1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// 行2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// 行3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// 行4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// 行5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// 行6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// 行7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// 行8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// PivotTableReport シートを追加
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// PivotData!A1:D9 をソースとし、PivotTableReport の A1 に配置するピボットテーブルを作成
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// フィールドを追加
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // フルーツ
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // 年
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // 地域
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // 金額
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// ページフィールド領域のレイアウトを設定: ページフィールドを横方向に先に配置し、2つごとに改行する
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// 更新して計算
pivotTable.calculateData();

// 保存
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **例2: Down Then Over（縦優先）**
この例では、例1とまったく同様に、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` が最初）、`Amount`（Sum）をデータフィールドとして配置します。次に、`pageFieldOrder` を `PrintOrderType.DownThenOver` に、`pageFieldWrapCount` を `2` に設定します。`DownThenOver` と折り返し数2を使用すると、2つのページフィールドは垂直に積み重ねられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブルの上部に1列を形成します。したがって、帯は例1とは対照的に、幅1で2行を占めます。
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);

const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

const data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **例3: ページフィールドの移動**
3番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト（折り返し数 `2` の `OverThenDown`）を設定してから、`pageFields.move` 操作を実演します。`move(0, 1)` 呼び出しは、インデックス0にあるページフィールド（`Year`）を位置1に移動し、位置1にあったページフィールド（`Region`）を位置0にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が2番目になります。折り返しと順序モードは変更されないため、帯はまだ横並びでレンダリングされます。2つのドロップダウンの順序のみが入れ替わります。
```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();

const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");

dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");

dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);

dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);

dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);

dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);

dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);

dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);

dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);

dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);

const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);

const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **関連記事**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/) — ページフィールドをピボットテーブルに追加する方法を紹介する親ページ。
- [ピボットテーブルの行と列フィールド](/cells/ja/nodejs-cpp/row-and-column-fields/) — ここで示すページ軸の作業を補完する、行と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドを管理する](/cells/ja/nodejs-cpp/manage-value-fields/) — このドキュメントで使用されている `Sum` 集計を含む、データ（値）領域の設定方法について説明します。
- [ピボットテーブルを更新する](/cells/ja/nodejs-cpp/refresh-pivot-table/) — ページフィールドを並べ替えた後に必要な `refreshData` と `calculateData` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/) — ページフィールドの帯がレイアウトされた後、レンダリングされたピボットテーブルを書式設定する方法を示します。
{{< app/cells/assistant language="nodejs-cpp" >}}