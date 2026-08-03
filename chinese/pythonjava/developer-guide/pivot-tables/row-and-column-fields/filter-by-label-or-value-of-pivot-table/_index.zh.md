---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for Python via Java 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 名筛选以及通过隐藏或取消隐藏数据透视表项来筛选数据透视表数据。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 名筛选, 数据透视表项, 隐藏数据透视表项
type: docs
weight: 10
url: /zh/python-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了五种实用的策略用于筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，当字段仅包含日期时间单元格或空白时使用日期筛选，对聚合数值应用值筛选，使用前 10 名筛选按值字段进行排名，或者使用 `is_hidden` 属性手动隐藏和取消隐藏各个数据透视表项。每种策略都通过 `PivotField` 和 `PivotItem` 类上的专用 API 公开。

{{% /alert %}}

## **简介**

数据透视表是强大的分析工具，但原始汇总通常包含的信息远远超过您需要呈现的内容。筛选是将数据透视表缩小到特定报告所需行、列或值的主要机制。Aspose.Cells for Python via Java 镜像了 Microsoft Excel 中可用的筛选功能，并将其通过编程方式公开，以便完全自动化报告生成。

本文涵盖了以下筛选策略：

1. **标签筛选** — 根据文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白）的行或列字段。
3. **值筛选** — 根据数据字段的聚合值筛选项。
4. **前 10 名筛选** — 仅显示按值字段排名前 N 位或后 N 位的项。
5. **隐藏/取消隐藏数据透视表项** — 手动控制字段中每个单独项的可见性。

每种方法在 `PivotField` 类上使用不同的方法，或在 `PivotItem` 类上使用属性。应用任何筛选后，必须在数据透视表上调用 `refresh_data()` 和 `calculate_data()`，以便缓存数据和计算值反映新的筛选状态。

## **标签筛选**

标签筛选允许您通过将行或列字段项的文本标题与模式进行比较来筛选这些项。当您希望仅显示名称以特定字母开头、包含特定单词或符合其他基于标题的条件的产品时，这非常有用。

Aspose.Cells 通过 `PivotField.filter_by_label(PivotFilterType, str)` 方法公开标签筛选功能。`PivotFilterType` 枚举包含诸如 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。

以下示例加载包含现有数据透视表的工作簿，应用标签筛选以仅保留标题以指定前缀开头的项，刷新数据透视表，然后保存结果。

```python
jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

fileName = "sample.xlsx"
prefix = "B"

# 加载包含数据透视表的现有工作簿
workbook = Workbook(fileName)

# 通过索引访问工作表（第一个工作表）
worksheet = workbook.getWorksheets().get(0)

# 通过索引访问数据透视表
pivotTable = worksheet.getPivotTables().get(0)

# 检索第一个行 PivotField
rowField = pivotTable.getRowFields().get(0)

# 应用标签筛选器——仅显示标签以所提供前缀开头的行项
rowField.filterByLabel(PivotFilterType.CaptionBeginsWith, prefix, "")

# 刷新并重新计算数据透视表数据，使筛选生效
pivotTable.getPivotCache().refresh()

# 将工作簿保存回磁盘
workbook.save(fileName)

jpype.shutdownJVM()
```

## **日期筛选**

日期筛选允许您按基于日期的条件（如今天、上周、本月、下个季度或特定日期范围）来缩小数据透视表的范围。它们是专门用于处理存储日期时间信息的字段的筛选器。

{{% alert color="primary" %}}

日期筛选仅在行或列区域仅包含日期时间单元格或空白值时才有效。如果基础字段包含其他数据类型（如数字或文本），则日期筛选将无法产生预期结果。在应用此筛选之前，请确保字段已设置为日期格式，并且所有值都是有效的 `DateTime` 实例或空单元格。

{{% /alert %}}

Aspose.Cells 通过 `PivotField.filter_by_date(PivotFilterType, values)` 方法公开日期筛选功能。`PivotFilterType` 枚举包含专用的日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您传递一个或两个 `DateTime` 值（对于 `Between`，传递开始日期和结束日期）。

以下示例加载一个数据透视表的行区域包含日期字段的工作簿，应用日期筛选将可见项限制在特定日期范围内，刷新数据透视表，然后保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

inputPath = "sample.xlsx"
outputPath = "output_filtered.xlsx"

if not os.path.exists(inputPath):
    raise FileNotFoundError(f"Source workbook not found: {inputPath}")

# 加载包含数据透视表的现有工作簿
workbook = Workbook(inputPath)

# 通过索引访问包含数据透视表的工作表
worksheet = workbook.getWorksheets().get(0)

# 通过索引访问数据透视表
pivotTable = worksheet.getPivotTables().get(0)

# 从行区域检索日期透视字段
# (日期筛选仅在行/列区域仅包含日期时间单元格或空白时有效)
dateField = pivotTable.getRowFields().get(0)

# 为 Between 筛选定义日期条件
Date = jpype.JClass("java.util.Date")
startDate = Date(2020 - 1900, 0, 1)
endDate = Date(2020 - 1900, 11, 31)

# 在透视字段上应用日期筛选
dateField.filterByDate(PivotFilterType.DateBetween, startDate, endDate)

# 刷新并重新计算数据透视表以使筛选生效
pivotTable.getPivotCache().refresh()

# 保存工作簿
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **值筛选**

值筛选作用于数据透视表在其数据区域中计算的聚合值。它们不是匹配文本标签，而是将数值总数与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易计数在某个范围内的区域。

Aspose.Cells 通过 `PivotField.filter_by_value(value_field, filter_type, values)` 方法公开值筛选功能。`filter_type` 参数使用诸如 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 之类的值。`value_field` 参数指定应评估哪个数据字段，最后一个参数提供阈值。

以下示例加载一个包含数据透视表的工作簿，应用值筛选仅保留聚合销售额超过数值阈值的项，刷新数据透视表，然后保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFilterType

workbook = Workbook("sample.xlsx")
worksheet = workbook.getWorksheets().get(0)
pivotTable = worksheet.getPivotTables().get(0)

rowField = pivotTable.getRowFields().get(0)
dataField = pivotTable.getDataFields().get(0)

# 由于 PivotFieldCollection 没有 IndexOf 方法，所以手动查找数据字段索引
dataFieldIndex = -1
for i in range(pivotTable.getDataFields().getCount()):
    if pivotTable.getDataFields().get(i) == dataField:
        dataFieldIndex = i
        break

if dataFieldIndex >= 0:
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivotTable.getPivotCache().refresh()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **前 10 名筛选**

前 10 名筛选是值筛选的一种特殊形式，仅保留基于所选值字段的最高或最低 N 个项。它常用于排名报告，例如"按收入排名前 10 的产品"或"按销售数量排名后 5 的区域"。

{{% alert color="primary" %}}

前 10 名筛选仅在数据透视表的数据区域中具有一个或多个值透视字段时才有效。如果至少没有一个值字段，则没有可用于对项进行排名的聚合度量，并且无法应用该筛选。

{{% /alert %}}

Aspose.Cells 通过 `PivotField.filter_top10(item_count, is_top, value_field, filter_type)` 方法公开前 10 名筛选功能。`item_count` 参数定义要保留的项数，`is_top` 指示是否保留排名靠前的项（true）或排名靠后的项（false），`value_field` 引用用于排名的数据字段，`filter_type` 控制值的计算方式（通常为 `Sum`，也可以是 `Count` 和 `Percent`）。

以下示例加载一个包含值字段的数据透视表的工作簿，应用前 10 名筛选以仅保留按销售总额排名前 10 的项，刷新数据透视表，然后保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, PivotTable, PivotField, PivotFilterType

# 加载包含数据透视表的现有工作簿
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = Workbook(inputPath)

# 访问包含数据透视表的工作表（索引 0）
worksheet = workbook.getWorksheets().get(0)

# 按索引访问数据透视表
pivotTable = worksheet.getPivotTables().get(0)

# 确认数据区域中至少有一个值 PivotField
if pivotTable.getDataFields().getCount() == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.getDataFields().get(0)

# 检索目标行 PivotField（要对其应用前 10 筛选的字段）
rowField = pivotTable.getRowFields().get(0)

# 第一个（也是唯一的）数据字段位于索引 0；前 10 按它进行排名。
valueFieldIndex = 0

# 对行字段应用前 10 筛选：
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true（前 N；false 表示后 N）
#   - valueFieldIndex = 用于对项进行排名的数据字段的索引
rowField.filterTop10(10, PivotFilterType.Sum, True, valueFieldIndex)

# 刷新数据透视表数据并重新计算，以使筛选生效
pivotTable.getPivotCache().refresh()

# 保存工作簿
workbook.save(outputPath)

jpype.shutdownJVM()
```

## **通过隐藏或取消隐藏数据透视表项进行筛选**

除了结构化筛选 API 之外，Aspose.Cells 还允许您直接控制每个单独数据透视表项的可见性。通过遍历 `PivotField` 的 `PivotItems` 集合并切换 `is_hidden` 属性，您可以选择性地隐藏特定项，而无需应用基于公式的筛选。设置 `is_hidden = True` 会从数据透视表中隐藏该项；设置 `is_hidden = False` 会取消隐藏它并使其再次可见。

当筛选规则不规则或针对特定项时（例如，隐藏不应出现在特定报告中的少量命名类别），此方法非常有用。下面的示例加载一个数据透视表，通过名称隐藏特定项，演示如何取消隐藏它，刷新数据透视表，然后保存工作簿。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotField, PivotItem

# 加载包含数据透视表的现有工作簿
workbook = Workbook("pivot_table_sample.xlsx")

# 访问包含数据透视表的第一个工作表
sheet = workbook.getWorksheets().get(0)

# 按索引访问数据透视表（工作表上的第一个数据透视表）
pivotTable = sheet.getPivotTables().get(0)

# 获取目标 PivotField（我们要隐藏/显示其中项的第一个行标签字段）
pivotField = pivotTable.getRowFields().get(0)

# 遍历所选 PivotField 的 PivotItems 集合
itemCount = pivotField.getPivotItems().getCount()
for i in range(itemCount):
    item = pivotField.getPivotItems().get(i)

    # 隐藏符合特定名称/条件的数据透视项
    if item.getName() == "Item1" or item.getName() == "Item2":
        item.setIsHidden(True)

    # 演示取消隐藏：重新显示之前隐藏的数据透视项
    if item.getName() == "Item3":
        item.setIsHidden(False)

# 刷新并重新计算数据透视表以使更改生效
pivotTable.getPivotCache().refresh()

# 保存工作簿 — 隐藏的项保留在底层数据中
# 但从显示的数据透视表输出中排除
workbook.save("output_pivot_filtered.xlsx")

jpype.shutdownJVM()
```

## **总结**

Aspose.Cells for Python via Java 提供了一组完整的数据透视表筛选功能，与 Microsoft Excel 中的功能相匹配。标签、日期和值筛选涵盖了最常见的分析场景，而前 10 名筛选处理排名报告。当筛选规则不规则时，`PivotItem.is_hidden` 属性提供了一个灵活的、项级别的后备方案。结合这些策略（例如，应用标签筛选然后隐藏特定项），您可以完全通过代码构建精确针对性的数据透视表报告。
{{< app/cells/assistant language="python" >}}