---
title: ピボットテーブルで上位10件の表示またはフィルター
linktitle: ピボットテーブルで上位10件の表示またはフィルター
description: Aspose.Cells for .Net を使用すると、ピボットフィールドを基準として上位または下位の項目だけを表示する方法を学びます。このdrvパートでは、Excel 97-2003 の Top10AutoShow メソッド、Top10AutoShowSettings によるオプションの読み取り、FilterTop10 による Excel 2007-365 の上位10件フィルターについて説明します。
keywords: Aspose.Cells, .NET, ピボットテーブル, 上位10件, 自動表示, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /ja/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用可能なシナリオ**
行フィールドのすべての項目を一覧表示するピボットテーブルは、そのフィールドに数十個の項目がある場合に読みにくくなることがあります。上位10件レポートでは、順位が上位または下位の項目だけを残せるため、「売上上位5つの製品」や「販売件数下位3つの地域」などの順位レポートに最適です。Aspose.Cells は2つのメカニズムをサポートしており、それぞれ Microsoft Excel の2つの世代に対応します。
- **Excel 97-2003 の AutoShow** — `PivotField.Top10AutoShow()` メソッドです。これは、ピボットフィールドに直接保存される従来の「上位/下位 N 項目を表示」設定です。元のピボットテーブル形式の一部であるため、新旧を問わず、すべての Excel バージョンで機能します。
- **Excel 2007-365 の上位10件フィルター** — `PivotField.FilterTop10()` メソッドです。これは、フィールドメニューの「値フィルター」に含まれる新しい上位10件値フィルターです。フィールドに添付された `PivotFilter` オブジェクトとして保存され、項目数またはパーセントに基づく順位付けを提供します。

## **Excel 97-2003 での上位10件表示 (Top10AutoShow)**
従来の AutoShow は、`PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)` を1回呼び出すことで設定します。
- `isAutoShow` — フィールドの AutoShow 設定を有効または無効にします。
- `isTop` — `true` の場合は順位が上位の項目（上位）を保持し、`false` の場合は順位が下位の項目（下位）を保持します。
- `count` — 保持する項目数です。たとえば、従来の上位10件レポートでは 10 を指定します。
- `rankBy` — 項目を順位付けする **値フィールド** の0始まりのインデックスです。フィールド自体を基準に項目を順位付けする場合は -1 を指定します。
順位付けの基準は値フィールドまたはフィールド自体にできます。以下に、代表的な2つの形式を示します。

### **値フィールドを基準に順位付け**
行フィールドの項目を、「Sales の合計」のような値フィールドの値に基づいて順位付けします。次の例では、行フィールド1つ (`Sport`) と値フィールド1つ (`Sales`) を備えたピボットテーブルを作成し、`Sales` の値に基づく上位2つのスポーツを表示します。`rankBy` が 0 なのは、「Sales の合計」がインデックス 0 の値フィールドだからです。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// "Sum of Sales"（データフィールドのインデックス 0）に基づいて、上位 2 項目を表示する
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **フィールド自体を基準に順位付け**
フィールド自体を基準に順位付けすることもできます。この場合は `rankBy` に -1 を指定します。この形式では追加の値フィールドは不要であり、フィールドを行領域（または列領域）に配置するだけです。次の例では、フィールド自体を基準に下位3つのスポーツを表示します。この設定を保存すると、-1 はこの形式における既定値であるため、`rankBy` 属性はピボットテーブル XML から省略されます。また、`Top10AutoShowSettings.RankBy` を読み取ると -1 が返されます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// フィールド自体に基づいて順位付けされた下位3項目を表示 (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **現在のオプションの読み取り (Top10AutoShowSettings)**
`PivotField.Top10AutoShowSettings` プロパティは、フィールドに現在保存されている AutoShow オプションを表す `PivotFieldTop10AutoShowSettings` オブジェクトを返します。これを使って、既存のワークブック、または設定したばかりのピボットテーブルが項目をどのように表示するかを確認できます。ファイルから読み込んだワークブックも対象です。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

4つのプロパティは、ピボットテーブル XML に書き込まれる従来の AutoShow 属性（`autoShow`、`topAutoShow`、`itemPageCount`、`rankBy`）と対応しています。したがって、読み取られる値は、すべての Excel バージョンで適用される値になります。

## **注意**

{{% alert color="primary" %}}
- `PivotField` の直接プロパティである `IsAutoShow`、`IsAscendShow`、`AutoShowCount`、`AutoShowField` は、非推奨として示されています。代わりに `Top10AutoShowSettings` オブジェクトを使用してください。`IsAutoShow` は `Top10AutoShowSettings.IsAutoShow`、`IsAscendShow` は `Top10AutoShowSettings.IsTop`、`AutoShowCount` は `Top10AutoShowSettings.AutoShowCount`、`AutoShowField` は `Top10AutoShowSettings.RankBy` に相当します。設定を変更する方法としてサポートされているのは `Top10AutoShow()` メソッドです。
- `Top10AutoShow` は行フィールドと列フィールドで機能します。ページ（フィルター）領域のみにあるフィールドは、その項目がピボットテーブルの本体領域に配置されないため、この方法では順位付けできません。
{{% /alert %}}

## **Excel 2007-365: 上位10件フィルター (FilterTop10)**
新しいバージョンの Excel では、フィールドメニューの「値フィルター」→「上位10件...」から、上位10件を値フィルターとして利用できます。Aspose.Cells は、作成された `PivotFilter` を返す `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` メソッドでこの機能に対応しています。
- `valueFieldIndex` — 集計値に基づいて項目を順位付けする値フィールドの0始まりのインデックスです。
- `type` — `itemCount` の意味を決定します。`PivotFilterType.Count` は固定数の項目を保持します（ダイアログの「項目」オプション）。`PivotFilterType.Percent` は項目の割合を保持するため、`itemCount` には割合自体を指定します。つまり、30 を指定すると上位30パーセントを保持します。`PivotFilterType.Sum` は累積値に基づいて項目を順位付けします。
- `isTop` — `true` の場合は上位、`false` の場合は下位です。
- `itemCount` — 上位N件におけるNの値です。単位は `type` によって決まります。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Top 10 フィルター — "Sum of Sales" に基づいて上位 2 項目を保持（データフィールドインデックス 0）
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// 代わりにパーセントベースのフィルターを使用する場合は、項目の上位 30 パーセントを保持します:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` と `FilterTop10` は別の機能です。AutoShow はピボットフィールドに設定される従来の `autoShow` 属性群を書き込むため、Excel 97 以降のすべての Excel バージョンで適用されます。`FilterTop10` は新しい `PivotFilter` エントリを書き込むため、Excel 2007 以降が必要です。古いバージョンの Excel でワークブックを開くと、この新しいフィルターを使用するピボットテーブルは、すべての項目を表示します。旧来のツールとの往復処理が必要なドキュメントでは `Top10AutoShow` を、新しいバージョンのワークブックでは他の値フィルターと組み合わせられる `FilterTop10` を使用してください。
{{% /alert %}}

## **関連記事**
- [ラベルまたは値でピボットテーブルをフィルター処理](/cells/ja/net/filter-by-label-or-value-of-pivot-table/)
- [ピボットテーブルに行と列のフィールドを追加](/cells/ja/net/pivot-table-add-row-and-column-fields/)
- [ピボットテーブルでピボットフィールドをグループ化](/cells/ja/net/group-pivot-fields-in-the-pivot-table/)
- [ピボットテーブルを更新](/cells/ja/net/refresh-pivot-table/)
- [ピボットテーブルにページフィールドを追加](/cells/ja/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}