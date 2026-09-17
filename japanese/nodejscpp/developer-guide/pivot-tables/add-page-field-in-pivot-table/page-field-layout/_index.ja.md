---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for Node.js via C++ を使用して、ピボットテーブルのページフィールド領域のレイアウト（表示順、折り返し数、ピボットテーブル上部にあるページフィールドのフィールド順）を制御する方法を学びます。
keywords: Aspose.Cells, Node.js via C++ ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
この記事は「**ピボットテーブルにページフィールドを追加する**」トピックの続きです。ページフィールド領域（ピボットテーブル上部に表示されるフィルタコントロールの帯）のレイアウトを、表示順、折り返し数、フィールドの並べ替えを含めて制御する方法を説明します。
{{% /alert %}}

## **Introduction**
Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上部に位置する専用の**ページフィールド領域**があります。この領域はページフィールドごとに 1 つずつのドロップダウンフィルタコントロールの帯としてレンダリングされ、エンドユーザーが年や地域などの条件でピボットをスライスする際にクリックする場所です。Aspose.Cells for Node.js via C++ はこの領域を `pivotTable.pageFields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。
- `pivotTable.pageFieldOrder`（`Aspose.Cells.PrintOrderType` の値）は、追加のページフィールドを既存のフィールドの*横*に配置するか、*下*に配置するかを決定します。
- `pivotTable.pageFieldWrapCount` は、折り返し前に行または列ごとに配置されるページフィールドの数を設定します。
- `pivotTable.pageFields.move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドの順序を変更します。
この記事では、共有データセットに対してこれら 3 つの操作をそれぞれ示す 3 つのコード例を通じて、結果を並べて比較できるようにします。

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
8 行すべてがすべてのコード例で同一の順序で入力されているため、シナリオ間でソースデータが異ることはなく、異なるのはページフィールドのレイアウトプロパティのみです。

## **Example 1: Over Then Down**
最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブルの上部に**単一の行で横並びに**表示するよう設定します。`Fruit` を行軸に割り当て、`Year` を最初、`Region` を 2 番目にページ軸に配置し（`addFieldToArea` の呼び出し順序が開始インデックスを決定します）、データフィールドとして `Amount`（Sum）を追加し、`pageFieldOrder` を `PrintOrderType.OverThenDown` に、`pageFieldWrapCount = 2` に設定します。`OverThenDown` と折り返し数 2 の組み合わせにより、2 つのページフィールドはピボットテーブル上部の単一の行に水平方向に横並びで配置されるため、帯は幅 2 の 1 行を占めます。

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
// Headers (row 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Row 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Row 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Row 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Row 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Row 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Row 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Row 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Row 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// Add PivotTableReport sheet
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();
// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
// Add fields
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// Refresh and calculate
pivotTable.calculateData();
// Save
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**
この例では、例 1 と同様に、`Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` が最初）、データフィールドとして `Amount`（Sum）を配置します。次に、`pageFieldOrder` を `PrintOrderType.DownThenOver` に、`pageFieldWrapCount` を `2` に設定します。`DownThenOver` と折り返し数 2 の組み合わせにより、2 つのページフィールドは垂直方向に積み上げられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブルの上部に 1 列を形成します。したがって、帯は幅 1 で 2 行を占め、例 1 とは対照的になります。

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

## **Example 3: Move a Page Field**
3 番目のシナリオでは、このデータセットとフィールド割り当てを維持し、中立的なレイアウト（折り返し数 `2` の `OverThenDown`）を設定してから、`pageFields.move` 操作を示します。`move(0, 1)` の呼び出しは、インデックス 0 にあるページフィールド（`Year`）を位置 1 に移動し、位置 1 にあったページフィールド（`Region`）を位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドとなり、`Year` が 2 番目になります。折り返しと順序モードは変更されていないため、帯は依然として横方向に並んでレンダリングされ、2 つのドロップダウンの順序のみが入れ替わっています。

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

## **Related Articles**
- [ピボットテーブルにページフィールドを追加する](/cells/ja/nodejs-cpp/add-page-field-in-pivot-table/) — ページフィールドをピボットテーブルに追加する方法を紹介する親ページです。
- [ピボットテーブルの行と列のフィールド](/cells/ja/nodejs-cpp/row-and-column-fields/) — ここで示したページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルで値フィールドを管理する](/cells/ja/nodejs-cpp/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ（値）領域の設定方法を説明します。
- [ピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/) — ページフィールドの並べ替え後に必要な `refreshData` と `calculateData` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/) — ページフィールドの帯をレイアウトした後、レンダリングされたピボットテーブルを書式設定する方法を示します。

{{< app/cells/assistant language="nodejs-cpp" >}}