---
title: ピボットテーブルでの値の表示方法
description: Aspose.Cells for Java を使用して、ピボットテーブルのデータフィールドの値を総計に対するパーセンテージ、基準アイテムとの差、累積合計、ランクなどとして表示します。
linktitle: Show Values As
keywords: Aspose.Cells, ピボットテーブル, 値の表示方法, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Java
type: docs
weight: 145
url: /ja/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` といった集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば総計に対するパーセンテージ、累積合計、基準アイテムとの差、ランクなどを表示できるようにします。これにより、補助的な数式や計算列を使用せずに比較分析が可能になります。  
典型的な使用例としては、行・列・総計に対するパーセンテージによるシェア分析、期間フィールドでの累積レポート、ベンチマーク項目に対する差分またはパーセンテージ差分による変動分析、最小から最大または最大から最小へのランキングなどがあります。  
Aspose.Cells for Java では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` ゲッターは `PivotShowValuesSetting` オブジェクトを返し、`setCalculationType(...)`、`setBaseFieldIndex(...)`、`setBaseItemPositionType(...)`、`setBaseItemIndex(...)` メソッドで動作を構成します。便利メソッド `PivotField.showValuesAs(...)` はこれら 4 つの設定を一度に適用します。設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに対して適用します。

## **PivotFieldDataDisplayFormat 列挙メンバー**
データフィールドは集計関数（Sum や Count など）を保持したまま、Show Values As によって集計結果の表示方法だけが変換されます。  
`PivotShowValuesSetting` のセッターを直接使用する（最後のセクション参照）か、1 回の呼び出しで同じ構成を適用する便利メソッドを使用します。

```java
public class CodeRunner
{
    public void showValuesAs(PivotFieldDataDisplayFormat displayFormat, int baseField,
                             PivotItemPositionType baseItemPositionType, int baseItem)
    {
    }
}
```

| パラメータ | 意味 | 必要条件 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に必須。 |
| `baseField` | ピボットテーブルの基準フィールド群のうち、基準アイテムが属する行フィールドの 0 ベースインデックス。 | 以下の 6 つの基準関連フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 現在のアイテムに対して基準アイテムを選択する方法：`PivotItemPositionType.PREVIOUS`、`NEXT`、または `CUSTOM`。 | 3 つの基準項目フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | 基準アイテムの 0 ベースインデックス。 | `baseItemPositionType` が `CUSTOM` の場合にのみ使用（正確な基準アイテムを指定）。`PREVIOUS`／`NEXT` および基準アイテム形式以外では無視されるので `0` を渡してください。 |

| 計算タイプ | 動作 | 基準アイテムパラメータ |
| --- | --- | --- |
| `NORMAL` | 二次計算なし。集計値をそのまま表示（既定）。 | — |
| `DIFFERENCE_FROM` | 基準フィールドの基準アイテムの値との差として表示。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_OF` | 基準フィールドの基準アイテムの値に対するパーセンテージとして表示。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `PERCENTAGE_DIFFERENCE_FROM` | 基準フィールドの基準アイテムの値に対するパーセンテージ差として表示。 | `baseField` + `PREVIOUS`/`NEXT`/`CUSTOM`（`CUSTOM` の場合は `baseItem`） |
| `RUNNING_TOTAL_IN` | 基準フィールドの連続アイテムに対する累積合計として表示。 | `baseField`（累積の順序を決めるフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_TOTAL` | 総計に対するパーセンテージとして表示。 | — |
| `INDEX` | Excel の INDEX 式 ((value * grand total)/(row total * column total)) を使用して表示。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対するパーセンテージとして表示。 | `baseField`（基準となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 基準フィールドの累積合計に対するパーセンテージとして表示。 | `baseField`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 最小 (1) から最大へランク付け。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 最大 (1) から最小へランク付け。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` は `setCalculationType(...)`、`setBaseFieldIndex(...)`、`setBaseItemPositionType(...)`、`setBaseItemIndex(...)` の 4 つの `PivotShowValuesSetting` 値を設定します。メソッドとプロパティオブジェクトは、Excel の Show Values As ダイアログにある基準フィールドおよび基準アイテム選択と同等の状態を構成する 2 つの方法です。
{{% /alert %}}

## **総計に対するパーセンテージとして値を表示**
`PivotField.showValuesAs(...)` メソッドに `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、すべてのデータフィールドセル（総計を含む）が総計に対するシェアとして変換されます。表示される数値は結果セット全体に対する割合として読み取れます。この形式は総計に対してのみ測定するため、基準フィールドや基準アイテムは不要です。フォーマットが無視するパラメータ（`0`、`PivotItemPositionType.PREVIOUS`、`0`）は単にプレースホルダーとして残します。

```java
import com.aspose.cells.*;
// Load or create a workbook with source data
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Amount");
String[] fruits = { "Apple", "Banana", "Apple", "Cherry", "Banana", "Apple" };
int[] amounts = { 10, 20, 30, 40, 50, 60 };
for (int i = 0; i < fruits.length; i++)
{
    dataSheet.getCells().get(i + 1, 0).putValue(fruits[i]);
    dataSheet.getCells().get(i + 1, 1).putValue(amounts[i]);
}
// Add a pivot table on a new worksheet
int pivotSheetIndex = workbook.getWorksheets().add();
PivotTable pivotTable = workbook.getWorksheets().get(pivotSheetIndex).getPivotTables()
        .add("=Sheet1!A1:B7", 2, 2);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.calculateData();
// Show the Amount data field as a percentage of the grand total with the
// one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
// base arguments (0, PREVIOUS, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL, 0,
        PivotItemPositionType.PREVIOUS, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting の取得と構成**
現在の設定は `PivotField.getShowValuesSetting()` で取得できます。この読み取り専用ゲッターはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティが有効な Show Values As 計算を表します。設定を変更するには `PivotField.showValuesAs(...)` メソッドを呼び出します。これにより 4 つの設定が一括で書き込まれ、個別にプロパティを設定する必要がなくなります。  
`PivotShowValuesSetting` オブジェクトが公開する 4 つのプロパティは次のとおりです。
- `getCalculationType()` / `setCalculationType(...)` → `PivotFieldDataDisplayFormat` の二次計算を選択します。
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` → 基準フィールドの 0 ベースインデックスを指定します。基準関連フォーマットで使用されます。
- `getBaseItemPositionType()` / `setBaseItemPositionType(...)` → 基準アイテムの位置決め方法を決定し、`PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS`、`PivotItemPositionType.CUSTOM` のいずれかを受け取ります。
- `getBaseItemIndex()` / `setBaseItemIndex(...)` → 0 ベースの基準アイテムインデックスを指定し、`BaseItemPositionType` が `CUSTOM` の場合に使用されます。  
`showValuesAs(...)` の呼び出し後は、`PivotTable.calculateData()` を再度呼び出してピボット本体を再計算し、更新された設定で再描画されるようにします。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("CalculationType: " + settings.getCalculationType());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemPositionType: " + settings.getBaseItemPositionType());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("CalculationType now: " + dataField.getShowValuesSetting().getCalculationType());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/java/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}