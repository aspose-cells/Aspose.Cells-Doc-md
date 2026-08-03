---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for Node.js via C++ 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选以及通过隐藏或取消隐藏透视项来筛选数据透视表数据。
keywords: Aspose.Cells, Node.js via C++ library, spreadsheet, pivot table, filter, label filter, value filter, date filter, top 10 filter, pivot item, hide pivot item
type: docs
weight: 10
url: /zh/nodejs-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了五种实用的策略来筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，在字段仅包含日期时间单元格或空白时使用日期筛选，对汇总数字应用值筛选，使用前 10 项筛选按值字段排序，或者使用 `IsHidden` 属性手动隐藏和取消隐藏各个透视项。每种策略都通过 `PivotField` 和 `PivotItem` 类上的专用 API 公开。

{{% /alert %}}

## **简介**

数据透视表是强大的分析工具，但原始汇总通常包含的信息远多于您需要呈现的内容。筛选是将数据透视表缩小到特定报告中重要的行、列或值的主要机制。Aspose.Cells for Node.js via C++ 镜像了 Microsoft Excel 中可用的筛选功能，并通过编程方式公开这些功能，以便完全自动化生成报告。

本文涵盖以下筛选策略：

1. **标签筛选** — 根据文本标签筛选行或列字段项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白）的行或列字段。
3. **值筛选** — 根据数据字段的汇总值筛选项。
4. **前 10 项筛选** — 仅显示按值字段排序的前 N 项或后 N 项。
5. **隐藏/取消隐藏透视项** — 手动控制字段中各个项的可见性。

每种方法都使用 `PivotField` 类上的不同方法或 `PivotItem` 类上的属性。应用任何筛选后，您必须在数据透视表上调用 `refreshData()` 和 `calculateData()`，以便缓存数据和计算值反映新的筛选状态。

## **标签筛选**

标签筛选允许您通过将文本标题与模式进行比较来筛选行或列字段的项。当您只想显示名称以特定字母开头、包含特定单词或匹配其他基于标题条件的项时，这非常有用。

Aspose.Cells 通过 `PivotField.filterByLabel(PivotFilterType, string)` 方法公开标签筛选。`PivotFilterType` 枚举包括 `CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等值。第二个参数提供用于比较的标签字符串。

以下示例加载包含现有数据透视表的工作簿，应用标签筛选以使仅标题以指定前缀开头的项保持可见，刷新数据透视表，并保存结果。

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// 加载包含数据透视表的现有工作簿
let workbook = new AsposeCells.Workbook(fileName);

// 按索引访问工作表（第一个工作表）
let worksheet = workbook.getWorksheets().get(0);

// 按索引访问数据透视表
let pivotTable = worksheet.getPivotTables().get(0);

// 获取第一个行数据透视字段
let rowField = pivotTable.getRowFields().get(0);

// 应用标签筛选器——仅显示标签以所提供前缀开头的行项
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// 刷新并重新计算数据透视表数据，使筛选器生效
pivotTable.getPivotCache().refresh();

// 将工作簿保存回磁盘
workbook.save(fileName);
```

## **日期筛选**

日期筛选允许您按基于日期的条件（如今天、上周、本月、下季度或特定日期范围）缩小数据透视表。它们是专门的筛选，仅适用于存储日期时间信息的字段。

{{% alert color="primary" %}}

日期筛选仅在行或列区域仅包含日期时间单元格或空白值时才有效。如果基础字段包含其他数据类型（如数字或文本），则日期筛选将无法产生预期结果。在应用此筛选之前，请确保字段格式化为日期，并且所有值都是有效的 `DateTime` 实例或空单元格。

{{% /alert %}}

Aspose.Cells 通过 `PivotField.filterByDate(PivotFilterType, params DateTime[] values)` 方法公开日期筛选。`PivotFilterType` 枚举包含专门的日期值，如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选类型，您传递一个或两个 `DateTime` 值（对于 `Between`，传递开始和结束日期）。

以下示例加载一个工作簿，其数据透视表的行区域包含日期字段，应用日期筛选将可见项限制为特定日期范围，刷新数据透视表，并保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("源工作簿未找到: " + inputPath);
}

// 加载包含数据透视表的现有工作簿
const workbook = new AsposeCells.Workbook(inputPath);

// 通过索引访问包含数据透视表的工作表
const worksheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表
const pivotTable = worksheet.getPivotTables().get(0);

// 从行区域获取日期透视字段
// (日期筛选仅在行/列区域仅包含日期时间单元格或空白时有效)
const dateField = pivotTable.getRowFields().get(0);

// 定义 Between 筛选器的日期条件
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// 在透视字段上应用日期筛选
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// 刷新并重新计算数据透视表以使筛选生效
pivotTable.getPivotCache().refresh();

// 保留工作簿
workbook.save(outputPath);
```

## **值筛选**

值筛选对数据透视表在其数据区域中计算的汇总值进行操作。它们不是匹配文本标签，而是将数字总数与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易计数在某个范围内的区域。

Aspose.Cells 通过 `PivotField.filterByValue(PivotField valueField, PivotFilterType filterType, params object[] values)` 方法公开值筛选。`filterType` 参数使用 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。`valueField` 参数指定应评估哪个数据字段，最后一个参数提供阈值。

以下示例加载一个包含数据透视表的工作簿，应用值筛选仅保留汇总销售超过数字阈值的项，刷新数据透视表，并保存工作簿。

```javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");
```

## **前 10 项筛选**

前 10 项筛选是值筛选的一种专门形式，仅基于所选值字段保留最高或最低的 N 个项。它通常用于排名报告，例如"按收入排名前 10 位的产品"或"按销售数量排名后 5 位的区域"。

{{% alert color="primary" %}}

前 10 项筛选仅在数据透视表的数据区域中有一个或多个值透视字段时才有效。如果没有至少一个值字段，则没有可汇总的度量来对项进行排序，因此无法应用筛选。

{{% /alert %}}

Aspose.Cells 通过 `PivotField.filterTop10(int itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` 方法公开前 10 项筛选。`itemCount` 参数定义要保留的项数，`isTop` 指示是否保留前项（true）或后项（false），`valueField` 引用用于排序的数据字段，`filterType` 控制如何计算值（通常为 `Sum`，但也可以是 `Count` 和 `Percent`）。

以下示例加载一个包含数据透视表的工作簿，该数据透视表包含一个值字段，应用前 10 项筛选以仅按销售总和保留最高的 10 个项，刷新数据透视表，并保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");

// 加载包含数据透视表的现有工作簿
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// 访问包含数据透视表的工作表（索引 0）
const worksheet = workbook.getWorksheets().get(0);

// 按索引访问数据透视表
const pivotTable = worksheet.getPivotTables().get(0);

// 确认数据区域中至少有一个值 PivotField
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("数据透视表没有值（数据）PivotField。");
}
const valueField = pivotTable.getDataFields().get(0);

// 获取目标行 PivotField（我们想要对其应用前 10 筛选的字段）
const rowField = pivotTable.getRowFields().get(0);

// 第一个（也是唯一的）数据字段位于索引 0；前 10 按它进行排名。
const valueFieldIndex = 0;

// 对行字段应用前 10 筛选：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true（前 N；false 表示后 N）
//   - valueFieldIndex = 用于对项进行排名的数据字段的索引
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// 刷新数据透视表数据并重新计算，以使筛选生效
pivotTable.getPivotTableCache().refresh();

// 保存工作簿
workbook.save(outputPath);
```

## **通过隐藏或取消隐藏透视项进行筛选**

除了结构化筛选 API 之外，Aspose.Cells 还允许您直接控制每个透视项的可见性。通过迭代 `PivotField` 的 `PivotItems` 集合并切换 `IsHidden` 属性，您可以选择性地抑制特定项而无需应用基于公式的筛选。设置 `IsHidden = true` 会从数据透视表中隐藏该项；设置 `IsHidden = false` 会取消隐藏该项并使其再次可见。

当筛选规则不规则或特定于项时，此方法很有用，例如隐藏少量不应出现在特定报告中的已命名类别。下面的示例加载一个数据透视表，按名称隐藏特定项，演示如何取消隐藏它，刷新数据透视表，并保存工作簿。

```javascript
const AsposeCells = require("aspose.cells");

// 加载包含数据透视表的现有工作簿
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// 访问包含数据透视表的第一个工作表
const sheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表（工作表上的第一个数据透视表）
const pivotTable = sheet.getPivotTables().get(0);

// 检索目标 PivotField（我们将对其中的项进行隐藏/取消隐藏的第一个行标签字段）
const pivotField = pivotTable.getRowFields().get(0);

// 遍历所选 PivotField 的 PivotItems 集合
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // 隐藏符合特定名称/条件的数据透视项
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // 演示取消隐藏：重新显示先前隐藏的数据透视项
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// 刷新并重新计算数据透视表以使更改生效
pivotTable.getPivotCache().refreshData();

// 保存工作簿 — 隐藏的项保留在底层数据中
// 但会从显示的数据透视表输出中排除
workbook.save("output_pivot_filtered.xlsx");
```

## **总结**

Aspose.Cells for Node.js via C++ 提供了一套完整的数据透视表筛选功能，与 Microsoft Excel 中的功能相匹配。标签、日期和值筛选涵盖了最常见的分析场景，而前 10 项筛选处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供灵活的项级后备。结合这些策略 — 例如，应用标签筛选然后隐藏特定项 — 您可以完全通过代码构建精确针对的数据透视表报告。
{{% alert color="primary" %}}

Aspose.Cells provides five practical strategies for filtering the data displayed in a pivot table...

{{% /alert %}}

```javascript
let fileName = "sample.xlsx";
let prefix = "B";

// 加载包含数据透视表的现有工作簿
let workbook = new AsposeCells.Workbook(fileName);

// 按索引访问工作表（第一个工作表）
let worksheet = workbook.getWorksheets().get(0);

// 按索引访问数据透视表
let pivotTable = worksheet.getPivotTables().get(0);

// 获取第一个行数据透视字段
let rowField = pivotTable.getRowFields().get(0);

// 应用标签筛选器——仅显示标签以所提供前缀开头的行项
rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, prefix, "");

// 刷新并重新计算数据透视表数据，使筛选器生效
pivotTable.getPivotCache().refresh();

// 将工作簿保存回磁盘
workbook.save(fileName);javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const inputPath = "sample.xlsx";
const outputPath = "output_filtered.xlsx";

if (!fs.existsSync(inputPath))
{
    throw new Error("源工作簿未找到: " + inputPath);
}

// 加载包含数据透视表的现有工作簿
const workbook = new AsposeCells.Workbook(inputPath);

// 通过索引访问包含数据透视表的工作表
const worksheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表
const pivotTable = worksheet.getPivotTables().get(0);

// 从行区域获取日期透视字段
// (日期筛选仅在行/列区域仅包含日期时间单元格或空白时有效)
const dateField = pivotTable.getRowFields().get(0);

// 定义 Between 筛选器的日期条件
const startDate = new Date(2020, 0, 1);
const endDate = new Date(2020, 11, 31);

// 在透视字段上应用日期筛选
dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);

// 刷新并重新计算数据透视表以使筛选生效
pivotTable.getPivotCache().refresh();

// 保留工作簿
workbook.save(outputPath);javascript
let dataFieldIndex = -1;
for (let i = 0; i < pivotTable.getDataFields().getCount(); i++) {
    if (pivotTable.getDataFields().get(i) === dataField) {
        dataFieldIndex = i;
        break;
    }
}

if (dataFieldIndex >= 0) {
    rowField.filterByValue(dataFieldIndex, AsposeCells.PivotFilterType.ValueGreaterThan, 5000, Number.MAX_VALUE);
}

pivotTable.getPivotCache().refresh();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// 加载包含数据透视表的现有工作簿
const inputPath = "input.xlsx";
const outputPath = "output.xlsx";
const workbook = new AsposeCells.Workbook(inputPath);

// 访问包含数据透视表的工作表（索引 0）
const worksheet = workbook.getWorksheets().get(0);

// 按索引访问数据透视表
const pivotTable = worksheet.getPivotTables().get(0);

// 确认数据区域中至少有一个值 PivotField
if (pivotTable.getDataFields().getCount() === 0) {
    throw new Error("数据透视表没有值（数据）PivotField。");
}
const valueField = pivotTable.getDataFields().get(0);

// 获取目标行 PivotField（我们想要对其应用前 10 筛选的字段）
const rowField = pivotTable.getRowFields().get(0);

// 第一个（也是唯一的）数据字段位于索引 0；前 10 按它进行排名。
const valueFieldIndex = 0;

// 对行字段应用前 10 筛选：
//   - itemCount   = 10
//   - filterType  = PivotFilterType.Sum
//   - isTop       = true（前 N；false 表示后 N）
//   - valueFieldIndex = 用于对项进行排名的数据字段的索引
rowField.filterTop10(10, AsposeCells.PivotFilterType.Sum, true, valueFieldIndex);

// 刷新数据透视表数据并重新计算，以使筛选生效
pivotTable.getPivotTableCache().refresh();

// 保存工作簿
workbook.save(outputPath);javascript
const AsposeCells = require("aspose.cells");

// 加载包含数据透视表的现有工作簿
const workbook = new AsposeCells.Workbook("pivot_table_sample.xlsx");

// 访问包含数据透视表的第一个工作表
const sheet = workbook.getWorksheets().get(0);

// 通过索引访问数据透视表（工作表上的第一个数据透视表）
const pivotTable = sheet.getPivotTables().get(0);

// 检索目标 PivotField（我们将对其中的项进行隐藏/取消隐藏的第一个行标签字段）
const pivotField = pivotTable.getRowFields().get(0);

// 遍历所选 PivotField 的 PivotItems 集合
const itemCount = pivotField.getPivotItems().getCount();
for (let i = 0; i < itemCount; i++)
{
    const item = pivotField.getPivotItems().get(i);

    // 隐藏符合特定名称/条件的数据透视项
    if (item.getName() == "Item1" || item.getName() == "Item2")
    {
        item.setIsHidden(true);
    }

    // 演示取消隐藏：重新显示先前隐藏的数据透视项
    if (item.getName() == "Item3")
    {
        item.setIsHidden(false);
    }
}

// 刷新并重新计算数据透视表以使更改生效
pivotTable.getPivotCache().refreshData();

// 保存工作簿 — 隐藏的项保留在底层数据中
// 但会从显示的数据透视表输出中排除
workbook.save("output_pivot_filtered.xlsx");
```

## **总结**

Aspose.Cells for Node.js via C++ 提供了一套完整的数据透视表筛选功能，与 Microsoft Excel 中的功能相匹配。标签、日期和值筛选涵盖了最常见的分析场景，而前 10 项筛选处理排名报告。当筛选规则不规则时，`PivotItem.IsHidden` 属性提供灵活的项级后备。结合这些策略 — 例如，应用标签筛选然后隐藏特定项 — 您可以完全通过代码构建精确针对的数据透视表报告。
{{< app/cells/assistant language="nodejs-cpp" >}}