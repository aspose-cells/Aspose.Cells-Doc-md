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
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells[0, 0].put_value("Category")
worksheet.cells[0, 1].put_value("Item")
worksheet.cells[0, 2].put_value("Year")
worksheet.cells[0, 3].put_value("Amount")
worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)
worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)
worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)
worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)
worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)
worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)
worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)
worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **Scenario 2 — Suppressing All Subtotals (None)**
`set_subtotals(PivotFieldSubtotalType.NONE, True)` を呼び出すと、ピボットからすべての集計行が削除され、フィールド行と下部の総合計のみが残ります。これは、集計行のない生のグループ化データが必要な場合に便利です。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
headers = ["Category", "Item", "Year", "Amount"]
for j in range(len(headers)):
    worksheet.cells[0, j].put_value(headers[j])
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
        worksheet.cells[i + 1, j].put_value(data[i][j])
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
for st in [ac.PivotFieldSubtotalType.SUM, ac.PivotFieldSubtotalType.COUNT, ac.PivotFieldSubtotalType.AVERAGE, ac.PivotFieldSubtotalType.MAX, ac.PivotFieldSubtotalType.MIN, ac.PivotFieldSubtotalType.PRODUCT]:
    category_field.set_subtotals(st, True)
pivot_table.calculate_data()
workbook.save("output_none.xlsx")
```

## **Scenario 3 — Custom Subtotal Subset (Sum + Average)**
単一の集計タイプに限定されません。各 `set_subtotals` 呼び出しは 1 つのタイプに対して独立して動作するため、`SUM` で 1 回、`AVERAGE` で 1 回、計 2 回メソッドを呼び出すと、各 `Category` グループに対して 2 つの集計行のカスタムサブセットが生成されます。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"
worksheet.cells["A1"].put_value("Category")
worksheet.cells["B1"].put_value("Item")
worksheet.cells["C1"].put_value("Year")
worksheet.cells["D1"].put_value("Amount")
worksheet.cells[1, 0].put_value("Fruit")
worksheet.cells[1, 1].put_value("Apple")
worksheet.cells[1, 2].put_value(2020)
worksheet.cells[1, 3].put_value(100)
worksheet.cells[2, 0].put_value("Fruit")
worksheet.cells[2, 1].put_value("Apple")
worksheet.cells[2, 2].put_value(2021)
worksheet.cells[2, 3].put_value(150)
worksheet.cells[3, 0].put_value("Fruit")
worksheet.cells[3, 1].put_value("Banana")
worksheet.cells[3, 2].put_value(2020)
worksheet.cells[3, 3].put_value(80)
worksheet.cells[4, 0].put_value("Fruit")
worksheet.cells[4, 1].put_value("Banana")
worksheet.cells[4, 2].put_value(2021)
worksheet.cells[4, 3].put_value(90)
worksheet.cells[5, 0].put_value("Vegetable")
worksheet.cells[5, 1].put_value("Carrot")
worksheet.cells[5, 2].put_value(2020)
worksheet.cells[5, 3].put_value(50)
worksheet.cells[6, 0].put_value("Vegetable")
worksheet.cells[6, 1].put_value("Carrot")
worksheet.cells[6, 2].put_value(2021)
worksheet.cells[6, 3].put_value(60)
worksheet.cells[7, 0].put_value("Vegetable")
worksheet.cells[7, 1].put_value("Daikon")
worksheet.cells[7, 2].put_value(2020)
worksheet.cells[7, 3].put_value(40)
worksheet.cells[8, 0].put_value("Vegetable")
worksheet.cells[8, 1].put_value("Daikon")
worksheet.cells[8, 2].put_value(2021)
worksheet.cells[8, 3].put_value(45)
pivot_tables = worksheet.pivot_tables
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(ac.PivotFieldSubtotalType.SUM, True)
category_field.set_subtotals(ac.PivotFieldSubtotalType.AVERAGE, True)
pivot_table.calculate_data()
workbook.save("output_custom.xlsx")
```

## **Recap**

## **Related Articles**
- [ピボットテーブルのページフィールド](/cells/ja/python-net/add-page-field-in-pivot-table/)
- [Aspose.Cells for Python via .NET でピボットテーブルを更新する](/cells/ja/python-net/refresh-pivot-table/)
- [ピボットテーブルへのスタイルの適用](/cells/ja/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}