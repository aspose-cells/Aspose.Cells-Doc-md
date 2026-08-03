---
title: 在 Aspose.Cells for Java 中刷新数据透视表和数据透视缓存
linktitle: 刷新数据透视表
description: 学习如何使用 v26.7+ 的数据透视表刷新 API 在 Aspose.Cells for Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并附有实用的代码示例。
keywords: Aspose.Cells, Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells 提供了一个分层级的刷新 API，允许您在四个不同的范围内重新加载透视数据 — 从整个工作簿到单个数据透视表。从 **Aspose.Cells for Java v26.7** 起，旧的方法 `PivotTable.refreshData()` 已被标记为过时，应替换为本文介绍的更高效的、具备缓存感知能力的 API。

{{% /alert %}}

## 简介

刷新数据透视表很少是一个单一的操作。在后台，Aspose.Cells 维护着一个分层的数据链，将您的原始数据源与您在工作表中看到的渲染值连接起来。理解这个数据链是为各种场景选择合适刷新 API 的关键。

四级数据链如下：

1. **数据源（Data Source）** — 原始的工作表区域、数据库查询或合并区域，原始数据存储在此。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据的收集和聚合都在这里完成。
3. **数据透视表（PivotTable）** — 定义行、列、值和筛选字段的视图对象。`PivotTable` *只* 从其 `PivotCache` 读取数据，从不直接从数据源读取。
4. **单元格（Cells）** — `PivotTable` 将其计算后的值和样式渲染到的 `Worksheet` 中的 `Cells`。

一个特别重要的概念是 **共享缓存（shared cache）**。当工作簿中多个数据透视表引用相同的源区域时，它们共享*同一个* `PivotCache` 实例。一个 `PivotCache` 可以被多个数据透视表引用，刷新该缓存将一次性刷新所有依赖的 `PivotTable`。

{{% alert color="primary" %}}

`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。自 v26.7 起，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型 — 即存储在工作表区域中的数据。外部数据源（数据库、外部连接等）尚不能通过缓存 API 进行刷新。

{{% /alert %}}

由于这种数据链的存在，Aspose.Cells 中有两条基本的刷新路径：

- **`PivotCache.refresh()`** — 在一次操作中重新加载源数据到缓存，并重新计算所有依赖的 `PivotTable`。
- **`PivotTable.calculateData()`** — 从已缓存的数据重新计算单个 `PivotTable` 的显示，无需回访数据源。

本文中的所有场景都使用工作表单元格源数据，因此源类型为 `Sheet`，刷新操作的行为如上所述。

## 必需的导入语句

本文中的所有 Java 示例都以以下导入语句开头，因为数据透视表相关的类型位于 `com.aspose.cells.pivot` 包中：

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## 刷新工作簿中的所有数据透视表

当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。一次调用即可遍历整个工作簿 — 从其源刷新每个 `PivotCache`，然后重新计算每个依赖的 `PivotTable`。在对性能没有特殊要求的一般性全文档刷新场景中，这是推荐的方法。

以下示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改一些源数据值，然后使用 `refreshAll()` 在一次调用中将所有内容更新到最新状态。

```java
import com.aspose.cells.*;

// 创建一个新的工作簿
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配透视表字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 修改源数据中若干 Amount 值以模拟数据变化
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);

// 刷新工作簿中的所有数据透视表 / 数据透视表缓存
workbook.refreshAll();

// 保存工作簿
workbook.save("output.xlsx");
```

## 刷新单个工作表上的所有数据透视表

有时您只需要刷新位于特定工作表上的数据透视表 — 例如，当已知其他工作表上的数据透视表与此无关，不应被触动时。针对这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其作用范围限定在单个 `Worksheet` 实例内。

这比 `Workbook.refreshAll()` 更加具有选择性：只有目标工作表上的数据透视表会被刷新，其他工作表上的数据透视表保持不变。

以下示例填充了相同的 Fruit/Year/Amount 源数据，在第一个工作表上添加一个数据透视表，修改一些源数据值，然后仅刷新该工作表上的数据透视表。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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

int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

worksheet.getCells().get("C2").putValue(300);
worksheet.getCells().get("C5").putValue(250);
worksheet.getCells().get("C9").putValue(400);

worksheet.refreshPivotTables();

workbook.save("output.xlsx");
```

## 刷新单个数据透视表

当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两个选项。它们之间的选择取决于实际发生的变化：是底层源数据发生了变化，还是仅仅是数据透视表本身的视图/布局设置发生了变化。

### 源数据已更改 — 使用 `PivotCache.refresh()`

如果底层源数据已更改，则正确的入口点是 `pivotTable.getPivotCache().refresh()`。此调用会将源数据重新读取到缓存中，然后重新计算依赖该缓存的每个 `PivotTable`。

{{% alert color="primary" %}}

由于数据透视表共享同一个 `PivotCache` 实例，调用 `PivotCache.refresh()` 将重新计算构建在该缓存之上的**所有**数据透视表 — 而不仅仅是您引用的那一个。如果两个数据透视表共享同一源区域，刷新其中一个缓存将同时刷新两者。

{{% /alert %}}

以下示例在同一源区域上创建两个数据透视表以演示此共享缓存行为，修改一些源数据值，然后通过一个缓存引用执行刷新。

```java
import com.aspose.cells.*;

// 创建新的工作簿并访问第一个工作表
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 写入表头行：水果 / 年份 / 金额
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 写入约9行数据（葡萄 / 蓝莓 / 猕猴桃 / 樱桃，跨越2020-2021年）
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

// 添加第一个数据透视表"Pivot1"，锚定在E3单元格，数据源区域为A1:C9
int pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = worksheet.getPivotTables().get(pivotIndex1);

// 为Pivot1分配字段
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount");

// 添加第二个数据透视表"Pivot2"，锚定在E15，使用相同的数据源区域A1:C9
// 由于数据源区域相同，Pivot1和Pivot2共享同一个PivotCache。
int pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = worksheet.getPivotTables().get(pivotIndex2);

// 为Pivot2分配相同的字段
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount");

// 修改源数据中的几个"金额"单元格值以模拟数据更改
worksheet.getCells().get("C2").putValue(150);
worksheet.getCells().get("C4").putValue(350);
worksheet.getCells().get("C7").putValue(650);

// 刷新共享的PivotCache。
// 因为Pivot1和Pivot2共享同一个PivotCache，这一调用
// 从更新后的源刷新两个数据透视表（数据 + 样式）。
pivotTable1.getPivotCache().refresh();

// 保存工作簿
workbook.save("output.xlsx");
```

### 仅视图/布局已更改 — 使用 `calculateData()`

如果源数据*没有*更改，而只是数据透视表的视图或布局设置发生了修改（例如，某个字段被移至不同的区域，或者切换了打开文件时刷新的设置），则无需回访数据源。缓存中已包含正确的数据；只需重新计算渲染后的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。

这避免了不必要的数据源获取操作，并且在多个数据透视表共享同一缓存时显著更快。

以下示例修改数据透视表的非源属性，然后调用 `calculateData()` 从现有缓存重新渲染。

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

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

// 添加一个名为 "Pivot1" 的数据透视表，放置在目标单元格 E3，源数据来自 A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// 分配字段：Fruit 到行，Year 到列，Amount 到数据
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// 修改视图/布局属性 -- 这只是显示层面的更改，
// 因此不需要通过 PivotCache.Refresh() 重新读取源数据。
pivotTable.setRefreshDataOnOpeningFile(false);

// calculateData() 从 PivotCache 中已持有的数据
// 重新呈现此数据透视表的显示（数据 + 样式）。因为源数据没有更改，
// 不会执行到源数据的往返 -- 仅将缓存中的值重新计算
// 到工作表单元格中。
pivotTable.calculateData();

// 将工作簿保存到磁盘
workbook.save("output.xlsx");
```

## 获取共享同一 PivotCache 的所有数据透视表

一个工作簿通常包含许多数据透视表，它们都构建在一个共享缓存之上。若要枚举它们 — 例如，在执行批量刷新之前，或诊断共享缓存的影响 — 可使用 `PivotCache.getPivotTables()`。此方法返回依赖于该缓存的每个 `PivotTable` 的集合。

这也是确认两个数据透视表确实共享同一 `PivotCache` 实例的最直接方法：您可以比较缓存引用（使用 `==` 运算符），或者简单地迭代 `getPivotTables()` 返回的集合，观察其中出现了哪些数据透视表。

以下示例在同一源区域上创建两个数据透视表，验证它们共享同一缓存实例，然后枚举该缓存的数据透视表。


## 从过时的 `PivotTable.refreshData()` 迁移

在 Aspose.Cells for Java v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.refreshData()`。自 v26.7 起，该方法被标记为**过时**，应替换为上文介绍的具备缓存感知能力的 API。

在现实世界的工作簿中，按表调用的 `refreshData()` 方法存在两个问题：

- 它*每次*调用时都会从源重新获取数据，即使源数据并未更改。
- 每次调用都会刷新整个共享缓存。当多个数据透视表共享一个缓存时，重复按表调用 `refreshData()` 会导致同一缓存被反复重新获取，速度非常慢。

推荐的替代方案是：

- **刷新工作簿中的所有数据透视表** → 使用 `workbook.refreshAll();`
- **刷新其中的一部分** → 对一个缓存使用 `pivotTable.getPivotCache().refresh();`。由于缓存是共享的，这一次性调用将更新构建在该缓存之上的每个数据透视表。位于已刷新缓存之上的其他数据透视表可以安全地跳过。
- **仅数据透视表的视图/布局发生了变化** → 使用 `pivotTable.calculateData();` 从现有缓存重新渲染，无需任何源数据往返。

以下示例演示了对于多个数据透视表共享同一缓存的工作簿，新的高效模式。

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);

// --- 构建源数据：水果 / 年份 / 金额（标题 + 9 行）---
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
int idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable1 = sheet.getPivotTables().get(idx1);
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount");

// --- 在同一源数据范围上添加第二个数据透视表（Pivot2）---
int idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2");
PivotTable pivotTable2 = sheet.getPivotTables().get(idx2);
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year");
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount");

// --- 修改源数据中的若干 Amount 值 ---
sheet.getCells().get("C2").putValue(5000);   // 葡萄 2020
sheet.getCells().get("C5").putValue(7500);   // 樱桃 2020
sheet.getCells().get("C9").putValue(9500);   // 樱桃 2021

// --- 新版 v26.7+ 模式：刷新缓存一次，然后按需重新渲染 ---
pivotTable1.getPivotCache().refresh();

// 重新渲染第二个数据透视表的视图/布局，不触及源数据
pivotTable2.calculateData();

workbook.save("output.xlsx");
```

## 应该使用哪个刷新 API？

下表汇总了可用的刷新 API 以及每种 API 的适用场景。

| 目标 | 推荐的 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 一次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 限定在单个工作表范围内。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的数据源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前进行枚举。 |

在实际应用中，应优先选择基于缓存的 API，而不是过时的按表 `refreshData()`。它们能够感知共享缓存，避免冗余的数据源获取，并允许您选择满足刷新需求的最小范围。

{{< app/cells/assistant language="java" >}}
