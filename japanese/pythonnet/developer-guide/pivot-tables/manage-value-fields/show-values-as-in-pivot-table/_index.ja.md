---
title: ピボットテーブルでの値の表示方法
linktitle: ピボットテーブルでの値の表示方法
description: Aspose.Cells for Python via .NET を使用して、ピボットテーブルのデータフィールドの値を合計の割合、基準項目との差、累計、順位などとして表示できます。
keywords: Aspose.Cells, ピボットテーブル, 値の表示方法, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, show_values_as, base_field_index, base_item_index, Python
type: docs
weight: 145
url: /ja/python-net/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` といった集計関数で各データフィールドを集計します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、たとえば総計に対するパーセンテージ、累計、選択した基準項目との差、順位などを表示できるようにします。これにより、ヘルパー数式や計算列を使わずに比較分析が可能になります。  
典型的な使用例としては、行・列・総計に対するパーセンテージによる構成比分析、期間フィールドでの累積レポート、基準項目との差やパーセンテージ差によるベンチマーク分析、最小から最大、または最大から最小への順位付けなどがあります。  
Aspose.Cells for Python via .NET では、`PivotShowValuesAsType` 列挙体で二次計算を選択します。読み取り専用の `PivotField.show_values_setting` プロパティは `PivotShowValuesSetting` オブジェクトを返し、書き込み可能な `show_values_as`、`base_field_index`、`base_item_index` プロパティで動作を構成できます。便利メソッド `PivotField.show_values_as(...)` でも同じ設定を 1 回の呼び出しで適用できます。これらの設定は `PivotTable.data_fields` から取得したデータまたは値フィールドに適用します。

## **PivotShowValuesAsType 列挙体メンバー**
データフィールドは `SUM` や `COUNT` といった集計関数を保持したまま、Show Values As は集計値の表示方法だけを変換します。  
`PivotShowValuesSetting` プロパティを直接設定する方法（最終セクション参照）に加えて、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。2 つの形式があり、インデックスで基底フィールドと基底項目を指定するものと、名前で指定するものがあります。

```python
from aspose.cells.pivot import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
) -> None:
    pivot_field.show_values_as(
        show_values_as_type,
        base_field,
        base_item,
    )
```

| パラメータ | 意味 | 必要な場合 |
| --- | --- | --- |
| `show_values_as_type` | 適用する `PivotShowValuesAsType` 二次計算。 | 常に必須です。 |
| `base_field` | ピボットテーブルの基底フィールドのゼロベースインデックス（例: 基底項目が属する行フィールドのインデックス）、または名前形式の場合は基底フィールド名。 | 下記 8 つの基底相対形式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）で使用し、その他の形式では `0`（名前形式では `None`）を渡します。 |
| `base_item` | 基底項目のゼロベースインデックス。2 つのセンチネルがあり、`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）は前の項目、`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）は次の項目を選択します。名前形式の場合は基底項目のキャプションを使用し、基底項目が不要な形式では `None` を指定します。 | `DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM` の 3 つの基底項目形式で評価され、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、順位形式の 5 つでは無視されます — その場合は `0` または `None` を渡します。 |

| 計算タイプ | 動作 | 基準項目パラメータ |
| --- | --- | --- |
| `NORMAL` | 二次計算を行わず、集計値をそのまま表示（デフォルト）。 | — |
| `DIFFERENCE_FROM` | 基底フィールドの基底項目の値との差として表示。 | `base_field` + `base_item`（インデックスまたはキャプション、または前/次センチネル） |
| `PERCENTAGE_OF` | 基底フィールドの基底項目の値に対するパーセンテージとして表示。 | `base_field` + `base_item`（インデックスまたはキャプション、または前/次センチネル） |
| `PERCENTAGE_DIFFERENCE_FROM` | 基底フィールドの基底項目の値に対するパーセンテージ差として表示。 | `base_field` + `base_item`（インデックスまたはキャプション、または前/次センチネル） |
| `RUNNING_TOTAL_IN` | 基底フィールドの項目順に累積した合計として表示。 | `base_field`（累積の基準となるフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_TOTAL` | 総計に対するパーセンテージとして表示。 | — |
| `INDEX` | Excel のインデックス数式 ((value * grand total) / (row total * column total)) を使用して表示。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | ネストされた行フィールドの場合、親行合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | ネストされた列フィールドの場合、親列合計に対するパーセンテージとして表示。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親合計に対するパーセンテージとして表示。 | `base_field`（参照対象となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | 基底フィールドの累計に対するパーセンテージとして表示。 | `base_field`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 値を最小（1）から最大へ順位付け。 | `base_field`（順位の範囲を定義するフィールド） |
| `RANK_LARGEST_TO_SMALLEST` | 値を最大（1）から最小へ順位付け。 | `base_field`（順位の範囲を定義するフィールド） |

{{% alert color="primary" %}}
`show_values_as(...)` は `PivotShowValuesSetting` プロパティ（`show_values_as`、`base_field_index`、`base_item_index`）を書き込みます。メソッドとプロパティオブジェクトは同じ状態を構成する 2 つの方法であり、Excel の「値の表示形式」ダイアログの基底フィールドと基底項目の選択肢を反映します。
{{% /alert %}}

## **総計のパーセンテージとして値を表示**
`PivotField.show_values_as` メソッドに `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、すべてのデータフィールドセル（総計を含む）が総計に対する割合として変換されます。表示される数値は全体結果セットの比率として読み取れます。この形式は総計のみを基準とするため、基底フィールドや基底項目は不要です。テーブルで示したように、後続の引数（`0`、`0`）はフォーマットが無視するプレースホルダーです。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType
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
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.data_fields[0]
data_field.show_values_as(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculate_data()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
```

## **PivotField.show_values_setting の取得と構成**
現在の構成は `PivotField.show_values_setting` で取得できます。読み取り専用プロパティはフィールドの `PivotShowValuesSetting` オブジェクトを返し、プロパティで現在の「値の表示形式」計算が確認できます。構成を変更するには `PivotField.show_values_as` メソッドを呼び出します。このメソッドは 1 回の呼び出しで全設定を書き込むため、個別にプロパティを設定する必要はありません。  
`PivotShowValuesSetting` オブジェクトが保持する状態は次のとおりです。
- `show_values_as` は `PivotShowValuesAsType` の二次計算を選択します。
- `base_field_index` は基底フィールドのゼロベースインデックスを指定し、基底相対形式で使用されます。
- `base_item_index` は基底項目を指定します。具体的には特定のピボット項目のゼロベースインデックス、または 2 つのセンチネルのいずれか（`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）で前項目、`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）で次項目）です。基底項目形式で使用されます。
- `base_field_name` と `base_item_caption` は読み取り専用ビューで、解決された基底フィールド名と基底項目キャプションを返します。たとえば前項目センチネルを選択した場合、`base_item_caption` は `(previous)` と表示されます。  
`show_values_as` を呼び出した後は、`PivotTable.calculate_data()` を再度呼び出してピボット本体を再計算し、更新された構成で再描画してください。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotShowValuesAsType, PivotShowValuesSetting
workbook = ac.Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.worksheets[1].pivot_tables[0]
data_field = pivot_table.data_fields[0]
# Read the current show-values settings
settings = data_field.show_values_setting
print(f"ShowValuesAs: {settings.show_values_as}")
print(f"BaseFieldIndex: {settings.base_field_index}")
print(f"BaseItemIndex: {settings.base_item_index}")
print(f"BaseFieldName: {settings.base_field_name}")
print(f"BaseItemCaption: {settings.base_item_caption}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.show_values_as(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.row_fields[0].base_index,
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM
)
pivot_table.calculate_data()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.show_values_setting.show_values_as}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
```

## **関連記事**
- [ピボットテーブルの値フィールドの管理](/cells/ja/python-net/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/python-net/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}