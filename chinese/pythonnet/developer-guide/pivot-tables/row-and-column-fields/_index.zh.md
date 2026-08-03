---
title: 在 Aspose.Cells for Python via .NET 中添加数据透视表的行字段和列字段
linktitle: 行字段和列字段
description: 了解如何在 Aspose.Cells for Python via .NET 中将基本字段添加到数据透视表的行区域和列区域，以及如何使用 PivotField.set_subtotals 控制数据透视字段小计。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 行字段, 列字段, PivotField, set_subtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **向行或列区域添加字段**

`PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` 方法可将一个基本字段从源数据移动到四个数据透视区域之一。`field_type` 参数接受以下 `PivotFieldType` 值之一。

- `ROW` — 垂直放置在左侧的字段
- `COLUMN` — 水平放置在顶部的字段
- `DATA` — 其值会被聚合的字段
- `PAGE` — 用作报表筛选器的字段

添加字段后，您可以通过 `PivotTable.row_fields` 和 `PivotTable.column_fields` 属性访问它们。每个属性返回一个 `PivotFieldCollection`。`row_fields` 中索引为 0 的字段是最外层的行字段，后续索引表示嵌套在其内部的字段。相同的索引约定同样适用于 `column_fields`。

字段的嵌套顺序很重要。先将 `Category` 添加到行区域，然后再添加 `Item`，会生成一个外层分组为 `Category`、内层分组为 `Item` 的数据透视表。反转顺序则会反转层次结构。

## **数据透视字段小计**

`PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` 方法控制哪些小计行会出现在数据透视字段中。每次调用都会独立切换一种小计类型。传入 `shown = True` 会显示小计，而传入 `shown = False` 则会隐藏小计。由于每次调用仅影响一种类型，因此可以使用不同的 `subtotal_type` 值多次调用该方法，以构建自定义的小计子集。

`PivotFieldSubtotalType` 枚举定义了可用的小计类型。

- `AUTOMATIC` — Aspose.Cells 选择默认选项（通常对数值字段使用 `SUM`）
- `NONE` — 抑制所有小计行
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
小计仅在行区域（或列区域）中有两个或更多数据透视字段时才会呈现。单个字段之间没有有意义的内容可供小计，因此在这种情况下对 `set_subtotals` 的调用没有可见效果。因此，本文在每个示例中都会在行区域放置两个行字段（外层 `Category`，内层 `Item`），以便能够看到每个 `Category` 组之间的小计边界。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**

如果您完全不调用 `set_subtotals`，Aspose.Cells 会将 `AUTOMATIC` 选项应用于数值字段。下面的示例通过在外层 `Category` 行字段上调用 `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` 来明确确认此行为。

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

## **场景 2 — 抑制所有小计（None）**

调用 `set_subtotals(PivotFieldSubtotalType.NONE, True)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计行。当您希望仅查看分组的原始数据而没有任何汇总行时，这非常有用。

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

## **场景 3 — 自定义小计子集（Sum + Average）**

您并不局限于单一的小计类型。每次 `set_subtotals` 调用都会独立作用于一种类型，因此调用该方法两次（一次使用 `SUM`，一次使用 `AVERAGE`）会为每个 `Category` 组生成一个包含两种小计行的自定义子集。

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

## **总结**

上述三个场景共享相同的数据集和数据透视表结构。它们之间唯一的区别是应用于外层 `Category` 行字段的 `set_subtotals` 调用。请记住两条字段规则：区域中只有一个字段时没有任何内容可供小计，因此当您希望 `set_subtotals` 产生可见效果时，请始终在行或列区域中至少放置两个字段。
{{< app/cells/assistant language="python-net" >}}
