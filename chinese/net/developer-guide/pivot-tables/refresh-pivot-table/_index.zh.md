---
title: 刷新 Aspose.Cells for .NET 中的数据透视表
linktitle: 刷新 Aspose.Cells for .NET 中的数据透视表
description: 学习如何使用 v26.7+ 的数据透视表刷新 API 在 Aspose.Cells for .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附带实用代码示例。
keywords: Aspose.Cells, .NET, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一套分层刷新 API，允许您在四个不同的层级重新加载数据透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for .NET v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已被标记为过时，应替换为本文介绍的更高效的、感知缓存的 API。
{{% /alert %}}
## 简介
刷新数据透视表很少是一个单一的操作。在底层，Aspose.Cells 维护着一个分层的数据链，将您的原始源数据连接到您在工作表中看到的渲染值。理解这个数据链是为任何场景选择正确刷新 API 的关键。
四层数据链如下：
1. **数据源** — 原始工作表区域、数据库查询或合并区域，原始值就存放在这里。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据的收集和聚合都在这里完成。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **Cells** — `PivotTable` 将计算出的值和样式渲染到的工作表 `Cells` 中。
一个特别重要的概念是**共享缓存**。当工作簿中的多个数据透视表引用同一个源区域时，它们共享**一个** `PivotCache` 实例。单个 `PivotCache` 可以被许多数据透视表引用，刷新该缓存即可一次性刷新所有依赖的 `PivotTable`。
{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 两种源类型——即位于工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。
{{% /alert %}}
由于这种链式结构，Aspose.Cells 中存在两条基本的刷新路径：
- **`PivotCache.Refresh()`** — 在一次操作中重新加载源数据到缓存，并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.CalculateData()`** — 仅从已缓存的数据重新计算单个 `PivotTable` 的显示，不会往返访问数据源。
本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作按所述方式执行。
## 必需的 Using 指令
本文中的所有 C# 示例都以以下三个 using 指令开头，因为数据透视类型位于 `Aspose.Cells.Pivot` 命名空间中：
## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿——刷新每个 `PivotCache` 的源数据，然后重新计算每个依赖的 `PivotTable`。在性能不是问题的一般性、全文档刷新场景中，这是推荐的方法。
下面的示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源数据值，然后使用 `RefreshAll()` 通过单次调用将所有内容更新到最新状态。
```csharp
using Aspose.Cells;

Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```
## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表与此无关且不应被触动时。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用范围限定在单个 `Worksheet` 实例内。
这比 `Workbook.RefreshAll()` 更有选择性：只刷新目标工作表上的数据透视表，而其他工作表上的数据透视表保持不变。
下面的示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源数据值，然后仅刷新该工作表上的数据透视表。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建一个新的工作簿
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 将表头行写入单元格 A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 将数据行写入单元格 A2:C9（8 行水果数据，跨 2020 和 2021 年）
worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(50);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(60);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(70);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(80);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(90);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(100);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(110);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(120);

// 添加数据透视表：源区域 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 分配透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改源数据中的若干 Amount 值以模拟更改
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// 刷新工作簿中的所有数据透视表/数据透视缓存
workbook.RefreshAll();

// 保存工作簿
workbook.Save("output.xlsx");
```
## 刷新单个数据透视表
当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际发生变化的内容：底层的源数据，还是仅数据透视表本身的视图/布局设置。
### 源数据已更改 — 使用 `PivotCache.Refresh()`
如果底层源数据已更改，正确的入口是 `pivotTable.PivotCache.Refresh()`。此调用将源数据重新读入缓存，然后重新计算依赖该缓存的每个 `PivotTable`。
{{% alert color="primary" %}}
由于数据透视表共享单个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算**所有**基于该缓存构建的数据透视表——而不仅仅是您引用的那一个。如果两个数据透视表共享同一源区域，刷新其中一个缓存即可同时刷新两者。
{{% /alert %}}
下面的示例在同一源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源数据值，然后通过一个缓存引用进行刷新。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("blueberry");
worksheet.Cells["B3"].PutValue(2021);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("cherry");
worksheet.Cells["B5"].PutValue(2021);
worksheet.Cells["C5"].PutValue(120);

worksheet.Cells["A6"].PutValue("grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(180);

worksheet.Cells["A7"].PutValue("blueberry");
worksheet.Cells["B7"].PutValue(2020);
worksheet.Cells["C7"].PutValue(130);

worksheet.Cells["A8"].PutValue("kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(220);

worksheet.Cells["A9"].PutValue("cherry");
worksheet.Cells["B9"].PutValue(2020);
worksheet.Cells["C9"].PutValue(140);

int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

worksheet.Cells["C2"].PutValue(300);
worksheet.Cells["C5"].PutValue(250);
worksheet.Cells["C9"].PutValue(400);

worksheet.RefreshPivotTables();

workbook.Save("output.xlsx");
```
### 仅视图/布局已更改 — 使用 `CalculateData()`
如果源数据**没有**更改，但仅修改了数据透视表的视图或布局设置（例如，将字段移动到不同的区域，或切换了打开文件时刷新设置），则无需往返访问数据源。缓存已包含正确的数据；只需重新计算渲染后的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。
这避免了不必要的源数据获取，当多个数据透视表共享同一缓存时速度显著提升。
下面的示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染它。
```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建新工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 写入表头行：Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 写入大约 9 行数据（grape / blueberry / kiwi / cherry 横跨 2020-2021）
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

// 添加第一个数据透视表 "Pivot1"，锚定在单元格 E3，源数据范围为 A1:C9
int pivotIndex1 = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivotIndex1];

// 为 Pivot1 分配字段
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据范围 A1:C9
// 由于源数据范围相同，Pivot1 和 Pivot2 共享同一个 PivotCache
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// 为 Pivot2 分配相同的字段
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改源数据中的几个 Amount 单元格值以模拟数据变化
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// 刷新共享的 PivotCache
// 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，这一个调用
// 即可刷新两个数据透视表（数据 + 样式），使其来源于更新后的数据
pivotTable1.PivotCache.Refresh();

// 保存工作簿
workbook.Save("output.xlsx");
```
## 获取共享同一 PivotCache 的所有数据透视表
工作簿中通常包含许多都构建在同一个共享缓存之上的数据透视表。要枚举它们——例如在执行批量刷新之前，或诊断共享缓存的影响——可以使用 `PivotCache.GetPivotTables()`。此方法返回依赖给定缓存的所有 `PivotTable` 的集合。
这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或者简单地遍历 `GetPivotTables()` 返回的集合，观察其中出现了哪些数据透视表。
下面的示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。
```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;

var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// 写入 Fruit / Year / Amount 表头行
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 写入 8 行数据（第 2-9 行，符合源数据范围 A1:C9）
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(150);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(250);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(350);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(450);

// 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改视图/布局属性 —— 这仅是显示上的更改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() 从 PivotCache 中已有的数据重新呈现此数据透视表的显示（数据 + 样式）。因为源数据未发生变化，
// 所以不会执行与源数据的往返 —— 仅将缓存的值重新计算到工作表单元格中。
pivotTable.CalculateData();

// 将工作簿保存到磁盘
workbook.Save("output.xlsx");
```
## 从过时的 `PivotTable.RefreshData()` 迁移
在 Aspose.Cells for .NET v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上述感知缓存的 API。
在真实场景的工作簿中，按表调用的 `RefreshData()` 方法存在两个问题：
- 每次调用都会重新从源获取数据，即使源数据并未发生变化。
- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，对每个数据透视表重复调用 `RefreshData()` 会导致同一个缓存被反复重新获取，这非常慢。
推荐的替代方案为：
- **刷新工作簿中的所有数据透视表** → 使用 `workbook.RefreshAll();`
- **刷新其中部分数据透视表** → 对一个缓存使用 `pivotTable.PivotCache.Refresh();`。由于缓存是共享的，此单次调用将更新基于该缓存构建的所有数据透视表。可以安全地跳过基于已刷新缓存的其他数据透视表。
- **仅数据透视视图/布局已更改** → 使用 `pivotTable.CalculateData();` 从现有缓存重新渲染，无需任何源数据往返。
下面的示例演示了针对多个共享单个缓存的数据透视表工作簿的新的高效模式。

## 应该使用哪种刷新 API？
下表总结了可用的刷新 API 以及每种 API 的适用场景。
| 目标 | 推荐 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定为单个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新前枚举。 |
在实际应用中，应优先使用基于缓存的 API，而非过时的按表 `RefreshData()`。它们能够感知共享缓存、避免冗余的源数据获取，并允许您选择满足刷新需求的最小范围。{{< app/cells/assistant language="csharp" >}}
