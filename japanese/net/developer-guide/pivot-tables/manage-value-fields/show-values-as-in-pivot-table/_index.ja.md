---
title: ピボットテーブルでの「Show Values As」機能
linktitle: ピボットテーブルでの「Show Values As」機能
description: Aspose.Cells for .NET を使用して、ピボットテーブルのデータ フィールドの値を合計に対するパーセンテージ、ベース項目との差、累計、順位などとして表示できます。
keywords: Aspose.Cells, ピボットテーブル, 値の表示形式, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, C#
type: docs
weight: 145
url: /ja/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` などの集計関数で各データ フィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算に置き換えます。たとえば、総計に対するパーセンテージ、累計、選択したベース項目との差、または順位などで表示し、ヘルパー式や計算列を使用せずに比較分析を実行できます。  
典型的な使用例として、行・列・総計のパーセンテージを含む全体比率分析、期間フィールドでの累計を使用した累積レポート、ベース項目との差またはパーセンテージ差を使用したベンチマーク項目に対する変動分析、そして最小から最大、または最大から最小への順位付けがあります。  
Aspose.Cells for .NET では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.ShowValuesSetting` プロパティは `PivotShowValuesSetting` オブジェクトを返し、書き込み可能な `CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex` プロパティで動作を設定します。便利メソッド `PivotField.ShowValuesAs(...)` は同じ 4 つの設定を一度の呼び出しで適用します。これらの設定は `PivotTable.DataFields` から取得したデータ フィールドまたは値フィールドに適用してください。

## **PivotFieldDataDisplayFormat 列挙体のメンバー**
データ フィールドは Sum や Count などの集計関数を保持しますが、Show Values As は集計された値の表示方法のみを変換します。  
`PivotShowValuesSetting` プロパティを直接設定する（最後のセクションを参照）以外に、ワンコールの便利メソッドで同じ構成を適用できます。

```csharp
public void ShowValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField, PivotItemPositionType baseItemPositionType, int baseItem)
```

| パラメータ | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | `PivotFieldDataDisplayFormat` の二次計算を適用します。 | 常に |
| `baseField` | ピボットテーブルのベース フィールドの中でのベース フィールドのゼロベースインデックス（例: ベース項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | ベース項目が現在の項目に対してどのように選択されるか：`PivotItemPositionType.Previous`、`.Next`、または `.Custom`。 | 3 つの基準項目フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | ベース項目のゼロベースインデックス。 | `baseItemPositionType` が `Custom` の場合にのみ必要です（項目インデックスで正確なベース項目を指定）。`Previous` / `Next` およびベース項目以外の形式では無視されます — `0` を渡してください。 |

| 計算タイプ | 動作 | ベース項目パラメータ |
| --- | --- | --- |
| `Normal` | 二次計算なし；集計値はそのまま表示されます（デフォルト）。 | — |
| `DifferenceFrom` | ベース フィールドのベース項目の値との差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（Custom の場合のみ `baseItem`） |
| `PercentageOf` | ベース フィールドのベース項目の値に対するパーセンテージとして表示します。 | `baseField` + `Previous`/`Next`/`Custom`（Custom の場合のみ `baseItem`） |
| `PercentageDifferenceFrom` | ベース フィールドのベース項目の値に対するパーセンテージ差として表示します。 | `baseField` + `Previous`/`Next`/`Custom`（Custom の場合のみ `baseItem`） |
| `RunningTotalIn` | ベース フィールドの連続項目に対する累計として表示します。 | `baseField`（項目の順序が累積を決定するフィールド） |
| `PercentageOfRow` | 行合計のパーセンテージとして表示します。 | — |
| `PercentageOfColumn` | 列合計のパーセンテージとして表示します。 | — |
| `PercentageOfTotal` | 総計のパーセンテージとして表示します。 | — |
| `Index` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) を使用して値を表示します。 | — |
| `PercentageOfParentRowTotal` | 親行合計のパーセンテージとして表示します。 | — |
| `PercentageOfParentColumnTotal` | 親列合計のパーセンテージとして表示します。 | — |
| `PercentageOfParentTotal` | 親合計のパーセンテージとして表示します。 | `baseField`（基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | ベース フィールドの累計に対するパーセンテージとして表示します。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 最小 (1) から最大へ順位付けします。 | — |
| `RankLargestToSmallest` | 最大 (1) から最小へ順位付けします。 | — |

{{% alert color="primary" %}}
`ShowValuesAs(...)` は `PivotShowValuesSetting` プロパティ（`CalculationType`、`BaseFieldIndex`、`BaseItemPositionType`、`BaseItemIndex`）を書き込みます。メソッドとプロパティ オブジェクトは同じ状態を構成する 2 つの方法であり、Excel の Show Values As ダイアログのベース フィールドとベース項目ピッカーを反映しています。
{{% /alert %}}

## **総計に対するパーセンテージとして値を表示**
`PivotField.ShowValuesAs` メソッドに `PivotFieldDataDisplayFormat.PercentageOfTotal` を指定して呼び出すと、総計を含むすべてのデータ フィールド セルを総計に対する比率に変換します。表示される数値は全結果セットの割合として解釈されます。この形式はすべての値を総計のみで測定するため、ベース フィールドやベース 項目は不要です — 後続の引数（`0`、`PivotItemPositionType.Previous`、`0`）は、フォーマットが無視するプレースホルダーです（上記パラメータ表参照）。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Amount");
string[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.Length; i++)
{
    dataSheet.Cells[i + 1, 0].PutValue(fruits[i]);
    dataSheet.Cells[i + 1, 1].PutValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.Worksheets.Add();
PivotTable pivotTable = workbook.Worksheets[pivotSheetIndex].PivotTables.Add("=Sheet1!A1:B7", 2, 2);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.PercentageOfTotal, 0, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.ShowValuesSetting の取得と構成**
`PivotField.ShowValuesSetting` を介して現在の構成を取得します。読み取り専用プロパティはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティで現在の Show Values As 計算を表します。構成を変更するには `PivotField.ShowValuesAs` メソッドを呼び出します — 1 回の呼び出しで 4 つの設定すべてを書き込むため、プロパティを個別に設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトは `ShowValuesAs` が書き込む 4 つのプロパティを公開します：
- `CalculationType` は `PivotFieldDataDisplayFormat` の二次計算を選択します。
- `BaseFieldIndex` はピボットテーブルのフィールド内のベース フィールドのゼロベースインデックスを指定します。基準関連フォーマットで使用されます。
- `BaseItemPositionType` はベース項目が現在の項目に対してどの位置にあるかを決定し、`PivotItemPositionType.Next`、`PivotItemPositionType.Previous`、または `PivotItemPositionType.Custom` を受け入れます。
- `BaseItemIndex` はゼロベースのベース項目インデックスを指定し、`BaseItemPositionType` が `Custom` の場合に使用されます。  
`ShowValuesAs` を呼び出した後、`PivotTable.CalculateData()` を再度呼び出して、ピボット本体を再計算および再描画し、更新された構成を反映させます。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"CalculationType: {settings.CalculationType}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemPositionType: {settings.BaseItemPositionType}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotItemPositionType.Previous, 0);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"CalculationType now: {dataField.ShowValuesSetting.CalculationType}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/net/manage-value-fields/)
- [ピボットテーブルの DataField のデータ表示形式の操作](/cells/ja/net/working-with-data-display-forms-of-datafield-in-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/net/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}