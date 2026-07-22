---
title: 在 Aspose.Cells for .NET 中刷新数据透视表
linktitle: 数据透视表刷新
description: 了解如何使用 v26.7+ 的 pivot-refresh API 在 Aspose.Cells for .NET 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并提供实用的代码示例。
keywords: Aspose.Cells, .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/net/refresh-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一个分层刷新 API，允许您在四个不同的范围内重新加载透视数据 —— 从整个工作簿到单个数据透视表。从 **Aspose.Cells for .NET v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已标记为过时，应替换为本文描述的更高效、支持缓存感知的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是单一操作。在后台，Aspose.Cells 维护着一个分层的数据链，将您的原始源数据连接到工作表中呈现的值。理解这个数据链是选择适合各种场景的正确刷新 API 的关键。

四层数据链如下：

1. **数据源（Data Source）** —— 原始工作表区域、数据库查询或合并区域，原始数据存储在这些位置。
2. **PivotCache** —— 源数据在内存中的快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据的收集和聚合都在此处完成。
3. **数据透视表（PivotTable）** —— 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **单元格（Cells）** —— `PivotTable` 将其计算值和样式渲染到的工作表 `Cells`。

一个特别重要的概念是**共享缓存（shared cache）**。当工作簿中的多个数据透视表引用同一源区域时，它们共享**同一个** `PivotCache` 实例。单个 `PivotCache` 可以被许多数据透视表引用，刷新该缓存即可一次性刷新所有依赖的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型 —— 即存储在工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。

{{% /alert %}}

由于这个数据链的存在，Aspose.Cells 中有两条基本的刷新路径：

- **`PivotCache.Refresh()`** —— 在一次操作中重新加载源 → 缓存并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.CalculateData()`** —— 从已缓存的数据重新计算单个 `PivotTable` 的显示，不往返于数据源。

本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作按所述方式运行。

## 必需的 Using 指令

本文中的所有 C# 示例都以下列三个 using 指令开头，因为透视类型位于 `Aspose.Cells.Pivot` 命名空间中：

- `using System;`
- `using Aspose.Cells;`
- `using Aspose.Cells.Pivot;`

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。单次调用即可遍历整个工作簿 —— 刷新每个 `PivotCache` 的源数据，然后重新计算每个依赖的 `PivotTable`。在性能不是问题的情况下，对于一般的完整文档刷新，这是推荐的方法。

以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `RefreshAll()` 通过单次调用使所有内容保持最新。

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

// 将数据行写入单元格 A2:C9（涵盖 2020 和 2021 年的 8 行水果数据）
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

// 添加数据透视表：数据源区域为 "A1:C9"，目标单元格为 "E3"，名称为 "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// 分配数据透视字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改源数据中的几个 Amount 值以模拟数据变化
worksheet.Cells["C2"].PutValue(55);
worksheet.Cells["C5"].PutValue(85);
worksheet.Cells["C9"].PutValue(125);

// 刷新工作簿中的所有数据透视表/数据透视缓存
workbook.RefreshAll();

// 保存工作簿
workbook.Save("output.xlsx");
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表 —— 例如，当已知其他工作表上的数据透视表与此无关且不应被刷新时。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其范围限定在单个 `Worksheet` 实例内。

这比 `Workbook.RefreshAll()` 更有针对性：只有目标工作表上的数据透视表会被刷新，其他工作表上的数据透视表保持不变。

以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。

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

当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际更改的内容：是底层源数据，还是仅数据透视表本身的视图/布局设置。

### 源数据已更改 —— 使用 `PivotCache.Refresh()`

如果底层源数据已更改，正确的入口点是 `pivotTable.PivotCache.Refresh()`。此调用将源数据重新读取到缓存中，然后重新计算依赖该缓存的每个 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享单个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算构建在同一缓存上的**所有**数据透视表 —— 而不仅仅是您引用的那一个。如果两个数据透视表共享同一源区域，刷新一个缓存会同时刷新两者。

{{% /alert %}}

以下示例在同一源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建新工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// 写入表头行：水果 / 年份 / 金额
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 写入约 9 行数据（2020-2021 年的葡萄 / 蓝莓 / 猕猴桃 / 樱桃）
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
// 由于源数据范围相同，Pivot1 和 Pivot2 共享同一个 PivotCache。
int pivotIndex2 = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivotIndex2];

// 为 Pivot2 分配相同的字段
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改源数据中的几个金额单元格值以模拟数据变化
worksheet.Cells["C2"].PutValue(150);
worksheet.Cells["C4"].PutValue(350);
worksheet.Cells["C7"].PutValue(650);

// 刷新共享的 PivotCache。
// 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，这单次调用
// 会从更新后的源数据刷新两个数据透视表（数据 + 样式）。
pivotTable1.PivotCache.Refresh();

// 保存工作簿
workbook.Save("output.xlsx");
```

### 仅视图/布局已更改 —— 使用 `CalculateData()`

如果源数据**未**更改，但仅修改了数据透视表的视图或布局设置（例如，将字段移动到不同区域，或切换了打开时刷新设置），则无需往返于数据源。缓存已包含正确的数据；只需重新计算渲染后的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。

这避免了不必要的源获取操作，当许多数据透视表共享同一缓存时，速度显著更快。

以下示例修改数据透视表的非源属性，然后调用 `CalculateData()` 以从现有缓存重新渲染它。

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

// 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，源数据来自 A1:C9
int pivotIndex = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.PivotTables[pivotIndex];

// 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// 修改视图/布局属性——这只是显示上的更改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.RefreshDataOnOpeningFile = false;

// CalculateData() 重新渲染此数据透视表的显示（数据 + 样式），
// 数据来自 PivotCache 中已保存的数据。因为源数据没有更改，
// 所以不会执行到源数据的往返操作——只是将缓存中的值重新计算
// 到工作表单元格中。
pivotTable.CalculateData();

// 将工作簿保存到磁盘
workbook.Save("output.xlsx");
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿通常包含许多都构建在同一个共享缓存之上的数据透视表。要枚举它们 —— 例如在执行批量刷新之前，或诊断共享缓存的影响 —— 请使用 `PivotCache.GetPivotTables()`。此方法返回依赖给定缓存的每个 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或者简单地迭代 `GetPivotTables()` 返回的集合，观察其中出现的数据透视表。

以下示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Sheet1";

worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

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

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

int pivot1Index = worksheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.PivotTables[pivot1Index];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

int pivot2Index = worksheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.PivotTables[pivot2Index];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

bool sameCache = object.ReferenceEquals(pivotTable1.PivotCache, pivotTable2.PivotCache);
Console.WriteLine("Pivot1 and Pivot2 share the same PivotCache: " + sameCache);

PivotTable[] sharedPivotTables = pivotTable1.PivotCache.GetPivotTables();
Console.WriteLine("Number of pivot tables sharing the cache: " + sharedPivotTables.Length);

foreach (PivotTable pt in sharedPivotTables)
{
    Console.WriteLine("Pivot table name: " + pt.Name);
}

workbook.Save("output.xlsx");
```

## 从过时的 `PivotTable.RefreshData()` 进行迁移

在 Aspose.Cells for .NET v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法已标记为**过时（obsolete）**，应替换为上述支持缓存感知的 API。

在真实工作簿中，按表调用 `RefreshData()` 的方法存在两个问题：

- 每次调用时都会从源重新获取数据，即使源未更改也是如此。
- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，重复按数据透视表调用 `RefreshData()` 会导致同一缓存被反复重新获取，速度非常慢。

推荐的替代方案是：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.RefreshAll();`
- **刷新其中部分** → 使用 `pivotTable.PivotCache.Refresh();` 刷新一个缓存。由于缓存是共享的，此单次调用会更新构建在该缓存之上的每个数据透视表。可以安全地跳过位于已刷新缓存上的其他数据透视表。
- **仅数据透视视图/布局已更改** → 使用 `pivotTable.CalculateData();` 从现有缓存重新渲染，无需往返于源。

以下示例演示了对于共享单个缓存的多个数据透视表工作簿的新高效模式。

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// 创建一个新工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// --- 构建源数据：水果/年份/金额（表头 + 9 行）---
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

sheet.Cells["A2"].PutValue("Grape");      sheet.Cells["B2"].PutValue(2020); sheet.Cells["C2"].PutValue(1000);
sheet.Cells["A3"].PutValue("Blueberry");  sheet.Cells["B3"].PutValue(2020); sheet.Cells["C3"].PutValue(2000);
sheet.Cells["A4"].PutValue("Kiwi");       sheet.Cells["B4"].PutValue(2020); sheet.Cells["C4"].PutValue(1500);
sheet.Cells["A5"].PutValue("Cherry");     sheet.Cells["B5"].PutValue(2020); sheet.Cells["C5"].PutValue(2500);
sheet.Cells["A6"].PutValue("Grape");      sheet.Cells["B6"].PutValue(2021); sheet.Cells["C6"].PutValue(3000);
sheet.Cells["A7"].PutValue("Blueberry");  sheet.Cells["B7"].PutValue(2021); sheet.Cells["C7"].PutValue(1800);
sheet.Cells["A8"].PutValue("Kiwi");       sheet.Cells["B8"].PutValue(2021); sheet.Cells["C8"].PutValue(2200);
sheet.Cells["A9"].PutValue("Cherry");     sheet.Cells["B9"].PutValue(2021); sheet.Cells["C9"].PutValue(2700);

// --- 在目标单元格 E3 处添加第一个数据透视表（Pivot1）---
int idx1 = sheet.PivotTables.Add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.PivotTables[idx1];
pivotTable1.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- 在同一个源数据范围上添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共享同一个底层 PivotCache。
// 这正是旧版逐表调用 RefreshData()
// 方法变得低效的场景：刷新一个表会重新获取整个
// 共享缓存，因此刷新 N 个表会导致 N 次相同的高开销获取。
int idx2 = sheet.PivotTables.Add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.PivotTables[idx2];
pivotTable2.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.AddFieldToArea(PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.Cells["C2"].PutValue(5000);   // 葡萄 2020
sheet.Cells["C5"].PutValue(7500);   // 樱桃 2020
sheet.Cells["C9"].PutValue(9500);   // 樱桃 2021

// --- 已过时的模式（26.7 之前）— PivotTable.RefreshData() ---
// pivotTable1.RefreshData();  // 从源重新获取数据，刷新整个缓存
// pivotTable2.RefreshData();  // 再次重新获取数据 — 缓存已经是新的了！
// 每次调用都会重建共享缓存，因此 N 个表 = N 次冗余获取。

// --- 新的 v26.7+ 模式：刷新缓存一次，然后根据需要重新渲染 ---
// 一次 PivotCache.Refresh() 调用会将修改后的值提取到共享
// 缓存中，并重新计算引用该缓存的每个数据透视表的显示。
// 由于 Pivot1 和 Pivot2 共享同一个 PivotCache，这一个调用就能更新
// 两个表 — 无需再次访问源数据。
pivotTable1.PivotCache.Refresh();

// CalculateData() 仅从缓存中已有的数据重新渲染数据透视表的显示（数据 + 样式），
// 它不会访问源数据。我们在这里对 Pivot2 调用它纯粹是为了演示 API：在缓存
// 被刷新一次后，任何依赖该缓存的表都可以重新渲染，而无需
// 重新访问源数据。仅当数据透视表的视图/布局设置发生更改
// 而缓存为最新时，可单独使用 CalculateData()。
pivotTable2.CalculateData();

workbook.Save("output.xlsx");
```

## 我应该使用哪个刷新 API？

下表总结了可用的刷新 API 以及何时选择每个 API。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 单次调用；涵盖所有缓存和数据透视表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 范围限定在单个工作表内。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 在批量刷新前用于枚举。 |

实际上，应优先使用基于缓存的 API，而非过时的按表调用 `RefreshData()`。它们支持共享缓存感知，可避免冗余的源获取，并允许您选择满足刷新需求的最小范围。

{{< app/cells/assistant language="csharp" >}}