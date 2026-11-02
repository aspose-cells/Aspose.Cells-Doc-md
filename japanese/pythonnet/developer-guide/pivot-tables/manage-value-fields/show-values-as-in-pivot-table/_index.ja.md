---
title: ピボットテーブルの Show Values As
linktitle: ピボットテーブルの Show Values As
description: Aspose.Cells for Python via .NET を使用して、ピボットテーブルのデータフィールドの値を合計の割合、ベース項目との差分、累積合計、ランクなどとして表示します。
keywords: Aspose.Cells for Python via .NET, ピボットテーブル, Show Values As, データ表示形式, PivotFieldDataDisplayFormat, PercentageOfTotal, PivotShowValuesSetting, CalculationType, BaseFieldIndex, Python
type: docs
weight: 145
url: /ja/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **使用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` などの集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換えます。たとえば、全体合計に対するパーセンテージ、累積合計、選択したベース項目との差分、または順位などです。これにより、補助的な数式や計算列を使用せずに比較分析が可能になります。  
典型的な使用例としては、行・列・全体合計に対するパーセンテージによるシェア分析、期間フィールドにおける累積合計レポート、ベース項目との差またはパーセンテージ差によるベンチマーク分析、最小から最大、または最大から最小への順位付けなどがあります。  
Aspose.Cells for Python via .NET では、`PivotFieldDataDisplayFormat` が二次計算を選択します。読み取り専用の `PivotField.show_values_setting` プロパティは `PivotShowValuesSetting` オブジェクトを返し、その書き込み可能な `calculation_type`、`base_field_index`、`base_item_position_type`、`base_item_index` プロパティで動作を構成します。便利メソッド `PivotField.show_values_as(...)` は同じ 4 つの設定を一度に適用します。これらの設定は `PivotTable.data_fields` から取得したデータまたは値フィールドに適用します。

## **PivotFieldDataDisplayFormat 列挙メンバー**
データフィールドは `SUM` や `COUNT` などの集計関数を保持したまま、Show Values As は集計値の表示方法だけを変換します。  
`PivotShowValuesSetting` プロパティを直接設定する（最終セクション参照）以外に、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。

```python
from aspose.cells.pivot import PivotField, PivotFieldDataDisplayFormat, PivotItemPositionType
def show_values_as(
    pivot_field: PivotField,
    display_format: PivotFieldDataDisplayFormat,
    base_field: int,
    base_item_position_type: PivotItemPositionType,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        display_format,
        base_field,
        base_item_position_type,
        base_item,
    )
```

| パラメーター | 意味 | 必要な場合 |
| --- | --- | --- |
| `display_format` | 適用する `PivotFieldDataDisplayFormat` の二次計算。 | 常に。 |
| `base_field` | ピボットテーブルのベースフィールドのゼロベースインデックス（例: ベース項目が属する行フィールドのインデックス）。 | 以下の 6 つの基準関連フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`）のみで使用され、その他のフォーマットでは無視されます。 |
| `base_item_position_type` | 現在の項目に対してベース項目が選択される位置：`PivotItemPositionType.PREVIOUS`、`.NEXT`、または `.CUSTOM`。 | 3 つの基準項目フォーマット（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`）のみで使用され、その他のフォーマットでは無視されます。 |
| `base_item` | ベース項目のゼロベースインデックス。 | `base_item_position_type` が `CUSTOM` のときのみ必要（正確なベース項目を指定）。`PREVIOUS` / `NEXT` の場合やベース項目形式でない場合は `0` を渡してください。 |

| 計算タイプ | 動作 | ベース項目パラメーター |
| --- | --- | --- |
| `NORMAL` | 二次計算なし; 集計値はそのまま表示されます（デフォルト）。 | — |
| `DIFFERENCE_FROM` | ベースフィールドのベース項目の値との差として表示します。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`base_item` は `CUSTOM` のみ） |
| `PERCENTAGE_OF` | ベースフィールドのベース項目の値に対するパーセンテージとして表示します。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`base_item` は `CUSTOM` のみ） |
| `PERCENTAGE_DIFFERENCE_FROM` | ベースフィールドのベース項目の値に対するパーセンテージ差として表示します。 | `base_field` + `PREVIOUS`/`NEXT`/`CUSTOM`（`base_item` は `CUSTOM` のみ） |
| `RUNNING_TOTAL_IN` | ベースフィールドの項目順序に従って累積合計として表示します。 | `base_field`（蓄積を駆動するフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_TOTAL` | 全体合計に対するパーセンテージとして表示します。 | — |
| `INDEX` | Excel の INDEX 方式（(value * grand total) / (row total * column total)）で表示します。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示します。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対するパーセンテージとして表示します。 | `baseField`（基準となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | ベースフィールドの累積合計に対するパーセンテージとして表示します。 | `base_field`（蓄積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 値を最小 (1) から最大へ順位付けします。 | — |
| `RANK_LARGEST_TO_SMALLEST` | 値を最大 (1) から最小へ順位付けします。 | — |

{{% alert color="primary" %}}
`show_values_as(...)` は `PivotShowValuesSetting` プロパティ（`calculation_type`、`base_field_index`、`base_item_position_type`、`base_item_index`）を書き込みます — このメソッドとプロパティオブジェクトは同じ状態を構成する 2 通りの方法であり、Excel の Show Values As ダイアログのベースフィールドとベース項目選択と同様です。
{{% /alert %}}

## **全体合計に対するパーセンテージとして表示**
`PivotField.show_values_as` メソッドに `PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、全体合計を含むすべてのデータフィールドセルを全体合計に対するシェアに変換します。表示される数値は結果全体の比率として解釈されます。この形式は全体合計に対してのみ各値を測定するため、ベースフィールドやベース項目は不要です — 後続の引数（`0`、`PivotItemPositionType.PREVIOUS`、`0`）はこの形式が無視するプレースホルダーです（上記のパラメーター表参照）。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
# Load or create a workbook with source data
workbook = ac.Workbook()
data_sheet = workbook.worksheets[0]
data_sheet.cells.get("A1").put_value("Fruit")
data_sheet.cells.get("B1").put_value("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
amounts = [10, 20, 30, 40, 50, 60]
for i in range(len(fruits)):
    data_sheet.cells.get(i + 1, 0).put_value(fruits[i])
    data_sheet.cells.get(i + 1, 1).put_value(amounts[i])
# Add a pivot table on a new worksheet (worksheets.add() returns the sheet index)
pivot_sheet_index = workbook.worksheets.add()
pivot_table = workbook.worksheets[pivot_sheet_index].pivot_tables.add("=Sheet1!A1:B7", 2, 2)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Show the Amount data field as a percentage of the grand total with the
# one-call method; PercentageOfTotal takes no base item, so the trailing
# base arguments (0, Previous, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(
    PivotFieldDataDisplayFormat.PERCENTAGE_OF_TOTAL,
    0,
    PivotItemPositionType.PREVIOUS,
    0,
)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **PivotField.show_values_setting の取得と構成**
`PivotField.show_values_setting` を使用して現在の構成を読み取ります: この読み取り専用プロパティはフィールドの `PivotShowValuesSetting` オブジェクトを返し、4 つのプロパティが現在の Show Values As 計算を表します。構成を変更するには `PivotField.show_values_as` メソッドを呼び出します — 1 回の呼び出しで 4 つの設定すべてを書き込むため、個別にプロパティを設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトは `show_values_as` が書き込む 4 つのプロパティを公開します:
- `calculation_type` は `PivotFieldDataDisplayFormat` の二次計算を選択します。
- `base_field_index` はピボットフィールド内のベースフィールドのゼロベースインデックスを指定します。基準関連フォーマットで使用されます。
- `base_item_position_type` はベース項目が現在の項目に対してどの位置にあるかを決定し、`PivotItemPositionType.NEXT`、`PivotItemPositionType.PREVIOUS`、`PivotItemPositionType.CUSTOM` のいずれかを受け入れます。
- `base_item_index` はゼロベースのベース項目インデックスを指定し、`base_item_position_type` が `CUSTOM` の場合に使用されます。
`show_values_as` を呼び出した後、`PivotTable.calculate_data()` を再度呼び出してピボット本体を再計算し、更新された構成で再描画します。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotFieldType, PivotItemPositionType
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"CalculationType: {settings.calculation_type}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemPositionType: {settings.base_item_position_type}")
print(f"BaseItemIndex: {settings.base_item_index}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotFieldDataDisplayFormat.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotItemPositionType.PREVIOUS,
    0
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"CalculationType now: {data_field.show_values_setting.calculation_type}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **関連記事**
- [ピボットテーブルの値フィールドの管理](/cells/ja/python-net/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/python-net/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}