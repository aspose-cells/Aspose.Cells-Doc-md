---
title: 在 Aspose.Cells for Python via Java 中向数据透视表添加筛选字段
linktitle: 在 Aspose.Cells for Python via Java 中向数据透视表添加筛选字段
description: 了解如何使用 Aspose.Cells for Python via Java 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选和多选筛选。
keywords: Aspose.Cells, Python, Java, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
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
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType
# 创建新工作簿
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Data")
# 设置表头行
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
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
    worksheet.getCells().get(i + 1, 0).putValue(data[i][0])
    worksheet.getCells().get(i + 1, 1).putValue(data[i][1])
    worksheet.getCells().get(i + 1, 2).putValue(data[i][2])
# 在 E3 单元格添加数据透视表
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "PivotTable1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# 将字段添加到对应区域：水果作为行字段，数量作为数据字段，年份作为页字段
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")
# 刷新并计算数据透视表数据
pivotTable.calculateData()
# 保存工作簿
workbook.save("pageFieldSample.xlsx")
jpype.shutdownJVM()
```

### 使用 page_fields.add 添加筛选字段
当您已经使用 `PivotField` 实例时，可以将其直接传递给 `PivotTable.page_fields.add`。数据透视表和筛选字段的构建方式与上一场景完全相同；只是最终的筛选区域注册替换为底层 API 调用。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType
# — 透视表和页面字段的构建方式与场景 1a 完全相同
#   (水果/年份/金额数据,透视表位于 E3,水果→行,
#   金额→数据)。下面我们从 BaseFields 集合中
#   获取 Year PivotField 并将其传递给 PageFields.Add —
#   这是 AddFieldToArea 的底层替代方案。其结果
#   与场景 1a 在功能上完全相同。
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# 表头
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")
# 示例数据(9 行)
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)
# 在 E3 添加覆盖 A1:C10 的透视表
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)
# 水果 -> 行,金额 -> 数据(年份将在下面添加到页面)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# 底层方法:从 BaseFields 中获取已存在的 Year PivotField,
# 并通过 PageFields.Add(PivotField) 将其注册到页面区域。
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)
# 刷新数据以使新的页面字段反映在保存的工作簿中
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
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# 创建新工作簿
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
# 填充水果/年份/数量数据
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
# 在 E3 创建数据透视表
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)
# 配置数据透视字段：水果→行，数量→数据，年份→页
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")
pivotTable.calculateData()
# 清除页面筛选，以便显示页面字段中的所有项目。
# 0x7FFD（十进制 32765）是表示"所有项目"的特殊哨兵值 —
# 等同于在 Excel 的页字段下拉菜单中选择"(全部)"。
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
from asposecells.api import Workbook
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
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)
# Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")
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
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re
# — 数据透视表和页字段的构造方式与
#   场景 1a 完全相同（Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
#   Amount→数据，Year→页通过 AddFieldToArea）。
#   下面我们对页字段应用多选筛选。
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()
# 示例数据：Fruit | Year | Amount
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
pivotIndex = pivots.add("E3", "A1:C10", "PivotTable1")
pivotTable = pivots.get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")
# — 在页字段上启用多选
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)
# Part A — 选择所有项（使每个项都可见）
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)
# Part B — 按源值仅选择特定项
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