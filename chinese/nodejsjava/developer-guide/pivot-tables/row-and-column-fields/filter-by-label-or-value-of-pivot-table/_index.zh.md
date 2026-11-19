---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选
description: Aspose.Cells for Node.js via Java 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选以及通过隐藏/取消隐藏透视项来筛选数据透视表数据。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 透视项, 隐藏透视项
type: docs
weight: 10
url: /zh/nodejs-java/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对文本类型的行或列字段应用标签筛选，在字段仅包含日期时间单元格或空白时使用日期筛选，对聚合数值应用值筛选，使用前 10 项筛选按值字段进行排名，或者使用 `IsHidden` 属性手动隐藏和取消隐藏各个透视项。每种策略都通过 `PivotField` 和 `PivotItem` 类上专用的 API 公开。
{{% /alert %}}

## **简介**
数据透视表是强大的分析工具，但原始汇总通常包含的信息远多于您需要呈现的内容。筛选是将数据透视表缩小到特定报告所需行、列或值的主要机制。Aspose.Cells for Node.js via Java 实现了 Microsoft Excel 中可用的筛选功能，并以编程方式将其公开，从而可以完全自动化生成报告。
本文涵盖以下筛选策略：
1. **标签筛选** — 基于文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白）的行或列字段。
3. **值筛选** — 基于数据字段的聚合值筛选项。
4. **前 10 项筛选** — 仅显示按值字段排序的前 N 项或后 N 项。
5. **隐藏 / 取消隐藏透视项** — 手动控制字段中每个单独项的可见性。
每种方法使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，必须在数据透视表上调用 `getPivotCache().refresh()`，以便缓存数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选允许您通过将行或列字段项的文本标题与模式进行比较来筛选这些项。当您希望仅显示名称以特定字母开头、包含特定单词或满足其他基于标题条件的项时，此功能非常有用。
Aspose.Cells 通过 `PivotField.filterByLabel(PivotFilterType, string)` 方法公开标签筛选功能。`PivotFilterType` 枚举包含 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。
以下示例加载包含现有数据透视表的工作簿，应用标签筛选以便仅保留标题以指定前缀开头的项，刷新数据透视表并保存结果。

```javascript
const AsposeCells = require("aspose.cells");
let fileName = "sample.xlsx";
let prefix = "B";
// Load the existing workbook containing a pivot table
let workbook = new AsposeCells.Workbook(fileName);
// Access the worksheet by index (first worksheet)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the first row PivotField
let rowField = pivotTable.getRowFields().get(0);
// Apply the label filter — show only row items whose labels begin with the supplied prefix
rowField.filterByLabel(AsposeCells.PivotFilterType.CAPTION_BEGINS_WITH, prefix, "");
// Refresh and recalculate the pivot table data so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook back to disk
workbook.save(fileName);
```

## **日期筛选**
日期筛选允许您按日期条件（例如今天、上周、本月、下个季度或特定日期范围）缩小数据透视表范围。它们是专用筛选器，仅对存储日期时间信息的字段有效。

{{% alert color="primary" %}}
日期筛选仅在行或列区域包含日期时间单元格或空白值时才有效。如果基础字段包含其他数据类型（例如数字或文本），则日期筛选将无法产生预期结果。在应用此筛选之前，请确保字段设置为日期格式，并且所有值都是有效的 `DateTime` 实例或空白单元格。
Aspose.Cells 通过 `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` 方法公开日期筛选功能。`PivotFilterType` 枚举包含专用的日期值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您可以传递一个或两个 `DateTime` 值（对于 `Between`，传递开始日期和结束日期）。
以下示例加载一个包含行区域包含日期字段的数据透视表的工作簿，应用日期筛选将可见项限制为特定日期范围，刷新数据透视表并保存工作簿。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
let inputPath = "sample.xlsx";
let outputPath = "output_filtered.xlsx";
if (!fs.existsSync(inputPath))
{
    throw new Error("Source workbook not found. Path: " + inputPath);
}
// Load the existing workbook that contains the pivot table
var workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (by index)
var worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
var pivotTable = worksheet.getPivotTables().get(0);
// Retrieve the date PivotField from the row area
// (Date filter only works when the row/column area contains only date-time cells or blanks)
let dateField = pivotTable.getRowFields().get(0);
// Define the date criterion for the Between filter
let startDate = new Date(2020, 0, 1);
let endDate = new Date(2020, 11, 31);
// Apply the date filter on the pivot field
dateField.filterByDate(AsposeCells.PivotFilterType.DATE_BETWEEN, startDate, endDate);
// Refresh and recalculate the pivot table so the filter takes effect
pivotTable.getPivotCache().refresh();
// Persist the workbook
workbook.save(outputPath);
```

## **值筛选**
值筛选作用于数据透视表在数据区域计算的聚合值。它们不是匹配文本标签，而是将数字总和与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易数量在某个范围内的区域。
Aspose.Cells 通过 `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` 方法公开值筛选功能。`filterType` 参数使用诸如 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 之类的值。`valueField` 参数指定要评估的数据字段，最后一个（或多个）参数提供阈值（一个或多个）。
以下示例加载一个包含数据透视表的工作簿，应用值筛选以仅保留聚合销售超过数值阈值的项，刷新数据透视表并保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");
var workbook = new AsposeCells.Workbook("sample.xlsx");
var worksheet = workbook.getWorksheets().get(0);
var pivotTable = worksheet.getPivotTables().get(0);
var rowField = pivotTable.getRowFields().get(0);
var dataField = pivotTable.getDataFields().get(0);
// Find the data field index manually since PivotFieldCollection doesn't have IndexOf
var dataFieldIndex = -1;
for (var i = 0; i < pivotTable.getDataFields().getCount(); i++)
{
    if (pivotTable.getDataFields().get(i) == dataField)
    {
        dataFieldIndex = i;
        break;
    }
}
if (dataFieldIndex >= 0)
{
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.VALUE_GREATER_THAN, 5000, Number.MAX_VALUE);
}
pivotTable.getPivotCache().refresh();
workbook.save("output.xlsx");
```

## **前 10 项筛选**
前 10 项筛选是值筛选的一种特殊形式，仅根据所选值字段保留最高或最低的 N 个项。它通常用于排名报告，例如"按收入排名前 10 的产品"或"按销售数量排名后 5 的区域"。

{{% alert color="primary" %}}
前 10 项筛选仅在数据透视表的数据区域中具有一个或多个值数据透视字段时才有效。如果没有任何值字段，则没有聚合度量可用于项排序，也无法应用该筛选。
Aspose.Cells 通过 `PivotField.filterTop10(valueFieldIndex, filterType, isTop, itemCount)` 方法公开前 10 筛选功能。`valueFieldIndex` 参数是用于对项进行排名的数据字段的索引，`filterType` 选择 `itemCount` 的单位（`PivotFilterType.COUNT` 保留固定数量的项，`PivotFilterType.PERCENT` 保留一定百分比的项，此时 `itemCount` 即为百分比值），`isTop` 指示是保留排名靠前的项（true）还是排名靠后的项（false），`itemCount` 定义要保留的项数或百分比。
以下示例加载一个包含具有值字段的数据透视表的工作簿，应用前 10 项筛选仅保留按销售总额排名前 10 的项，刷新数据透视表并保存工作簿。
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let inputPath = "input.xlsx";
let outputPath = "output.xlsx";
let workbook = new AsposeCells.Workbook(inputPath);
// Access the worksheet that holds the pivot table (index 0)
let worksheet = workbook.getWorksheets().get(0);
// Access the pivot table by index
let pivotTable = worksheet.getPivotTables().get(0);
// Confirm there is at least one value PivotField in the data area
if (pivotTable.getDataFields().getCount() == 0)
{
    throw new Error("Pivot table has no value (data) PivotField.");
}
let valueField = pivotTable.getDataFields().get(0);
// Retrieve the target row PivotField (the field we want to apply Top 10 on)
let rowField = pivotTable.getRowFields().get(0);
// The first (and only) data field is at index 0; Top 10 ranks by it.
let valueFieldIndex = 0;
// Apply the Top 10 filter on the row field:
//   - itemCount   = 10
//   - filterType  = PivotFilterType.SUM
//   - isTop       = true (top N; false would mean bottom N)
//   - valueFieldIndex = the index of the data field used to rank items
rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.COUNT, true, 10);
// Refresh the pivot table data and recalculate it so the filter takes effect
pivotTable.getPivotCache().refresh();
// Save the workbook
workbook.save(outputPath);
```

## **通过隐藏或取消隐藏透视项进行筛选**
除结构化的筛选 API 外，Aspose.Cells 还允许您直接控制每个单独透视项的可见性。通过遍历 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以选择性地隐藏特定项，而无需应用基于公式的筛选。将 `IsHidden = true` 设置为从数据透视表中隐藏该项；将 `IsHidden = false` 设置为取消隐藏并使其再次可见。
当筛选规则不规则或特定于项时（例如隐藏特定报告中不应出现的小部分命名类别），此方法非常有用。下面的示例加载数据透视表，按名称隐藏特定项，演示如何取消隐藏它，刷新数据透视表并保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");
// Access the first worksheet which contains the pivot table
let sheet = workbook.getWorksheets().get(0);
// Access the pivot table by index (the first pivot table on the sheet)
let pivotTable = sheet.getPivotTables().get(0);
// Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
let pivotField = pivotTable.getRowFields().get(0);
// Iterate through the PivotItems collection of the selected PivotField
let itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++) {
    let item = pivotField.getPivotItems().get(i);
    // Hide pivot items that match a specific name/criterion
    if (item.getName() == "Item1" || item.getName() == "Item2") {
        item.setHidden(true);
    }
    // Demonstrate unhiding: re-show a previously hidden pivot item
    if (item.getName() == "Item3") {
        item.setHidden(false);
    }
}
// Refresh and recalculate the pivot table so changes take effect
pivotTable.getPivotCache().refresh();
// Save the workbook — hidden items stay in the underlying data
// but are excluded from the displayed pivot table output
workbook.save("output_pivot_filtered.xlsx");
```

## **总结**
Aspose.Cells for Node.js via Java 提供了完整的、与 Microsoft Excel 功能相匹配的数据透视表筛选功能。标签筛选、日期筛选和值筛选涵盖了最常见的分析场景，而前 10 项筛选则处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供了灵活的项级后备方案。结合使用这些策略（例如，应用标签筛选然后隐藏特定项），您可以从代码完全构建精准定位的数据透视表报告。

## 相关文章
- [在 Aspose.Cells for Node.js via Java 中添加数据透视表的行和列字段](/cells/zh/nodejs-java/pivot-table-add-row-and-column-fields/)
- [在 Aspose.Cells for Node.js via Java 中向数据透视表添加筛选字段](/cells/zh/nodejs-java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via Java 中管理数据透视表的值字段](/cells/zh/nodejs-java/manage-value-fields/)
- [在 Aspose.Cells for Node.js via Java 中刷新数据透视表和透视缓存](/cells/zh/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}