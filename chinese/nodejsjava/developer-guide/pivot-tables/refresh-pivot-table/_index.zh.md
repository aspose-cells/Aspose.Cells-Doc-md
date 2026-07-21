---
title: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
linktitle: 在 Aspose.Cells for Node.js via Java 中刷新数据透视表
description: 学习如何使用 v26.7+ 数据透视表刷新 API 在 Aspose.Cells for Node.js via Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附带实用的代码示例。
keywords: Aspose.Cells, Node.js, Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/nodejs-java/refresh-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供了一个分层刷新 API，允许您在四个不同的范围内重新加载透视数据 —— 从整个工作簿到单个数据透视表。从 **Aspose.Cells for Aspose.Cells for Node.js via Java v26.7** 开始，旧版方法 `PivotTable.RefreshData()` 已被标记为过时，应替换为本文中介绍的更高效、支持缓存的 API。

{{% /alert %}}

## 简介

刷新数据透视表通常并不是单一操作。在后台，Aspose.Cells 维护着一个分层数据链，它将您的原始源数据连接到工作表中显示的渲染值。理解此数据链是针对任何情况选择正确刷新 API 的关键。

四层数据链如下：

1. **数据源** —— 原始的工作表区域、数据库查询或合并区域，其中存放原始值。
2. **PivotCache** —— 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据都在此处进行收集和聚合。
3. **PivotTable** —— 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **Cells** —— 工作表的 `Cells`，`PivotTable` 将其计算出的值和样式渲染到其中。

一个特别重要的概念是 **共享缓存**。当工作簿中的多个数据透视表引用相同的源区域时，它们共享**一个** `PivotCache` 实例。单个 `PivotCache` 可以被许多数据透视表引用，刷新该缓存会一次性刷新所有依赖的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.SourceType`（枚举 `PivotTableSourceType`）指示缓存数据的来源。从 v26.7 开始，`PivotCache.Refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型 —— 即位于工作表区域中的数据。外部源（数据库、外部连接等）尚无法通过缓存 API 进行刷新。

{{% /alert %}}

由于存在此数据链，Aspose.Cells 中有两条基本的刷新路径：

- **`PivotCache.Refresh()`** —— 重新加载源 → 缓存，**并**在单次操作中重新计算所有依赖的 `PivotTable`。
- **`PivotTable.CalculateData()`** —— 从已缓存的数据重新计算单个 `PivotTable` 的显示，无需往返访问数据源。

本文中的所有场景均使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作的行为如所述。

## 必需的导入

本文中的所有 JavaScript 示例都需要 Aspose.Cells for Node.js via Java 模块。透视类型位于 `Aspose.Cells.Pivot` 命名空间中，该命名空间是同一模块的一部分：

- `const aspose = require('aspose.cells');`
- 或者对于特定的导入：`const { Workbook, Cells, PivotTableSourceType } = require('aspose.cells');`

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.RefreshAll()`。单次调用将遍历整个工作簿 —— 从每个源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。对于不需要特别考虑性能的一般完整文档刷新，这是推荐的方法。

以下示例构建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源值，然后使用 `RefreshAll()` 通过单次调用将所有内容更新到最新状态。

```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新工作簿
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 将表头行写入 A1:C1 单元格
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 将数据行写入 A2:C9 单元格（跨 2020 和 2021 年的 8 行水果数据）
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

// 修改源数据中的几个 Amount 值以模拟更改
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的所有数据透视表/透视缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表 —— 例如，当已知其他工作表上的数据透视表与此无关且不应被触及时。对于这种情况，Aspose.Cells 提供了 `Worksheet.RefreshPivotTables()`，其作用域限定为单个 `Worksheet` 实例。

这比 `Workbook.RefreshAll()` 更有选择性：仅刷新目标工作表上的数据透视表，其他工作表上的数据透视表保持不变。

以下示例填充相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源值，然后仅刷新该工作表上的数据透视表。

```javascript
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

## 刷新单个数据透视表

当您希望对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际发生变化的内容：底层源数据，还是仅仅是数据透视表本身的视图/布局设置。

### 源数据已更改 —— 使用 `PivotCache.Refresh()`

如果底层源数据已更改，则正确的入口点是 `pivotTable.PivotCache.Refresh()`。此调用会重新将源数据读入缓存，然后重新计算依赖该缓存的每个 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享单个 `PivotCache` 实例，调用 `PivotCache.Refresh()` 会重新计算**所有**基于该缓存构建的数据透视表 —— 而不仅仅是您所引用的那一个。如果两个数据透视表共享相同的源区域，则刷新一个缓存会同时刷新这两张数据透视表。

{{% /alert %}}

以下示例在相同的源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源值，然后通过一个缓存引用进行刷新。

```javascript
const AsposeCells = require("aspose.cells");

// 创建一个新的工作簿并访问第一个工作表
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 数量
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入大约 9 行数据（2020-2021 年的葡萄 / 蓝莓 / 猕猴桃 / 樱桃）
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

// 添加第一个数据透视表 "Pivot1"，锚定在 E3 单元格，源数据范围 A1:C9
const pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
const pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为 Pivot1 分配字段
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 添加第二个数据透视表 "Pivot2"，锚定在 E15，使用相同的源数据范围 A1:C9
// 因为源数据范围相同，Pivot1 和 Pivot2 共享同一个 PivotCache。
const pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
const pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为 Pivot2 分配相同的字段
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改源数据中几个 Amount 单元格的值以模拟数据变化
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的 PivotCache。
// 因为 Pivot1 和 Pivot2 共享同一个 PivotCache，这一次调用
// 会从更新后的源数据刷新两个数据透视表（数据 + 样式）。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");
```

### 仅视图/布局已更改 —— 使用 `CalculateData()`

如果源数据**未**更改，但仅修改了数据透视表的视图或布局设置（例如，将字段移动到不同的区域，或切换了打开文件时刷新的设置），则无需往返访问数据源。缓存已包含正确的数据；只需重新计算渲染的 `PivotTable`。在这种情况下，`pivotTable.CalculateData()` 是正确的选择。

这避免了不必要的源获取，当许多数据透视表共享同一缓存时，速度会显著提高。

以下示例修改数据透视表的非源属性，然后调用 `CalculateData()` 从现有缓存重新渲染它。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 写入 Fruit / Year / Amount 表头行
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入 8 行数据（第 2-9 行，匹配源数据范围 A1:C9）
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

// 添加名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，数据源为 A1:C9
var pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
var pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// 修改视图/布局属性 — 这是仅与显示相关的更改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(false);

// CalculateData() 从 PivotCache 中已持有的数据
// 重新呈现此数据透视表的显示（数据和样式）。由于源数据未更改，
// 不会执行与源数据的往返 — 仅将缓存的值重新计算
// 到工作表单元格中。
pivotTable.calculateData();

// 将工作簿保存到磁盘
workbook.save("output.xlsx");
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿通常包含许多数据透视表，它们都构建在一个共享缓存之上。要枚举它们 —— 例如，在执行批量刷新之前，或诊断共享缓存的影响 —— 请使用 `PivotCache.GetPivotTables()`。此方法返回依赖给定缓存的每个 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用，或者只需迭代 `GetPivotTables()` 返回的集合，观察其中出现了哪些数据透视表。

以下示例在相同的源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。

```javascript
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

## 从已过时的 `PivotTable.RefreshData()` 迁移

在 Aspose.Cells for Aspose.Cells for Node.js via Java v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.RefreshData()`。从 v26.7 开始，该方法被标记为**过时**，应替换为上文所述的支持缓存的 API。

在真实工作簿中，按表调用 `RefreshData()` 方法存在两个问题：

- 每次调用都会从源**重新**获取数据，即使源未发生更改也是如此。
- 每次调用都会刷新整个共享缓存。当许多数据透视表共享一个缓存时，重复地对每个数据透视表调用 `RefreshData()` 会导致同一缓存被反复重新获取，这非常慢。

推荐替换如下：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`
- **刷新其中部分数据透视表** → 对一个缓存使用 `pivotTable.getPivotCache().refresh();`。由于缓存是共享的，此单次调用会更新构建在该缓存之上的每个数据透视表。位于已刷新缓存上的其他数据透视表可以安全地跳过。
- **仅数据透视表视图/布局已更改** → 使用 `pivotTable.calculateData();` 从现有缓存重新渲染，无需任何源往返。

以下示例演示了对于具有共享单个缓存的多个数据透视表的工作簿，新的高效模式。

```javascript
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（表头 + 9 行）---
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

// --- 在同一源数据范围内添加第二个数据透视表（Pivot2）---
// Pivot1 和 Pivot2 共享同一个底层 PivotCache。
// 这正是传统的按表调用 RefreshData() 方法
// 变得低效的场景：刷新一张表会重新获取整个
// 共享缓存，因此刷新 N 张表意味着进行 N 次相同的昂贵获取操作。
let idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
let pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // 葡萄 2020
sheet.getCells().get("C5").putValue(7500);   // 樱桃 2020
sheet.getCells().get("C9").putValue(9500);   // 樱桃 2021

// --- 已过时的模式（26.7 之前）— PivotTable.RefreshData() ---
// pivotTable1.refreshData();  // 从源重新获取数据，刷新整个缓存
// pivotTable2.refreshData();  // 再次重新获取 —— 但缓存已经是最新了！
// 每次调用都会重建共享缓存，因此 N 张表 = N 次冗余获取。

// --- v26.7+ 新模式：只需刷新缓存一次，然后根据需要重新渲染 ---
// 调用一次 PivotCache.Refresh() 会将修改后的值拉取到共享
// 缓存中，并重新计算所有引用它的数据透视表的显示。
// 由于 Pivot1 和 Pivot2 共享一个 PivotCache，这单次调用即可更新
// 两张表 —— 无需再回到源数据进行第二次往返。
pivotTable1.getPivotCache().refresh();

// CalculateData() 仅重新渲染数据透视表的显示（数据 + 样式），
// 数据来自缓存中已有的内容 —— 它不会触及源数据。
// 我们在 Pivot2 上调用它纯粹是为了演示该 API：在缓存
// 被刷新一次之后，任何依赖它的表都可以重新渲染，而无需
// 返回源数据。当仅有数据透视表的视图/布局设置发生变化，
// 且缓存已是最新时，可单独使用 CalculateData()。
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## 应该使用哪个刷新 API？

下表汇总了可用的刷新 API 以及选择每个 API 的适用场景。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.RefreshAll()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.RefreshPivotTables()` | 作用域限定为一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.PivotCache.Refresh()` | 刷新该共享缓存上的**所有**数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.CalculateData()` | 跳过不必要的源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.GetPivotTables()` | 用于在批量刷新之前枚举。 |

在实践中，建议优先使用基于缓存的 API，而非已过时的按表调用 `RefreshData()`。它们支持共享缓存，可避免冗余的源获取，并允许您选择满足刷新需求的最小范围。

{{< app/cells/assistant language="javascript" >}}