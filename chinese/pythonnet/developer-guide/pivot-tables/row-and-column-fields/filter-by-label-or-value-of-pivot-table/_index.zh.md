---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for Python via .NET 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选以及通过隐藏或取消隐藏数据透视项来筛选数据透视表数据。
keywords: Aspose.Cells, Python via .NET 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/python-net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，当字段仅包含日期时间单元格或空白时使用日期筛选，对聚合数值应用值筛选，使用前 10 项筛选按值字段进行排名，或者使用 `is_hidden` 属性手动隐藏和取消隐藏各个数据透视项。每种策略都通过 `PivotField` 和 `PivotItem` 类上的专用 API 公开。
{{% /alert %}}
## **简介**
数据透视表是强大的分析工具，但原始摘要通常包含的信息远远超过您需要呈现的内容。筛选是将数据透视表缩小到特定报告所需的行、列或值的主要机制。Aspose.Cells for Python via .NET 反映了 Microsoft Excel 中可用的筛选功能，并通过编程方式公开这些功能，以便完全自动化报告生成。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白）的行或列字段。
3. **值筛选** — 根据数据字段的聚合值筛选项。
4. **前 10 项筛选** — 仅显示按值字段排序的前 N 项或后 N 项。
5. **隐藏/取消隐藏数据透视项** — 手动控制字段中每个项的可见性。
每种方法都使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，必须在数据透视表上调用 `refresh_data()` 和 `calculate_data()`，以便缓存数据和计算值反映新的筛选状态。
## **标签筛选**
标签筛选允许您通过将行或列字段项的文本标题与模式进行比较来筛选它们。当您希望仅显示名称以特定字母开头、包含特定单词或匹配其他基于标题的条件的产品时，这非常有用。
Aspose.Cells 通过 `PivotField.filter_by_label(PivotFilterType, label_string)` 方法公开标签筛选。`PivotFilterType` 枚举包括 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。
以下示例加载包含现有数据透视表的工作簿，应用标签筛选以使仅标题以指定前缀开头的项保持可见，刷新数据透视表，然后保存结果。
```python
aspose.cells as ac

fileName = "sample.xlsx"
prefix = "B"

# 加载包含数据透视表的现有工作簿
workbook = ac.Workbook(fileName)

# 通过索引访问工作表（第一个工作表）
worksheet = workbook.worksheets[0]

# 通过索引访问数据透视表
pivot_table = worksheet.pivot_tables[0]

# 获取第一个行 PivotField
row_field = pivot_table.row_fields[0]

# 应用标签筛选——仅显示标签以所提供前缀开头的行项目
row_field.filter_by_label(ac.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "")

# 刷新并重新计算数据透视表数据以使筛选生效
pivot_table.pivot_cache.refresh()

# 将工作簿保存回磁盘
workbook.save(fileName)
```
## **日期筛选**
日期筛选允许您按基于日期的条件（例如今天、上周、本月、下个季度或特定日期范围）缩小数据透视表。它们是仅适用于存储日期时间信息的字段的专用筛选器。
{{% alert color="primary" %}}
日期筛选仅在行或列区域仅包含日期时间单元格或空白值时才有效。如果底层字段包含其他数据类型（如数字或文本），日期筛选将无法产生预期结果。在应用此筛选之前，请确保该字段格式化为日期，并且所有值都是有效的 `DateTime` 实例或空单元格。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.filter_by_date(PivotFilterType, *date_times)` 方法公开日期筛选。`PivotFilterType` 枚举包含专用日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您需要传递一个或两个 `DateTime` 值（对于 `Between`，传递开始和结束日期）。
以下示例加载一个包含数据透视表的工作簿（该数据透视表的行区域包含日期字段），应用日期筛选将可见项限制为特定日期范围，刷新数据透视表，然后保存工作簿。
```python
from datetime import datetime

input_path = "sample.xlsx"
output_path = "output_filtered.xlsx"

if not os.path.exists(input_path):
    raise FileNotFoundError("Source workbook not found.", input_path)

# 加载包含数据透视表的现有工作簿
workbook = ac.Workbook(input_path)

# 通过索引访问包含数据透视表的工作表
worksheet = workbook.worksheets[0]

# 通过索引访问数据透视表
pivot_table = worksheet.pivot_tables[0]

# 从行区域检索日期 PivotField
# （日期筛选仅在行/列区域仅包含日期时间单元格或空白单元格时有效）
date_field = pivot_table.row_fields[0]

# 为 Between 筛选定义日期条件
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)

# 在数据透视字段上应用日期筛选
date_field.filter_by_date(ac.PivotFilterType.DATE_BETWEEN, start_date, end_date)

# 刷新并重新计算数据透视表以使筛选生效
pivot_table.pivot_cache.refresh()

# 保存工作簿
workbook.save(output_path)
```
## **值筛选**
值筛选作用于数据透视表在其数据区域中计算的聚合值。它们不是匹配文本标签，而是将数值总计与阈值进行比较。典型用例包括仅显示销售额总和超过目标金额的产品，或仅显示交易计数在某个范围内的区域。
Aspose.Cells 通过 `PivotField.filter_by_value(value_field, PivotFilterType, *thresholds)` 方法公开值筛选。`PivotFilterType` 参数使用 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。`value_field` 参数指定应评估哪个数据字段，最后的参数提供阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选以仅保留聚合销售额超过数值阈值的项，刷新数据透视表，然后保存工作簿。
```python
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]
pivot_table = worksheet.pivot_tables[0]

row_field = pivot_table.row_fields[0]
data_field = pivot_table.data_fields[0]

# 手动查找数据字段索引，因为 PivotFieldCollection 没有 IndexOf
data_field_index = -1
for i in range(pivot_table.data_fields.count):
    if pivot_table.data_fields[i] == data_field:
        data_field_index = i
        break

if data_field_index >= 0:
    row_field.filter_by_value(data_field_index, ac.PivotFilterType.VALUE_GREATER_THAN, 5000, float('inf'))

pivot_table.pivot_cache.refresh()

workbook.save("output.xlsx")
```
## **前 10 项筛选**
前 10 项筛选是值筛选的一种特殊形式，它仅根据所选值字段保留最高或最低的 N 个项。它通常用于排名报告，例如"按收入排名前 10 的产品"或"按销售数量排名后 5 的区域"。
{{% alert color="primary" %}}
前 10 项筛选仅在数据透视表的数据区域中具有一个或多个值数据透视字段时才有效。如果没有至少一个值字段，则没有可用来对项进行排名的聚合度量，因此无法应用该筛选。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.filter_top_10(item_count, is_top, value_field, PivotFilterType)` 方法公开前 10 项筛选。`item_count` 参数定义要保留的项数，`is_top` 指示是保留顶部项（True）还是底部项（False），`value_field` 引用用于排名的数据字段，`PivotFilterType` 控制值的计算方式（通常为 `Sum`，但也可以是 `Count` 和 `Percent`）。
以下示例加载一个包含数据透视表（其中包含值字段）的工作簿，应用前 10 项筛选以仅保留销售额总和最高的前 10 项，刷新数据透视表，然后保存工作簿。
```python
import aspose.cells as ac
import aspose.cells.pivot as acp

# 加载包含数据透视表的现有工作簿
inputPath = "input.xlsx"
outputPath = "output.xlsx"
workbook = ac.Workbook(inputPath)

# 访问包含数据透视表的工作表（索引 0）
worksheet = workbook.worksheets[0]

# 通过索引访问数据透视表
pivotTable = worksheet.pivot_tables[0]

# 确认数据区域中至少有一个值 PivotField
if pivotTable.data_fields.count == 0:
    raise Exception("Pivot table has no value (data) PivotField.")
valueField = pivotTable.data_fields[0]

# 检索目标行 PivotField（我们要对其应用前 10 筛选的字段）
rowField = pivotTable.row_fields[0]

# 第一个（也是唯一一个）数据字段位于索引 0；前 10 按它进行排序。
valueFieldIndex = 0

# 在行字段上应用前 10 筛选器：
#   - itemCount   = 10
#   - filterType  = PivotFilterType.Sum
#   - isTop       = true（前 N；false 表示后 N）
#   - valueFieldIndex = 用于对项进行排名的数据字段的索引
rowField.filter_top10(10, acp.PivotFilterType.Sum, True, valueFieldIndex)

# 刷新数据透视表数据并重新计算以使筛选器生效
pivotTable.pivot_cache.refresh()

# 保存工作簿
workbook.save(outputPath)
```
## **通过隐藏或取消隐藏数据透视项进行筛选**
除了结构化的筛选 API 之外，Aspose.Cells 还允许您直接控制每个数据透视项的可见性。通过迭代 `PivotField` 的 `PivotItems` 集合并切换 `is_hidden` 属性，您可以有选择地抑制特定项，而无需应用基于公式的筛选。将 `is_hidden = True` 设置为从数据透视表中隐藏该项；将 `is_hidden = False` 设置为取消隐藏该项并使其再次可见。
当筛选规则不规则或特定于项时（例如隐藏特定报告中不应出现的少数命名类别），此方法非常有用。下面的示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏它，刷新数据透视表，然后保存工作簿。
```python
import aspose.cells as ac

# 加载包含数据透视表的现有工作簿
workbook = ac.Workbook("pivot_table_sample.xlsx")

# 访问包含数据透视表的第一个工作表
sheet = workbook.worksheets[0]

# 按索引访问数据透视表（工作表上的第一个数据透视表）
pivot_table = sheet.pivot_tables[0]

# 获取目标 PivotField（我们将隐藏/取消隐藏项的第一个行标签字段）
pivot_field = pivot_table.row_fields[0]

# 遍历所选 PivotField 的 PivotItems 集合
item_count = pivot_field.pivot_items.count
for i in range(item_count):
    item = pivot_field.pivot_items[i]

    # 隐藏符合特定名称/条件的数据透视表项
    if item.name == "Item1" or item.name == "Item2":
        item.is_hidden = True

    # 演示取消隐藏：重新显示之前隐藏的数据透视表项
    if item.name == "Item3":
        item.is_hidden = False

# 刷新并重新计算数据透视表以使更改生效
pivot_table.pivot_cache.refresh()

# 保存工作簿 —— 隐藏的项保留在底层数据中
# 但在显示的数据透视表输出中被排除
workbook.save("output_pivot_filtered.xlsx")
```
## **总结**
Aspose.Cells for Python via .NET 提供了一套完整的数据透视表筛选功能，与 Microsoft Excel 中所提供的功能相匹配。标签、日期和值筛选涵盖了最常见的分析场景，而前 10 项筛选处理排名报告。当筛选规则不规则时，`PivotItem.is_hidden` 属性提供了灵活的、项级别的备用方案。结合这些策略 — 例如，应用标签筛选然后隐藏特定项 — 您可以完全通过代码构建精确目标的数据透视表报告。
{{< app/cells/assistant language="python-net" >}}