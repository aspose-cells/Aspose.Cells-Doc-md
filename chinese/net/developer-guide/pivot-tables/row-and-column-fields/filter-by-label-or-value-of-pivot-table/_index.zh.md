---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for .NET 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 筛选，以及通过隐藏或取消隐藏数据透视项来筛选数据透视表数据。
keywords: Aspose.Cells, .NET 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/net/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，当字段仅包含日期时间单元格或空白时使用日期筛选，对汇总数字应用值筛选，使用前 10 筛选按值字段进行排名，或者使用 `IsHidden` 属性手动隐藏和取消隐藏各个数据透视项。每种策略都通过 `PivotField` 和 `PivotItem` 类上的专用 API 公开。
{{% /alert %}}

## **介绍**
数据透视表是强大的分析工具，但原始汇总通常包含的信息远超您需要呈现的内容。筛选是将数据透视表缩小到特定报告所需的行、列或值的主要机制。Aspose.Cells for .NET 镜像了 Microsoft Excel 中提供的筛选功能，并将其以编程方式公开，从而可以完全自动化报告生成。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白）的行或列字段。
3. **值筛选** — 根据数据字段的汇总值筛选项。
4. **前 10 筛选** — 仅显示按值字段排名的前 N 个或后 N 个项。
5. **隐藏 / 取消隐藏数据透视项** — 手动控制字段中每个项的可见性。
每种方法都使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，您必须对数据透视表调用 `PivotCache.Refresh()`，以便缓存的数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选允许您通过将行或列字段项的文本标题与模式进行比较来筛选这些项。当您希望仅显示名称以特定字母开头、包含特定单词或匹配其他基于标题条件的项时，此功能非常有用。
Aspose.Cells 通过 `PivotField.FilterByLabel(PivotFilterType filterType, string label1, string label2)` 方法公开标签筛选功能。`filterType` 参数选择比较模式（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等）。`label1` 和 `label2` 参数提供比较文本 — 当您仅需要单一值匹配（例如开头匹配或包含匹配）时，为 `label2` 传递 `string.Empty`。
以下示例加载包含现有数据透视表的工作簿，应用标签筛选以使仅标题以指定前缀开头的项保持可见，刷新数据透视表，并保存结果。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string fileName = "sample.xlsx";
string prefix = "B";
// 加载包含数据透视表的现有工作簿
Workbook workbook = new Workbook(fileName);
// 按索引访问工作表（第一个工作表）
Worksheet worksheet = workbook.Worksheets[0];
// 按索引访问数据透视表
PivotTable pivotTable = worksheet.PivotTables[0];
// 获取第一个行 PivotField
PivotField rowField = pivotTable.RowFields[0];
// 应用标签筛选器 — 仅显示标签以提供的前缀开头的行项
rowField.FilterByLabel(PivotFilterType.CaptionBeginsWith, prefix, string.Empty);
// 刷新并重新计算数据透视表数据，使筛选器生效
pivotTable.PivotCache.Refresh();
// 将工作簿保存回磁盘
workbook.Save(fileName);
```

## **日期筛选**
日期筛选允许您根据基于日期的条件（如今天、上周、本月、下季度或特定日期范围）来缩小数据透视表的范围。它们是仅对存储日期时间信息的字段有效的专用筛选器。

{{% alert color="primary" %}}
日期筛选仅在行或列区域仅包含日期时间单元格或空白值时才有效。如果基础字段包含其他数据类型（如数字或文本），则日期筛选将无法产生预期的结果。在应用此筛选之前，请确保该字段格式设置为日期，且所有值均为有效的 `DateTime` 实例或空单元格。
Aspose.Cells 通过 `PivotField.FilterByDate(PivotFilterType, params DateTime[] values)` 方法公开日期筛选功能。`PivotFilterType` 枚举包含专用日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您传递一个或两个 `DateTime` 值（对于 `Between`，您传递开始日期和结束日期）。
以下示例加载一个工作簿，其中数据透视表的行区域包含日期字段，应用日期筛选将可见项限制在特定日期范围内，刷新数据透视表，并保存工作簿。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string inputPath = "sample.xlsx";
string outputPath = "output_filtered.xlsx";
if (!File.Exists(inputPath))
{
    throw new FileNotFoundException("Source workbook not found.", inputPath);
}
// 加载包含数据透视表的现有工作簿
var workbook = new Workbook(inputPath);
// 通过索引访问包含数据透视表的工作表
var worksheet = workbook.Worksheets[0];
// 通过索引访问数据透视表
var pivotTable = worksheet.PivotTables[0];
// 从行区域获取日期 PivotField
// （日期筛选仅在行/列区域只包含日期时间单元格或空白单元格时有效）
PivotField dateField = pivotTable.RowFields[0];
// 为 Between 筛选定义日期条件
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// 对数据透视字段应用日期筛选
dateField.FilterByDate(PivotFilterType.DateBetween, startDate, endDate);
// 刷新并重新计算数据透视表，使筛选生效
pivotTable.PivotCache.Refresh();
// 保存工作簿
workbook.Save(outputPath);
```

## **值筛选**
值筛选作用于数据透视表在其数据区域中计算的汇总值。它们不匹配文本标签，而是将数值总数与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易计数在某个范围内的区域。
Aspose.Cells 通过 `PivotField.FilterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` 方法公开值筛选功能。`valueFieldIndex` 参数指定应评估哪个数据字段（使用 `pivotTable.DataFields.IndexOf(dataField)` 或遍历集合以查找位置）。`filterType` 参数使用 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。两个 `double` 参数提供阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选仅保留汇总销售额超过数值阈值的项，刷新数据透视表，并保存工作簿。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook("sample.xlsx");
var worksheet = workbook.Worksheets[0];
var pivotTable = worksheet.PivotTables[0];
var rowField = pivotTable.RowFields[0];
var dataField = pivotTable.DataFields[0];
// 手动查找数据字段索引，因为 PivotFieldCollection 没有 IndexOf
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.DataFields.Count; i++)
{
    if (pivotTable.DataFields[i] == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.FilterByValue(dataFieldIndex, PivotFilterType.ValueGreaterThan, 5000, double.MaxValue);
}
pivotTable.PivotCache.Refresh();
workbook.Save("output.xlsx");
```

## **前 10 筛选**
前 10 筛选是值筛选的一种特殊形式，它仅根据所选值字段保留最高或最低的 N 个项。它通常用于排名报告，例如"按收入排名前 10 的产品"或"按销售数量排名后 5 的区域"。

{{% alert color="primary" %}}
前 10 筛选仅在数据透视表的数据区域中具有一个或多个值字段时才有效。如果没有至少一个值字段，则没有可用于对项进行排名的汇总度量，因此无法应用该筛选。
Aspose.Cells 通过 `PivotField.FilterTop10(int itemCount, PivotFilterType filterType, bool isTop, int valueFieldIndex)` 方法公开前 10 筛选功能。`itemCount` 参数定义要保留的项数，`filterType` 控制如何计算值（通常为 `Sum`，但也可以是 `Count` 和 `Percent`），`isTop` 指示是保留排名靠前的项（true）还是排名靠后的项（false），`valueFieldIndex` 是用于对项进行排名的数据字段的索引。
以下示例加载一个包含数据透视表（其中包含值字段）的工作簿，应用前 10 筛选仅保留按销售总额排名前 10 的项，刷新数据透视表，并保存工作簿。
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 加载包含数据透视表的现有工作簿
string inputPath = "input.xlsx";
string outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// 访问包含数据透视表的工作表（索引 0）
Worksheet worksheet = workbook.Worksheets[0];
// 按索引访问数据透视表
PivotTable pivotTable = worksheet.PivotTables[0];
// 确认数据区域中至少有一个值 PivotField
if (pivotTable.DataFields.Count == 0)
{
    throw new InvalidOperationException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.DataFields[0];
// 获取目标行 PivotField（要对其应用 Top 10 的字段）
PivotField rowField = pivotTable.RowFields[0];
// 第一个（也是唯一一个）数据字段的索引为 0；Top 10 根据该字段进行排名。
int valueFieldIndex = 0;
// 对行字段应用 Top 10 筛选：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true（顶部 N；false 表示底部 N）
//   - valueFieldIndex = 用于对项目进行排名的数据字段索引
rowField.FilterTop10(valueFieldIndex, PivotFilterType.Sum, true, 10);
// 刷新数据透视表数据并重新计算，使筛选生效
pivotTable.PivotCache.Refresh();
// 保存工作簿
workbook.Save(outputPath);
```

## **通过隐藏或取消隐藏数据透视项进行筛选**
除了结构化筛选 API 之外，Aspose.Cells 还允许您直接控制每个数据透视项的可见性。通过遍历 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以选择性地隐藏特定项，而无需应用基于公式的筛选。将 `IsHidden = true` 会从数据透视表中隐藏该项；将 `IsHidden = false` 会取消隐藏并使其再次可见。
当筛选规则不规则或特定于项时，此方法很有用，例如隐藏少量不应出现在特定报告中的命名类别。以下示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏，刷新数据透视表，并保存工作簿。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 加载包含数据透视表的现有工作簿
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// 访问包含数据透视表的第一个工作表
Worksheet sheet = workbook.Worksheets[0];
// 通过索引访问数据透视表(工作表上的第一个数据透视表)
PivotTable pivotTable = sheet.PivotTables[0];
// 获取目标数据透视字段(第一个行标签字段,我们将在其中隐藏/取消隐藏项)
PivotField pivotField = pivotTable.RowFields[0];
// 遍历所选数据透视字段的 PivotItems 集合
int itemCount = pivotField.PivotItems.Count;
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.PivotItems[i];
    // 隐藏与特定名称/条件匹配的数据透视项
    if (item.Name == "Item1" || item.Name == "Item2")
    {
        item.IsHidden = true;
    }
    // 演示取消隐藏:重新显示之前隐藏的数据透视项
    if (item.Name == "Item3")
    {
        item.IsHidden = false;
    }
}
// 刷新并重新计算数据透视表以使更改生效
pivotTable.PivotCache.Refresh();
// 保存工作簿 — 隐藏项保留在底层数据中
// 但会从显示的数据透视表输出中排除
workbook.Save("output_pivot_filtered.xlsx");
```

## **总结**
Aspose.Cells for .NET 提供了一整套与 Microsoft Excel 中所具备的筛选功能相匹配的数据透视表筛选功能。标签筛选、日期筛选和值筛选涵盖了最常见的分析场景，而前 10 筛选则用于处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供了一种灵活的、项级别的后备方案。结合这些策略（例如，应用标签筛选然后隐藏特定项），您可以完全通过代码构建精确定位的数据透视表报告。

## 相关文章
- [在 Aspose.Cells for .NET 中添加数据透视表行和列字段](/cells/zh/net/pivot-table-add-row-and-column-fields/)
- [在 Aspose.Cells for .NET 中管理数据透视表值字段](/cells/zh/net/manage-value-fields/)
- [在 Aspose.Cells for .NET 中刷新数据透视表和数据透视缓存](/cells/zh/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}