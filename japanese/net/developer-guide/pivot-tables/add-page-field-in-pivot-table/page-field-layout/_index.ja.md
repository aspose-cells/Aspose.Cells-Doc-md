---
title: ピボットテーブルでページフィールドのレイアウトを変更する
linktitle: ピボットテーブルでページフィールドのレイアウトを変更する
description: Aspose.Cells for .NET を使用してピボットテーブル内のページフィールド領域のレイアウトを制御する方法を学びます。ページフィールドの表示順、折り返し数、ピボットテーブル上部でのページフィールドの順序の設定を含みます。
keywords: Aspose.Cells, .NET ライブラリ, スプレッドシート, ピボットテーブル, ページフィールド, ページフィールドの順序, ページフィールドの折り返し数, ページフィールドの移動
type: docs
weight: 191
url: /ja/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

この記事は「**ピボットテーブルにページフィールドを追加する**」トピックの続編です。ピボットテーブル上部にあるフィルターコントロールの帯であるページフィールド領域のレイアウトを、表示順、折り返し数、フィールドの並び替えを含めて制御する方法を説明します。

{{% /alert %}}

## **はじめに**

Microsoft Excel のピボットテーブルには、テーブルの行/列/データ本体の上部に配置される専用の **ページフィールド領域** があります。この領域はページフィールドごとに 1 つずつのドロップダウンフィルターコントロールの帯として表示され、エンドユーザーが年や地域などの条件でピボットを絞り込むためにクリックする部分です。Aspose.Cells ではこの領域を `PivotTable.PageFields` コレクションでモデル化し、帯の視覚的なレイアウトを制御する 3 つのプロパティを公開しています。

- `PivotTable.PageFieldOrder`（`Aspose.Cells.PrintOrderType` 値）は、追加のページフィールドを既存のフィールドの **横** に配置するか、**下** に配置するかを決定します。
- `PivotTable.PageFieldWrapCount` は、折り返す前に行または列ごとに配置するページフィールドの数を設定します。
- `PivotTable.PageFields.Move(currIndex, destIndex)` は、順序モードを変更せずにページフィールドの並び順を変更します。

この記事では、共通のデータセットに対してこれらの各操作を示す 3 つのコード例を順に説明し、結果を並べて比較できるようにします。

## **ソースデータ**

以下の 3 つの例では、これら 8 行の売上データを `PivotData` という名前のワークシートに読み込みます。データには 2 つのページフィールド候補（`Year`、`Region`）、1 つの行フィールド候補（`Fruit`）、および 1 つのメジャー（`Amount`）が含まれており、ページフィールドの帯を検査する意味のあるものになっています。

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

すべてのコード例で 8 行すべてが同じ順序で入力されているため、ソースデータはシナリオ間で変わることはありません。変わるのはページフィールドのレイアウトプロパティのみです。

## **例 1: Over Then Down**

最初のシナリオでは、2 つのページフィールド（`Year`、`Region`）をピボットテーブル上部の **単一行に横に並んで** 表示するように構成します。`Fruit` を行軸に割り当て、ページ軸には `Year` を最初に、`Region` を 2 番目に配置し（`AddFieldToArea` の呼び出し順序が開始インデックスを決定します）、`Amount`（Sum）をデータフィールドとして追加します。次に `PageFieldOrder` を `PrintOrderType.OverThenDown` に設定し、`PageFieldWrapCount` を `2` に設定します。`OverThenDown` と折り返し数 2 の組み合わせにより、2 つのページフィールドはピボットテーブル上部の単一の行に横に並んで配置されるため、帯は幅 2 の 1 行を占めます。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;

int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;

// ヘッダー (0行目)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// 1行目: リンゴ, 2022, 北, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// 2行目: リンゴ, 2023, 北, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// 3行目: バナナ, 2022, 南, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// 4行目: バナナ, 2023, 南, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// 5行目: さくらんぼ, 2022, 東, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// 6行目: さくらんぼ, 2023, 東, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// 7行目: ぶどう, 2022, 西, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// 8行目: ぶどう, 2023, 西, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// PivotTableReportシートを追加
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// PivotData!A1:D9 をデータソースとし、PivotTableReport の A1 に配置されるピボットテーブルを作成
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// フィールドを追加
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // 果物
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // 年
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // 地域
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // 金額
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// ページフィールド領域のレイアウトを設定: ページフィールドを横方向に先に配置し、2 つごとに折り返す
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// 更新と計算
pivotTable.CalculateData();

// 保存
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **例 2: Down Then Over**

この例では、例 1 と同様に `Fruit` を行軸に、`Year` と `Region` をページ軸に（`Year` を最初に）、`Amount`（Sum）をデータフィールドとして配置します。次に `PageFieldOrder` を `PrintOrderType.DownThenOver` に、`PageFieldWrapCount` を `2` に設定します。`DownThenOver` と折り返し数 2 の組み合わせにより、2 つのページフィールドは縦に積み重ねられ、`Year` が上、`Region` がその直下に配置され、ピボットテーブル上部に 1 つの列を形成します。したがって、帯は例 1 とは対照的に、幅 1 の 2 行を占めます。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];

var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}

var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};

for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}

int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **例 3: ページフィールドの移動**

3 番目のシナリオでは、このデータセットとフィールドの割り当てを維持し、中立的なレイアウト（折り返し数 `2` の `OverThenDown`）を設定してから、`PageFields.Move` 操作を示します。`Move(0, 1)` の呼び出しにより、インデックス 0（`Year`）のページフィールドが位置 1 に移動し、位置 1 にあったページフィールド（`Region`）が位置 0 にシフトします。この呼び出しの後、`Region` が最初のページフィールドになり、`Year` が 2 番目になります。折り返しと順序モードは変更されていないため、帯は依然として横に並んでレンダリングされます。2 つのドロップダウンの順序のみが入れ替わっています。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();

Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";

dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");

dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);

dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);

dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);

dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);

dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);

dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);

dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);

dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);

int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];

int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];

pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);

pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

pivotTable.PageFields.Move(0, 1);

pivotTable.CalculateData();

workbook.Save("pageFieldLayout_move.xlsx");
```

## **関連記事**

- [ピボットテーブルにページフィールドを追加する](/cells/ja/net/add-page-field-in-pivot-table/) — ピボットテーブルへのページフィールドの追加方法を紹介する親ページです。
- [ピボットテーブルの行フィールドと列フィールド](/cells/ja/net/pivot-table-add-row-and-column-fields/) — ここで示されているページ軸の作業を補完する、行軸と列軸へのフィールドの割り当てについて説明します。
- [ピボットテーブルの値フィールドの管理](/cells/ja/net/manage-value-fields/) — この記事で使用されている `Sum` 集計を含む、データ（値）領域の構成方法について説明します。
- [ピボットテーブルを更新する](/cells/ja/net/refresh-pivot-table/) — ページフィールドの並べ替え後に必要な `RefreshData` と `CalculateData` について説明します。
- [ピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/) — ページフィールドの帯が配置された後に、レンダリングされたピボットテーブルを書式設定する方法を示します。

{{< app/cells/assistant language="csharp" >}}