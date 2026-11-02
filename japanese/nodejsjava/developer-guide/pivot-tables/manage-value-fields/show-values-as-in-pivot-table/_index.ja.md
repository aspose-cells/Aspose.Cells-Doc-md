---
title: ピボットテーブルでの値の表示形式
linktitle: ピボットテーブルでの値の表示形式
description: Aspose.Cells for Node.js via Java を使用して、ピボットテーブルのデータ フィールドの値を合計のパーセンテージ、基準項目との差、累積合計、ランクなどとして表示できます。
keywords: Aspose.Cells, ピボットテーブル, 値の表示形式, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Node.js via Java
type: docs
weight: 145
url: /ja/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` といった集計関数で各データ フィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば総合計に対するパーセンテージ、累積合計、基準項目との差、ランクなどを表示できるようにします。これにより、補助数式や計算列を使用せずに比較分析が可能になります。  
典型的な利用例としては、行・列・総合計に対するパーセンテージによるシェア分析、期間フィールドでの累積レポート、基準項目との差またはパーセンテージ差によるベンチマーク分析、最小から最大（または最大から最小）への順位付けなどがあります。  
Aspose.Cells for Node.js via Java では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` メソッドは `PivotShowValuesSetting` オブジェクトを返します。このオブジェクトの `setCalculationType()`、`setBaseFieldIndex()`、`setBaseItemPositionType()`、`setBaseItemIndex()` メソッドで動作を構成できます。便利メソッド `PivotField.showValuesAs(...)` は、同じ 4 つの設定を 1 回の呼び出しで適用します。これらの設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに対して適用します。

## **PivotFieldDataDisplayFormat 列挙体メンバー**
データ フィールドは `SUM` や `COUNT` といった集計関数を保持したまま、Show Values As によって集計値の表示方法だけが変換されます。  
`PivotShowValuesSetting` を直接設定する方法（最終セクション参照）のほかに、1 回の呼び出しで同じ設定を行う便利メソッドがあります。

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
module.exports = { showValuesAs };
```

| パラメーター | 意味 | 必須条件 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルの基準フィールドのゼロベースインデックス（例: 基準項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在の項目に対する基準項目の選択方法：`PivotItemPositionType.PREVIOUS`、`.NEXT`、または `.CUSTOM`。 | 3 つの基準項目フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | 基準項目のゼロベースインデックス。 | `baseItemPositionType` が `CUSTOM` の場合にのみ使用（正確な基準項目を指定）。`PREVIOUS` / `NEXT` および基準項目以外の形式では `0` を渡してください。 |

| 計算タイプ | 動作 | 基準項目パラメーター |
| --- | --- | --- |
| `NORMAL` | 二次計算なし。集計値そのものが表示されます（デフォルト）。 | — |
| `DIFFERENCE_FROM` | 基準フィールドの基準項目の値との差として表示します。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_OF` | 基準フィールドの基準項目の値に対するパーセンテージとして表示します。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 基準フィールドの基準項目の値に対するパーセンテージ差として表示します。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `RUNNING_TOTAL_IN` | 基準フィールドの項目順に従って累積合計として表示します。 | `baseField`（累積を駆動するフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_TOTAL` | 総合計に対するパーセンテージとして表示します。 | — |
| `INDEX` | Excel のインデックス数式 ((value × grand total) / (row total × column total)) を使用して表示します。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 入れ子になった行フィールドの場合、親行合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 入れ子になった列フィールドの場合、親列合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対するパーセンテージとして表示します。 | `baseField`（基準となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 基準フィールドの累積合計に対するパーセンテージとして表示します。 | `baseField`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 最小 (1) から最大へ順位付けします。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 最大 (1) から最小へ順位付けします。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` は、`setCalculationType()`、`setBaseFieldIndex()`、`setBaseItemPositionType()`、`setBaseItemIndex()` の 4 つの `PivotShowValuesSetting` 設定を書き込みます。メソッドと設定オブジェクトは同じ状態を構成する 2 つの方法であり、Excel の **Show Values As** ダイアログにある基準フィールドと基準項目の選択肢を鏡のように再現します。
{{% /alert %}}

## **総合計のパーセンテージとして表示**
`PivotField.showValuesAs()` メソッドに `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、すべてのデータ フィールド セル（総合計を含む）が総合計に対するシェアとして変換されます。表示される数値は結果セット全体に対する比率となります。この形式は総合計のみを基準にするため、基準フィールドや基準項目は不要です。余分な引数（`0`、`PivotItemPositionType.PREVIOUS`、`0`）はフォーマットが無視するプレースホルダーです。

```javascript
const AsposeCells = require("aspose.cells");
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
const pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables().add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PercentageOfTotal takes no base item, so the trailing
// base arguments (0, Previous, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.PercentageOfTotal,
    0,
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting() の取得と構成**
`PivotField.getShowValuesSetting()` で現在の構成を取得します。この読み取り専用メソッドはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つの設定で現在の **Show Values As** 計算を表します。構成を変更するには `PivotField.showValuesAs()` を呼び出します。この便利メソッドはすべての設定を一度に書き込むため、個別に設定する必要がありません。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つの設定は次の通りです。
- `getCalculationType()` / `setCalculationType()` で `PivotFieldDataDisplayFormat` の二次計算を選択します。
- `getBaseFieldIndex()` / `setBaseFieldIndex()` で基準フィールドのゼロベースインデックスを指定します。基準関連フォーマットで使用されます。
- `getBaseItemPositionType()` / `setBaseItemPositionType()` で基準項目の位置関係を決定し、`PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS`、または `PivotItemPositionType.CUSTOM` を受け取ります。
- `getBaseItemIndex()` / `setBaseItemIndex()` でゼロベースの基準項目インデックスを指定し、`getBaseItemPositionType()` が `CUSTOM` の場合に使用されます。  
`showValuesAs()` 呼び出し後は、`PivotTable.calculateData()` を再度実行してピボット本体を再計算し、更新された構成で再描画します。

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("ShowValuesAsPercentageOfTotal.xlsx");
const pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
const dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
const settings = dataField.getShowValuesSetting();
console.log(`CalculationType: ${settings.getCalculationType()}`);
console.log(`BaseFieldIndex: ${settings.getBaseFieldIndex()}`);
console.log(`BaseItemPositionType: ${settings.getBaseItemPositionType()}`);
console.log(`BaseItemIndex: ${settings.getBaseItemIndex()}`);
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    AsposeCells.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.PivotItemPositionType.Previous,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
console.log(`CalculationType now: ${dataField.getShowValuesSetting().getCalculationType()}`);
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/nodejs-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}