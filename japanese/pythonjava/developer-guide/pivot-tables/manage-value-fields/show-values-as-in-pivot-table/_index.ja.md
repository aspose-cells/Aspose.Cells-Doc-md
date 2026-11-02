---
title: ピボットテーブルでの「値の表示」
linktitle: ピボットテーブルでの「値の表示」
description: Aspose.Cells for Python via Java を使用して、ピボットテーブルのデータフィールドの値を合計に対する割合、基準項目との差分、累積合計、順位などとして表示できます。
keywords: Aspose.Cells, ピボットテーブル, 値の表示, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python via Java
type: docs
weight: 145
url: /ja/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`Sum` や `Count` などの集計関数を使用して各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換えます。たとえば、合計に対する割合、累積合計、選択した基準項目との差分、または順位などで、補助数式や計算列を使用せずに比較分析を行うことができます。  
典型的な利用例としては、行・列・全体の合計に対する割合によるシェア分析、期間フィールドでの累積合計を使用した累計レポート、基準項目との差分または差分率を用いたベンチマーク項目との変動分析、最小から最大、または最大から最小への値の順位付けなどがあります。  
Aspose.Cells for Python via Java では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` メソッドは `PivotShowValuesSetting` オブジェクトを返し、書き込み可能な `setCalculationType`、`setBaseFieldIndex`、`setBaseItemPositionType`、`setBaseItemIndex` メソッドで動作を構成します。便利メソッド `PivotField.showValuesAs(...)` は同じ4つの設定を一度の呼び出しで適用します。これらの設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに適用してください。

## **PivotFieldDataDisplayFormat 列挙体メンバー**
データフィールドは Sum や Count などの集計関数を保持したまま、Show Values As は集計された値の表示方法のみを変換します。  
`PivotShowValuesSetting` のプロパティを直接設定する（最終セクション参照）以外に、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります：

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    PivotField,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.showValuesAs(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
jpype.shutdownJVM()
```

| パラメータ | 意味 | 必要な場合 |
| --- | --- | --- |
| `displayFormat` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に必要。 |
| `baseField` | ピボットテーブルの基準フィールドのゼロベースインデックス（例: 基準項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`、`RunningTotalIn`、`PercentageOfRunningTotalIn`、`PercentageOfParentTotal`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItemPositionType` | 基準項目が現在の項目に対してどのように選択されるかを示す。`PivotItemPositionType.Previous`、`.Next`、または `.Custom` のいずれか。 | 3 つの基準項目フォーマット（`DifferenceFrom`、`PercentageOf`、`PercentageDifferenceFrom`）のみで使用され、その他のフォーマットでは無視されます。 |
| `baseItem` | 基準項目のゼロベースインデックス。 | `baseItemPositionType` が `Custom` の場合にのみ使用され（正確な基準項目を指定）。`Previous` / `Next` や基準項目以外の形式では無視されるので `0` を渡してください。 |

| 計算タイプ | 動作 | 基準項目パラメータ |
| --- | --- | --- |
| `Normal` | 二次計算なし；集計された値をそのまま表示（デフォルト）。 | — |
| `DifferenceFrom` | 基準フィールド内の基準項目の値との差として表示。 | `baseField` + `Previous`/`Next`/`Custom`（`baseItem` は `Custom` の場合のみ） |
| `PercentageOf` | 基準フィールド内の基準項目の値に対する割合で表示。 | `baseField` + `Previous`/`Next`/`Custom`（`baseItem` は `Custom` の場合のみ） |
| `PercentageDifferenceFrom` | 基準フィールド内の基準項目の値に対する差分率で表示。 | `baseField` + `Previous`/`Next`/`Custom`（`baseItem` は `Custom` の場合のみ） |
| `RunningTotalIn` | 基準フィールドの項目順序に従って累積合計として表示。 | `baseField`（累積を推進するフィールド） |
| `PercentageOfRow` | 行合計に対する割合で表示。 | — |
| `PercentageOfColumn` | 列合計に対する割合で表示。 | — |
| `PercentageOfTotal` | 全体合計に対する割合で表示。 | — |
| `Index` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) を使用して表示。 | — |
| `PercentageOfParentRowTotal` | ネストされた行フィールドの親行合計に対する割合で表示。 | — |
| `PercentageOfParentColumnTotal` | ネストされた列フィールドの親列合計に対する割合で表示。 | — |
| `PercentageOfParentTotal` | 親合計に対する割合で表示。 | `baseField`（基準となる親フィールド） |
| `PercentageOfRunningTotalIn` | 基準フィールドの累積合計に対する割合で表示。 | `baseField`（累積フィールド） |
| `RankSmallestToLargest` | 最小から最大へ順位付け（1 が最小）。 | — |
| `RankLargestToSmallest` | 最大から最小へ順位付け（1 が最大）。 | — |

{{% alert color="primary" %}}
`showValuesAs(...)` は `setCalculationType`、`setBaseFieldIndex`、`setBaseItemPositionType`、`setBaseItemIndex` の 4 つの `PivotShowValuesSetting` の値を書き込みます。メソッドと設定オブジェクトは同じ状態を構成する 2 つの方法であり、Excel の「値の表示」ダイアログにある基準フィールドと基準項目の選択と同様です。
{{% /alert %}}

## **合計に対する割合として値を表示**
`PivotField.showValuesAs` メソッドに `PivotFieldDataDisplayFormat.PercentageOfTotal` を指定して呼び出すと、合計を含むすべてのデータフィールドセルが全体合計に対する割合に変換されます。表示される数値は結果全体の比例として示されます。この形式はすべての値を全体合計に対して測定するだけなので、基準フィールドや基準項目は不要です。末尾の引数 (`0`, `PivotItemPositionType.Previous`, `0`) はこの形式が無視するプレースホルダーです（上記のパラメータ表を参照）。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotTable,
    PivotField,
    PivotFieldType,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.getCells().get(i + 1, 0).putValue(fruits[i])
    data_sheet.getCells().get(i + 1, 1).putValue(amounts[i])
# Add a pivot table on a new worksheet (getWorksheets().add() returns the sheet index)
pivot_sheet_index = workbook.getWorksheets().add()
pivot_table = workbook.getWorksheets().get(pivot_sheet_index).getPivotTables().add("=Sheet1!A1:B7", 2, 2)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **PivotField.getShowValuesSetting() の取得と設定**
`PivotField.getShowValuesSetting()` を使用して現在の構成を取得します。この読み取り専用メソッドはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティで有効な「値の表示」計算を示します。構成を変更するには `PivotField.showValuesAs` メソッドを呼び出します。このメソッドは 1 回の呼び出しで 4 つの設定すべてを書き込むため、個別にプロパティを設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトは `showValuesAs` が書き込む 4 つのプロパティを公開します:
- `getCalculationType()` は `PivotFieldDataDisplayFormat` の二次計算を返し、`setCalculationType(...)` で変更できます。
- `getBaseFieldIndex()` と `setBaseFieldIndex(...)` はピボットフィールド内の基準フィールドのゼロベースインデックスを指定します。これは基準関連フォーマットで使用されます。
- `getBaseItemPositionType()` と `setBaseItemPositionType(...)` は基準項目が現在の項目に対してどの位置にあるかを決定し、`PivotItemPositionType.Next`、`PivotItemPositionType.Previous`、`PivotItemPositionType.Custom` を受け取ります。
- `getBaseItemIndex()` と `setBaseItemIndex(...)` はゼロベースの基準項目インデックスを指定し、`BaseItemPositionType` が `Custom` の場合に使用されます。
`showValuesAs` を呼び出した後、`PivotTable.calculateData()` を再度呼び出してピボット本体を再計算および再描画し、更新された構成を反映させます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    PivotFieldDataDisplayFormat,
    PivotItemPositionType,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"CalculationType: {settings.getCalculationType()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemPositionType: {settings.getBaseItemPositionType()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.getShowValuesSetting().getCalculationType()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **関連記事**
- [ピボットテーブルでの値フィールドの管理](/cells/ja/python-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}