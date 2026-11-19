---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for Java 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选，以及通过隐藏或取消隐藏数据透视项来筛选数据透视表数据。
keywords: Aspose.Cells, Java 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用策略来筛选数据透视表中显示的数据。可以对基于文本的行字段或列字段应用标签筛选；当字段仅包含日期时间单元格或空单元格时使用日期筛选；根据汇总数值应用值筛选；使用前 10 项筛选按值字段对各项进行排名；或使用 `IsHidden` 属性手动隐藏和取消隐藏各个数据透视项。每种策略均通过 `PivotField` 和 `PivotItem` 类上的专用 API 提供。
{{% /alert %}}

## **简介**
数据透视表是强大的分析工具，但原始汇总数据通常包含远超实际展示所需的信息。筛选是将数据透视表缩减至仅包含特定报告所需行、列或值的主要手段。Aspose.Cells for Java 提供与 Microsoft Excel 相同的筛选功能，并提供相应的编程接口，使报告生成能够完全自动化。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行字段或列字段中的项。
2. **日期筛选** — 筛选仅包含日期时间值（或空值）的行字段或列字段。
3. **值筛选** — 根据数据字段的汇总值筛选各项。
4. **前 10 项筛选** — 仅显示按值字段排名的前 N 项或后 N 项。
5. **隐藏/取消隐藏数据透视项** — 手动控制字段中各个项的可见性。
上述每种筛选方式分别使用 `PivotField` 类上的特定方法或 `PivotItem` 类上的属性。应用任一筛选后，必须在数据透视表上调用 `getPivotCache().refresh()`，使缓存数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选可依据指定的模式筛选行字段或列字段中的项，方法是将其文本标题与该模式进行比较。当您希望仅显示名称以特定字母开头、包含特定单词或满足其他以标题为依据的条件的产品时，此功能非常有用。
Aspose.Cells 通过 `PivotField.filterByLabel(PivotFilterType, String)` 方法提供标签筛选功能。`PivotFilterType` 枚举包含 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。
以下示例加载一个包含现有数据透视表的工作簿，应用标签筛选，仅保留标题以指定前缀开头的项，刷新数据透视表并保存结果。

```java
import com.aspose.cells.*;
String fileName = "sample.xlsx";
String prefix = "B";
// Load the existing workbook containing a pivot table
Workbook workbook = new Workbook(fileName);
// Access the worksheet by index (first worksheet)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
PivotField rowField = pivotTable.getRowFields().get(0);
// Apply the label filter - show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **日期筛选**
日期筛选可依据今天、上周、本月、下一季度或特定日期范围等日期条件来筛选数据透视表。日期筛选仅适用于存储日期时间信息的字段。

{{% alert color="primary" %}}
仅当行区域或列区域只包含日期时间单元格或空值时，日期筛选才会生效。如果底层字段包含数字或文本等其他数据类型，日期筛选将不会产生预期结果。应用此筛选前，请确保字段已设置为日期格式，且所有值均为有效的 `DateTime` 实例或空单元格。
Aspose.Cells 通过 `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` 方法提供日期筛选功能。`PivotFilterType` 枚举包含 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between` 等专用日期值。根据所选筛选类型，传入一个或两个 `DateTime` 值（对于 `Between`，传入开始日期和结束日期）。
以下示例加载一个工作簿，其中的数据透视表行区域包含日期字段。该示例应用日期筛选，将可见项限制在特定日期范围内，刷新数据透视表并保存工作簿。
{{% /alert %}}

```java
import java.io.File;
import java.io.FileNotFoundException;
String inputPath = "sample.xlsx";
String outputPath = "output_filtered.xlsx";
if (!new File(inputPath).exists())
{
    throw new FileNotFoundException("Source workbook not found: " + inputPath);
}
// Load the existing workbook that contains the pivot table
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
PivotField dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
DateTime startDate = new DateTime(2020, 1, 1);
DateTime endDate = new DateTime(2020, 12, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **值筛选**
值筛选根据数据透视表在数据区域中计算的汇总值进行筛选。它不匹配文本标签，而是将汇总数值与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易次数落在某一数值范围内的地区。
Aspose.Cells 通过 `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params Object[] values)` 方法提供值筛选功能。`filterType` 参数可取 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。`valueField` 参数指定要评估的数据字段，末尾的一个或多个参数提供相应的阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选，仅保留汇总销售值超过数值阈值的项，刷新数据透视表并保存工作簿。

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("sample.xlsx");
Worksheet worksheet = workbook.getWorksheets().get(0);
PivotTable pivotTable = worksheet.getPivotTables().get(0);
PivotField rowField = pivotTable.getRowFields().get(0);
PivotField dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
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
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **前 10 项筛选**
前 10 项筛选是值筛选的一种特殊形式，可根据指定的值字段仅保留 N 个排名最高或最低的项。常用于生成诸如“按收入排名前 10 的产品”或“按销售量排名后 5 的地区”等排名报告。

{{% alert color="primary" %}}
仅当数据透视表的数据区域中包含一个或多个值字段时，前 10 项筛选才会生效。如果数据区域中没有值字段，就没有可用于对各项进行排名的汇总度量，因此无法应用此筛选。
Aspose.Cells 通过 `PivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, boolean isTop, int itemCount)` 方法提供前 10 项筛选功能。`valueFieldIndex` 参数是数据字段的索引，该字段的汇总值用于对各项进行排名；`filterType` 选择 `itemCount` 的计量单位（`PivotFilterType.COUNT` 保留固定数量的项，`PivotFilterType.PERCENT` 保留项的百分比，因此 `itemCount` 本身即为百分比）；`isTop` 指定保留排名靠前的项（true）还是排名靠后的项（false）；`itemCount` 定义要保留的项数或百分比。
以下示例加载一个包含数据透视表的工作簿，该数据透视表含有一个值字段。示例应用前 10 项筛选，仅保留销售总额最高的 10 个项，刷新数据透视表并保存工作簿。
{{% /alert %}}

```java
import com.aspose.cells.*;
// Load the existing workbook that contains the pivot table
String inputPath = "input.xlsx";
String outputPath = "output.xlsx";
Workbook workbook = new Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
PivotTable pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new RuntimeException("Pivot table has no value (data) PivotField.");
}
PivotField valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
PivotField rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
int valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **按隐藏或取消隐藏数据透视项进行筛选**
除结构化筛选 API 外，Aspose.Cells 还允许您直接控制每个数据透视项的可见性。通过迭代 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以在不应用基于公式的筛选的情况下，选择性地隐藏特定项。设置 `IsHidden = true` 会从数据透视表中隐藏该项；设置 `IsHidden = false` 会取消隐藏该项并使其重新可见。
当筛选规则不规则或需要针对特定项处理时，此方法非常有用。例如，可以隐藏特定报告中不应出现的少量已命名的类别。以下示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏该项，刷新数据透视表并保存工作簿。

```java
import com.aspose.cells.*;
// Load an existing workbook containing a pivot table
Workbook workbook = new Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
Worksheet sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
PivotTable pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
PivotField pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
int itemCount = pivotField.getPivotItems().getCount();
for (int i = 0; i < itemCount; i++)
{
    PivotItem item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName().equals("Item1") || item.getName().equals("Item2"))
    {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName().equals("Item3"))
    {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook - hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **总结**
Aspose.Cells for Java 提供了一套与 Microsoft Excel 相同的数据透视表筛选功能。标签筛选、日期筛选和值筛选涵盖最常见的分析场景，前 10 项筛选则用于排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供了基于单个数据透视项的灵活替代方案。组合使用这些策略（例如先应用标签筛选，再隐藏特定项），即可完全通过代码生成具有精确筛选目标的数据透视表报告。

## 相关文章
- [插入数据透视表](/cells/zh/java/create-pivot-table/)
- [在 Aspose.Cells for Java 中为数据透视表添加行字段和列字段](/cells/zh/java/pivot-table-add-row-and-column-fields/)
- [在 Aspose.Cells for Java 中向数据透视表添加筛选字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Java 中管理数据透视表值字段](/cells/zh/java/manage-value-fields/)
- [在 Aspose.Cells for Java 中刷新数据透视表和数据透视缓存](/cells/zh/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}