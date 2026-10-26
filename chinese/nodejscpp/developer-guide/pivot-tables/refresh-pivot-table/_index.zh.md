---
title: 在 Aspose.Cells for Node.js via C++ 中刷新数据透视表和数据透视缓存
linktitle: 在 Aspose.Cells for Node.js via C++ 中刷新数据透视表和数据透视缓存
description: 学习如何在 Aspose.Cells for Node.js via C++ 中使用 v26.7+ 的数据透视刷新 API 来刷新数据透视表，本文涵盖 refreshAll、refreshPivotTables、PivotCache.refresh、calculateData 和 getPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, Node.js via C++, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/nodejs-cpp/refresh-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一个分层刷新 API，可在四个不同的范围重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Node.js via C++ v26.7** 开始，旧方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文介绍的更高效、可感知缓存的 API。
{{% /alert %}}

## Introduction
刷新数据透视表很少是单一操作。在后台，Aspose.Cells 维护着一条分层数据链，将原始源数据与您在工作表中看到的渲染值连接起来。理解这条数据链是针对任何情况选择合适刷新 API 的关键。
这条四层数据链包括：
1. **数据源** — 原始工作表区域、数据库查询或合并区域，其中存放着原始值。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据都在这里被收集和聚合。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，而不会直接从数据源读取。
4. **单元格** — 工作表的 `Cells`，`PivotTable` 将其计算后的值和样式渲染到其中。

{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型——也就是说，仅支持位于工作表区域中的数据。外部源（数据库、外部连接等）目前还无法通过缓存 API 进行刷新。
由于这种链式结构，Aspose.Cells 中存在两种基本的刷新路径：
- **`PivotTable.calculateData()`** — 从已缓存的数据重新计算单个 `PivotTable` 的显示，无需往返数据源。
本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作按所述方式运行。
{{% /alert %}}

## Quick Start
如果您只需要最短的代码来刷新工作簿中的所有数据透视表，只需一次调用即可：

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

本文其余部分将说明何时应选择更窄范围的 API。

## Required Imports
本文中的所有 JavaScript 示例都假定 Aspose.Cells for Node.js via C++ 模块已加载，并且透视类型位于 `Aspose.Cells.Pivot` 命名空间中。典型的设置如下：
- `const AsposeCells = require("aspose.cells.node");`
- `const { PivotFieldType } = AsposeCells;`（或通过 `AsposeCells.Pivot.PivotFieldType` 访问）

## Refresh All Pivot Tables in the Workbook
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。单次调用会遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于一般性能不受关注的全文档刷新，推荐使用此方法。
以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改某些源值，然后使用 `refreshAll()` 通过一次调用将所有内容更新到最新状态。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Write header row into cells A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(60);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(70);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(80);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(90);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(100);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(110);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(120);
// Add a pivot table: source range "A1:C9", destination cell "E3"
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

## Refresh All Pivot Tables on a Single Worksheet
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表无关且不应被触碰时。针对这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其范围限定在单个 `Worksheet` 实例内。

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("blueberry");
worksheet.getCells().get("B3").putValue(2021);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("cherry");
worksheet.getCells().get("B5").putValue(2021);
worksheet.getCells().get("C5").putValue(120);
worksheet.getCells().get("A6").putValue("grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(180);
worksheet.getCells().get("A7").putValue("blueberry");
worksheet.getCells().get("B7").putValue(2020);
worksheet.getCells().get("C7").putValue(130);
worksheet.getCells().get("A8").putValue("kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(220);
worksheet.getCells().get("A9").putValue("cherry");
worksheet.getCells().get("B9").putValue(2020);
worksheet.getCells().get("C9").putValue(140);
let pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);
worksheet.refreshPivotTables();
workbook.save("output.xlsx");
```

## Refresh a Single Pivot Table
当您需要对单个数据透视表进行精细控制时，基于缓存的 API 提供了两种选项。它们之间的选择取决于实际变更的内容：底层源数据，还是数据透视表自身的视图/布局设置。

### Source Data Changed — Use `PivotCache.refresh()`
如果底层源数据已更改，正确的入口点是 `pivotTable.PivotCache.refresh()`。此调用会重新读取源数据到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。

### Only View/Layout Changed — Use `calculateData()`
如果源数据*未*更改，而只是修改了数据透视表的视图或布局设置（例如，将某个字段移动到不同的区域，或切换了打开时刷新设置），则无需往返数据源。缓存中已包含正确的数据；只需重新计算渲染后的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。
以下示例修改数据透视表的非源属性，然后调用 `calculateData()` 从现有缓存重新渲染。

```javascript
const AsposeCells = require("aspose.cells.node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Write Fruit / Year / Amount header row
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// Write 8 data rows (rows 2-9, fitting the source range A1:C9)
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(150);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(250);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(350);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(450);
// Add a pivot table placed at destination cell E3, sourcing from A1:C9
var pivotTable = worksheet.getPivotTables().add("A1:C9", 2, 4);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Modify a view/layout property — this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed — only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

一个工作簿通常包含许多共享同一缓存的数据透视表。要枚举它们——例如在执行批量刷新之前，或诊断共享缓存的影响——可以使用 `PivotCache.getPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。

## Migrating from the Obsolete `PivotTable.RefreshData()`
在 Aspose.Cells for Node.js via C++ v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的、可感知缓存的 API。
在真实工作簿中，按表的 `RefreshData()` 方法存在两个问题：
- 每次调用时都会从源*重新获取*数据，即使源未发生变化。
推荐的替代方案如下：
以下示例演示了在多个共享单个缓存的数据透视表的工作簿中使用新的高效模式。

## Which Refresh API Should I Use?
下表总结了可用的刷新 API 以及何时选择每个 API。
| 目标 | 推荐 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 范围限定为单个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前枚举。 |
实际上，应优先使用基于缓存的 API，而不是过时的按表 `RefreshData()`。它们能够感知共享缓存，避免冗余的源获取，并允许您选择满足刷新需求的最小范围。

## Common Pitfalls
- **忘记在保存前刷新。** 数据透视表仅在其数据链被刷新时才会将渲染值写入工作表。如果您修改了源单元格，请在 `Workbook.save()` 之前调用 `PivotCache.refresh()`（或 `Workbook.refreshAll()`），否则保存的文件仍将包含旧的聚合值。
- **按表调用过时的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已标记为过时，并且每次调用都会重新获取源数据。当多个数据透视表共享一个缓存时，这意味着会进行 N 次冗余的源获取。应替换为对缓存调用一次 `PivotCache.refresh()`，然后对每个表调用 `calculateData()`。
- **仅布局更改时仍然刷新。** 如果您只更改了数据透视表的视图（列顺序、`ConsolidationFunction` 等）而未触及源数据，那么 `PivotCache.refresh()` 是不必要的且速度较慢。请调用 `pivotTable.calculateData()` 从现有缓存重新渲染。
- **`PivotCache.refresh()` 不支持外部源。** 如果数据透视表的源来自外部连接（数据库、OLAP 多维数据集等），则 `PivotCache.refresh()` 在 v26.7 中无法刷新它——它目前仅支持 `Sheet` 和 `Consolidation` 源类型。对于外部源，请重新打开工作簿或从源重建缓存。

{{< app/cells/assistant language="nodejs-cpp" >}}