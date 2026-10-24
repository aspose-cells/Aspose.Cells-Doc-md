---
title: Aspose.Cells for Python via .NET 中的行字段和列字段
linktitle: 行字段和列字段
description: 了解如何使用 Aspose.Cells for Python via .NET 将基础字段添加到数据透视表的行区域和列区域，以及如何使用 PivotField.set_subtotals 控制数据透视字段的小计
keywords: Aspose.Cells, Python via .NET, 数据透视表, 行字段, 列字段, PivotField, set_subtotals, PivotFieldSubtotalType, 小计
type: docs
weight: 220
url: /zh/python-net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

行字段和列字段是数据透视表的基本组成部分。放置在行区域的字段会垂直显示在数据透视表的左侧，而放置在列区域的字段则会水平显示在数据透视表的顶部。本文介绍如何通过编程方式将基础字段添加到这些区域，以及如何使用 `PivotField.set_subtotals` 方法控制字段组之间显示的小计。

## **向行区域或列区域添加字段**
`PivotTable.add_field_to_area(PivotFieldType field_type, string field_name)` 方法将一个基础字段从源数据移动到四个数据透视区域之一。`field_type` 参数接受以下 `PivotFieldType` 枚举值之一。
- `ROW` — 垂直放置在左侧的字段
- `COLUMN` — 水平放置在顶部的字段
- `DATA` — 其值被聚合的字段
- `PAGE` — 用作报表筛选器的字段
添加字段后，可以通过 `PivotTable.row_fields` 和 `PivotTable.column_fields` 属性访问它们。每个属性返回一个 `PivotFieldCollection`。`row_fields` 中索引 0 处的字段是最外层的行字段，后续索引表示嵌套在其中的字段。相同的索引约定同样适用于 `column_fields`。
字段的嵌套顺序很重要。先将 `Category` 添加到行区域，然后再添加 `Item`，则会生成一个外层分组为 `Category`、内层分组为 `Item` 的数据透视表。反转顺序则会反转层次结构。

## **数据透视字段小计**
`PivotField.set_subtotals(PivotFieldSubtotalType subtotal_type, bool shown)` 方法控制数据透视字段显示哪些小计行。每次调用独立切换一种小计类型。传入 `shown = True` 显示小计，而 `shown = False` 则隐藏小计。由于每次调用仅影响一种类型，因此使用不同的 `subtotal_type` 值多次调用该方法即可构建自定义的小计子集。
`PivotFieldSubtotalType` 枚举定义了可用的小计种类。
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
仅当行区域（或列区域）中存在两个或更多数据透视字段时，小计才会渲染。单个字段之间没有有意义的可小计内容，因此在这种情况下调用 `set_subtotals` 不会有任何可见效果。因此，本文在每个示例中都放置了两个行字段（外层为 `Category`，内层为 `Item`），以便显示每个 `Category` 组之间的小计边界。
{{% /alert %}}

## **场景 1 — 自动（默认）小计**
如果根本不调用 `set_subtotals`，Aspose.Cells 会将 `AUTOMATIC` 选择应用于数值字段。以下示例通过对外部 `Category` 行字段调用 `set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)` 来明确确认此行为。

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
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(PivotFieldType.ROW, "Category")
pivot_table.add_field_to_area(PivotFieldType.ROW, "Item")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
category_field = pivot_table.row_fields[0]
category_field.set_subtotals(PivotFieldSubtotalType.AUTOMATIC, True)
pivot_table.calculate_data()
workbook.save("output_automatic.xlsx")
```

## **场景 2 — 抑制所有小计（None）**
调用 `set_subtotals(PivotFieldSubtotalType.NONE, True)` 会从数据透视表中移除所有小计行，仅保留字段行和底部的总计行。当您希望仅查看原始的分组数据而不包含任何汇总行时，此功能非常有用。

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
pivot_index = worksheet.pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]
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

## **场景 3 — 自定义小计子集（Sum + Average）**
您并不局限于单一的小计类型。每次 `set_subtotals` 调用独立地作用于一种类型，因此调用该方法两次（一次使用 `SUM`，一次使用 `AVERAGE`）会为每个 `Category` 组生成一个包含两行小计的自定义子集。

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
pivot_index = pivot_tables.add("A1:D9", "F3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]
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

## **总结**

三种场景仅在 `set_subtotals` 调用上存在差异；其余部分——数据集、字段及其所分配的区域——均完全相同，这使得各布局之间可直接进行比较。
- **字段放置。** `PivotTable.add_field_to_area(PivotFieldType.ROW, fieldName)` 将源列移入某一区域；在同一个区域内，调用顺序即为显示顺序，因此首次调用对应的字段会成为最外层分组。 subtotal 计算需要同一区域中存在两个或更多字段：仅有一个字段时，组间不存在可进行小计的间隔。
- **场景 1——自动小计。** 若不调用 `set_subtotals`，则由 Excel 自行决定默认的小计方式，即对数值字段应用其内置默认小计函数；而显式调用 `set_subtotals` 并传入 `PivotFieldSubtotalType.AUTOMATIC` 可明确记录该选择，而非保留其隐含默认行为。
- **场景 2——不启用小计。** 传入 `PivotFieldSubtotalType.NONE` 调用 `set_subtotals` 可禁用默认小计，这样数据透视表将保留字段行与总计行，但剔除 Excel 在它们之间默认插入的小计行。
- **场景 3——选择性小计类型。** 每次调用仅切换一种小计类型，且各次调用所设设置累加而非相互覆盖；例如先以 `PivotFieldSubtotalType.SUM` 调用一次、再以 `PivotFieldSubtotalType.AVERAGE` 调用一次，则两者均保持启用状态，此时数据透视表将同时呈现求和小计、平均值小计及总计。

{{% alert color="primary" %}}
关于小计的设置并非仅限于行区域；对 `PivotTable.ColumnFields` 中取出的字段执行相同的 `set_subtotals` 调用，同样可在列轴上生成上述三种布局，因为该设置属于数据透视字段本身，而非其所在的轴。
{{% /alert %}}
## **相关文章**
- [数据透视表中的页字段](/cells/zh/python-net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via .NET 中刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)
- [为数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="python-net" >}}