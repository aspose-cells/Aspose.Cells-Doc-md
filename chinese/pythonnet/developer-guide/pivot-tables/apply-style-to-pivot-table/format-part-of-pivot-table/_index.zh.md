---
title: 格式化数据透视表的部分
description: 在 Aspose.Cells for Python via .NET 中通过 PivotTable.format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以格式化数据透视表的部分，格式存储在 PivotTable.pivot_formats 中，并在数据透视表刷新时保持不变。
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells for Python via .NET, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.format, pivot_formats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, select_field, format_all, Python via .NET
type: docs
weight: 20
url: /zh/python-net/format-part-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.format_all` 会对整个数据透视表应用单一样式，已在父页面中说明。它不会区分标签、数值、合计或报告的特定区域。  
在实际使用中，通常只需要突出显示数据透视表的某一部分。常见的目标包括属于某个行字段的标签、由某个字段生成的数值单元格、总计行，或诸如前两行项目的任意矩形区域。  
将样式直接应用于数据透视表所在工作表的单元格并不等同。Excel 将数据透视表的格式存储为语义的 `PivotArea` 区域，而不是普通的单元格样式记录。`PivotArea` 格式会附着在字段的标签或数据值等区域，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式只属于该单元格位置，不会被数据透视模型跟踪。  
Aspose.Cells 提供完整的 `PivotTable.format` 重载族，支持这两种格式化方式：
- `format(PivotArea, Style)` 将样式锚定到通过 `PivotArea.select` 或 `PivotArea.select_field` 构建的语义区域。
- `format(CellArea, Style)` 将样式锚定到数据透视表内工作表的矩形区域。
- `format(int row, int column, Style)` 目标单个单元格。
- `format_all(Style)` 格式化整个数据透视表。

## **格式化 Pivot 区域**
当需要让突出显示随字段或报告区域移动时，推荐使用语义区域工作流。  
1. 使用 `PivotArea(pivot_table)` 创建 `PivotArea`。该对象描述属于特定数据透视表的语义区域。  
1. 使用 `PivotArea.select(PivotFieldType axis_type, int field_position, PivotTableSelectionType selection_type)` 按轴上的零基位置选择字段。  
   - `PivotTableSelectionType.DATA_AND_LABEL` 选择字段的标签和数据。  
   - `PivotTableSelectionType.LABEL_ONLY` 仅选择字段的标签。  
   - `PivotTableSelectionType.DATA_ONLY` 仅选择字段的数据单元格。  
1. 使用 `PivotArea.select_field(PivotFieldType axis_type, string field_name)` 按名称选择字段。按名称选择行字段时，区域解析为该字段项目生成的数值单元格。  
1. 使用 `Workbook.create_style()` 创建 `Style`，配置字体、前景色和实线背景图案，并将该样式传递给 `PivotTable.format(area, style)`。  
1. 每次调用 `PivotArea` 重载都会向 `PivotTable.pivot_formats` 添加一个 `PivotTableFormat` 条目。  
1. 字段锚定的格式在计算数据时绘制。因此，在应用格式后调用 `PivotTable.calculate_data()` 使样式可见。  
下面的示例创建一个小型水果销售数据透视表，使用 `PivotArea.select` 与 `PivotTableSelectionType.LABEL_ONLY` 为 `Fruit` 行标签设置样式，使用 `PivotArea.select_field` 为同一行字段生成的数值单元格设置样式，然后重新计算数据透视表以绘制两种样式。

```python
from aspose.cells.pivot import PivotArea, PivotFieldType, PivotTableSelectionType
from aspose.pydrawing import Color
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cells = sheet.cells
# Fruit sales data
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
# Bold yellow fill on the row field's label cells
label_style = workbook.create_style()
label_style.font.is_bold = True
label_style.foreground_color = Color.yellow
label_style.pattern = ac.BackgroundType.SOLID
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.create_style()
value_style.foreground_color = Color.light_green
value_style.pattern = ac.BackgroundType.SOLID
value_area = PivotArea(pivot_table)
value_area.select_field(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculate_data()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
```

## **格式化数据透视表的单元格区域**
当感兴趣的区域是普通的工作表矩形而非语义的透视区域时，使用 `PivotTable.format(CellArea, Style)`。  
`CellArea` 由 `start_row`、`start_column`、`end_row`、`end_column` 属性描述。所有坐标均为零基工作表坐标，结束坐标标识矩形中包含的最后一行和最后一列，因此区域覆盖从起始位置到结束位置（含）的所有单元格。  
与字段锚定的格式不同，`CellArea` 格式会立即应用于单元格，无需再次调用 `calculate_data()`。  
`CellArea` 矩形可以同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 和 Excel 如何在内部表示该矩形。  
下面的示例使用斜体、淡蓝色样式格式化数据透视表的矩形 `E4:F5`，并在不再进行重新计算的情况下保存工作簿。

```python
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
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
pivot_table.calculate_data()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
```

## **Pivot 区域与 Cell 区域的映射关系**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 采用相同的模型，因此格式请求在记录时会被转换为透视区域。  
用户提供的 `CellArea` 与内部存储的透视区域之间是多对多的关系：  
- 一个 `CellArea` 可能产生多个透视区域。如果矩形同时跨越标签单元格和数值单元格，会被分解为独立的标签规则和数据规则，因为透视模型会独立处理标签格式和数据格式。  
- 一个透视区域可能解析为多个不相连的 `CellArea` 实例。诸如总计行或项不连续的字段等语义区域可以覆盖多个矩形，这就是 `PivotArea.get_cell_areas()` 返回集合而非单个矩形的原因。  
通过 `PivotTable.format` 执行的每一次格式化操作都会记录在 `PivotTable.pivot_formats` 中。每个 `PivotTableFormat` 条目公开其关联的 `PivotArea` 与所应用的 `Style`。`PivotArea` 重载每次调用只添加一个条目，而包含不同语义区域的 `CellArea` 则可能添加多个条目。  
为区分存储的区域，每个 `PivotArea` 公开 `only_label` 和 `only_data` 标记。下面的示例格式化一个同时覆盖标签和数值的单矩形，检查 `PivotTable.pivot_formats`，并打印每个存储的透视区域解析得到的 `CellArea` 坐标。

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
highlight_style = workbook.create_style()
highlight_style.font.is_italic = True
highlight_style.foreground_color = Color.from_argb(0xFF, 0x99, 0xCC, 0xFF)
highlight_style.pattern = ac.BackgroundType.SOLID
# ONE rectangle in...
rectangle = ac.CellArea()
rectangle.start_row = 3
rectangle.start_column = 4
rectangle.end_row = 4
rectangle.end_column = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print(f"Stored formats: {len(pivot_table.pivot_formats)}")
for i in range(len(pivot_table.pivot_formats)):
    stored_area = pivot_table.pivot_formats[i].pivot_area
    print(f"Format {i}: OnlyLabel={stored_area.only_label}, OnlyData={stored_area.only_data}")
    for resolved in stored_area.get_cell_areas():
        print(
            f"    rows {resolved.start_row + 1}-{resolved.end_row + 1}, "
            f"columns {resolved.start_column + 1}-{resolved.end_column + 1}"
        )
workbook.save("FormatPivotAreasMap.xlsx")
```

{{% alert color="primary" %}}
因为格式存储为透视区域而非普通单元格样式，它们在重新计算和刷新后仍然存在。当使用 `PivotTable.refresh_data` 刷新数据透视表，或使用 `calculate_data` 重新计算，或保存后重新加载时，每个存储的透视区域都会重新解析到其当前所在位置，并重新应用其样式。
{{% /alert %}}

在需要让突出显示随字段或语义区域在刷新后保持的场景下，使用通过 `select` 或 `select_field` 构建的 `PivotArea`；在仅需对当前布局中的固定矩形进行格式化的情况下，使用 `CellArea`。单元格重载 `format(int row, int column, Style)` 目标单个单元格。若需一次性重新样式整个数据透视表，请使用父页面中介绍的 `format_all`。

## **相关文档**
- [将样式应用于数据透视表](/cells/zh/python-net/apply-style-to-pivot-table/)
- [添加数据透视表的行字段和列字段](/cells/zh/python-net/pivot-table-add-row-and-column-fields/)
- [管理数据透视表中的值字段](/cells/zh/python-net/manage-value-fields/)
- [刷新数据透视表](/cells/zh/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}