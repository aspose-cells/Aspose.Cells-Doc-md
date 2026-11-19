---
title: ピボットテーブルでの「値の表示形式」設定
linktitle: ピボットテーブルでの「値の表示形式」設定
description: Aspose.Cells for Node.js via C++ を使用して、ピボットテーブルのデータ フィールドの値を合計のパーセンテージ、基準項目との差、累積合計、順位などで表示できます。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, ピボットテーブル, 値の表示形式, PivotShowValuesAsType, PercentageOfTotal, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ja/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` といった集計関数で各データ フィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば合計のパーセンテージ、累積合計、選択した基準項目との差、順位などを表示できるようにし、補助的な数式や計算列を使用せずに比較分析を実現します。  
代表的な使用例としては、行・列・総計のパーセンテージによるシェア分析、期間フィールドでの累積レポート、基準項目との差またはパーセンテージ差によるベンチマーク分析、最小から最大（または逆）への順位付けなどがあります。  
Aspose.Cells for Node.js via C++ では、`PivotShowValuesAsType` 列挙体で二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` アクセサは `PivotShowValuesSetting` オブジェクトを返し、`setShowValuesAs()`、`setBaseFieldIndex()`、`setBaseItemIndex()` メソッドで動作を設定できます。便利メソッド `PivotField.showValuesAs(...)` を使用すれば、同じ設定を 1 回の呼び出しで適用できます。これらの設定は `PivotTable.getDataFields()` で取得したデータ フィールドまたは値フィールドに対して適用します。

## **PivotShowValuesAsType 列挙体のメンバー**
データ フィールドは `SUM` や `COUNT` などの集計関数を保持したまま、Show Values As によって表示方法のみが変換されます。  
`PivotShowValuesSetting` を直接書き込む方法（最終セクション参照）に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。このメソッドは 2 つの形態で提供されます — インデックスでベース フィールドとベース 項目を指定する形、名前で指定する形です。

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PercentageOf, "Fruit", "Apple"
```

| パラメータ | 意味 | 必須か |
| --- | --- | --- |
| `showValuesAsType` | 適用する `PivotShowValuesAsType` の二次計算。 | 常に必要です。 |
| `baseField` | ピボットテーブルのベース フィールドの 0 ベースインデックス（例: 基準項目が属する行フィールドのインデックス）。名前形式の場合はベース フィールド名を指定します。 | 8 つのベース相対フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、`RankSmallestToLargest`、`RankLargestToSmallest`）で必要です。それ以外のフォーマットは `0`（名前形式では `null`）を指定してください。 |
| `baseItem` | ベース 項目の 0 ベースインデックス。2 つのセンチネルがあり、`-1` は直前の項目、`-2` は直後の項目を表します（バインディングは名前定数をエクスポートしません – リテラル値を渡してください）。名前形式の場合はベース 項目のキャプションを指定し、フォーマットがベース項目を必要としない場合は `null` を渡します。 | `DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom` の 3 つのベース 項目フォーマットでのみ使用します。`RunningTotalIn`、`PercentageOfParentTotal`、`PercentageOfRunningTotalIn`、および両方の順位フォーマットは無視し、`0` または `null` を指定してください。 |

| 計算タイプ | 動作 | ベース項目パラメータ |
| --- | --- | --- |
| `Normal` | 二次計算なし。集計値をそのまま表示（デフォルト）。 | — |
| `DifferenceFrom` | ベース フィールド内のベース 項目の値との差として表示。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前後センチネル） |
| `PercentageOf` | ベース フィールド内のベース 項目の値のパーセンテージとして表示。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前後センチネル） |
| `PercentageDifferenceFrom` | ベース フィールド内のベース 項目の値との差のパーセンテージとして表示。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前後センチネル） |
| `RunningTotalIn` | ベース フィールドの項目順に従い、累積合計として表示。 | `baseField`（累積の基準となるフィールド） |
| `PercentageOfRow` | 行合計に対するパーセンテージとして表示。 | — |
| `PercentageOfColumn` | 列合計に対するパーセンテージとして表示。 | — |
| `PercentageOfTotal` | 総合計に対するパーセンテージとして表示。 | — |
| `Index` | Excel のインデックス式 ((value * grand total) / (row total * column total)) に基づいて表示。 | — |
| `PercentageOfParentRowTotal` | 階層化された行フィールドの場合、親行合計に対するパーセンテージとして表示。 | — |
| `PercentageOfParentColumnTotal` | 階層化された列フィールドの場合、親列合計に対するパーセンテージとして表示。 | — |
| `PercentageOfParentTotal` | 親フィールドの合計に対するパーセンテージとして表示。 | `baseField`（参照する親フィールド） |
| `PercentageOfRunningTotalIn` | ベース フィールド内の累積合計に対するパーセンテージとして表示。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 値を最小（1）から最大へ順位付け。 | `baseField`（順位付けの対象となるフィールド） |
| `RankLargestToSmallest` | 値を最大（1）から最小へ順位付け。 | `baseField`（順位付けの対象となるフィールド） |

{{% alert color="primary" %}}
`showValuesAs(...)` は `PivotShowValuesSetting` の設定（`getShowValuesAs()`/`setShowValuesAs()`、`getBaseFieldIndex()`/`setBaseFieldIndex()`、`getBaseItemIndex()`/`setBaseItemIndex()`）を書き込みます。メソッドとプロパティ オブジェクトは同一の状態を構成する 2 つの方法であり、Excel の Show Values As ダイアログにあるベース フィールドおよびベース 項目ピッカーを反映しています。
{{% /alert %}}

## **合計のパーセンテージとして値を表示**
`PivotField.showValuesAs()` メソッドに `PivotShowValuesAsType.PercentageOfTotal` を指定して呼び出すと、すべてのデータ フィールド セル（総計を含む）が合計に対するシェアとして変換されます。表示される数値は結果全体の比率として解釈されます。この形式は合計に対してのみ測定するため、ベース フィールドやベース 項目は不要です。パラメータ表で示したように、末尾の引数（`0`, `0`）はフォーマットが無視するプレースホルダーです。

```javascript
const AsposeCells = require("aspose.cells.node");
// Load or create a workbook with source data
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
const fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"];
const amounts = [10, 20, 30, 40, 50, 60];
for (let i = 0; i < fruits.length; i++) {
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
const pivotSheetIndex = workbook.getWorksheets().add();
const pivotTable = workbook
    .getWorksheets()
    .get(pivotSheetIndex)
    .getPivotTables()
    .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PercentageOfTotal, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting() の取得と構成**
`PivotField.getShowValuesSetting()` で現在の構成を取得します。この読み取り専用アクセサはフィールドの `PivotShowValuesSetting` オブジェクトを返し、そこに設定された Show Values As の計算が記録されています。構成を変更するには `PivotField.showValuesAs()` を呼び出します。これによりすべての設定が 1 回の呼び出しで書き込まれ、個別に設定する手間が省けます。  
`PivotShowValuesSetting` オブジェクトが保持する状態は次のとおりです。  
- `getShowValuesAs()` と `setShowValuesAs()` で `PivotShowValuesAsType` の二次計算を選択します。  
- `getBaseFieldIndex()` と `setBaseFieldIndex()` でベース フィールドの 0 ベースインデックスを指定します。ベース相対フォーマットで使用されます。  
- `getBaseItemIndex()` と `setBaseItemIndex()` でベース 項目を指定します。インデックスまたは 2 つのセンチネル（`-1` は前項目、`-2` は次項目）で表現され、ベース 項目フォーマットで使用されます。  
- `getBaseFieldName()` と `getBaseItemCaption()` は読み取り専用ビューで、解決されたベース フィールド名とベース 項目キャプションを返します。たとえば、前項目センチネルを選択した場合、`getBaseItemCaption()` は `(previous)` を返します。  
`showValuesAs()` の呼び出し後に `PivotTable.calculateData()` を再度呼び出し、ピボット本体を再計算および再描画して設定を反映させます。

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`ShowValuesAs: ${settings.getShowValuesAs()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
console.log(`BaseFieldName: ${settings.getBaseFieldName()}`);
console.log(`BaseItemCaption: ${settings.getBaseItemCaption()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
// -1 is the previous-item sentinel (the binding does not export the named constant)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    -1
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`ShowValuesAs now: ${dataField.getShowValuesSetting().getShowValuesAs()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/nodejs-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}