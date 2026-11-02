---
title: ピボットテーブルでの「値の表示形式」
linktitle: ピボットテーブルでの「値の表示形式」
description: Aspose.Cells for Node.js via C++ を使用して、ピボットテーブルのデータフィールド値を総計に対する割合、基準項目との差、累計、ランクなどとして表示します。
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, ピボットテーブル, 値の表示形式, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex
type: docs
weight: 145
url: /ja/nodejs-cpp/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` などの集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、その集計結果を二次計算に置き換え、たとえば総計に対する割合、累積合計、基準項目との差、ランクなどを表示できるようにします。これにより、補助的な数式や計算列を使用せずに比較分析が可能になります。  
典型的な使用例としては、行・列・総計に対するパーセンテージによるシェア分析、期間フィールドでの累積レポート、ベンチマーク項目に対する差分またはパーセンテージ差分による差異分析、最小から最大、または最大から最小へのランク付けなどがあります。  
Aspose.Cells for Node.js via C++ では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` アクセサは `PivotShowValuesSetting` オブジェクトを返し、その `setCalculationType()`、`setBaseFieldIndex()`、`setBaseItemPositionType()`、`setBaseItemIndex()` メソッドで動作を設定できます。便利メソッド `PivotField.showValuesAs(...)` は同じ 4 つの設定を一度に適用します。これらの設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに適用します。

## **PivotFieldDataDisplayFormat 列挙メンバー**
データフィールドは `SUM` や `COUNT` などの集計関数を保持しますが、Show Values As は集計値の表示方法のみを変換します。  
`PivotShowValuesSetting` プロパティを直接設定する（最後のセクション参照）方法に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。

```javascript
const AsposeCells = require("aspose.cells.node");
function showValuesAs(pivotField, displayFormat, baseField, baseItemPositionType, baseItem) {
    pivotField.showValuesAs(displayFormat, baseField, baseItemPositionType, baseItem);
}
function pickEnum(enumType, candidates, fallback) {
    const type = enumType || {};
    for (const name of candidates) {
        if (type[name] !== undefined && type[name] !== null) {
            return type[name];
        }
    }
    return fallback;
}
const workbook = new AsposeCells.Workbook();
const sheet = workbook.getWorksheets().add("PivotData");
const cells = sheet.getCells();
// --- Source data -----------------------------------------------------------
const headers = ["Region", "Product", "Sales"];
for (const [c, header] of headers.entries()) {
    cells.get(0, c).putValue(header);
}
const rows = [
    ["East", "Apple", 100],
    ["East", "Banana", 120],
    ["West", "Apple", 90],
    ["West", "Banana", 60],
    ["North", "Apple", 75],
    ["North", "Banana", 45]
];
for (const [r, row] of rows.entries()) {
    for (const [c, value] of row.entries()) {
        cells.get(r + 1, c).putValue(value);
    }
}
// --- Pivot table ------------------------------------------------------------
const pivotTables = sheet.getPivotTables();
const pivotTableIndex = pivotTables.add("A1:C7", 0, 4);
const pivotTable = pivotTables.get(pivotTableIndex);
pivotTable.getRowFields().add("Region");
pivotTable.getDataFields().add("Sales");
const salesField = pivotTable.getDataFields().get(0);
// --- ShowValuesAs -----------------------------------------------------------
const displayFormat = pickEnum(
    AsposeCells.PivotFieldDataDisplayFormat,
    ["PERCENT_OF_TOTAL", "PercentOfTotal", "PERCENTAGE_OF_TOTAL", "PercentageOfTotal"],
    7
);
const baseItemPositionType = pickEnum(
    AsposeCells.PivotItemPositionType,
    ["DEFAULT", "Default"],
    0
);
showValuesAs(salesField, displayFormat, -1, baseItemPositionType, -1);
// --- Save -------------------------------------------------------------------
workbook.save("ShowValuesAs.xlsx");
console.log("ShowValuesAs applied and workbook saved.");
```

| パラメーター | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に必要です。 |
| `baseField` | ピボットテーブルの基準フィールドのゼロベースインデックス（例：基準項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在の項目に対して基準項目を選択する方法：`PivotItemPositionType.PREVIOUS`、`.NEXT`、または `.CUSTOM`。 | 3 つの基準項目フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | 基準項目のゼロベースインデックス。 | `baseItemPositionType` が `CUSTOM` のときのみ必要です（正確な基準項目を指定）。`PREVIOUS` / `NEXT` および基準項目を使用しない形式では `0` を渡してください。 |

| 計算タイプ | 動作 | 基準項目パラメーター |
| --- | --- | --- |
| `NORMAL` | 二次計算なし。集計値をそのまま表示（デフォルト）。 | — |
| `DIFFERENCE_FROM` | 基準フィールドの基準項目の値との差として表示。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_OF` | 基準フィールドの基準項目の値に対するパーセンテージとして表示。 | `baseField` + `PREVIOUS`/ `NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 基準フィールドの基準項目の値に対するパーセンテージ差として表示。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `RUNNING_TOTAL_IN` | 基準フィールドの連続項目に対して累積合計として表示。 | `baseField`（累積の順序を決定するフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_TOTAL` | 総計に対するパーセンテージとして表示。 | — |
| `INDEX` | Excel の INDEX 式 ((value * grand total) / (row total * column total)) を使用して表示。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対するパーセンテージとして表示。 | `baseField`（基準となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 基準フィールドの累積合計に対するパーセンテージとして表示。 | `baseField`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 値を最小 (1) から最大へランク付け。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 値を最大 (1) から最小へランク付け。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` は 4 つの `PivotShowValuesSetting` 設定（`getCalculationType()`/`setCalculationType()`、`getBaseFieldIndex()`/`setBaseFieldIndex()`、`getBaseItemPositionType()`/`setBaseItemPositionType()`、`getBaseItemIndex()`/`setBaseItemIndex()`）を書き込みます。メソッドとプロパティオブジェクトは同じ状態を構成する 2 つの方法であり、Excel の「値の表示形式」ダイアログの基準フィールドと基準項目ピッカーを鏡像しています。
{{% /alert %}}

## **合計に対するパーセンテージとして値を表示**
`PivotField.showValuesAs()` メソッドに `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、すべてのデータフィールドセル（合計セルも含む）が総計に対するシェアに変換されます。表示される数値は結果全体の比率として読み取れます。この形式は総計に対してのみ測定するため、基準フィールドや基準項目は不要です。フォーマットが無視する末尾の引数（`0`、`PivotItemPositionType.PREVIOUS`、`0`）はプレースホルダーです。

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
`PivotField.getShowValuesSetting()` を使用して現在の構成を取得します。この読み取り専用アクセサはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティで現在の「値の表示形式」計算を示します。構成を変更するには `PivotField.showValuesAs()` メソッドを呼び出します。このメソッドは 4 つの設定を一度に書き込むため、個別にプロパティを設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つの設定は次の通りです：
- `getCalculationType()` と `setCalculationType()` は二次計算として使用する `PivotFieldDataDisplayFormat` を選択します。  
- `getBaseFieldIndex()` と `setBaseFieldIndex()` は基準フィールドのゼロベースインデックスを指定し、基準関連フォーマットで使用されます。  
- `getBaseItemPositionType()` と `setBaseItemPositionType()` は基準項目の位置を現在の項目に対して決定し、`PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS`、または `PivotItemPositionType.CUSTOM` を受け入れます。  
- `getBaseItemIndex()` と `setBaseItemIndex()` はゼロベースの基準項目インデックスを指定し、`getBaseItemPositionType()` が `CUSTOM` の場合に使用されます。  
`showValuesAs()` の呼び出し後に `PivotTable.calculateData()` を再度呼び出すことで、ピボット本体が再計算され、更新された構成で再描画されます。

```javascript
const AsposeCells = require("aspose.cells.node");
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
    AsposeCells.Pivot.PivotFieldDataDisplayFormat.DifferenceFrom,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    AsposeCells.Pivot.PivotItemPositionType.Previous,
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
- [ピボットテーブルでの値フィールドの管理](/cells/ja/nodejs-cpp/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-cpp/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-cpp/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}