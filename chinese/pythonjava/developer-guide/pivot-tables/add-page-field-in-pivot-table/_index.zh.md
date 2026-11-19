---
title: 在 Aspose.Cells for Python via Java 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 了解如何使用 Aspose.Cells for Python via Java 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选和多选筛选。
keywords: Aspose.Cells, Python, Java, 数据透视表, 筛选字段, PivotFieldType.PAGE, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
type: docs
weight: 250
url: /zh/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或底层 `page_fields` 集合添加筛选字段，可以以单选模式驱动筛选、清除筛选以显示所有筛选项，或者将字段切换为多选模式，以便用户通过 Excel 中的复选框界面一次选择多个筛选项。
{{% /alert %}}

## **简介**
筛选字段是一种数据透视字段，用于控制数据透视表主体显示源数据的*哪些子集*。最终用户在 Excel 中渲染的数据透视表顶部将其视为一个下拉列表，选择某个可用的筛选项会重新构建数据透视表主体，使其仅汇总属于该筛选项的记录。当数据透视字段注册为 `PivotFieldType.PAGE` 而非 `PivotFieldType.ROW`、`PivotFieldType.COLUMN` 或 `PivotFieldType.DATA` 时，它就成为筛选字段。

## **添加筛选字段**

### 使用 add_field_to_area 添加筛选字段
以下示例构建一个小的 Fruit / Year / Amount 数据集，在 E3 单元格放置一个数据透视表，将 `Fruit` 放在行区域，将 `Amount` 放在数据区域，将 `Year` 放在筛选区域，然后刷新数据透视表并保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
# Create a new workbook
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
# Set up the header row
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# Populate 9 rows of sample data: Fruit, Year, Amount
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])
# Add a pivot table anchored at cell E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# Refresh and calculate the pivot table data
pivotTable.calculateData()
# Save the workbook
workbook.save("pageFieldSample.xlsx")
jpype.shutdownJVM()
```

### 使用 page_fields.add 添加筛选字段
当您已经使用 `PivotField` 实例时，可以将其直接传递给 `PivotTable.page_fields.add`。数据透视表和筛选字段的构建方式与上一场景完全相同；只是最终的筛选区域注册替换为底层 API 调用。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data). Below we obtain the Year PivotField from the
#   BaseFields collection and pass it to PageFields.Add — the
#   low-level alternative to AddFieldToArea. The result is
#   functionally identical to Scenario 1a.
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Headers
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
# Sample data (9 rows)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)
# Add pivot table at E3 covering A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Low-level approach: grab the existing Year PivotField from BaseFields
# and register it in the Page area via PageFields.Add(PivotField).
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)
# Refresh so the new page field is reflected in the saved workbook
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **单选筛选（显示一个筛选项）**
在默认的单选行为下，筛选字段呈现为单个下拉列表，`PivotField.current_page_item` 整数用于选择驱动数据透视表主体的筛选项。分配特定索引会选择该项；分配特殊标记值 `0x7FFD`（十进制 32765）会清除筛选，以便同时汇总所有筛选项。单选是默认模式，无需显式启用。

### 显示所有项
将 `current_page_item` 设置为魔法值 `0x7FFD` 等同于清除筛选：数据透视表主体将汇总每个筛选项，就好像没有应用筛选一样。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create a new workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# Populate Fruit/Year/Amount data
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
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
        sheet.getCells().get(r + 1, c).putValue(data[r][c])
# Create pivot table at E3
pivotTables = sheet.getPivotTables()
pivotTable = pivotTables.add("=A1:C7", 2, 4)
# Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
pivotTable.calculateData()
# Clear the page filter so every item in the page field is visible.
# 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
# equivalent to selecting "(All)" in Excel's page-field dropdown.
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

### 显示一个特定项
将 `current_page_item` 设置为实际索引仅选择该筛选项。该索引是筛选字段已排序项列表中该项的位置，因此例如 `1` 选择排序后的第二项。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# Create workbook
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Add sample data (Fruit/Year/Amount)
cells.get("A1").putValue("Fruit")
cells.get("B1").putValue("Year")
cells.get("C1").putValue("Amount")
cells.get("A2").putValue("Apple")
cells.get("B2").putValue("2020")
cells.get("C2").putValue("100")
cells.get("A3").putValue("Apple")
cells.get("B3").putValue("2021")
cells.get("C3").putValue("150")
cells.get("A4").putValue("Banana")
cells.get("B4").putValue("2020")
cells.get("C4").putValue("200")
cells.get("A5").putValue("Banana")
cells.get("B5").putValue("2021")
cells.get("C5").putValue("250")
# Add pivot table at E3
pivotTables = sheet.getPivotTables()
pivotTable = pivotTables.add("A1:C5", 2, 4)
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# Page-field-specific operations
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = second item in sorted order (e.g. "2021")
# Refresh and calculate pivot table
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **多选筛选**
多选筛选将筛选下拉列表转换为复选框列表，允许最终用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。必须先将 `PivotField.is_multiple_item_selection_allowed` 设置为 `True`，多选界面才会生效。启用后，`PivotItem.is_hidden` 控制哪些项出现在复选框列表中，因此您可以显示所有项或仅将特定项加入白名单。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re
# — The pivot table and page field are constructed exactly as in
#   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
#   Amount→Data, Year→Page via AddFieldToArea).
#   Below we apply multi-select filtering on the page field.
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# Sample data: Fruit | Year | Amount
cells.get(0, 0).putValue("Fruit")
cells.get(0, 1).putValue("Year")
cells.get(0, 2).putValue("Amount")
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
    cells.get(i + 1, 0).putValue(data[i][0])
    cells.get(i + 1, 1).putValue(int(data[i][1]))
    cells.get(i + 1, 2).putValue(int(data[i][2]))
pivotSheet = workbook.getWorksheets().add("Pivot")
pivots = pivotSheet.getPivotTables()
pivotTable = pivots.add("A1:C10", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
# — Enable multi-select on the page field
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)
# Part A — select ALL items (make every item visible)
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)
# Part B — select only specific items by source value
for i in range(pivotItems.getCount()):
    value = pivotItems.get(i).getStringValue()
    if value == "2020" or value == "grape" or value == "blueberry":
        pivotItems.get(i).setHidden(False)
    else:
        pivotItems.get(i).setHidden(True)
pivotTable.calculateData()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

> **注意：**当通过 `PivotItem.is_hidden` 使用多选筛选时，**至少必须保留一个 `PivotItem` 可见**（`is_hidden == False`）。如果每个项都隐藏，则 Excel 在打开文件时崩溃或呈现空白数据透视表。始终验证您的多选白名单包含源数据中的至少一个项。

## **应该使用哪个 API 和哪种模式？**
下表汇总了何时使用每个 API 和模式，以便您可以挑选合适的组合而无需详细阅读每个场景。
| 场景/用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名称添加筛选字段（最常见） | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | 不适用 | 高级 API，一行代码。除非需要 `PivotField` 引用，否则请使用此方法。 |
| 当您已经有 `PivotField` 对象时添加筛选字段 | `PivotTable.page_fields.add(PivotField)` | 不适用 | 当字段对象是在其他地方获取或需要重用时使用。 |
| 筛选到单个筛选项（默认模式） | `PivotField.current_page_item` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除筛选 | `PivotField.current_page_item` | 设置为 `0x7FFD` | 魔法值 `0x7FFD`（十进制 32765）是"所有项"的标记值。 |
| 在 Excel 中启用多选界面 | `PivotField.is_multiple_item_selection_allowed` | 设置为 `True` | 在任何 `is_hidden` 调用生效之前需要先设置。 |
| 在多选列表中隐藏/显示单个项 | `PivotItem.is_hidden` | 按项设置 | 至少必须保留一项可见（`is_hidden == False`）。 |

{{% alert color="primary" %}}
配置多选筛选时，请始终牢记可见性约束。如果多选筛选字段中的每个 `PivotItem` 都隐藏，则 Excel 在打开时崩溃或呈现空白数据透视表。根据源数据构建白名单，确保至少有一项保持可见，这样保存的工作簿将在每台计算机上可靠打开。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}