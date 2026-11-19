---
title: ピボットテーブルでの「Show Values As」機能の使用方法
linktitle: ピボットテーブルでの「Show Values As」機能の使用方法
description: Aspose.Cells for Python via Java を使用して、ピボットテーブルのデータ フィールドの値を合計に対するパーセンテージ、基準項目との差、累積合計、ランクなどとして表示します。
keywords: Aspose.Cells, ピボットテーブル, Show Values As, PivotShowValuesAsType, PERCENTAGE_OF_TOTAL, PivotShowValuesSetting, showValuesAs, BaseFieldIndex, BaseItemIndex, Python
type: docs
weight: 145
url: /ja/python-java/show-values-as-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **利用シナリオ**
ピボットテーブルは通常、`SUM` や `COUNT` といった集計関数で各データ フィールドを集約します。Excel の **Show Values As** 機能は、集計結果を二次計算で置き換え、例えば総計に対するパーセンテージ、累積合計、基準項目との差、ランクなどを表示できるようにします。これにより、補助数式や計算列を使用せずに比較分析が可能になります。  

主な使用例は、行・列・総計に対するパーセンテージによる全体シェア分析、期間フィールドでの累積レポート、基準項目との差異やパーセンテージ差によるベンチマーク分析、最小から最大または最大から最小へのランキングです。  

Aspose.Cells for Python via Java では、`PivotShowValuesAsType` 列挙体で二次計算を選択します。読み取り専用の `PivotField.getShowValuesSetting()` メソッドは `PivotShowValuesSetting` オブジェクトを返し、`setShowValuesAs(...)`、`setBaseFieldIndex(...)`、`setBaseItemIndex(...)` メソッドで動作を構成できます。便利メソッド `PivotField.showValuesAs(...)` でも同じ設定を一度に適用できます。これらの設定は `PivotTable.getDataFields()` で取得したデータまたは値フィールドに対して適用します。

## **PivotShowValuesAsType 列挙体メンバー**
データ フィールドは `SUM` や `COUNT` といった集計関数を保持したまま、Show Values As によって表示方法だけが変換されます。  

`PivotShowValuesSetting` のセッターを直接使用する方法（最終セクション参照）に加え、1 回の呼び出しで同じ構成を適用できる便利メソッドがあります。このメソッドは 2 つの形態で提供されます。1 つはインデックスでベース フィールドとベース項目を指定し、もう 1 つは名前で指定します。

```python
from asposecells.api import PivotField, PivotShowValuesAsType
def show_values_as(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: int,
    base_item: int,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)

def show_values_as_by_name(
    pivot_field: PivotField,
    show_values_as_type: PivotShowValuesAsType,
    base_field: str,
    base_item: str,
):
    pivot_field.showValuesAs(show_values_as_type, base_field, base_item)
```

| パラメーター | 説明 | 必要な場合 |
| --- | --- | --- |
| `show_values_as_type` | 適用する `PivotShowValuesAsType` の二次計算。 | 常に |
| `base_field` | ピボットテーブルのベース フィールド群の中でのゼロベースインデックス（例: ベース項目が属する行フィールドのインデックス）。名前形式の場合はベース フィールド名。 | 8 種類のベース相対形式（`DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM`、`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、`RANK_SMALLEST_TO_LARGEST`、`RANK_LARGEST_TO_SMALLEST`）で必要。その他の形式では `0`（名前形式では `None`）を指定 |
| `base_item` | ベース項目のゼロベースインデックス。2 つのセンチネルがあり、`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）は前の項目、`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）は次の項目を選択。名前形式ではベース項目のキャプションを指定し、ベース項目が不要な形式では `None` を使用。 | `DIFFERENCE_FROM`、`PERCENTAGE_OF`、`PERCENTAGE_DIFFERENCE_FROM` の 3 種類のベース項目形式で必要。`RUNNING_TOTAL_IN`、`PERCENTAGE_OF_PARENT_TOTAL`、`PERCENTAGE_OF_RUNNING_TOTAL_IN`、両方のランク形式では無視されるため `0` または `None` を指定 |

| 計算タイプ | 動作 | ベース項目パラメーター |
| --- | --- | --- |
| `NORMAL` | 二次計算なし。集計値そのものが表示される（デフォルト）。 | — |
| `DIFFERENCE_FROM` | ベース フィールドのベース項目の値との差として表示する。 | `base_field` + `base_item`（インデックスまたはキャプション、または前/次センチネル） |
| `PERCENTAGE_OF` | ベース フィールドのベース項目の値に対するパーセンテージとして表示する。 | `base_field` + `base_item` |
| `PERCENTAGE_DIFFERENCE_FROM` | ベース フィールドのベース項目の値との差のパーセンテージとして表示する。 | `base_field` + `base_item` |
| `RUNNING_TOTAL_IN` | ベース フィールドの項目順に従って累積合計として表示する。 | `base_field`（累積のトリガーになるフィールド） |
| `PERCENTAGE_OF_ROW` | 行合計に対するパーセンテージとして表示する。 | — |
| `PERCENTAGE_OF_COLUMN` | 列合計に対するパーセンテージとして表示する。 | — |
| `PERCENTAGE_OF_TOTAL` | 総計に対するパーセンテージとして表示する。 | — |
| `INDEX` | Excel の INDEX 式 ((value * grand total) / (row total * column total)) を使用して表示する。 | — |
| `PERCENTAGE_OF_PARENT_ROW_TOTAL` | 入れ子になった行フィールドの場合、親行合計に対するパーセンテージとして表示する。 | — |
| `PERCENTAGE_OF_PARENT_COLUMN_TOTAL` | 入れ子になった列フィールドの場合、親列合計に対するパーセンテージとして表示する。 | — |
| `PERCENTAGE_OF_PARENT_TOTAL` | 親フィールドの合計に対するパーセンテージとして表示する。 | `base_field`（参照先となる親フィールド） |
| `PERCENTAGE_OF_RUNNING_TOTAL_IN` | ベース フィールドの累積合計に対するパーセンテージとして表示する。 | `base_field`（累積フィールド） |
| `RANK_SMALLEST_TO_LARGEST` | 最小 (1) から最大へ順位付けする。 | `base_field`（順位付け範囲を定義するフィールド） |
| `RANK_LARGEST_TO_SMALLEST` | 最大 (1) から最小へ順位付けする。 | `base_field`（順位付け範囲を定義するフィールド） |

{{% alert color="primary" %}}
`showValuesAs(...)` は `setShowValuesAs`、`setBaseFieldIndex`、`setBaseItemIndex` を通じて `PivotShowValuesSetting` の値を書き込みます。メソッドと設定オブジェクトは同一状態を構成する 2 つの方法であり、Excel の「Show Values As」ダイアログのベース フィールドとベース項目選択を反映します。
{{% /alert %}}

## **総計に対するパーセンテージとして表示**
`PivotField.showValuesAs` メソッドに `PivotShowValuesAsType.PERCENTAGE_OF_TOTAL` を指定して呼び出すと、すべてのデータ フィールド セル（総計を含む）が総計に対するシェアとして変換されます。表示される数値は結果セット全体の割合として解釈されます。この形式は総計に対してのみ測定するため、ベース フィールドやベース項目は不要です。末尾の引数 (`0`, `0`) はフォーマットが無視するプレースホルダーであることが上記パラメータ表で示されています。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotShowValuesAsType,
)
# Load or create a workbook with source data
workbook = Workbook()
data_sheet = workbook.getWorksheets().get(0)
data_sheet.getCells().get("A1").putValue("Fruit")
data_sheet.getCells().get("B1").putValue("Amount")
fruits = ["Apple", "Banana", "Apple", "Cherry", "Banana", "Apple"]
# float literals keep putValue on the double overload (an untyped Python int is ambiguous between putValue(boolean/int/Object) overloads)
amounts = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
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
# one-call method; PERCENTAGE_OF_TOTAL takes no base item, so the trailing
# base arguments (0, 0) are placeholders the format ignores
data_field = pivot_table.getDataFields().get(0)
data_field.showValuesAs(PivotShowValuesAsType.PERCENTAGE_OF_TOTAL, 0, 0)
pivot_table.calculateData()
# Body now reads: Apple 47.62%, Banana 33.33%, Cherry 19.05%, Grand Total 100.00%
workbook.save("ShowValuesAsPercentageOfTotal.xlsx")
jpype.shutdownJVM()
```

## **PivotField.getShowValuesSetting() の取得と構成**
`PivotField.getShowValuesSetting()` を使用して現在の構成を取得します。この読み取り専用メソッドはフィールドの `PivotShowValuesSetting` オブジェクトを返し、プロパティで有効な「Show Values As」計算を示します。構成を変更するには `PivotField.showValuesAs` メソッドを呼び出します。このメソッドはすべての設定を一度に書き込むため、個別にプロパティを設定する必要はありません。  

`PivotShowValuesSetting` オブジェクトが公開する状態は次の通りです：  
- `getShowValuesAs()` は二次計算である `PivotShowValuesAsType` を返し、`setShowValuesAs(...)` で変更できます。  
- `getBaseFieldIndex()` と `setBaseFieldIndex(...)` はベース フィールドのゼロベースインデックスを指定し、ベース相対形式で使用されます。  
- `getBaseItemIndex()` と `setBaseItemIndex(...)` はベース項目を指定します。具体的には特定のピボット項目のゼロベースインデックス、または 2 つのセンチネル（`PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM`（-1）で前項目、`PivotShowValuesSetting.NEXT_PIVOT_ITEM`（-2）で次項目）です。ベース項目形式で使用されます。  
- `getBaseFieldName()` と `getBaseItemCaption()` は読み取り専用ビューで、解決されたベース フィールド名とベース項目キャプションを報告します。たとえば、前項目センチネルを選択した場合、`getBaseItemCaption()` は `(previous)` を返します。  

`showValuesAs` を呼び出した後は、`PivotTable.calculateData()` を再度実行してピボット本体を再計算し、更新された構成で再描画させます。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotShowValuesAsType,
    PivotShowValuesSetting,
)
workbook = Workbook("ShowValuesAsPercentageOfTotal.xlsx")
pivot_table = workbook.getWorksheets().get(1).getPivotTables().get(0)
data_field = pivot_table.getDataFields().get(0)
# Read the current show-values settings
settings = data_field.getShowValuesSetting()
print(f"ShowValuesAs: {settings.getShowValuesAs()}")
print(f"BaseFieldIndex: {settings.getBaseFieldIndex()}")
print(f"BaseItemIndex: {settings.getBaseItemIndex()}")
print(f"BaseFieldName: {settings.getBaseFieldName()}")
print(f"BaseItemCaption: {settings.getBaseItemCaption()}")
# Switch to a base-item calculation with the one-call method: difference
# from the value of the previous item in the row field
data_field.showValuesAs(
    PivotShowValuesAsType.DIFFERENCE_FROM,
    pivot_table.getRowFields().get(0).getBaseIndex(),
    PivotShowValuesSetting.PREVIOUS_PIVOT_ITEM,
)
pivot_table.calculateData()
# Note: the percentage number format saved by the previous example still
# clings to the data field cells; the underlying values are now differences
# Re-read the applied configuration
print(f"ShowValuesAs now: {data_field.getShowValuesSetting().getShowValuesAs()}")
workbook.save("ShowValuesAsDifferenceFrom.xlsx")
jpype.shutdownJVM()
```

## **関連項目**
- [ピボットテーブルの値フィールドの管理](/cells/ja/python-java/manage-value-fields/)
- [ピボットテーブルの更新](/cells/ja/python-java/refresh-pivot-table/)
- [ピボットテーブルへのスタイル適用](/cells/ja/python-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python" >}}