---
title: ピボットテーブルの値の表示形式
linktitle: ピボットテーブルの値の表示形式
description: Aspose.Cells for Node.js via Java を使用して、ピボットテーブルのデータフィールドの値を合計のパーセンテージ、基準項目との差、累積合計、ランクなどとして表示します。
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, ピボットテーブル, 値の表示形式, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex
type: docs
weight: 145
url: /ja/nodejs-java/show-values-as-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` などの集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換えます。たとえば、総計のパーセンテージ、累積合計、選択した基準項目との差、またはランクなどです。これにより、補助的な数式や計算列を使用せずに比較分析を行うことができます。  
一般的な使用例としては、行・列・総計のパーセンテージを含む合計シェア分析、期間フィールドでの累積合計を使用した累積レポート、基準項目からの差またはパーセンテージ差によるベンチマーク項目との乖離分析、最小から最大または最大から最小への値のランク付けなどがあります。  
Aspose.Cells for Node.js via Java では、`PivotShowValuesAsType` 列挙型で二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` メソッドは `PivotShowValuesSetting` オブジェクトを返し、`setShowValuesAs()`、`setBaseFieldIndex()`、`setBaseItemIndex()` メソッドで動作を構成します。便利メソッド `PivotField.showValuesAs(...)` は同じ設定を 1 回の呼び出しで適用します。これらの設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙メンバー**
データフィールドは `SUM` や `COUNT` などの集計関数を保持したまま、Show Values As は集計値の表示方法のみを変換します。  
`PivotShowValuesSetting` のセッターを直接使用する方法（最後のセクション参照）に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。このメソッドは 2 つの形式があり、インデックスでベースフィールドとベース項目を指定するものと、名前で指定するものがあります。

```javascript
const AsposeCells = require("aspose.cells");
function showValuesAs(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
function showValuesAsByName(pivotField, showValuesAsType, baseField, baseItem) {
    pivotField.showValuesAs(showValuesAsType, baseField, baseItem);
}
// index form: AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0
// name form:  AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF, "Fruit", "Apple"
```

| パラメータ | 説明 | 必要な場合 |
| --- | --- | --- |
| `showValuesAsType` | 適用する `PivotShowValuesAsType` の二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルのベースフィールドの 0 ベースインデックス（例: ベース項目が属する行フィールドのインデックス）。名前形式の場合はベースフィールド名。 | 以下の 8 つのベース相対形式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）で必要。その他の形式では `0`（名前形式では `null`）を指定。 |
| `baseItem` | ベース項目の 0 ベースインデックス。2 つのセンチネルがあり、-1 は前の項目、-2 は次の項目を選択します（パッケージのルートは `PivotShowValuesSetting` 定数をエクスポートしないため、リテラル値を使用）。名前形式ではベース項目のキャプションを使用し、必要な形式で `null` を指定。 | 3 つのベース項目形式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）で評価され、5 つのフィールド相対形式（`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、両方のランク）では無視されるため、`0` または `null` を指定。 |

| 計算タイプ | 動作 | ベース項目パラメータ |
| --- | --- | --- |
| `NORMAL` | 二次計算なし。集計値をそのまま表示（デフォルト）。 | — |
| `DIFFERENCE_FROM` | ベースフィールドのベース項目の値との差として表示。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前/次のセンチネル） |
| `PERCENTAGE_OF` | ベースフィールドのベース項目の値のパーセンテージとして表示。 | `baseField` + `baseItem` |
| `PERCENTAGE_DIFFERENCE_FROM` | ベースフィールドのベース項目の値との差のパーセンテージとして表示。 | `baseField` + `baseItem` |
| `RUNNING_TOTAL_IN` | ベースフィールドの項目順に従って累積合計として表示。 | `baseField`（蓄積を駆動するフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計のパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計のパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_TOTAL` | 総計のパーセンテージとして表示。 | — |
| `INDEX` | Excel の INDEX 式 ((value * grand total) / (row total * column total)) を使用して表示。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 親行合計のパーセンテージとして表示（入れ子の行フィールド用）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 親列合計のパーセンテージとして表示（入れ子の列フィールド用）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計のパーセンテージとして表示。 | `baseField`（参照となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | ベースフィールドの累積合計のパーセンテージとして表示。 | `baseField`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 最小 (1) から最大へランク付け。 | `baseField`（ランク範囲を決めるフィールド） |
| `RANK_LARGEST_TO_SMALLEST` | 最大 (1) から最小へランク付け。 | `baseField`（ランク範囲を決めるフィールド） |

{{% alert color="primary" %}}
`showValuesAs(...)` は `setShowValuesAs()`、`setBaseFieldIndex()`、`setBaseItemIndex()` を通じて `PivotShowValuesSetting` の状態を書き込みます。メソッドとプロパティオブジェクトは同じ状態を設定する 2 つの方法であり、Excel の Show Values As ダイアログのベースフィールドおよびベース項目選択と同様です。
{{% /alert %}}

## **総計のパーセンテージとして値を表示**
`PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` を指定して `PivotField.showValuesAs()` メソッドを呼び出すと、総計を含むすべてのデータフィールドセルを総計に対する割合に変換します。表示される数値は全体結果セットの比率として解釈されます。この形式は各値を総計とだけ比較するため、ベースフィールドやベース項目は不要です。末尾の引数 (`0`, `0`) はフォーマットが無視するプレースホルダーであることは上記のパラメータ表に記載されています。

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, 0) are placeholders the format ignores
const dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(AsposeCells.PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting() の取得と構成**
`PivotField.getShowValuesSetting()` を使用して現在の構成を取得します。この読み取り専用メソッドはフィールドの `PivotShowValuesSetting` オブジェクトを返し、その設定は現在有効な Show Values As 計算を示します。構成を変更するには `PivotField.showValuesAs()` メソッドを呼び出します。このメソッドはすべての設定を 1 回の呼び出しで書き込むため、個別に設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトは `showValuesAs()` が書き込む状態を公開します:
- `getShowValuesAs()` / `setShowValuesAs()` は `PivotShowValuesAsType` の二次計算を選択します。
- `getBaseFieldIndex()` / `setBaseFieldIndex()` はピボットフィールド内のベースフィールドの 0 ベースインデックスを指定します。ベース相対形式で使用されます。
- `getBaseItemIndex()` / `setBaseItemIndex()` はベース項目を指定します。特定のピボット項目の 0 ベースインデックス、または 2 つのセンチネル値（前の項目は -1、次の項目は -2）です（パッケージのルートは名前付き定数をエクスポートしません）。ベース項目形式で使用されます。
- `getBaseFieldName()` および `getBaseItemCaption()` は読み取り専用ビューで、解決されたベースフィールド名とベース項目のキャプションを返します。たとえば、前項目センチネルを選択した場合、`getBaseItemCaption()` は `(previous)` を返します。

`showValuesAs()` を呼び出した後、`PivotTable.calculateData()` を再度呼び出してピボット本体を再計算し、更新された構成で再描画します。

```javascript
const AsposeCells = require("aspose.cells");
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
// (-1 is the previous-item sentinel; the constants are not exported here)
dataField.showValuesAs(
    AsposeCells.PivotShowValuesAsType.DIFFERENCE_FROM,
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

## **Related Articles**
- [ピボットテーブルの値フィールドの管理](/cells/ja/nodejs-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/nodejs-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}