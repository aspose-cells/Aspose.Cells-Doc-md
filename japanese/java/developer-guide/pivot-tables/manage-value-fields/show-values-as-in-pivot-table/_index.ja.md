---
title: ピボットテーブルで値表示方法を使用
linktitle: ピボットテーブルで値表示方法を使用
description: Aspose.Cells for Java を使用して、ピボットテーブルのデータフィールド値を、合計に対する割合、基準項目との差、累計、順位などとして表示します。
keywords: Aspose.Cells, ピボットテーブル, 値表示方法, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Java
type: docs
weight: 145
url: /ja/java/show-values-as-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **考えられる使用シナリオ**
ピボットテーブルでは、通常、`Sum` や `Count` などの集計関数で各データフィールドを集計します。Excel の **値表示方法** 機能は、集計値を、総合計に対する割合、累計、指定した基準項目との差、順位など、その集計値から導かれる二次計算に置き換えます。これにより、補助数式や計算列を使用せずに比較分析を実行できます。
主な用途には、合計構成比の分析（行、列、または総合計に対する割合を含む）、期間フィールドで累計を使用した累積レポート、基準項目との差または基準項目との差の割合を使用してベンチマーク項目に対する差異を分析する用途、および値の小さい順から大きい順、または大きい順から小さい順への順位付けが含まれます。
Aspose.Cells for Java では、`PivotShowValuesAsType` 列挙型を使用して二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` ゲッターは `PivotShowValuesSetting` オブジェクトを返し、その `setShowValuesAs(...)`、`setBaseFieldIndex(...)`、`setBaseItemIndex(...)` メソッドで動作を設定します。便利な `PivotField.showValuesAs(...)` メソッドは、同じ設定を 1 回の呼び出しで適用します。これらの設定は、`PivotTable.getDataFields()` から取得したデータフィールドまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙型のメンバー**
データフィールドは `Sum` や `Count` などの集計関数を維持し、値表示方法では、集計値の表示方法だけが変換されます。
（最後のセクションを参照）`PivotShowValuesSetting` の設定用メソッドを直接使用することに加えて、1 回の呼び出しで同じ設定を適用できる便利なメソッドもあります。このメソッドには 2 つのオーバーロードがあり、1 つは基準フィールドと基準項目をインデックスで指定し、もう 1 つは名前で指定します。

```java
public class CodeRunner
{
    public void showValuesAs(PivotShowValuesAsType showValuesAsType, int baseField, int baseItem)
    {
    }

    public void showValuesAs(PivotShowValuesAsType showValuesAsType, String baseField, String baseItem)
    {
    }
}
```

| パラメーター | 意味 | 必須条件 |
| --- | --- | --- |
| `showValuesAsType` | 適用する `PivotShowValuesAsType` の二次計算。 | 必須。 |
| `baseField` | ピボットテーブルの基準フィールド群における基準フィールドのゼロベース インデックス（例：基準項目が属する行フィールドのインデックス）。`String` オーバーロードでは基準フィールドの名前を指定します。 | 以下の 8 つの基準フィールド相対形式 (`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`) では必須です。それ以外の形式には `0`（`String` オーバーロードでは `null`）を渡します。 |
| `baseItem` | 基準項目のゼロベース インデックス。2 つのセンチネル値があり、`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) は前の項目、`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) は次の項目を選択します。`String` オーバーロードでは基準項目のキャプションを指定します。選択した形式に基準項目が不要な場合は `null` を指定します。 | 基準項目を使う 3 つの形式 (`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`) でのみ基準項目を評価します。5 つのフィールド相対形式 (`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、2 つの順位形式) では無視されるため、`0` または `null` を渡します。 |

| 計算タイプ | 動作 | 基準項目パラメーター |
| --- | --- | --- |
| `NORMAL` | 二次計算は行いません。集計値はそのまま表示されます（既定）。 | — |
| `DIFFERENCE_FROM` | 基準フィールド内の基準項目の値との差として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `PERCENTAGE_OF` | 基準フィールド内の基準項目の値の割合として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `PERCENTAGE_DIFFERENCE_FROM` | 基準フィールド内の基準項目の値に対する差の百分率として値を表示します。 | `baseField` + `baseItem`（インデックスまたはキャプション、または前／次のセンチネル値） |
| `RUNNING_TOTAL_IN` | 基準フィールドの連続する項目に対する累計として値を表示します。 | `baseField`（累積順序を定義するフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対する割合として値を表示します。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対する割合として値を表示します。 | — |
| `PERCENTAGE_OF_TOTAL` | 総合計に対する割合として値を表示します。 | — |
| `INDEX` | Excel のインデックス数式 `((value * grand total) / (row total * column total))` を使用して値を表示します。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 親行合計に対する割合として値を表示します（ネストされた行フィールドの場合）。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 親列合計に対する割合として値を表示します（ネストされた列フィールドの場合）。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対する割合として値を表示します。 | `baseField`（合計の基準となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 基準フィールドの累計に対する割合として値を表示します。 | `baseField`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 値が小さい順（1）から大きい順に順位を付けます。 | `baseField`（順位付けの対象範囲を定義するフィールド） |
| `RANK_LARGEST_TO_SMALLEST` | 値が大きい順（1）から小さい順に順位を付けます。 | `baseField`（順位付けの対象範囲を定義するフィールド） |

{{% alert color="primary" %}}
`showValuesAs(...)` は、`setShowValuesAs(...)`、`setBaseFieldIndex(...)`、`setBaseItemIndex(...)` を通じて、`PivotShowValuesSetting` の状態をそのまま設定します。設定用メソッドと設定オブジェクトは、Excel の値表示方法ダイアログにある基準フィールドと基準項目の選択ボックスに対応しています。
{{% /alert %}}

## **合計に対する割合として値を表示**
`PivotField.showValuesAs(...)` メソッドを `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` とともに呼び出すと、総合計を含むすべてのデータフィールドセルを、総合計に対する割合に変換します。表示される数値は、結果全体に対する割合として解釈できます。この形式は各値を総合計のみと比較するため、基準フィールドや基準項目は不要です。末尾の引数 (`0`, `0`) は、この形式では無視されるプレースホルダーです。詳細については、上のパラメーターテーブルを参照してください。

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
// base arguments (0, 0) are placeholders the format ignores
PivotField dataField = pivotTable.getDataFields().get(0);
dataField.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0);
pivotTable.calculateData();
// Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx");
```

## **PivotField.getShowValuesSetting の取得と構成**
現在の構成は `PivotField.getShowValuesSetting()` を通じて読み取ります。この読み取り専用ゲッターは、フィールドの `PivotShowValuesSetting` オブジェクトを返し、そのプロパティで適用中の値表示方法を確認できます。構成を変更するには `PivotField.showValuesAs(...)` メソッドを呼び出します。このメソッドは、すべての設定を 1 回の呼び出しで書き込むため、プロパティを 1 つずつ設定する必要はありません。
`PivotShowValuesSetting` オブジェクトは、`showValuesAs(...)` で書き込まれる次の状態を開示します。
- `getShowValuesAs()` / `setShowValuesAs(...)` は、`PivotShowValuesAsType` の二次計算を選択します。
- `getBaseFieldIndex()` / `setBaseFieldIndex(...)` は、ピボットフィールド内における基準フィールドのゼロベース インデックスを指定します。基準フィールド相対形式で使用されます。
- `getBaseItemIndex()` / `setBaseItemIndex(...)` は、基準項目を指定します。具体的なピボット項目のゼロベース インデックス、または 2 つのセンチネル値を指定できます。`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM` (-1) は前の項目を、`PivotShowValuesSetting.NEXT_PIVOT_ITEM` (-2) は次の項目を選択します。基準項目を使う形式で使用されます。
- `getBaseFieldName()` と `getBaseItemCaption()` は、解決された基準フィールド名と基準項目のキャプションを返す読み取り専用プロパティです。たとえば、前の項目センチネル値を選択した後、`getBaseItemCaption()` は `(previous)` を返します。
`showValuesAs(...)` の呼び出し後は、更新した構成でピボットテーブルの本体を再計算し、再描画するため、`PivotTable.calculateData()` を再度呼び出します。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("ShowValuesAsPercentageOfTotal.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(1).getPivotTables().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Read the current show-values settings
PivotShowValuesSetting settings = dataField.getShowValuesSetting();
System.out.println("ShowValuesAs: " + settings.getShowValuesAs());
System.out.println("BaseFieldIndex: " + settings.getBaseFieldIndex());
System.out.println("BaseItemIndex: " + settings.getBaseItemIndex());
System.out.println("BaseFieldName: " + settings.getBaseFieldName());
System.out.println("BaseItemCaption: " + settings.getBaseItemCaption());
// Switch to a base-item calculation with the one-call method: difference
// from the value of the previous item in the row field
dataField.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivotTable.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
);
pivotTable.calculateData();
// Note: the percentage number format saved by the previous example still
// clings to the data field cells; the underlying values are now differences
// Re-read the applied configuration
System.out.println("ShowValuesAs now: " + dataField.getShowValuesSetting().getShowValuesAs());
workbook.save("ShowValuesAsDifferenceFrom.xlsx");
```

## **関連記事**
- [ピボットテーブルで値フィールドを管理する](/cells/ja/java/manage-value-fields/)
- [ピボットテーブルを更新する](/cells/ja/java/refresh-pivot-table/)
- [ピボットテーブルにスタイルを適用する](/cells/ja/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="java" >}}