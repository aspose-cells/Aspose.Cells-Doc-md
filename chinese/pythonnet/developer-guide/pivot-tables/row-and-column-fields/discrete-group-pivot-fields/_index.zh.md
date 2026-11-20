---
title: 数据透视字段项的离散分组
description: 了解如何使用 DiscreteGroupItem 和 pivot_field_group_options.discrete_group_items 在 Aspose.Cells for Python via .NET 中将数据透视字段项归入自定义命名组，例如水果和蔬菜。
linktitle: 离散分组
keywords: Aspose.Cells for Python via .NET, 数据透视表, 离散分组, DiscreteGroupItem, PivotFieldGroupOptions, 对数据透视项进行分组, 自定义组, PivotField.group, Python, Excel 数据透视表
type: docs
weight: 90
url: /zh/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 自动分组根据数据类型归集项目，例如将日期归入月份和季度，或将数字归入不同的数值范围。离散分组解决的是相反的问题，即将特定的互不相关的项目归入自定义命名组，例如将产品分为水果和蔬菜、将商店归入区域，或将账户归入分区。Aspose.Cells 通过 `DiscreteGroupItem` 类和 `pivot_field_group_options.discrete_group_items` 属性提供离散分组功能。
- `DiscreteGroupItem` 由组名及属于该组的项目组成。可以通过两种方式标识这些项目：按名称（`DiscreteGroupItem("fruit", ["grape", "cherry"])`）或按其在源数据中从零开始的位置（`DiscreteGroupItem("fruit", [0, 3])`）。两种形式会产生相同的结果。
- 离散分组通过将选项传递给 `pivot_field.group(PivotFieldGroupOptions)`，应用于数据透视表行区域或列区域中的字段。

## **按项目名称对数据透视字段项进行分组**
以下示例构建一个小型销售列表（产品、日期和金额），并据此创建数据透视表：将 `product` 放在行区域，将 `date` 放在列区域，将 `amount` 放在数据区域；随后按项目名称定义两个自定义组，即水果（葡萄、樱桃）和蔬菜（胡萝卜、马铃薯）。结果呈现两级行布局：组名位于外层，原始项目嵌套在其下，便于分别按自定义组和单个项目查看趋势。

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

调用 `calculate_data()` 后，数据透视表的行区域会显示 `fruit`（`grape` 50、`cherry` 80）和 `vegetable`（`carrot` 60、`potato` 70），总计为 260；列标签仍保留四个日期（`2/5/2021`、`3/8/2022`、`4/10/2023`、`5/16/2024`）。

## **按项目索引对数据透视字段项进行分组**
当项目名称较长或已本地化时，可以使用 `DiscreteGroupItem` 的第二个构造函数按索引标识项目。这些索引是项目在源数据中出现顺序里的从零开始的位置，而不是按字母顺序排列。在上述示例数据中，`grape` 是项目 0，`carrot` 是项目 1，`potato` 是项目 2，`cherry` 是项目 3，因此 `fruit` 是 `{ 0, 3 }`，`vegetable` 是 `{ 1, 2 }`。结果与按名称分组的示例完全相同。

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **注意**

{{% alert color="primary" %}}
- 未分配到任何自定义组的项目不会丢失。它们仍保留在数据透视表中，与自定义组处于同一层级，每项均作为独立的单项条目显示。在上述示例中，仅定义 `fruit` 组时，`carrot` 和 `potato` 仍会作为独立条目保留在行区域中，与 `fruit` 组并列。
- `pivot_field_group_options.new_pivot_field` 属性控制离散分组的布局。其默认值为 `True`，会在原始字段旁新增一个外层分组字段，从而生成上述两级布局（`row_fields` 增至 2）。将其设置为 `False` 可改为替换原始字段；此时行区域只显示一个层级，其中仅包含组名及其汇总值，即 `fruit` 130（50 + 80）和 `vegetable` 130（60 + 70）。
- 在同一个 `discrete_group_items` 列表中，可以混合使用 `DiscreteGroupItem` 基于名称和基于索引的构造函数。
{{% /alert %}}

## **相关文章**
- [在数据透视表中对数据透视字段进行分组](/cells/zh/python-net/group-pivot-fields-in-the-pivot-table/)
- [在数据透视表中添加行字段和列字段](/cells/zh/python-net/pivot-table-add-row-and-column-fields/)
- [按标签或值筛选数据透视表](/cells/zh/python-net/filter-by-label-or-value-of-pivot-table/)
- [将样式应用到数据透视表](/cells/zh/python-net/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}