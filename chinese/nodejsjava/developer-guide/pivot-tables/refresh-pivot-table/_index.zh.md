---
title: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
linktitle: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
description: 学习如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for Node.js via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用代码示例。
keywords: Aspose.Cells, Node.js, Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
```

Now the body:

Alert block 1:
"Aspose.Cells provides a layered refresh API that lets you reload pivot data at four different scopes — from the entire workbook down to a single pivot table. Starting with **Aspose.Cells for Node.js via Java v26.7**, the legacy method `PivotTable.RefreshData()` is marked obsolete and should be replaced with the more efficient, cache-aware APIs described in this article."

Translation:
"Aspose.Cells 提供了一个分层刷新 API，允许您在四个不同范围内重新加载透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for Node.js via Java v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文介绍的更高效的、缓存感知的 API。"

Wait, I need to be careful about the doubled product name - "Aspose.Cells for Node.js via Java v26.7" should be corrected to "Aspose.Cells for Node.js via Java v26.7".

Let me continue translating...

Introduction section:
"Refreshing a pivot table is rarely a single operation. Behind the scenes, Aspose.Cells maintains a layered data chain that connects your original source data to the rendered values you see in the worksheet. Understanding this chain is the key to choosing the right refresh API for any situation."

"刷新数据透视表很少是单一操作。在后台，Aspose.Cells 维护了一个分层数据链，将您的原始源数据连接到工作表中呈现的值。理解这个数据链是针对任何情况选择正确刷新 API 的关键。"

"The four-layer data chain is:"

"四层数据链是："

"1. **Data Source** — the original worksheet ranges, database query, or consolidation range where the raw values live."
"1. **数据源** — 原始值所在的工作表区域、数据库查询或合并区域。"

"2. **PivotCache** — the in-memory snapshot of the source data. Every pivot table is built on top of a `PivotCache`; this is where all data is gathered and aggregated."
"2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在 `PivotCache` 之上；这是所有数据被收集和聚合的地方。"

"3. **PivotTable** — the view object that defines row, column, value, and filter fields. A `PivotTable` reads *only* from its `PivotCache`, never directly from the data source."
"3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，绝不从数据源直接读取。"

"4. **Cells** — the worksheet `Cells` that the `PivotTable` renders its computed values and styles into."
"4. **单元格** — 数据透视表将其计算值和样式渲染到的工作表 `Cells`。"

"A particularly important concept is the **shared cache**. When multiple pivot tables in a workbook reference the same source range, they share *one* `PivotCache` instance. A single `PivotCache` can be referenced by many pivot tables, and refreshing that cache refreshes every dependent `PivotTable` at once."

"一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用同一源区域时，它们共享*一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存会立即刷新所有依赖的 `PivotTable`。"

Alert block 2:
"`PivotCache.SourceType` (enum `PivotTableSourceType`) indicates where the cache data came from. As of v26.7, `PivotCache.Refresh()` supports only the **`Sheet`** and **`Consolidation`** source types — that is, data that lives in worksheet ranges. External sources (databases, external connections, etc.) are not yet refreshable through the cache API."

"`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型——即驻留在工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。"

"Because of this chain, there are two fundamental refresh paths in Aspose.Cells:"

"由于这种链式结构，Aspose.Cells 中存在两种基本的刷新路径："

"- **`PivotCache.Refresh()`** — reloads source → cache AND recalculates all dependent `PivotTable`s in a single operation."
"- **`PivotCache.Refresh()`** — 重新加载源→缓存，并在单个操作中重新计算所有依赖的 `PivotTable`。"

"- **`PivotTable.CalculateData()`** — recalculates one `PivotTable`'s display from already-cached data, with no round-trip back to the data source."
"- **`PivotTable.CalculateData()`** — 从已缓存的数据重新计算一个 `PivotTable` 的显示，无需往返到数据源。"

"All scenarios in this article use worksheet-cell source data, so the source type is `Sheet` and refresh operations behave as described."

"本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作按所述进行。"

## Required Imports section:

"All JavaScript examples in this article require the Aspose.Cells for Node.js via Java module. The pivot types live in the `Aspose.Cells.Pivot` namespace, which is part of the same module:"

"本文中的所有 JavaScript 示例都需要 Aspose.Cells for Node.js via Java 模块。透视表类型位于 `Aspose.Cells.Pivot` 命名空间中，该命名空间是同一模块的一部分："

"- `const aspose = require('aspose.cells');`"
"- `const aspose = require('aspose.cells');`"

"- Or for specific imports: `const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`"
"- 或者针对特定导入：`const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`"

## Refresh All Pivot Tables section:

"When you need to ensure that every pivot cache and every pivot table in the workbook reflects the latest source data, the simplest and most comprehensive API is `Workbook.RefreshAll()`. A single call traverses the entire workbook — refreshing each `PivotCache` from its source and then recalculating every dependent `PivotTable`. This is the recommended approach for general, full-document refreshes where performance is not a concern."

"当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单、最全面的 API 是 `Workbook.RefreshAll()`。一次调用即可遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于一般性的全文档刷新（不关心性能的情况），这是推荐的方法。"

"The following example builds a workbook with a Fruit/Year/Amount source range, creates one pivot table, modifies some source values, and then uses `RefreshAll()` to bring everything up to date in a single call."

"以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `RefreshAll()` 一次性将所有内容更新到最新状态。"

## Refresh All Pivot Tables on a Single Worksheet section:

"Sometimes you only need to refresh the pivot tables that live on one specific worksheet — for example, when pivot tables on other worksheets are known to be unrelated and shouldn't be touched. For this case, Aspose.Cells provides `Worksheet.RefreshPivotTables()`, which is scoped to a single `Worksheet` instance."

"有时您只需要刷新驻留在某个特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表不相关并且不应被触动时。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其范围限定在单个 `Worksheet` 实例。"

"This is more selective than `Workbook.RefreshAll()`: only the pivot tables on the targeted worksheet are refreshed, leaving any pivot tables on other worksheets untouched."

"这比 `Workbook.RefreshAll()` 更有选择性：仅刷新目标工作表上的数据透视表，而其他工作表上的任何数据透视表均保持不变。"

"The following example populates the same Fruit/Year/Amount source data, adds a pivot table on the first worksheet, modifies some source values, and then refreshes only the pivot tables on that worksheet."

"以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。"

## Refresh a Single Pivot Table section:

"When you want fine-grained control over a single pivot table, the cache-based API gives you two options. The choice between them depends on what actually changed: the underlying source data, or just the view/layout settings of the pivot table itself."

"当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。两者之间的选择取决于实际更改的内容：底层源数据，还是仅仅是数据透视表本身的视图/布局设置。"

### Source Data Changed section:

"If the underlying source data has changed, the right entry point is `pivotTable.PivotCache.Refresh()`. This call re-reads the source data into the cache and then recalculates every `PivotTable` that depends on that cache."

"如果底层源数据已更改，则正确的入口点是 `pivotTable.PivotCache.Refresh()`。此调用将源数据重新读入缓存，然后重新计算依赖于该缓存的每个 `PivotTable`。"

Alert block 3:
"Because pivot tables share a single `PivotCache` instance, calling `PivotCache.Refresh()` recalculates **all** pivot tables built on that same cache — not just the one you reference. If two pivot tables share the same source range, refreshing one cache refreshes both."

"因为数据透视表共享单个 `PivotCache` 实例，所以调用 `PivotCache.Refresh()` 会重新计算构建在该同一缓存上的**所有**数据透视表——而不仅仅是您引用的那一个。如果两个数据透视表共享同一源区域，则刷新一个缓存将同时刷新两者。"

"The following example creates two pivot tables on the same source range to demonstrate this shared-cache behavior, modifies some source values, and then refreshes through one cache reference."

"以下示例在同一源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。"

### Only View/Layout Changed section:

"If the source data has *not* changed but only the pivot table's view or layout settings have been modified (for example, a field has been moved to a different area, or a refresh-on-open setting has been toggled), there is no need to round-trip back to the data source. The cache already holds the right data; only the rendered `PivotTable` needs recalculation. In this case, `pivotTable.CalculateData()` is the right choice."

"如果源数据*未*更改，而仅修改了数据透视表的视图或布局设置（例如，将字段移至不同区域，或切换了打开时刷新设置），则无需往返到数据源。缓存已包含正确的数据；只有渲染的 `PivotTable` 需要重新计算。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。"

"This avoids the unnecessary source fetch and is significantly faster when many pivot tables share the same cache."

"这避免了不必要的源获取，并且当许多数据透视表共享同一缓存时，速度明显更快。"

"The following example modifies a non-source property of the pivot table and then calls `CalculateData()` to re-render it from the existing cache."

"以下示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染它。"

## Get All Pivot Tables Sharing the Same PivotCache section:

"A workbook often contains many pivot tables that all sit on top of one shared cache. To enumerate them — for example, before performing a batch refresh, or to diagnose shared-cache impact — use `PivotCache.GetPivotTables()`. This method returns the collection of every `PivotTable` that depends on the given cache."

"工作簿通常包含许多数据透视表，它们都位于一个共享缓存之上。要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.GetPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。"

"This is also the most direct way to confirm that two pivot tables indeed share the same `PivotCache` instance: you can compare cache references, or simply iterate the collection returned by `GetPivotTables()` and observe which pivot tables appear in it."

"这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或者简单地迭代 `GetPivotTables()` 返回的集合，并观察其中出现了哪些数据透视表。"

"The following example creates two pivot tables on the same source range, verifies that they share the same cache instance, and then enumerates the cache's pivot tables."

"以下示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。"

## Migrating section:

"Prior to Aspose.Cells for Node.js via Java v26.7, the standard way to refresh a pivot table was to call `PivotTable.RefreshData()` on each pivot table individually. As of v26.7, that method is marked **obsolete** and should be replaced with the cache-aware APIs described above."

"在 Aspose.Cells for Node.js via Java v26.7 之前，刷新数据透视表的标准方法是在每个数据透视表上分别调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的缓存感知 API。"

"There are two reasons the per-table `RefreshData()` approach is problematic in real-world workbooks:"

"在现实世界的工作簿中，按表调用 `RefreshData()` 的方法存在两个问题："

"- It re-fetches data from the source *every* time it is called, even when the source has not changed."
"- 每次调用时都会从源*重新*获取数据，即使源未发生更改也是如此。"

"- Each call refreshes the entire shared cache. When many pivot tables share one cache, repeatedly calling `RefreshData()` per pivot table causes the same cache to be re-fetched over and over again, which is very slow."
"- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，针对每个数据透视表重复调用 `RefreshData()` 会导致同一缓存被反复重新获取，这非常慢。"

"The recommended replacements are:"

"推荐的替代方案是："

"- **Refresh ALL pivot tables in the workbook** → use `workbook.refreshAll();`"
"- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`"

"- **Refresh SOME of them** → use `pivotTable.getPivotCache().refresh();` for one cache. Because the cache is shared, this single call updates every pivot table built on top of that cache. Other pivot tables that sit on an already-refreshed cache can be safely skipped."
"- **刷新其中一些** → 对一个缓存使用 `pivotTable.getPivotCache().refresh();`。由于缓存是共享的，此单次调用将更新构建在该缓存之上的每个数据透视表。位于已刷新缓存上的其他数据透视表可以安全地跳过。"

"- **Only the pivot view/layout changed** → use `pivotTable.calculateData();` to re-render from the existing cache without any source round-trip."
"- **仅数据透视表视图/布局已更改** → 使用 `pivotTable.calculateData();` 从现有缓存重新渲染，无需任何源往返。"

"The following example demonstrates the new efficient pattern for workbooks with multiple pivot tables sharing a single cache."

"以下示例演示了针对具有多个共享单个缓存的数据透视表的工作簿的新高效模式。"

## Which Refresh API Should I Use section:

"The table below summarizes the available refresh APIs and when to choose each one."

"下表汇总了可用的刷新 API 以及何时选择每一个。"

Table:
| Goal | Recommended API | Notes |
|------|-----------------|-------|
| Refresh everything in the workbook | `Workbook.RefreshAll()` | One call; covers all caches and tables. |
| Refresh only pivot tables on a single sheet | `Worksheet.RefreshPivotTables()` | Scoped to one worksheet. |
| Source data changed for one cache | `pivotTable.PivotCache.Refresh()` | Refreshes ALL pivot tables on that shared cache. |
| Only view/layout settings changed | `pivotTable.CalculateData()` | Skips unnecessary source round-trip. |
| List all pivot tables on a shared cache | `pivotCache.GetPivotTables()` | Use to enumerate before bulk refresh. |

Translation:
| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定于一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前进行枚举。 |

"In practice, prefer the cache-based APIs over the obsolete per-table `RefreshData()`. They are aware of shared caches, they avoid redundant source fetches, and they let you choose the smallest scope that satisfies your refresh requirement."

"在实践中，应优先选择基于缓存的 API，而不是过时的按表调用 `RefreshData()`。它们能够感知共享缓存，避免冗余的源获取，并允许您选择满足刷新需求的最小范围。"

## Related Articles section:

"- [Inserting an Image into a Cell](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)"
"- [向单元格中插入图片](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)"

"- [Reading and Writing DBF Files](/cells/zh/nodejs-java/dbf/)"
"- [读取和写入 DBF 文件](/cells/zh/nodejs-java/dbf/)"

"- [Splitting Excel Files into Multiple Files](/cells/zh/nodejs-java/splitting-excel-files-into-multiple-files/)"
"- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-java/splitting-excel-files-into-multiple-files/)"

"- [Sparklines in Aspose.Cells for Node.js via Java](/cells/zh/nodejs-java/sparkline/)"
"- [Aspose.Cells for Node.js via Java 中的迷你图](/cells/zh/nodejs-java/sparkline/)"

Note: I need to fix the doubled product name in the last link.

Now let me check that I have all 6 code block placeholders preserved.

Looking at the original:
- ```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新的工作簿
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 将表头行写入单元格 A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 将数据行写入单元格 A2:C9（2020 和 2021 年共 8 行水果数据）
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

// 添加数据透视表：源区域 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中的几个 Amount 值以模拟变化
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的每个数据透视表/透视缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");
```
- ```javascript
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

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```
- ```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据区域为 A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为 Pivot1 分配字段
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据区域 A1:C9
// 由于源数据区域相同，Pivot1 和 Pivot2 共享同一个 PivotCache（透视缓存）。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 单元格的值，以模拟数据变化
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的 PivotCache。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，所以这一行调用
// 会同时刷新两个数据透视表（数据和样式），从更新后的源数据中获取。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");
```
- ```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
```
- ```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");
```
- ```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行数据）---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共用一个底层的 PivotCache（透视缓存）。
// 这正是一个典型的场景：在这种场景下，旧版逐表调用 RefreshData()
// 的方式会变得非常低效——刷新其中一个表会重新获取整个共享缓存，
// 因此刷新 N 个表就会执行 N 次同样昂贵的获取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 已废弃的写法（26.7 版本之前）—— PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // 从源数据重新获取，并刷新整个缓存
// pivotTable2.refreshData();  // 再次重新获取——缓存其实已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表就会产生 N 次冗余的获取操作。

// --- 新版 v26.7+ 写法：只需刷新缓存一次，然后按需重新渲染 ---
// 调用一次 PivotCache.Refresh() 即可将修改后的值拉取到共享缓存中，
// 并重新计算所有引用该缓存的数据透视表的显示结果。
// 由于 Pivot1 和 Pivot2 共用一个 PivotCache，这一次性调用就能
// 同时更新两个表——无需再次回到源数据去拉取。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示
// （数据 + 样式），并不会访问源数据。
// 这里对 Pivot2 调用它纯粹是为了演示该 API：缓存刷新一次之后，
// 任何依赖该缓存的表都可以重新渲染，而无需再次访问源数据。
// 当只有数据透视表的视图/布局设置发生更改、而缓存仍然是最新的
// 情况下，可以单独使用 CalculateData()。
pivotTable2.calculateData();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// 创建一个新的工作簿
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 将表头行写入单元格 A1:C1
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 将数据行写入单元格 A2:C9（2020 和 2021 年共 8 行水果数据）
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

// 添加数据透视表：源区域 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
const pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中的几个 Amount 值以模拟变化
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的每个数据透视表/透视缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");javascript
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

let pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");javascript
const AsposeCells = require("aspose.cells");

// 创建一个新工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨 2020-2021 年）
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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

// 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据区域为 A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为 Pivot1 分配字段
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据区域 A1:C9
// 由于源数据区域相同，Pivot1 和 Pivot2 共享同一个 PivotCache（透视缓存）。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 单元格的值，以模拟数据变化
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的 PivotCache。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，所以这一行调用
// 会同时刷新两个数据透视表（数据和样式），从更新后的源数据中获取。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Sheet1");

worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

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
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

let pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = worksheet.getPivotTables().get(pivot1Index);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = worksheet.getPivotTables().get(pivot2Index);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let sameCache = pivotTable1.getPivotCache() === pivotTable2.getPivotCache();
console.log("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

let sharedPivotTables = pivotTable1.getPivotCache().getPivotTables();
console.log("Number of pivot tables sharing the cache: " + sharedPivotTables.length);

for (let pt of sharedPivotTables) {
    console.log("Pivot table name: " + pt.getName());
}

workbook.save("output.xlsx");javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行数据）---
sheet.getCells().get("A1").putValue("Fruit");
sheet.getCells().get("B1").putValue("Year");
sheet.getCells().get("C1").putValue("Amount");

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000);
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500);
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500);
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000);
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800);
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200);
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700);

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
let idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
let pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共用一个底层的 PivotCache（透视缓存）。
// 这正是一个典型的场景：在这种场景下，旧版逐表调用 RefreshData()
// 的方式会变得非常低效——刷新其中一个表会重新获取整个共享缓存，
// 因此刷新 N 个表就会执行 N 次同样昂贵的获取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // Grape  2020
sheet.getCells().get("C5").putValue(7500);   // Cherry 2020
sheet.getCells().get("C9").putValue(9500);   // Cherry 2021

// --- 已废弃的写法（26.7 版本之前）—— PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // 从源数据重新获取，并刷新整个缓存
// pivotTable2.refreshData();  // 再次重新获取——缓存其实已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表就会产生 N 次冗余的获取操作。

// --- 新版 v26.7+ 写法：只需刷新缓存一次，然后按需重新渲染 ---
// 调用一次 PivotCache.Refresh() 即可将修改后的值拉取到共享缓存中，
// 并重新计算所有引用该缓存的数据透视表的显示结果。
// 由于 Pivot1 和 Pivot2 共用一个 PivotCache，这一次性调用就能
// 同时更新两个表——无需再次回到源数据去拉取。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅根据缓存中已有的数据重新渲染数据透视表的显示
// （数据 + 样式），并不会访问源数据。
// 这里对 Pivot2 调用它纯粹是为了演示该 API：缓存刷新一次之后，
// 任何依赖该缓存的表都可以重新渲染，而无需再次访问源数据。
// 当只有数据透视表的视图/布局设置发生更改、而缓存仍然是最新的
// 情况下，可以单独使用 CalculateData()。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## 应该使用哪个刷新 API？

下表汇总了可用的刷新 API 以及何时选择每一个。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定于一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前进行枚举。 |

在实践中，应优先选择基于缓存的 API，而不是过时的按表调用 `RefreshData()`。它们能够感知共享缓存，避免冗余的源获取，并允许您选择满足刷新需求的最小范围。

## 相关文章

- [向单元格中插入图片](/cells/zh/nodejs-java/inserting-an-image-into-a-cell/)
- [读取和写入 DBF 文件](/cells/zh/nodejs-java/dbf/)
- [将 Excel 文件拆分为多个文件](/cells/zh/nodejs-java/splitting-excel-files-into-multiple-files/)
- [Aspose.Cells for Node.js via Java 中的迷你图](/cells/zh/nodejs-java/sparkline/)

{{< app/cells/assistant language="javascript" >}}