---
title: Aspose.Cells for Python via .NET でピボットテーブルの行フィールドと列フィールドを追加する
linktitle: Aspose.Cells for Python via .NET でピボットテーブルの行フィールドと列フィールドを追加する
description: Aspose.Cells for Python via .NET で、ピボットテーブルの行領域と列領域にベースフィールドを追加し、PivotField.set_subtotals を使用してピボットフィールドの集計を制御する方法を学びます。
keywords: Aspose.Cells, Python via .NET, ピボットテーブル, 行フィールド, 列フィールド, PivotField, set_subtotals, PivotFieldSubtotalType, 集計
type: docs
weight: 220
url: /ja/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Adding a Field to the Row or Column Region**
`PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` メソッドは、ベースフィールドをソースデータから 4 つのピボット領域のいずれかに移動します。`field_type` 引数は、次の `PivotFieldType` 値のいずれかを受け入れます。
- `ROW` — 左側に垂直に配置されるフィールド
- `COLUMN` — 上部に水平方向に配置されるフィールド
- `DATA` — 値が集計されるフィールド
- `PAGE` — レポートフィルターとして使用されるフィールド
フィールドのネスト順序は重要です。`Category` を最初に行領域に追加し、その後に `Item` を追加すると、外側グループ化が `Category`、内側グループ化が `Item` であるピボットが生成されます。順序を逆にした場合は階層が逆になります。

## **Pivot Field Subtotals**
`PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` メソッドは、ピボットフィールドに表示される集計行を制御します。各呼び出しは 1 つの集計タイプを独立して切り替えます。`shown = True` を渡すと集計が表示され、`shown = False` を渡すと非表示になります。各呼び出しは 1 つのタイプにのみ影響を与えるため、異なる `subtotal_type` 値でメソッドを複数回呼び出すと、集計のカスタムサブセットを構築できます。
`PivotFieldSubtotalType` 列挙型は、利用可能な集計の種類を定義します。
- `AUTOMATIC` — Aspose.Cells がデフォルトの選択（通常は数値フィールドに対して `SUM`）を自動的に選択します
- `NONE` — すべての集計行を抑制する
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STDDEV`
- `STDDEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
集計は、行領域（または列領域）に 2 つ以上のピボットフィールドがある場合にのみ表示されます。単一のフィールドには集計する意味のある対象が存在しないため、その場合 `set_subtotals` を呼び出しても目に見える効果はありません。したがって、この記事のすべての例では 2 つの行フィールド（外側が `Category`、内側が `Item`）を配置し、各 `Category` グループ間の集計境界が見えるようにしています。
{{% /alert %}}

## **Scenario 1 — Automatic (Default) Subtotals**
`set_subtotals` をまったく呼び出さない場合、Aspose.Cells は数値フィールドに `AUTOMATIC` の選択を適用します。次の例では、外側の `Category` 行フィールドに対して `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` を呼び出すことで、この動作を明示的に確認します。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get(0, 0).put_value("Category")
worksheet.cells.get(0, 1).put_value("Item")
worksheet.cells.get(0, 2).put_value("Year")
worksheet.cells.get(0, 3).put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Scenario 2 — Suppressing All Subtotals (None)**
`set_subtotals(PivotFieldSubtotalType.NONE, True)` を呼び出すと、ピボットからすべての集計行が削除され、フィールド行と下部の総合計のみが残ります。これは、集計行のない生のグループ化データが必要な場合に便利です。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells.get(0, j).put_value(headers[j])
data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45],
]
for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.cells.get(i + 1, j).put_value(data[i][j])
pivot_table = worksheet.pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [PivotFieldSubtotalType.SUM, PivotFieldSubtotalType.COUNT, PivotFieldSubtotalType.AVERAGE, PivotFieldSubtotalType.MAX, PivotFieldSubtotalType.MIN, PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
単一の集計タイプに限定されません。各 `set_subtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、`SUM` で 1 回、`AVERAGE` で 1 回、計 2 回メソッドを呼び出すと、各 `Category` グループに対して 2 つの集計行のカスタムサブセットが生成されます。

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldSubtotalType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells.get("A1").put_value("Category")
worksheet.cells.get("B1").put_value("Item")
worksheet.cells.get("C1").put_value("Year")
worksheet.cells.get("D1").put_value("Amount")
worksheet.cells.get(1, 0).put_value("Fruit")
worksheet.cells.get(1, 1).put_value("Apple")
worksheet.cells.get(1, 2).put_value(2020)
worksheet.cells.get(1, 3).put_value(100)
worksheet.cells.get(2, 0).put_value("Fruit")
worksheet.cells.get(2, 1).put_value("Apple")
worksheet.cells.get(2, 2).put_value(2021)
worksheet.cells.get(2, 3).put_value(150)
worksheet.cells.get(3, 0).put_value("Fruit")
worksheet.cells.get(3, 1).put_value("Banana")
worksheet.cells.get(3, 2).put_value(2020)
worksheet.cells.get(3, 3).put_value(80)
worksheet.cells.get(4, 0).put_value("Fruit")
worksheet.cells.get(4, 1).put_value("Banana")
worksheet.cells.get(4, 2).put_value(2021)
worksheet.cells.get(4, 3).put_value(90)
worksheet.cells.get(5, 0).put_value("Vegetable")
worksheet.cells.get(5, 1).put_value("Carrot")
worksheet.cells.get(5, 2).put_value(2020)
worksheet.cells.get(5, 3).put_value(50)
worksheet.cells.get(6, 0).put_value("Vegetable")
worksheet.cells.get(6, 1).put_value("Carrot")
worksheet.cells.get(6, 2).put_value(2021)
worksheet.cells.get(6, 3).put_value(60)
worksheet.cells.get(7, 0).put_value("Vegetable")
worksheet.cells.get(7, 1).put_value("Daikon")
worksheet.cells.get(7, 2).put_value(2020)
worksheet.cells.get(7, 3).put_value(40)
worksheet.cells.get(8, 0).put_value("Vegetable")
worksheet.cells.get(8, 1).put_value("Daikon")
worksheet.cells.get(8, 2).put_value(2021)
worksheet.cells.get(8, 3).put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_table = pivot_tables.add("A1:D9", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Recap**
三つのシナリオの違いは、`set_subtotals` の呼び出し方のみです。データセット、フィールド、およびそれらが割り当てられるエリアについては、すべて同一です。この点が、レイアウトを直接比較可能である理由です。
- **フィールドの配置。** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` は、ソース列をエリア内に移動します。同一エリア内では、このメソッド呼び出しの順序が表示順序となり、最初の呼び出しが最も外側のグループになります。小計を算出するには、同一エリア内に 2 つ以上のフィールドが必要です。1 つのフィールドしかないと、グループ間に小計を算出する対象が存在しなくなります。
- **シナリオ 1 — 自動小計。** `set_subtotals` を呼び出さない場合、小計の適用は Excel に委ねられ、Excel は数値フィールドに対して独自のデフォルト小計を適用します。`PivotFieldSubtotalType.AUTOMATIC` を指定して `set_subtotals` を呼び出すと、その選択を暗黙的ではなく明示的に記録します。
- **シナリオ 2 — 小計なし。** `PivotFieldSubtotalType.NONE` を指定して `set_subtotals` を呼び出すと、デフォルトの小計が無効化され、ピボットテーブルはフィールド行と合計行は維持しつつ、Excel が挿入していた中間の小計行を削除します。
- **シナリオ 3 — 選択的サブセット。** 各呼び出しは、正確に 1 つの小計タイプの有効/無効を切り替えます。呼び出しは互いにリセットするのではなく累積されます。そのため、`PivotFieldSubtotalType.SUM` を一度、`PivotFieldSubtotalType.AVERAGE` を一度呼び出すと、両方が有効化された状態となり、ピボットテーブルには「合計」小計、「平均」小計、および合計が表示されます。

{{% alert color="primary" %}}
小計に関する設定は、行エリアに特有のものではありません。`PivotTable.ColumnFields` から取得したフィールドに対して同じ `set_subtotals` の呼び出しを行うと、列軸上でも同じ 3 つのレイアウトが得られます。なぜなら、この設定は軸ではなくピボットフィールド自体に属しているからです。
{{% /alert %}}

## **Related Articles**
- [ピボットテーブルのページフィールド](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルを更新する](/cells/ja/python-net/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}