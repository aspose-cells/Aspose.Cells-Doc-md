---
title: 在 Aspose.Cells for Python via Java 中向数据透视表添加筛选字段
linktitle: 添加筛选字段
description: 学习如何使用 Aspose.Cells for Python via Java 在数据透视表中添加和配置筛选字段，包括添加筛选字段、单选筛选以及多选筛选。
keywords: Aspose.Cells, Python, Java, 数据透视表, 筛选字段, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, 筛选
type: docs
weight: 250
url: /zh/python-java/add-page-field-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持数据透视表中筛选字段的完整生命周期。您可以通过高级便捷 API 或通过底层 `page_fields` 集合添加筛选字段，并且可以以单选模式驱动筛选器、清除筛选器以显示每个筛选项，或者将该字段切换到多选模式，以便用户能够通过 Excel 中的复选框 UI 一次选择多个筛选项。
{{% /alert %}}

## **简介**

筛选字段是一种数据透视字段，用于控制*哪个子集*的源数据由数据透视表主体显示。最终用户在 Excel 中将其视为渲染的数据透视表顶部的下拉列表，从可用的筛选项中选择一个后，会重新构建数据透视表主体，使其仅汇总属于该筛选项的记录。当某个数据透视字段被注册为 `PivotFieldType.PAGE`（而不是 `PivotFieldType.ROW`、`PivotFieldType.COLUMN` 或 `PivotFieldType.DATA`）时，它就成为筛选字段。

筛选字段可以以两种行为模式运行。在默认的**单选**行为模式下，一次只能显示一个筛选项，因此数据透视表主体仅汇总一个子集。在**多选**行为模式下，该字段会显示一个复选框列表，数据透视表主体汇总所有已勾选筛选项的并集。同一个源字段可以通过切换单个属性在这些行为模式之间来回切换。

Aspose.Cells for Python via Java 提供了两种等效的方式来注册筛选字段。高级 API 是 `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")`，它接收源列名并在一次调用中添加字段。底层 API 是 `PivotTable.page_fields.add(PivotField)`，当您已经持有 `PivotField` 引用并希望将同一字段实例添加到筛选区域时，会使用该 API。这两个 API 最终都会填充同一个 `page_fields` 集合，本文接下来将演示如何在它们之间进行选择以及如何驱动每种筛选模式。

## **添加筛选字段**

在筛选区域中注册数据透视字段有两种方法。高级调用以字符串形式接收源列名，是最常用的方式。底层调用接受现有的 `PivotField` 实例，当同一字段对象必须在多个数据透视区域中重复使用时，这种方式非常方便。这两种调用都会将字段放入 `PivotTable.page_fields` 中，此后它会作为页面下拉列表显示在渲染后的数据透视表顶部。

### 使用 add_field_to_area 添加筛选字段

以下示例构建一个小型 Fruit / Year / Amount 数据集，在 E3 单元格放置一个数据透视表，其中 `Fruit` 位于行区域，`Amount` 位于数据区域，`Year` 位于筛选区域，刷新数据透视表，并保存工作簿。

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

# 将字段添加到相应区域：水果作为行字段，数量作为数据字段，年份作为页字段
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

当您已经在使用 `PivotField` 实例时，可以将其直接传递给 `PivotTable.page_fields.add`。数据透视表和筛选字段的构造方式与前一个场景完全相同；只是最终的筛选区域注册被替换为底层 API 调用。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotFieldType

# — 数据透视表和页面字段的构建方式与方案 1a 完全相同
#   （Fruit/Year/Amount 数据，数据透视表位于 E3，Fruit→行，
#   Amount→数据）。下面我们从 BaseFields 集合中获取 Year PivotField，
#   并将其传递给 PageFields.Add——这是 AddFieldToArea 的底层替代方法。
#   其结果在功能上与方案 1a 完全相同。

workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# 表头
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

# 示例数据（9 行）
sheet.getCells().get("A2").putValue("apple");    sheet.getCells().get("B2").putValue("2020"); sheet.getCells().get("C2").putValue(100)
sheet.getCells().get("A3").putValue("apple");    sheet.getCells().get("B3").putValue("2021"); sheet.getCells().get("C3").putValue(150)
sheet.getCells().get("A4").putValue("apple");    sheet.getCells().get("B4").putValue("2022"); sheet.getCells().get("C4").putValue(200)
sheet.getCells().get("A5").putValue("grape");    sheet.getCells().get("B5").putValue("2020"); sheet.getCells().get("C5").putValue(300)
sheet.getCells().get("A6").putValue("grape");    sheet.getCells().get("B6").putValue("2021"); sheet.getCells().get("C6").putValue(400)
sheet.getCells().get("A7").putValue("grape");    sheet.getCells().get("B7").putValue("2022"); sheet.getCells().get("C7").putValue(500)
sheet.getCells().get("A8").putValue("blueberry"); sheet.getCells().get("B8").putValue("2020"); sheet.getCells().get("C8").putValue(250)
sheet.getCells().get("A9").putValue("blueberry"); sheet.getCells().get("B9").putValue("2021"); sheet.getCells().get("C9").putValue(350)
sheet.getCells().get("A10").putValue("blueberry");sheet.getCells().get("B10").putValue("2022"); sheet.getCells().get("C10").putValue(450)

# 在 E3 位置添加覆盖 A1:C10 区域的数据透视表
pivotIndex = sheet.getPivotTables().add("E3", "A1:C10", "PivotTable1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Fruit -> 行，Amount -> 数据（Year 将在下方添加到页面区域）
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# 底层方法：从 BaseFields 中获取现有的 Year PivotField，
# 并通过 PageFields.Add(PivotField) 将其注册到页面区域。
yearField = pivotTable.getBaseFields().get("Year")
pivotTable.getPageFields().add(yearField)

# 刷新数据，使新添加的页面字段在保存的工作簿中生效
pivotTable.calculateData()

workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **单选筛选（显示一个筛选项）**

在默认的单选行为模式下，筛选字段呈现为单个下拉列表，`PivotField.current_page_item` 整数选择哪个筛选项驱动数据透视表主体。分配特定索引将选取该项；分配特殊标记值 `0x7FFD`（十进制 32765）将清除筛选器，以便一次性汇总所有筛选项。单选是默认模式，您无需显式启用它。

### 显示所有项

将 `current_page_item` 设置为魔术值 `0x7FFD` 等同于清除筛选器：数据透视表主体会汇总所有筛选项，就好像没有应用筛选器一样。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建一个新工作簿
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# 填充 Fruit/Year/Amount 数据
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

# 在 E3 位置创建数据透视表
pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C7", "E3", "PivotTable1")
pivotTable = pivotTables.get(index)

# 配置数据透视表字段：Fruit→行，Amount→数据，Year→页面
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
pivotTable.addFieldToArea(PivotFieldType.PAGE, "Year")

pivotTable.calculateData()

# 清除页面筛选，以便页面字段中的每一项都可见。
# 0x7FFD（十进制 32765）是表示"所有项"的特殊哨兵值 —
# 等同于在 Excel 页面字段下拉列表中选择"（全部）"。
pivotTable.getPageFields().get(0).setCurrentPageItem(0x7FFD)

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### 显示一个特定项

将 `current_page_item` 设置为实际索引将仅选取该一个筛选项。该索引是项在筛选字段已排序项列表中的位置，例如 `1` 选择排序后的第二项。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# 创建工作簿
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# 添加示例数据（水果/年份/金额）
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

# 在 E3 处添加数据透视表
pivotTables = sheet.getPivotTables()
pivotIndex = pivotTables.add("A1:C5", "E3", "PivotTable1")
pivotTable = pivotTables.get(pivotIndex)

# 添加字段：水果→行，金额→数据，年份→页
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
pivotTable.addFieldToArea(PivotFieldType.Page, "Year")

# 页字段特定操作
pivotTable.getPageFields().get(0).setCurrentPageItem(1) # 1 = 排序顺序中的第二项（例如 "2021"）

# 刷新并计算数据透视表
pivotTable.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **多选筛选**

多选筛选将页面下拉列表转变为复选框列表，允许最终用户同时选择多个筛选项。Aspose.Cells 公开了两个协同工作的属性。`PivotField.is_multiple_item_selection_allowed` 必须设置为 `True`，多选 UI 才能生效。启用该属性后，`PivotItem.is_hidden` 控制哪些项出现在复选框列表中，因此您可以选择显示所有项，也可以仅白名单列出特定项。

下面的代码在场景 1a 中构建的同一 Year 筛选字段上启用多选，然后展示两种模式：Part A 通过对每个条目将 `is_hidden` 设置为 `False` 来显示每个筛选项，而 Part B 通过 `switch (pivot_items[i].get_string_value())` 块仅白名单列出您选择的源值并隐藏其他所有项。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
import os
import re

# — 数据透视表和页面字段的构建与以下场景完全相同
#   场景 1a（Fruit/Year/Amount 数据，透视表位于 E3，Fruit→行，
#   Amount→数据，Year→页面 通过 AddFieldToArea）。
#   下面我们对页面字段应用多选筛选。

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

# — 启用页面字段的多选功能
pivotTable.getPageFields().get(0).setMultipleItemSelectionAllowed(True)

# 部分 A — 选择所有项（使每个项都可见）
pivotItems = pivotTable.getPageFields().get(0).getPivotItems()
for i in range(pivotItems.getCount()):
    pivotItems.get(i).setHidden(False)

# 部分 B — 仅按源值选择特定项
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

> **注意：** 通过 `PivotItem.is_hidden` 使用多选筛选时，**至少必须保留一个 `PivotItem` 可见**（`is_hidden == False`）。如果每个项都被隐藏，Excel 在打开文件时会崩溃或渲染一个空白的数据透视表。请始终确认您的多选白名单中至少包含源数据中的一项。

## **应使用哪种 API 和哪种模式？**

下表汇总了何时使用每个 API 和模式，以便您无需详细阅读每个场景即可选择正确的组合。

| 场景 / 用例 | 推荐 API | 使用的属性 | 备注 |
|---|---|---|---|
| 按源列名添加筛选字段（最常见） | `PivotTable.add_field_to_area(PivotFieldType.PAGE, "fieldName")` | n/a | 高级、单行 API。除非需要 `PivotField` 引用，否则请使用此方式。 |
| 在已拥有 `PivotField` 对象时添加筛选字段 | `PivotTable.page_fields.add(PivotField)` | n/a | 当字段对象来自其他位置或需要重复使用时，请使用此方式。 |
| 筛选为单个筛选项（默认模式） | `PivotField.current_page_item` | 设置为特定索引 | 例如，`1` 显示已排序列表中的第二项。 |
| 显示所有项 / 清除筛选器 | `PivotField.current_page_item` | 设置为 `0x7FFD` | 魔术值 `0x7FFD`（十进制 32765）是"所有项"的标记值。 |
| 在 Excel 中启用多选 UI | `PivotField.is_multiple_item_selection_allowed` | 设置为 `True` | 在任何 `is_hidden` 调用生效之前必需。 |
| 在多选列表中隐藏 / 显示各个项 | `PivotItem.is_hidden` | 逐项设置 | 至少必须保留一项可见（`is_hidden == False`）。 |

{{% alert color="primary" %}}
在配置多选筛选时，请始终牢记可见性约束。如果多选筛选字段中每个 `PivotItem` 都被隐藏，Excel 在打开时会崩溃或渲染一个空白的数据透视表。请根据源数据构建白名单，使至少一项保持可见，这样保存的工作簿就能在每台机器上可靠打开。
{{% /alert %}}

{{< app/cells/assistant language="python" >}}
