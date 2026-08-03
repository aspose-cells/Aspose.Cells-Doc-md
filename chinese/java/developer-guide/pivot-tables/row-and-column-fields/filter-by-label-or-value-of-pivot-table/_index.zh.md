---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for Java 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选以及通过隐藏或显示透视表项来筛选数据透视表数据。
keywords: Aspose.Cells, Java 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 透视表项, 隐藏透视表项
type: docs
weight: 10
url: /zh/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，当字段仅包含日期时间单元格或空白时使用日期筛选，对聚合数字应用值筛选，使用前 10 项筛选按值字段排序，或者使用 `IsHidden` 属性手动隐藏和显示各个透视表项。每种策略都通过 `PivotField` 和 `PivotItem` 类上的专用 API 公开。
{{% /alert %}}
## **简介**
数据透视表是强大的分析工具，但原始汇总通常包含的信息远多于您需要呈现的内容。筛选是将数据透视表缩小到特定报告中所需的行、列或值的主要机制。Aspose.Cells for Java 镜像了 Microsoft Excel 中提供的筛选功能，并通过编程方式公开这些功能，以便可以完全自动化生成报告。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据行或列字段项的文本标签进行筛选。
2. **日期筛选** — 对仅包含日期时间值（或空白）的行或列字段进行筛选。
3. **值筛选** — 根据数据字段的聚合值筛选项。
4. **前 10 项筛选** — 仅显示按值字段排序的前 N 项或后 N 项。
5. **隐藏/显示透视表项** — 手动控制字段中每个单独项的可见性。
每种方法都使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，您必须在数据透视表上调用 `refreshData()` 和 `calculateData()`，以便缓存数据和计算值反映新的筛选状态。
## **标签筛选**
标签筛选允许您通过将行或列字段的项的文本标题与模式进行比较来筛选它们。当您希望仅显示名称以特定字母开头、包含特定单词或匹配其他基于标题的条件的产品时，这非常有用。
Aspose.Cells 通过 `PivotField.filterByLabel(PivotFilterType, String)` 方法公开标签筛选。`PivotFilterType` 枚举包括以下值：`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等。第二个参数提供用于比较的标签字符串。
以下示例加载一个包含现有数据透视表的工作簿，应用标签筛选以仅保留标题以指定前缀开头的项，刷新数据透视表，并保存结果。
```java
import com.aspose.cells.*;

String fileName = "sample.xlsx";
String prefix = "B";

// 加载包含数据透视表的现有工作簿
Workbook workbook = new Workbook(fileName);

// 通过索引访问工作表（第一个工作表）
Worksheet worksheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// 获取第一个行字段 PivotField
PivotField rowField = pivotTable.getRowFields().get(0);

// 应用标签筛选器 - 仅显示标签以所提供前缀开头的行项
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");

// 刷新并重新计算数据透视表数据以使筛选器生效
pivotTable.refreshData();

// 将工作簿保存回磁盘
workbook.save(fileName);
```
## **日期筛选**
日期筛选允许您根据日期条件（如今天、上周、本月、下个季度或特定日期范围）缩小数据透视表的范围。它们是仅适用于存储日期时间信息的字段的专用筛选器。
{{% alert color="primary" %}}
日期筛选仅在行或列区域仅包含日期时间单元格或空白值时有效。如果基础字段包含其他数据类型（如数字或文本），则日期筛选将无法产生预期的结果。在应用此筛选之前，请确保字段格式设置为日期，并且所有值都是有效的 `DateTime` 实例或空单元格。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` 方法公开日期筛选。`PivotFilterType` 枚举包含专用日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您传递一个或两个 `DateTime` 值（对于 `Between`，传递开始日期和结束日期）。
以下示例加载一个工作簿，其中包含一个数据透视表，其行区域包含日期字段，应用日期筛选将可见项限制为特定日期范围，刷新数据透视表，并保存工作簿。
```java
import java.io.File;
import java.io.FileNotFoundException;

String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";

if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}

// 加载包含数据透视表的现有工作簿
Workbook workbook = new Workbook(inputPath);

// 通过索引访问包含数据透视表的工作表
Worksheet worksheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// 从行区域获取日期数据透视字段
// (日期筛选仅在行/列区域仅包含日期时间单元格或空白单元格时有效)
PivotField dateField = pivotTable.getRowFields().get(0);

// 为"介于"筛选定义日期条件
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);

// 在数据透视字段上应用日期筛选
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);

// 刷新并重新计算数据透视表以使筛选生效
pivotTable.refreshData();

// 保存工作簿
workbook.save(outputPath);
```
## **值筛选**
值筛选对数据透视表在其数据区域中计算的聚合值进行操作。它们不匹配文本标签，而是将数字总和与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易计数在某个范围内的区域。
Aspose.Cells 通过 `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` 方法公开值筛选。`filterType` 参数使用以下值：`ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual`。`valueField` 参数指定应评估的数据字段，最后的参数提供阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选以仅保留聚合销售额超过数值阈值的项，刷新数据透视表，并保存工作簿。
```java
import com.aspose.cells.*;

Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);

PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);

// 由于 PivotFieldCollection 没有 IndexOf 方法，因此手动查找数据字段索引
int dataFieldIndex = -1;
for (int i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, PivotFilterType.VALUE_GREATER_THAN, 5000, Double.MAX_VALUE);
}

pivotTable.refreshData();

workbook.save("output.xlsx");
```
## **前 10 项筛选**
前 10 项筛选是值筛选的一种特殊形式，仅保留基于所选值字段的最高或最低 N 个项。它通常用于排名报告，例如"按收入排名前 10 的产品"或"按销售数量排名后 5 的区域"。
{{% alert color="primary" %}}
前 10 项筛选仅在数据透视表的数据区域中具有一个或多个值透视字段时才有效。如果没有至少一个值字段，则没有可对项进行排序的聚合度量，并且无法应用筛选。
{{% /alert %}}
Aspose.Cells 通过 `PivotField.filterTop10(int itemCount, boolean isTop, PivotField valueField, PivotFilterType filterType)` 方法公开前 10 项筛选。`itemCount` 参数定义要保留的项数，`isTop` 指示是否保留排名靠前的项（true）或排名靠后的项（false），`valueField` 引用用于排名的数据字段，`filterType` 控制值的计算方式（通常为 `Sum`，也可以是 `Count` 和 `Percent`）。
以下示例加载一个包含具有值字段的数据透视表的工作簿，应用前 10 项筛选以仅保留按销售总额排名前 10 的项，刷新数据透视表，并保存工作簿。
```java
import com.aspose.cells.*;

// 加载包含数据透视表的现有工作簿
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);

// 访问包含数据透视表的工作表（索引为 0）
Worksheet worksheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表
PivotTable pivotTable = worksheet.getPivotTables().get(0);

// 确认数据区域中至少有一个值 PivotField
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);

// 获取目标行 PivotField（我们要对其应用前 10 筛选的字段）
PivotField rowField = pivotTable.getRowFields().get(0);

// 第一个（也是唯一的）数据字段位于索引 0 处；前 10 筛选按它进行排名。
int valueFieldIndex = 0;

// 在行字段上应用前 10 筛选：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true（前 N；false 表示后 N）
//   - valueFieldIndex = 用于对项进行排名的数据字段的索引
rowField.filterTop10(10, PivotFilterType.SUM, true, valueFieldIndex);

// 刷新数据透视表数据并重新计算，以使筛选生效
pivotTable.refreshData();

// 保存工作簿
workbook.save(outputPath);
```
## **通过隐藏或显示透视表项进行筛选**
除了结构化筛选 API 外，Aspose.Cells 还允许您直接控制每个单独透视表项的可见性。通过迭代 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以选择性抑制特定项，而无需应用基于公式的筛选。设置 `IsHidden = true` 会从数据透视表中隐藏该项；设置 `IsHidden = false` 会取消隐藏并使其再次可见。
当筛选规则不规则或针对特定项时，此方法非常有用，例如隐藏不应出现在特定报告中的少量命名类别。下面的示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏，刷新数据透视表，并保存工作簿。
```java
import com.aspose.cells.*;

// 加载包含数据透视表的现有工作簿
Workbook workbook = new Workbook("pivot_table_sample.xlsx");

// 访问包含数据透视表的第一个工作表
Worksheet sheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表(工作表上的第一个数据透视表)
PivotTable pivotTable = sheet.getPivotTables().get(0);

// 获取目标 PivotField(我们将隐藏/取消隐藏项的第一个行标签字段)
PivotField pivotField = pivotTable.getRowFields().get(0);

// 遍历所选 PivotField 的 PivotItems 集合
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);

    // 隐藏符合特定名称/条件的数据透视项
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setHidden(true);
    }

    // 演示取消隐藏:重新显示之前隐藏的数据透视项
    if (item.getName() == "Item3")
    {
        item.setHidden(false);
    }
}

// 刷新并重新计算数据透视表以使更改生效
pivotTable.refreshData();

// 保存工作簿 - 隐藏项保留在底层数据中
// 但会从显示的数据透视表输出中排除
workbook.save("output_pivot_filtered.xlsx");
```
## **总结**
Aspose.Cells for Java 提供了一整套与 Microsoft Excel 中找到的数据透视表筛选功能相匹配的功能。标签、日期和值筛选涵盖最常见的分析场景，而前 10 项筛选处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供了灵活的项级后备方案。组合使用这些策略（例如，先应用标签筛选，然后隐藏特定项）使您能够完全通过代码构建精确针对的数据透视表报告。
{{< app/cells/assistant language="java" >}}