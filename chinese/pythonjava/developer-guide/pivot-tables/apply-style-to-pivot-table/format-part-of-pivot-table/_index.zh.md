---
title: 格式化数据透视表的部分
linktitle: 格式化数据透视表的部分
description: 通过 PivotTable.format 将样式应用于语义 PivotArea 区域或 CellArea 矩形，以在 Aspose.Cells for Python via Java 中格式化数据透视表的部分，格式存储在 PivotTable.getPivotFormats() 中，并在数据透视表刷新时保留。
keywords: Aspose.Cells, Aspose.Cells for Python via Java, 数据透视表, 格式化, PivotArea, CellArea, PivotTable.format, getPivotFormats, PivotTableSelectionType, LABEL_ONLY, DATA_ONLY, selectField, formatAll, Python
type: docs
weight: 20
url: /zh/python-java/format-part-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
`PivotTable.formatAll` 为整个数据透视表应用单一样式，已在父页面中说明。它不会区分标签、数值、合计或报告的特定区域。  
在实际使用中，通常只需要突出数据透视表的某一部分。常见的目标包括属于某行字段的标签、某字段生成的数值单元格、总计行，或诸如前两行项目的任意矩形区域。  
将样式直接应用于数据透视表工作表单元格并不等同。Excel 将数据透视表的格式存储为语义 `PivotArea` 区域，而非普通单元格样式记录。PivotArea 格式会附着在诸如字段标签或数据值的区域上，并在数据透视表重新计算、刷新或展开时重新解析。相反，直接写入单元格的样式仅属于该单元格位置，未被数据透视表模型跟踪。  
Aspose.Cells 暴露完整的 `PivotTable.format` 重载系列，以提供两种格式化方式：
- `format(PivotArea, Style)` 将样式锚定到使用 `PivotArea.select` 或 `PivotArea.selectField` 构建的语义区域。
- `format(CellArea, Style)` 将样式锚定到数据透视表内的工作表矩形。
- `format(int row, int column, Style)` 目标单元格。
- `formatAll(Style)` 格式化整个数据透视表。

## **格式化 Pivot Area**
当突出显示必须随字段或报告区域移动时，推荐使用语义区域工作流。  
1. 使用 `PivotArea(pivot_table)` 创建 `PivotArea`。该对象描述属于该特定数据透视表的语义区域。  
2. 通过 `PivotArea.select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)` 根据给定轴上零基位置选择字段。  
   - `PivotTableSelectionType.DATA_AND_LABEL` 选择该字段的标签和数据。  
   - `PivotTableSelectionType.LABEL_ONLY` 仅选择字段的标签。  
   - `PivotTableSelectionType.DATA_ONLY` 仅选择字段的数据单元格。  
3. 使用 `PivotArea.selectField(PivotFieldType axisType, String fieldName)` 按名称选择字段。若按名称选择行字段，则该区域解析为该字段项生成的数值单元格。  
4. 使用 `workbook.createStyle()` 创建 `Style`，配置其字体、前景色和实线背景图案，然后将该样式传递给 `PivotTable.format(area, style)`。  
5. 每次调用 `PivotArea` 重载时，都会向 `PivotTable.getPivotFormats()` 添加一个 `PivotTableFormat` 条目。  
6. 字段锚定的格式会在计算数据透视表数据时绘制。因此，在应用格式后调用 `PivotTable.calculateData()` 以使样式可见。  
下面的示例构建了一个小型水果销售数据透视表，使用 `PivotArea.select` 和 `PivotTableSelectionType.LABEL_ONLY` 为 `Fruit` 行标签设置样式，使用 `PivotArea.selectField` 为同一行字段生成的数值单元格设置样式，然后重新计算数据透视表，使两种样式均被绘制。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Style,
    Color,
    BackgroundType,
    PivotArea,
    PivotFieldType,
    PivotTableSelectionType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Fruit sales data
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Bold yellow fill on the row field's label cells
label_style = workbook.createStyle()
label_style.getFont().setBold(True)
label_style.setForegroundColor(Color.getYellow())
label_style.setPattern(BackgroundType.SOLID)
label_area = PivotArea(pivot_table)
label_area.select(PivotFieldType.ROW, 0, PivotTableSelectionType.LABEL_ONLY)
pivot_table.format(label_area, label_style)
# Light green fill on the value cells the row field produces
value_style = workbook.createStyle()
value_style.setForegroundColor(Color.getLightGreen())
value_style.setPattern(BackgroundType.SOLID)
value_area = PivotArea(pivot_table)
value_area.selectField(PivotFieldType.ROW, "Fruit")
pivot_table.format(value_area, value_style)
# Field-anchored formats are painted when the data is calculated
pivot_table.calculateData()
# Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.save("FormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **格式化数据透视表的 Cell Area**
当感兴趣的区域是普通工作表矩形而非语义数据透视区域时，请使用 `PivotTable.format(CellArea, Style)`。  
`CellArea` 由 `getStartRow()`、`getStartColumn()`、`getEndRow()` 和 `getEndColumn()` 属性描述。属性值为零基工作表坐标，结束坐标标识矩形中包含的最后一行和列，因此该区域覆盖从起始位置到结束位置（包括结束位置）的单元格。  
不同于字段锚定的格式，`CellArea` 格式会立即应用于单元格。无需再次调用 `PivotTable.calculateData()` 即可使样式显示。  
`CellArea` 矩形可能同时包含标签单元格和数值单元格。下一节将说明 Aspose.Cells 和 Excel 在内部如何表示该矩形。  
下面的示例使用斜体、浅蓝色样式格式化数据透视表的矩形 `E4:F5`，并在无需进一步重新计算的情况下保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    Color,
    BackgroundType,
    CellArea,
    PivotFieldType,
)
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Highlight the first two fruit rows (the rectangle E4:F5)
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# E4:F5 is italic on light blue immediately, no recalculation needed
workbook.save("FormatPivotCellArea.xlsx")
jpype.shutdownJVM()
```

## **Pivot Area 与 Cell Area 的映射关系**
Excel 将数据透视表的格式存储为 `pivotArea` 记录，而非普通工作表单元格样式记录。Aspose.Cells 使用相同的模型，因此格式化请求在记录时会转换为 pivot area。  
用户提供的 `CellArea` 与内部存储的 pivot area 之间的关系是双向多对多的。  
- 一个 `CellArea` 可能生成多个 pivot area。如果矩形同时包含标签单元格和数值单元格，它会被分解为独立的标签规则和数据规则，因为数据透视模型会独立处理标签格式和数据格式。  
- 一个 pivot area 可能对应多个不相连的 `CellArea` 实例。诸如总计行之类的语义区域，或项目不连续的字段，可能覆盖多个矩形。这就是 `PivotArea.getCellAreas()` 返回集合而非单个矩形的原因。  
通过 `PivotTable.format` 执行的每一次格式化操作都会记录在 `PivotTable.getPivotFormats()` 中。每个 `PivotTableFormat` 条目公开其关联的 `PivotArea` 以及应用于该区域的 `Style`。`PivotArea` 重载每次调用仅添加一个条目，而包含不同语义区域的 `CellArea` 则可能添加多个条目。  
为区分存储的区域，每个 `PivotArea` 提供 `getOnlyLabel()` 和 `getOnlyData()` 标志。下面的示例对覆盖标签和数值的单个矩形进行格式化，检查 `PivotTable.getPivotFormats()`，并打印每个存储的 pivot area 所解析的 `CellArea` 坐标。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import Color, CellArea, Style, BackgroundType
from asposecells.api import PivotTable, PivotArea, PivotFieldType
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
fruits = ["Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry"]
years = [2024, 2024, 2025, 2025, 2024, 2025]
amounts = [100, 150, 120, 180, 90, 110]
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
for i in range(len(fruits)):
    cells.get(i + 1, 0).putValue(fruits[i])
    cells.get(i + 1, 1).putValue(years[i])
    cells.get(i + 1, 2).putValue(amounts[i])
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
highlight_style = workbook.createStyle()
highlight_style.getFont().setItalic(True)
highlight_style.setForegroundColor(Color.fromArgb(0xFF, 0x99, 0xCC, 0xFF))
highlight_style.setPattern(BackgroundType.SOLID)
# ONE rectangle in...
rectangle = CellArea()
rectangle.StartRow = 3
rectangle.StartColumn = 4
rectangle.EndRow = 4
rectangle.EndColumn = 5
pivot_table.format(rectangle, highlight_style)
# ...TWO semantic pivot areas out: the label part and the data part are stored separately
print("Stored formats: " + str(pivot_table.getPivotFormats().getCount()))
for i in range(pivot_table.getPivotFormats().getCount()):
    stored_area = pivot_table.getPivotFormats().get(i).getPivotArea()
    print(
        f"Format {i}: OnlyLabel={stored_area.getOnlyLabel()}, "
        f"OnlyData={stored_area.getOnlyData()}"
    )
    for resolved in stored_area.getCellAreas():
        print(
            f"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, "
            f"columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}"
        )
# This prints:
# Stored formats: 2
# Format 0: OnlyLabel=True, OnlyData=False
#     rows 4-5, columns 5-5        (E4:E5, the label part)
# Format 1: OnlyLabel=False, OnlyData=True
#     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.save("FormatPivotAreasMap.xlsx")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
由于格式存储为 pivot area 而非普通单元格样式，它们在重新计算和刷新后仍然有效。当使用 `PivotTable.refreshData()` 刷新数据透视表，或使用 `PivotTable.calculateData()` 重新计算，亦或保存后重新加载时，所有存储的 pivot area 都会重新解析到其区域的当前位置并重新应用样式。
{{% /alert %}}

当突出显示必须在刷新后仍附着在字段或语义区域上时，请使用通过 `select` 或 `selectField` 构建的 `PivotArea`；而在当前数据透视表布局中只需对固定矩形进行格式化时，则使用 `CellArea`。`format(int row, int column, Style)` 重载用于定位单个单元格。若需一次性重新样式化整个数据透视表，请使用在父页面中介绍的 `formatAll`。

## **相关文章**
- [将样式应用于数据透视表](/cells/zh/python-java/apply-style-to-pivot-table/)
- [添加数据透视表行列字段](/cells/zh/python-java/pivot-table-add-row-and-column-fields/)
- [管理数据透视表值字段](/cells/zh/python-java/manage-value-fields/)
- [刷新数据透视表](/cells/zh/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}