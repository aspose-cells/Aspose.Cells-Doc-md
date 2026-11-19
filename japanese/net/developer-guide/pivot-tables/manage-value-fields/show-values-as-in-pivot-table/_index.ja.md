---
title: ピボットテーブルで値を表示
linktitle: ピボットテーブルで値を表示
description: Aspose.Cells for .NET を使用して、ピボットテーブルのデータフィールドの値を、総合計に対する割合、基準項目との差、累計、順位などの形式で表示します。
keywords: Aspose.Cells, ピボットテーブル, 値表示, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, ShowValuesAs, BaseFieldIndex, BaseItemIndex, C#
type: docs
weight: 145
url: /ja/net/show-values-as-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ピボットテーブルでは通常、`Sum` や `Count` などの集計関数を使って各データフィールドを集計します。Excel の **値表示** 機能は、各表示結果を、その集計値に基づく二次計算の結果に置き換えます。たとえば、総合計に対する割合、累計、選択した基準項目との差、順位などを表示できるため、補助の数式や計算列を用意せずに比較分析を実行できます。
代表的な用途には、構成比分析（行、列、または総合計に対する割合）、期間フィールドで累計値を使用する累積レポート、基準項目との差や差の割合を使ってベンチマーク項目との差異を分析する比較分析、および値の小さい順から大きい順、または大きい順から小さい順への順位付けがあります。
Aspose.Cells for .NET では、`PivotShowValuesAsType` 列挙型で二次計算を選択します。読み取り専用の `PivotField.ShowValuesSetting` プロパティは `PivotShowValuesSetting` オブジェクトを返し、その書き込み可能な `ShowValuesAs`、`BaseFieldIndex`、`BaseItemIndex` プロパティを設定して動作を構成できます。簡易メソッド `PivotField.ShowValuesAs(...)` を使用すると、同じ設定を一度の呼び出しで適用できます。これらの設定は、`PivotTable.DataFields` から取得したデータフィールドまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙型のメンバー**
データフィールドは `Sum` や `Count` などの集計関数を保持し、「値表示」では、集計値そのものではなく、その表示方法だけが変更されます。
また、`PivotShowValuesSetting` のプロパティを直接設定する代わりに（最後のセクションを参照）、一度の呼び出しで同じ設定を適用できる簡易メソッドがあります。このメソッドには 2 つのオーバーロードがあり、それぞれ添字または名前で基準フィールドと基準項目を指定します。

```csharp
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
public void ShowValuesAs(PivotShowValuesAsType showValuesAsType, string baseField, string baseItem)
```

| パラメーター | 意味 | 必要な場合 |
| --- | --- | --- |
| `showValuesAsType` | 適用する二次計算を指定します (`PivotShowValuesAsType`)。 | 常に必要。 |
| `baseField` | 基準フィールドの 0 始まりのインデックス（例: 基準項目が属する行フィールドのインデックス）。文字列オーバーロードでは基準フィールド名を指定します。 | 次の 8 つの、基準フィールドを基準とする形式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）で必要です。それ以外のすべての形式では `0`（文字列オーバーロードでは `null`）を渡します。 |
| `baseItem` | 基準項目の 0 始まりのインデックス。使用できる 2 つのセンチネル値があり、`PivotShowValuesSetting.PreviousPivotItem` (-1) は直前の項目を、`PivotShowValuesSetting.NextPivotItem` (-2) は直後の項目を選択します。文字列オーバーロードでは基準項目のキャプションを指定します。選択した形式に基準項目が不要な場合は `null` を指定します。 | 基準項目を使用する 3 つの形式（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）でのみ基準項目を参照します。5 つのフィールドを基準とする形式（`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、2 つの順位形式）では基準項目を無視するため、`0` または `null` を渡します。 |

| 計算タイプ | 動作 | 基準項目のパラメーター |
| --- | --- | --- |
| `Normal` | 二次計算は適用されません。集計値はそのまま表示されます（既定）。 | — |
| `DifferenceFrom` | 基準フィールドにある基準項目の値との差として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `PercentageOf` | 基準フィールドにある基準項目の値に対する割合として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `PercentageDifferenceFrom` | 基準フィールドにある基準項目の値との差の割合として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `RunningTotalIn` | 基準フィールドの連続する項目に対して、値を累計として表示します。 | `baseField`（項目の順序が累積を左右するフィールド） |
| `PercentageOfRow` | 行合計に対する割合として値を表示します。 | — |
| `PercentageOfColumn` | 列合計に対する割合として値を表示します。 | — |
| `PercentageOfTotal` | 総合計に対する割合として値を表示します。 | — |
| `Index` | Excel のインデックス数式（(値 * 総合計) / (行合計 * 列合計)）を使用して値を表示します。 | — |
| `PercentageOfParentRowTotal` | ネストされた行フィールドでは、その親行の合計に対する割合として値を表示します。 | — |
| `PercentageOfParentColumnTotal` | ネストされた列フィールドでは、その親列の合計に対する割合として値を表示します。 | — |
| `PercentageOfParentTotal` | 親合計に対する割合として値を表示します。 | `baseField`（合計の参照元となる親フィールド） |
| `PercentageOfRunningTotalIn` | 基準フィールドの累計に対する割合として値を表示します。 | `baseField`（累積するフィールド） |
| `RankSmallestToLargest` | 値の小さい項目から大きい項目へ順位を付け、小さい値を 1 とします。 | `baseField`（順位範囲を定義する項目が属するフィールド） |
| `RankLargestToSmallest` | 値の大きい項目から小さい項目へ順位を付け、大きい値を 1 とします。 | `baseField`（順位範囲を定義する項目が属するフィールド） |

{{% alert color="primary" %}}
`ShowValuesAs(...)` は `PivotShowValuesSetting` の状態（`ShowValuesAs`、`BaseFieldIndex`、`BaseItemIndex`）を設定します。このメソッドと `PivotShowValuesSetting` プロパティは、同じ状態を設定する 2 つの方法であり、Excel の「値表示」ダイアログにある基準フィールドおよび基準項目の選択欄に対応します。
{{% /alert %}}

## **総合計に対する割合として値を表示**
`PivotField.ShowValuesAs` メソッドに `PivotShowValuesAsType.PercentageOfTotal` を指定して呼び出すと、総合計を含むすべてのデータフィールドセルが、総合計に対する割合として表示されます。表示される数値は、結果セット全体に対する割合として解釈されます。この形式では、各値を総合計に対する比率として評価するため、基準フィールドも基準項目も不要です。末尾の引数（`0`、`0`）は、この形式では無視されるプレースホルダーであり、上記のパラメーターテーブルの記載のとおりです。

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.DataFields[0];
dataField.ShowValuesAs(PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.CalculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.Save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.ShowValuesSetting の取得と設定**
現在の設定は `PivotField.ShowValuesSetting` から取得します。この読み取り専用プロパティは、フィールドの `PivotShowValuesSetting` オブジェクトを返し、そのプロパティが現在の「値表示」の計算内容を表します。設定を変更するには `PivotField.ShowValuesAs` メソッドを呼び出します。このメソッドはすべての設定を一度の呼び出しで反映するため、各プロパティを個別に代入する必要はありません。
`PivotShowValuesSetting` オブジェクトは、`ShowValuesAs` が設定する次の状態を開示します。
- `ShowValuesAs` は、適用する `PivotShowValuesAsType` の二次計算を選択します。
- `BaseFieldIndex` は、ピボットフィールド内における基準フィールドの 0 始まりのインデックスを指定します。基準フィールドを基準とする形式で使用されます。
- `BaseItemIndex` は、基準項目を指定します。特定のピボット項目の 0 始まりのインデックス、または 2 つのセンチネル値を指定できます。直前の項目には `PivotShowValuesSetting.PreviousPivotItem` (-1)、直後の項目には `PivotShowValuesSetting.NextPivotItem` (-2) を使用します。基準項目を使用する形式で使用されます。
- `BaseFieldName` と `BaseItemCaption` は読み取り専用で、特定された基準フィールド名と基準項目キャプションを示します。たとえば、直前の項目センチネルを選択すると、`BaseItemCaption` は `(previous)` を返します。
`ShowValuesAs` の呼び出し後は、更新された設定に基づいてピボットテーブルの本体を再計算して再描画するため、`PivotTable.CalculateData()` を再度呼び出してください。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.Worksheets[1].PivotTables[0];
PivotField dataField = pivotTable.DataFields[0];
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.ShowValuesSetting;
Console.WriteLine($"ShowValuesAs: {settings.ShowValuesAs}");
Console.WriteLine($"BaseFieldIndex: {settings.BaseFieldIndex}");
Console.WriteLine($"BaseItemIndex: {settings.BaseItemIndex}");
Console.WriteLine($"BaseFieldName: {settings.BaseFieldName}");
Console.WriteLine($"BaseItemCaption: {settings.BaseItemCaption}");
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.ShowValuesAs(PivotShowValuesAsType.DifferenceFrom,
    pivotTable.RowFields[0].BaseIndex, PivotShowValuesSetting.PreviousPivotItem);
pivotTable.CalculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
Console.WriteLine($"ShowValuesAs now: {dataField.ShowValuesSetting.ShowValuesAs}");
workbook.Save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルの値フィールドの管理](/cells/ja/net/manage-value-fields/)
- [ピボットテーブルの DataField のデータ表示形式を操作する](/cells/ja/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
- [ピボットテーブルの更新](/cells/ja/net/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}