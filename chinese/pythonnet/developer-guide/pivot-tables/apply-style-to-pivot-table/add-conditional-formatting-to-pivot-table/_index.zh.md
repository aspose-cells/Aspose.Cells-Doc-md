---
title: 向数据透视表添加条件格式
linktitle: 向数据透视表添加条件格式
description: 在 Aspose.Cells for Python via .NET 中向数据透视表添加条件格式——使用 apply_to 并指定 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 add_cell_area 与 pivot_areas 定义目标区域，然后通过 format_conditions.add_condition 附加规则和样式。
keywords: Aspose.Cells, Aspose.Cells for Python via .NET, 数据透视表, 条件格式, PivotConditionalFormat, conditional_formats, apply_to, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, add_cell_area, pivot_areas, add_pivot_area, format_conditions, add_condition, FormatConditionType, Python
type: docs
weight: 30
url: /zh/python-net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域仅绘制一次，无论数值如何都保持其样式。条件格式是基于规则的对应方式——突出显示所有大于 200 的金额、为中间五十百分比着色，或标记排名靠后的项目——并且在数据透视表重新计算或刷新时，突出显示会随数值变化而更新。
在 Aspose.Cells 中，数据透视表的条件格式位于 `pivot_table.conditional_formats` 集合中。每个条目都是一个 `PivotConditionalFormat`，独立地回答两个问题：
- **规则适用于哪里？** 目标区域可以通过 `apply_to(row: int, column: int, scope: PivotConditionFormatScopeType)` 定义，这与 Excel 用户界面的范围选择器对应；也可以通过 `add_cell_area(cell_area: CellArea)` 和 `pivot_areas` 集合显式命名区域。
- **规则测试什么？** 使用 `format_conditions.add_condition(type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` 向 `format_conditions` 添加一个或多个条件，每个条件都有自己的 `style`。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `format_conditions` 对象上调用 `format_conditions.add(cell_area: CellArea, type: FormatConditionType, operator_type: OperatorType, formula1: str, formula2: str)` 或 `format_conditions.add_area(cell_area: CellArea)`。这两个重载来自普通工作表条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视表区域，因此请求会被静默忽略。始终在 `pivot_conditional_format` 本身上定义区域（`apply_to`、`add_cell_area` 或 `pivot_areas`），并使用 `add_condition` 的任意重载来添加规则。
{{% /alert %}}

## **使用范围应用规则（Excel UI 方式）**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格使用零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格向哪儿延伸：
- `PivotConditionFormatScopeType.DATA` - 所有数据透视表生成的值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格所指字段的值单元格，不包括总计。单元格必须是字段单元格，例如行字段标签；如果传入值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅该单元格选择的交叉处的值单元格，通常是单个值单元格。
下面的示例创建了一个水果销售数据透视表，左上角位于 E3，采用 `PivotConditionFormatScopeType.DATA` 范围在单元格 F4（第 3 行，第 5 列）锚定条件格式，并将所有大于 200 的金额以红底白字加粗显示。数据为 Apple 220、Banana 330、Cherry 200，合计 750 时，规则会对 F4、F5 和 F7 染色——解析后的区域是整列数据 F4:F7，只有满足规则的单元格会被点亮。

```python
from aspose.cells.pivot import PivotFieldType, PivotConditionFormatScopeType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
format.apply_to(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.GREATER_THAN,
    "200",
    None
)
style = workbook.create_style()
style.font.is_bold = True
style.font.color = Color.white
style.foreground_color = Color.red
style.pattern = ac.BackgroundType.SOLID
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatData.xlsx")
```

在行字段标签 E4（第 3 行，第 4 列）使用 `PivotConditionFormatScopeType.FIELD` 范围锚定相同规则时，解析得到的区域为 F4:F6——同一数据列但不包括总计行——因为范围现在描述的是 `Fruit` 字段而不是整个值区域。`PivotConditionFormatScopeType.SELECTION` 范围锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式指定区域。

### **使用 add_cell_area 定义工作表矩形区域**
`add_cell_area(cell_area: CellArea)` 将给定的矩形记录为规则的目标区域。坐标采用零基工作表坐标，区域正好是提供的矩形——不会扩展到数据列，也没有总计逻辑。当感兴趣的单元格是当前数据透视表布局中已知的固定矩形时使用此方法。

```python
from aspose.cells import BackgroundType, FormatConditionType, OperatorType
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.conditional_formats.add()
conditional_format = pivot_table.conditional_formats[index]
area = ac.CellArea()
area.start_row = 3
area.start_column = 5
area.end_row = 5
area.end_column = 5
conditional_format.add_cell_area(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.format_conditions.add_condition(
    FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "150", "300"
)
style = workbook.create_style()
style.font.is_italic = True
style.foreground_color = Color.light_yellow
style.pattern = BackgroundType.SOLID
conditional_format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatCellArea.xlsx")
```

### **使用 pivot_areas 定义语义数据透视区域**
`pivot_areas` 与兄弟页面用于静态样式的语义区域模型相同。创建一个 `PivotArea`，使用 `select` 或 `select_field` 选择字段或区域，然后通过 `pivot_areas.add_pivot_area(pivot_area)` 添加。语义区域会绑定到其字段上，因此在数据透视表刷新且布局变化时，条件格式会随字段移动。`pivot_areas.add(pivot_area)` 重载仍可编译，但已标记为过时——推荐使用 `add_pivot_area`。

```python
from aspose.cells.pivot import PivotFieldType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").put_value("Fruit")
cells.get("B1").put_value("Year")
cells.get("C1").put_value("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).put_value(fruits[i])
    cells.get(i + 1, 1).put_value(years[i])
    cells.get(i + 1, 2).put_value(amounts[i])
pivot_table = sheet.pivot_tables.add("=A1:C7", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.conditional_formats.add()
format = pivot_table.conditional_formats[index]
area = ac.PivotArea(pivot_table)
area.select_field(PivotFieldType.DATA, "Amount")
format.pivot_areas.add_pivot_area(area)
# Rule - grey text for amounts below 150
condition_index = format.format_conditions.add_condition(
    ac.FormatConditionType.CELL_VALUE,
    ac.OperatorType.LESS_THAN,
    "150",
    None
)
style = workbook.create_style()
style.font.color = Color.gray
format.format_conditions[condition_index].style = style
workbook.save("PivotConditionalFormatPivotArea.xlsx")
```

## **规则的存储位置及重新加载后的持久性**
每次调用 `pivot_table.conditional_formats.add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。这些条件、公式以及样式会随工作簿一起保存——下面示例重新打开文件时，仍然保留这条规则的类型、运算符和公式，且 `get_cell_areas()` 返回相同的区域。未设置任何条件的条目在保存工作簿时会被移除，这与 Excel 丢弃没有规则的条件格式的方式相同。

```python
import aspose.cells as ac
workbook = ac.Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
print("Conditional formats: " + str(pivot_table.conditional_formats.count))
for i in range(pivot_table.conditional_formats.count):
    format = pivot_table.conditional_formats[i]
    for j in range(format.format_conditions.count):
        condition = format.format_conditions[j]
        print(f"Format {i}: {condition.type} {condition.operator} formula1={condition.formula1}")
    for area in format.get_cell_areas():
        print(
            f"    rows {area.start_row + 1}-{area.end_row + 1}, "
            f"columns {area.start_column + 1}-{area.end_column + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Related Articles**
- [对数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)
- [格式化数据透视表的部分](/cells/zh/python-net/format-part-of-pivot-table/)
- [在数据透视表中显示或筛选前 10 项](/cells/zh/python-net/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值过滤数据透视表](/cells/zh/python-net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python-net" >}}