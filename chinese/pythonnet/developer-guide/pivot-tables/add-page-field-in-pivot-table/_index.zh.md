---
title: 在 Aspose.Cells for .NET 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 学习如何使用 Aspose.Cells for Python via .NET 在数据透视表中添加和配置页字段，包括添加页字段、单选过滤和多选过滤。
keywords: Aspose.Cells, Python via .NET, 数据透视表, 页字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 过滤
type: docs
weight: 250
url: /zh/python-net/add-filter-field-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中页字段的完整生命周期。您可以通过高级便捷 API 或低级 `page_fields` 集合来添加页字段，并且可以以单选模式驱动页过滤器、清除它以显示每个页项，或者将字段切换为多选，以便用户通过 Excel 中的复选框 UI 一次选择多个页项。
{{% /alert %}}

## **简介**

页字段是一种透视字段，用于控制透视体显示源数据的*哪个子集*。最终用户在 Excel 中将其视为已渲染透视表顶部的下拉列表；选择可用的页项之一后，透视体会重新构建，以便仅汇总属于该页项的记录。当透视字段被注册为 `PivotFieldType.PAGE`（而非 `PivotFieldType.ROW`、`PivotFieldType.COLUMN` 或 `PivotFieldType.DATA`）时，它就成为页字段。

页字段有两种运行行为。在默认的**单选**行为下，一次只能看到一个页项，因此透视体恰好汇总一个子集。在**多选**行为下，字段会显示一个复选框列表，透视体会汇总所有已勾选页项的并集。同一源字段可以通过切换一个属性在这些行为之间来回切换。

Aspose.Cells for Python via .NET 公开了两种等效的方式来注册页字段。高级 API 是 `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")`，它接收源列名并在一次调用中完成字段添加。低级 API 是 `PivotTable.page_fields.add(PivotField)`，当您已经持有 `PivotField` 引用，并希望将同一字段实例添加到页区域时使用。两种 API 最终都会填充同一个 `page_fields` 集合，本文的其余部分将演示如何在它们之间进行选择，以及如何驱动每种过滤模式。

## **添加页字段**

在页区域中注册透视字段有两种方式。高级调用以字符串形式接收源列名，是最常用的途径。低级调用接受现有的 `PivotField` 实例，当同一字段对象需要在多个透视区域之间重用时尤为方便。两种调用都会将字段放入 `PivotTable.page_fields` 中，之后它将作为页下拉列表显示在已渲染透视表的顶部。

### 使用 add_field_to_area 添加页字段

以下示例构建一个小型 Fruit / Year / Amount 数据集，将数据透视表放在单元格 E3 处，其中 `Fruit` 放在行区域，`Amount` 放在数据区域，`Year` 放在页区域，然后刷新透视表并保存工作簿。

```python
import aspose.cells as ac

# 创建一个新的工作簿
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Data"

# 设置表头行
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 填充 9 行示例数据：水果、年份、数量
data = [
    ["apple", 2020, 100],
    ["banana", 2021, 200],
    ["apple", 2021, 150],
    ["grape", 2020, 120],
    ["orange", 2022, 180],
    ["banana", 2020, 90],
    ["grape", 2021, 130],
    ["apple", 2022, 170],
    ["orange", 2021, 110]
]

for i in range(len(data)):
    worksheet.cells[i + 1, 0].put_value(data[i][0])
    worksheet.cells[i + 1, 1].put_value(data[i][1])
    worksheet.cells[i + 1, 2].put_value(data[i][2])

# 在 E3 单元格添加一个数据透视表
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "PivotTable1")
pivot_table = worksheet.pivot_tables[pivot_index]

# 将字段添加到相应区域：水果作为行字段，数量作为数据字段，年份作为页字段
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

# 刷新并计算数据透视表的数据
pivot_table.calculate_data()

# 保存工作簿
workbook.save("pageFieldSample.xlsx")
```

### 使用 page_fields.add 添加页字段

当您已经使用 `PivotField` 实例时，可以直接将其传递给 `PivotTable.page_fields.add`。数据透视表和页字段的构建方式与前面的场景完全相同；只是最终的页区域注册被替换为低级 API 调用。

```python
import aspose.cells as ac

# — 数据透视表和页字段的构建与
#   场景 1a 完全相同（Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
#   Amount→数据）。下面我们从
#   BaseFields 集合中获取 Year PivotField 并将其传递给 PageFields.Add — 这是
#   AddFieldToArea 的底层替代方案。其结果与
#   场景 1a 在功能上完全相同。

workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# 表头
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

# 示例数据（9 行）
sheet.cells["A2"].put_value("apple");    sheet.cells["B2"].put_value("2020"); sheet.cells["C2"].put_value(100)
sheet.cells["A3"].put_value("apple");    sheet.cells["B3"].put_value("2021"); sheet.cells["C3"].put_value(150)
sheet.cells["A4"].put_value("apple");    sheet.cells["B4"].put_value("2022"); sheet.cells["C4"].put_value(200)
sheet.cells["A5"].put_value("grape");    sheet.cells["B5"].put_value("2020"); sheet.cells["C5"].put_value(300)
sheet.cells["A6"].put_value("grape");    sheet.cells["B6"].put_value("2021"); sheet.cells["C6"].put_value(400)
sheet.cells["A7"].put_value("grape");    sheet.cells["B7"].put_value("2022"); sheet.cells["C7"].put_value(500)
sheet.cells["A8"].put_value("blueberry"); sheet.cells["B8"].put_value("2020"); sheet.cells["C8"].put_value(250)
sheet.cells["A9"].put_value("blueberry"); sheet.cells["B9"].put_value("2021"); sheet.cells["C9"].put_value(350)
sheet.cells["A10"].put_value("blueberry");sheet.cells["B10"].put_value("2022"); sheet.cells["C10"].put_value(450)

# 在 E3 处添加数据透视表，覆盖 A1:C10
pivot_index = sheet.pivot_tables.add("E3", "A1:C10", "PivotTable1")
pivot_table = sheet.pivot_tables[pivot_index]

# Fruit -> 行，Amount -> 数据（Year 将在下方添加到页字段）
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# 底层方法：从 BaseFields 中获取现有的 Year PivotField
#   并通过 PageFields.Add(PivotField) 将其注册到页字段区域。
year_field = pivot_table.base_fields["Year"]
pivot_table.page_fields.add(year_field)

# 刷新数据以便新页字段反映在保存的工作簿中
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **单选过滤（显示一个页项）**

在默认的单选行为下，页字段呈现为单个下拉列表，`PivotField.current_page_item` 整数选择哪个页项驱动透视体。分配特定索引会选取该项；分配特殊哨兵值 `0x7FFD`（十进制 32765）则会清除过滤器，从而一次性汇总每个页项。单选是默认模式，您无需显式启用它。

### 显示所有项

将 `current_page_item` 设置为魔术值 `0x7FFD` 等同于清除页过滤器：透视体会汇总每个页项，就像未应用过滤器一样。

```python
import aspose.cells as ac

# 创建新的工作簿
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# 填充 Fruit/Year/Amount 数据
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

data = [
    ["Apple", 2022, 100],
    ["Apple", 2023, 150],
    ["Banana", 2022, 80],
    ["Banana", 2023, 120],
    ["Cherry", 2022, 200],
    ["Cherry", 2023, 250]
]

for r in range(len(data)):
    for c in range(len(data[r])):
        sheet.cells[r + 1, c].put_value(data[r][c])

# 在 E3 创建数据透视表
pivot_tables = sheet.pivot_tables
index = pivot_tables.add("=A1:C7", "E3", "PivotTable1")
pivot_table = pivot_tables[index]

# 配置透视字段：Fruit→行，Amount→数据，Year→页面
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.Page, "Year")

pivot_table.calculate_data()

# 清除页面筛选器，以便显示页面字段中的所有项。
# 0x7FFD（十进制 32765）是表示"所有项"的特殊哨兵值 ——
# 相当于在 Excel 的页面字段下拉列表中选择"(全部)"。
pivot_table.page_fields[0].current_page_item = 0x7FFD

workbook.save("output.xlsx")
```

### 显示一个特定项

将 `current_page_item` 设置为实际索引将仅选取该一个页项。索引是页字段已排序项列表中项的位置，因此例如 `1` 在排序后选择第二项。

```python
import aspose.cells as ac

# 创建工作簿
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# 添加示例数据（水果/年份/数量）
cells["A1"].put_value("Fruit")
cells["B1"].put_value("Year")
cells["C1"].put_value("Amount")

cells["A2"].put_value("Apple")
cells["B2"].put_value("2020")
cells["C2"].put_value("100")

cells["A3"].put_value("Apple")
cells["B3"].put_value("2021")
cells["C3"].put_value("150")

cells["A4"].put_value("Banana")
cells["B4"].put_value("2020")
cells["C4"].put_value("200")

cells["A5"].put_value("Banana")
cells["B5"].put_value("2021")
cells["C5"].put_value("250")

# 在 E3 处添加数据透视表
pivot_tables = sheet.pivot_tables
pivot_index = pivot_tables.add("A1:C5", "E3", "PivotTable1")
pivot_table = pivot_tables[pivot_index]

# 添加字段：水果→行，数量→数据，年份→页
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# 页字段特定操作
pivot_table.page_fields[0].current_page_item = 1  # 1 = 排序顺序中的第二项（例如 "2021"）

# 刷新并计算数据透视表
pivot_table.calculate_data()

workbook.save("output.xlsx")
```

## **多选过滤**

多选过滤将页下拉列表转换为复选框列表，并允许最终用户同时选择多个页项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.is_multiple_item_selection_allowed` 设置为 `True`，多选 UI 才会真正生效。启用之后，`PivotItem.is_hidden` 控制哪些项出现在复选框列表中，因此您既可以显示每一项，也可以仅将特定项列入白名单。

下面的代码在场景 1a 中构建的同一 Year 页字段上启用多选，然后展示两种模式：Part A 通过将每个条目的 `is_hidden` 保持为 `False` 来显示每一个页项；而 Part B 通过测试 `pivot_items[i].get_string_value()` 的 `if` / `elif` 块，仅将您选择的源值列入白名单，并隐藏其他所有项。

```python
import aspose.cells as ac

# — 透视表和页面字段的构造方式与场景 1a 完全相同
#   （Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
#   Amount→数据，Year→页面通过 AddFieldToArea 添加）。
#   下面我们对页面字段应用多选筛选。

workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells

# 示例数据：Fruit | Year | Amount
cells[0, 0].put_value("Fruit")
cells[0, 1].put_value("Year")
cells[0, 2].put_value("Amount")

data = [
    ["apple",  "2019", "100"],
    ["apple",  "2020", "150"],
    ["apple",  "2021", "200"],
    ["banana", "2019", "110"],
    ["banana", "2020", "160"],
    ["banana", "2021", "210"],
    ["grape",  "2019", "120"],
    ["grape",  "2020", "170"],
    ["grape",  "2021", "220"]
]

for i in range(len(data)):
    cells[i + 1, 0].put_value(data[i][0])
    cells[i + 1, 1].put_value(int(data[i][1]))
    cells[i + 1, 2].put_value(int(data[i][2]))

pivot_sheet = workbook.worksheets.add("Pivot")
pivots = pivot_sheet.pivot_tables
pivot_index = pivots.add("E3", "A1:C10", "PivotTable1")
pivot_table = pivots[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.add_field_to_area(ac.PivotFieldType.PAGE, "Year")

# — 在页面字段上启用多选
pivot_table.page_fields[0].is_multiple_item_selection_allowed = True

# Part A — 选择所有项目（使每个项目都可见）
pivot_items = pivot_table.page_fields[0].pivot_items
for i in range(pivot_items.count):
    pivot_items[i].is_hidden = False

# Part B — 按源值仅选择特定项目
for i in range(pivot_items.count):
    value = pivot_items[i].get_string_value()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivot_items[i].is_hidden = False
    else:
        pivot_items[i].is_hidden = True

pivot_table.calculate_data()

workbook.save("output.xlsx")
```

> **注意：** 通过 `PivotItem.is_hidden` 使用多选过滤时，**至少必须保留一个 `PivotItem` 可见**（`is_hidden == False`）。如果所有项都被隐藏，Excel 在打开文件时可能会崩溃，或渲染出空白透视表。请始终确认您的多选白名单中至少包含一项源数据。

## **应该使用哪个 API 和哪种模式？**

下表汇总了在各种场景下应使用的 API 和模式，以便您在不必阅读每个场景细节的情况下选择合适的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名添加页字段（最常用） | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "field_name")` | n/a | 高级 API，一行代码。除非需要 `PivotField` 引用，否则请使用此方式。 |
| 在已拥有 `PivotField` 对象时添加页字段 | `PivotTable.page_fields.add(PivotField)` | n/a | 当字段对象来自其他地方或需要重用时使用。 |
| 过滤为单个页项（默认模式） | `PivotField.current_page_item` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除页过滤器 | `PivotField.current_page_item` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是"所有项"的哨兵值。 |
| 在 Excel 中启用多选 UI | `PivotField.is_multiple_item_selection_allowed` | 设置为 `True` | 在任何 `is_hidden` 调用生效之前必须设置。 |
| 在多选列表中隐藏 / 显示各个项 | `PivotItem.is_hidden` | 按项设置 | 至少必须保留一项可见（`is_hidden == False`）。 |

{{% alert color="primary" %}}
配置多选过滤时，请务必牢记可见性约束。如果多选页字段中的每个 `PivotItem` 都被隐藏，Excel 在打开时会崩溃，或渲染出空白透视表。请根据源数据构建白名单，确保至少有一项保持可见，这样保存的工作簿才能在每台机器上可靠打开。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}
