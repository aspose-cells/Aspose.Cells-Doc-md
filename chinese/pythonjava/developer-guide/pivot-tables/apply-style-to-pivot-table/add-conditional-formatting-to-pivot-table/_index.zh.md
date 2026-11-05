---
title: 添加条件格式到数据透视表
linktitle: 添加条件格式到数据透视表
description: 在 Aspose.Cells for Python via Java 中向数据透视表添加条件格式，通过 applyTo 和 PivotConditionFormatScopeType 范围将规则锚定到数据区域，或使用 addCellArea 和 getPivotAreas 定义目标，然后通过 getFormatConditions().addCondition 附加规则和样式
keywords: Aspose.Cells for Python via Java, 数据透视表, 条件格式, PivotConditionalFormat, getConditionalFormats, applyTo, PivotConditionFormatScopeType, DATA, FIELD, SELECTION, addCellArea, getPivotAreas, addPivotArea, getFormatConditions, addCondition, FormatConditionType, Python via Java
type: docs
weight: 30
url: /zh/python-java/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
父页面和兄弟页面中描述的样式是静态的——`PivotArea` 或 `CellArea` 区域只会被绘制一次，无论数值如何都会保持其样式。条件格式是规则驱动的对应方式——突出显示所有大于 200 的金额、为中间五十百分比着色，或标记排名靠后的项目——并且在数据透视表重新计算或刷新时，高亮会随数值变化。
在 Aspose.Cells 中，数据透视表的条件格式位于 `PivotTable.getConditionalFormats()` 集合中。每个条目都是一个 `PivotConditionalFormat`，它独立回答两个问题：
- **规则应用于哪里？** 目标区域可以通过 `PivotConditionalFormat.applyTo(int row, int column, PivotConditionFormatScopeType scope)` 定义，这与 Excel 用户界面中的范围选择器相对应，或者通过 `PivotConditionalFormat.addCellArea(CellArea)` 以及 `PivotConditionalFormat.getPivotAreas()` 集合显式命名区域。
- **规则测试什么？** 可以使用 `FormatConditionCollection.addCondition(FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 向 `PivotConditionalFormat.getFormatConditions()` 添加一个或多个条件，每个条件携带其自身的 `Style`。

{{% alert color="primary" %}}
不要在数据透视表条件格式的 `PivotConditionalFormat.getFormatConditions()` 对象上调用 `FormatConditionCollection.add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, String formula1, String formula2)` 或 `FormatConditionCollection.addArea(CellArea)`。这两个重载继承自普通工作表的条件格式 API，无法用于数据透视表——单元格区域永远不会转换为数据透视表区域，所以请求会被静默忽略。始终在 `PivotConditionalFormat` 本身上定义区域（`applyTo`、`addCellArea` 或 `getPivotAreas()`），并使用其中一种 `addCondition` 重载来添加规则。
{{% /alert %}}

## **使用范围（Excel UI 方式）应用规则**
第一种方式按照 Excel 用户界面的方式定位规则。数据透视表的单元格通过其零基工作表坐标命名，`PivotConditionFormatScopeType` 范围告诉 Aspose.Cells 规则应从该单元格向外延伸的范围：
- `PivotConditionFormatScopeType.DATA` - 所有数值单元格，包括总计。
- `PivotConditionFormatScopeType.FIELD` - 属于该单元格所标识字段的数值单元格，不包括总计。单元格必须是字段单元格，例如行字段标签；如果传入数值单元格会抛出异常。
- `PivotConditionFormatScopeType.SELECTION` - 仅该单元格所选交叉点的数值单元格，通常为单个数值单元格。
下面的示例创建了一个左上角位于 E3 的水果销售数据透视表，在单元格 F4（第 3 行，第 5 列）使用 `DATA` 范围锚定条件格式，并将所有大于 200 的金额以红底白字加粗高亮。对于 Apple 220、Banana 330、Cherry 200 以及总计 750，该规则会为 F4、F5、F7 着色——解析后的区域为整个数据列 F4:F7，只有满足条件的单元格会被点亮。

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
    PivotFieldType,
    PivotConditionFormatScopeType,
    FormatConditionType,
    OperatorType,
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
# Pivot table with its top-left corner at E3
pivot_table = sheet.getPivotTables().add("=A1:C7", 2, 4)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Amount")
pivot_table.calculateData()
# Anchor the conditional format at F4 (row 3, column 5) with the Data scope
index = pivot_table.getConditionalFormats().add()
format = pivot_table.getConditionalFormats().get(index)
format.applyTo(3, 5, PivotConditionFormatScopeType.DATA)
# Rule - highlight amounts greater than 200
condition_index = format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.GREATER_THAN,
    "200",
    None,
)
style = workbook.createStyle()
style.getFont().setBold(True)
style.getFont().setColor(Color.getWhite())
style.setForegroundColor(Color.getRed())
style.setPattern(BackgroundType.SOLID)
format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatData.xlsx")
jpype.shutdownJVM()
```

如果在行字段标签 E4（第 3 行，第 4 列）使用 `FIELD` 范围锚定相同的规则，则解析为 F4:F6——同一数据列但不包括总计行——因为该范围描述的是 `Fruit` 字段而不是整个数值区域。使用 `SELECTION` 范围锚定在 F4 时，仅解析为 F4 本身。

## **手动定义区域**
第二种方式跳过范围选择器，直接在 `PivotConditionalFormat` 上显式指定区域。

### **使用 addCellArea() 定义工作表矩形**
`addCellArea(CellArea)` 将给定的矩形记录为规则的目标。坐标采用零基工作表坐标，区域正好是提供的矩形——不会扩展到数据列，也不包含总计逻辑。当感兴趣的单元格是当前数据透视布局中已知的固定矩形时使用它。

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
    CellArea,
    Color,
    BackgroundType,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Target the rectangle F4:F6 (the value cells without the grand total)
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = CellArea()
area.StartRow = 3
area.StartColumn = 5
area.EndRow = 5
area.EndColumn = 5
conditional_format.addCellArea(area)
# Rule - italic on light yellow for amounts between 150 and 300
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.BETWEEN,
    "150",
    "300",
)
style = workbook.createStyle()
style.getFont().setItalic(True)
style.setForegroundColor(Color.getLightYellow())
style.setPattern(BackgroundType.SOLID)
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatCellArea.xlsx")
jpype.shutdownJVM()
```

### **使用 getPivotAreas() 定义语义数据透视区域**
`getPivotAreas()` 集合使用与兄弟页面用于静态样式相同的语义区域模型。创建一个 `PivotArea`，使用 `PivotArea.select(...)` 或 `PivotArea.selectField(...)` 选择字段或区域，然后通过 `getPivotAreas().addPivotArea(PivotArea)` 将其添加。语义区域会绑定到其字段上，因此在数据透视表刷新且布局变化时，条件格式会随字段移动。`getPivotAreas().add(PivotArea)` 重载仍可编译，但已标记为过时——推荐使用 `addPivotArea`。

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
    PivotArea,
    PivotFieldType,
    FormatConditionType,
    OperatorType,
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
# Attach the rule to the Amount data field as a semantic region
index = pivot_table.getConditionalFormats().add()
conditional_format = pivot_table.getConditionalFormats().get(index)
area = PivotArea(pivot_table)
area.selectField(PivotFieldType.DATA, "Amount")
conditional_format.getPivotAreas().addPivotArea(area)
# Rule - grey text for amounts below 150
condition_index = conditional_format.getFormatConditions().addCondition(
    FormatConditionType.CELL_VALUE,
    OperatorType.LESS_THAN,
    "150",
    None,
)
style = workbook.createStyle()
style.getFont().setColor(Color.getGray())
conditional_format.getFormatConditions().get(condition_index).setStyle(style)
workbook.save("PivotConditionalFormatPivotArea.xlsx")
jpype.shutdownJVM()
```

## **规则的存储位置及其在重新加载后如何保持**
每次调用 `PivotTable.getConditionalFormats().add()` 都会向数据透视表追加一个 `PivotConditionalFormat`。条件、其公式以及样式会随工作簿一起保存——在下面示例中重新打开文件时，会看到相同的规则以及其类型、运算符和公式保持完整，并且 `PivotConditionalFormat.getCellAreas()` 报告相同的区域。未收到任何条件的条目在保存工作簿时会被丢弃，这与 Excel 丢弃没有规则的条件格式的方式相同。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("PivotConditionalFormatData.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
print("Conditional formats: " + str(pivot_table.getConditionalFormats().getCount()))
for i in range(pivot_table.getConditionalFormats().getCount()):
    pivot_format = pivot_table.getConditionalFormats().get(i)
    format_conditions = pivot_format.getFormatConditions()
    for j in range(format_conditions.getCount()):
        condition = format_conditions.get(j)
        print(
            f"Format {i}: {condition.getType()} "
            f"{condition.getOperator()} formula1={condition.getFormula1()}"
        )
    for area in pivot_format.getCellAreas():
        print(
            f"    rows {area.StartRow + 1}-{area.EndRow + 1}, "
            f"columns {area.StartColumn + 1}-{area.EndColumn + 1}"
        )
# This prints:
# Conditional formats: 1
# Format 0: CellValue GreaterThan formula1==200
#     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
jpype.shutdownJVM()
```

## **相关文档**
- [应用样式到数据透视表](/cells/zh/python-java/apply-style-to-pivot-table/)
- [格式化数据透视表的一部分](/cells/zh/python-java/format-part-of-pivot-table/)
- [前 10 名显示或筛选在数据透视表中](/cells/zh/python-java/top-10-show-or-filter-in-pivot-table/)
- [按标签或数值过滤数据透视表](/cells/zh/python-java/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="python" >}}