---
title: 在 Aspose.Cells for .NET 中刷新数据透视表与数据透视缓存
linktitle: 在 Aspose.Cells for .NET 中刷新数据透视表与数据透视缓存
description: 学习如何使用 v26.7+ 的数据透视表刷新 API 在 Aspose.Cells for .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并配有实用代码示例。
keywords: Aspose.Cells, .NET, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一套分层刷新 API，允许您在四个不同的范围内重新加载数据透视数据——从整个工作簿到单个数据透视表。从 **Aspose.Cells for .NET v26.7** 开始，旧方法 `PivotTable.RefreshData()` 已被标记为过时，应替换为本文中介绍的更高效、支持缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表很少是一个单一操作。在内部，Aspose.Cells 维护着一个分层的数据链，将您的原始源数据连接到工作表中显示的呈现值。理解这个数据链是为任何场景选择合适刷新 API 的关键。
四层数据链如下：
1. **数据源** — 原始工作表区域、数据库查询或合并区域，其中存放着原始数据。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据的收集和聚合都在此处完成。
3. **数据透视表** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，绝不会直接从数据源读取。
4. **单元格** — 工作表 `Cells`，`PivotTable` 将其计算结果和样式呈现到其中。

{{% alert color="primary" %}}
`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型，即位于工作表区域中的数据。外部源（数据库、外部连接等）目前尚无法通过缓存 API 进行刷新。
{{% /alert %}}

由于这种数据链，Aspose.Cells 中存在两种基本的刷新路径：
- **`PivotTable.CalculateData()`** — 从已缓存数据重新计算一个 `PivotTable` 的显示，无需返回数据源。
本文中的所有场景均使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为与所述一致。

## 快速入门
如果您只需要最短的代码来刷新工作簿中的每个数据透视表，一次调用即可：

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

本文的其余部分将解释何时选择范围更窄的 API。

## 必需的 Using 指令
本文中所有 C# 示例都以以下三个 using 指令开头，因为数据透视类型位于 `Aspose.Cells.Pivot` 命名空间中：
- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。一次调用即可遍历整个工作簿——从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于性能不是问题的一般性全文档刷新，这是推荐的方法。
以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `RefreshAll()` 在一次调用中将所有内容更新到最新状态。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// 创建一个新工作簿
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// 将表头行写入单元格 A1:C1
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 将数据行写入单元格 A2:C9（2020 和 2021 年的 8 行水果数据）
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
// 添加数据透视表：源数据范围 "A1:C9"，目标单元格 "E3"，名称 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];
// 分配数据透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 修改源数据中的几个 Amount 值以模拟数据更改
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);
// 刷新工作簿中的所有数据透视表/数据透视缓存
workbook.RefreshAll();
// 保存工作簿
workbook.Save("output.xlsx");
```

## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表——例如，当已知其他工作表上的数据透视表不相关且不应被修改时。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用范围限定于单个 `Worksheet` 实例。

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

## 刷新单个数据透视表
当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 提供了两种选项。两者之间的选择取决于实际更改的内容：是底层源数据，还是仅数据透视表本身的视图/布局设置。

### 源数据已更改 — 使用 `PivotCache.Refresh()`
如果底层源数据已更改，正确的入口点是 `pivotTable.PivotCache.Refresh()`。此调用将源数据重新读取到缓存中，然后重新计算依赖于该缓存的每个 `PivotTable`。

### 仅视图/布局已更改 — 使用 `CalculateData()`
如果源数据*没有*更改，但仅修改了数据透视表的视图或布局设置（例如，字段已移动到其他区域，或切换了打开时刷新设置），则无需返回数据源。缓存已保存正确的数据；只需重新计算呈现的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。
以下示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新呈现它。

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// 写入 Fruit / Year / Amount 表头行
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 写入 8 行数据（第 2-9 行，匹配源数据区域 A1:C9）
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
// 添加名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];
// 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// 修改视图/布局属性——这是仅展示层面的修改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.RefreshDataOnOpeningFile = false;
// CalculateData() 从 PivotCache 中已持有的数据重新渲染此数据透视表的显示（数据 + 样式）。
// 因为源数据未发生变化，
// 不会执行与源数据的往返操作——仅将缓存的值重新计算到工作表单元格中。
pivotTable.CalculateData();
// 将工作簿保存到磁盘
workbook.Save("output.xlsx");
```

一个工作簿通常包含许多数据透视表，它们都构建在一个共享缓存之上。要枚举它们——例如，在执行批量刷新之前，或诊断共享缓存的影响——请使用 `PivotCache.GetPivotTables()`。此方法返回依赖于给定缓存的每个 `PivotTable` 的集合。

## 从过时的 `PivotTable.RefreshData()` 迁移
在 Aspose.Cells for .NET v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文介绍的缓存感知 API。
在现实世界的工作簿中，按表调用 `RefreshData()` 的方法存在两个问题：
- 每次调用时它都会从源重新获取数据，即使源未发生更改。
推荐的替代方案如下：
以下示例演示了对于共享单个缓存的多个数据透视表的工作簿的新高效模式。

## 应该使用哪个刷新 API？
下表总结了可用的刷新 API 以及选择每个 API 的时机。
| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定于单个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 在批量刷新前用于枚举。 |
在实际应用中，应优先使用基于缓存的 API，而不是过时的按表 `RefreshData()`。它们能够感知共享缓存，避免冗余的源获取，并允许您选择满足刷新要求的最小范围。

## 常见陷阱
- **保存前忘记刷新。** 数据透视表仅在其数据链被刷新时才会将其呈现值写入工作表。如果修改了源单元格，请在 `Workbook.Save()` 之前调用 `PivotCache.Refresh()`（或 `Workbook.RefreshAll()`），否则保存的文件仍包含旧的聚合值。
- **对每个表调用过时的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已被标记为过时，并且每次调用都会重新获取源。对于共享缓存的多个数据透视表，这意味着 N 次冗余的源获取。请替换为对 `PivotCache.Refresh()` 的一次调用，然后对每个表调用 `CalculateData()`。
- **仅布局更改时仍进行刷新。** 如果仅更改了数据透视表的视图（列顺序、`ConsolidationFunction` 等）而未修改源数据，则 `PivotCache.Refresh()` 不必要且速度较慢。请调用 `pivotTable.CalculateData()` 从现有缓存重新呈现。
- **`PivotCache.Refresh()` 不支持外部源。** 如果数据透视表的源来自外部连接（数据库、OLAP 多维数据集等），`PivotCache.Refresh()` 在 v26.7 中无法刷新它——它目前仅支持 `Sheet` 和 `Consolidation` 源类型。对于外部源，请重新打开工作簿或从源重建缓存。

{{< app/cells/assistant language="csharp" >}}