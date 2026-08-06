---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Node.js via Java を使用してピボットテーブル内のページフィールド領域のレイアウトを制御する方法を学びます。ピボットテーブル上部のページフィールドの表示順序、折り返し数、フィールド順序の設定を含みます。
keywords: Aspose.Cells, Node.js via Java ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
この記事は「**ピボットテーブルにページフィールドを追加**」トピックの続きです。ピボットテーブル上部にあるフィルターコントロールの帯であるページフィールド領域のレイアウトを、表示順序、折り返し数、フィールドの並び替えを含めて制御する方法を説明します。
{{% /alert %}}
## **はじめに**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上部に位置する専用の**ページフィールド領域**があります。この領域はドロップダウンフィルターコントロールの帯（ページフィールドごとに 1 つ）としてレンダリングされ、エンドユーザーが年や地域などの条件でピボットをスライスするためにクリックする部分です。Aspose.Cells はこの領域を `PivotTable.PageFields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `PivotTable.PageFieldOrder`（`Aspose.Cells.PrintOrderType` 値）は、追加のページフィールドを既存のものの*横*に配置するか*下*に配置するかを決定します。
- `PivotTable.PageFieldWrapCount` は、折り返し前に 1 行または 1 列に配置されるページフィールドの数を設定します。
- `PivotTable.PageFields.Move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドの順序を変更します。
この記事では、共有データセットに対してこれらの各操作を示す 3 つのコード例を順を追って説明するため、結果として得られるレイアウトを並べて比較できます。
## **ソースデータ**
以下の 3 つの例すべては、これらの 8 行の売上データを `PivotData` という名前のワークシートにロードします。データには 2 つのページフィールド候補（`Year`、`Region`）、1 つの行フィールド候補（`Fruit`）、および 1 つのメジャー（`Amount`）が含まれており、ページフィールドの帯を検査するうえで意味のある構成になっています。
8 行すべてが各コード例で同じ順序で入力されるため、ソースデータはシナリオ間で変わることはなく、変わるのはページフィールドのレイアウトプロパティのみです。
## **例 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブル上部に**1 行に横並びで**表示するように設定します。`Fruit` を行軸に割り当て、ページ軸には `Year` を最初、`Region` を 2 番目に配置し（`addFieldToArea` 呼び出しの順序が開始インデックスを決定します）、`Amount`（Sum）をデータフィールドとして追加し、`PageFieldOrder` を `PrintOrderType.OVER_THEN_DOWN` に、`PageFieldWrapCount` を 2 に設定します。`OVER_THEN_DOWN` と折り返し数 2 により、2 つのページフィールドはピボットテーブル上部の 1 行に水平方向に横並びで配置されるため、帯は幅 2 の 1 行を占めます。
```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });

let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();

let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();

// ヘッダー（0行目）
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

// PivotTableReportシートを追加
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// PivotData!A1:D9をデータソースとするピボットテーブルをPivotTableReportのA1に作成
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// フィールドを追加
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// ページフィールド領域のレイアウトを設定: ページフィールドを最初に横に配置し、2つごとに折り返す
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// 更新して計算
pivotTable.calculateData();

// 保存
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **例 2: Down Then Over**
この例では、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を最初に）、`Amount`（Sum）をデータフィールドとして配置します — これは例 1 とまったく同じです。次に `PageFieldOrder` を `PrintOrderType.DOWN_THEN_OVER` に、`PageFieldWrapCount` を 2 に設定します。`DOWN_THEN_OVER` と折り返し数 2 により、2 つのページフィールドは垂直方向に積み重なります — `Year` が上、`Region` がすぐ下 — ピボットテーブル上部に単一列を形成します。したがって、帯は例 1 とは対照的に、幅 1 の 2 行を占めます。
```javascript
= new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);

var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}

var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];

for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}

var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);

pivotTable.calculateData();

workbook.save("pageFieldLayout_downThenOver.xlsx");
```
## **例 3: ページフィールドの移動**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト（折り返し数 2 の `OVER_THEN_DOWN`）を設定してから、`PageFields.Move` 操作を実演します。`Move(0, 1)` 呼び出しは、インデックス 0 のページフィールド（`Year`）を位置 1 に移動し、位置 1 にあったページフィールド（`Region`）を位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が 2 番目になります。折り返しと順序モードは変更されていないため、帯は依然として水平方向に横並びでレンダリングされます — 2 つのドロップダウンの順序のみが入れ替わっています。
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

pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);

pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

pivotTable.getPageFields().move(0, 1);

pivotTable.calculateData();

workbook.save("pageFieldLayout_move.xlsx");
```
## **関連記事**
- [ピボットテーブルにページフィールドを追加](/cells/ja/nodejs-java/add-page-field-in-pivot-table/) — ピボットテーブルにページフィールドを追加する方法を紹介する親ページ。
- [ピボットテーブルの行と列のフィールド](/cells/ja/nodejs-java/row-and-column-fields/) — ここでのページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドを管理する](/cells/ja/nodejs-java/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ（値）領域の構成方法について説明します。
- [ピボットテーブルを更新する](/cells/ja/nodejs-java/refresh-pivot-table/) — ページフィールドの順序変更後に必要な `refreshData` と `calculateData` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/nodejs-java/apply-style-to-pivot-table/) — ページフィールドの帯が配置された後にレンダリングされたピボットテーブルを書式設定する方法を示します。
{{< app/cells/assistant language="nodejs-java" >}}