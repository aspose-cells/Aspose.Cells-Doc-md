---
title: 在 Aspose.Cells for Java 中刷新数据透视表和数据透视缓存
linktitle: 在 Aspose.Cells for Java 中刷新数据透视表和数据透视缓存
description: 了解如何使用 v26.7+ 数据透视刷新 API 在 Aspose.Cells for Java 中刷新数据透视表。本文涵盖 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并配有实用的代码示例。
keywords: Aspose.Cells, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了一组分层的刷新 API，允许您在四个不同的范围内重新加载数据透视数据 — 从整个工作簿到单个数据透视表。从 **Aspose.Cells for Java v26.7** 开始，旧方法 `PivotTable.refreshData()` 被标记为过时，应替换为本文介绍的更高效、支持缓存的 API。
{{% /alert %}}

## 简介
刷新数据透视表通常不是单一操作。在后台，Aspose.Cells 维护着一个分层的数据链，用于连接您的原始数据源与在工作表中呈现的值。理解该数据链是针对任何场景选择合适刷新 API 的关键。
四层数据链如下：
1. **数据源** — 原始工作表区域、数据库查询或合并区域，用于存放原始值。
2. **PivotCache** — 源数据的内存快照。每个数据透视表都基于一个 `PivotCache` 构建；所有数据的汇集与聚合都在此处完成。
3. **PivotTable** — 定义行、列、值和筛选字段的视图对象。`PivotTable` 仅从其 `PivotCache` 读取数据，而不会直接从数据源读取。
4. **Cells** — 工作表的 `Cells`，`PivotTable` 将计算所得的值和样式渲染到其中。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。自 v26.7 起，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型 — 即位于工作表区域中的数据。外部数据源（数据库、外部连接等）目前还无法通过缓存 API 进行刷新。
{{% /alert %}}

由于这种链式结构，Aspose.Cells 中存在两种基本的刷新路径：
- **`PivotTable.calculateData()`** — 使用已缓存的数据重新计算单个 `PivotTable` 的显示，无需往返数据源。
本文中的所有场景都使用工作表单元格数据作为源数据，因此源类型为 `Sheet`，刷新操作按所述方式运行。

## 快速开始
如果您只需要最短的代码来刷新工作簿中的所有数据透视表，只需一次调用即可：
本文余下部分将说明何时应使用范围更小的 API。

## 必需的导入语句
本文中的所有 Java 示例都以以下导入语句开头，因为数据透视相关类型位于 `com.aspose.cells.pivot` 包中：
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## 刷新工作簿中的所有数据透视表
当您需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新的源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。单次调用即可遍历整个工作簿 — 从每个 `PivotCache` 的数据源刷新数据，然后重新计算所有依赖的 `PivotTable`。在不考虑性能的一般性全文档刷新场景中，推荐使用此方法。
下面的示例构建了一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源值，然后使用 `refreshAll()` 通过单次调用使所有内容保持最新。

## 刷新单个工作表上的所有数据透视表
有时您只需要刷新位于特定工作表上的数据透视表 — 例如，当已知其他工作表上的数据透视表与此无关且不应被触动时。针对此场景，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其作用范围限定为单个 `Worksheet` 实例。

## 刷新单个数据透视表
当您需要对单个数据透视表进行细粒度控制时，基于缓存的 API 为您提供了两种选项。它们之间的选择取决于实际发生变化的内容：底层源数据，还是仅仅是数据透视表本身的视图/布局设置。

### 源数据已更改 — 使用 `PivotCache.refresh()`
如果底层源数据已更改，正确的入口点是 `pivotTable.getPivotCache().refresh()`。此调用会重新将源数据读入缓存，然后重新计算所有依赖该缓存的 `PivotTable`。

### 仅视图/布局已更改 — 使用 `calculateData()`
如果源数据并未发生更改，而仅修改了数据透视表的视图或布局设置（例如，将某个字段移动到不同的区域，或切换了打开时刷新的设置），则无需往返数据源。缓存中已保存正确的数据；只需重新计算呈现后的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。
下面的示例修改了数据透视表的非源数据属性，然后调用 `calculateData()` 从现有缓存中重新渲染它。
一个工作簿中通常包含许多数据透视表，它们都建立在同一个共享缓存之上。要枚举它们 — 例如，在执行批量刷新之前，或诊断共享缓存的影响 — 可以使用 `PivotCache.getPivotTables()`。此方法返回依赖于给定缓存的所有 `PivotTable` 的集合。

## 从过时的 `PivotTable.refreshData()` 迁移
在 Aspose.Cells for Java v26.7 之前，刷新数据透视表的标准方法是对每个数据透视表单独调用 `PivotTable.refreshData()`。自 v26.7 起，该方法被标记为**过时**，应替换为上文介绍的基于缓存的 API。
在真实工作簿中，对每个表调用 `refreshData()` 的方式存在两个问题：
- 它会在每次调用时都从数据源重新获取数据，即使源数据并未更改。
推荐的替代方案如下：
下面的示例演示了针对共享同一缓存的多个数据透视表的工作簿的新高效模式。

## 应使用哪个刷新 API？
下表汇总了可用的刷新 API 以及何时选择每个 API。
| 目标 | 推荐 API | 备注 |
|------|-----------------|-------|
| 刷新工作簿中的所有内容 | `Workbook.refreshAll()` | 单次调用；涵盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 范围限定为一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图/布局设置已更改 | `pivotTable.calculateData()` | 跳过不必要的源数据往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前枚举。 |
在实践中，应优先使用基于缓存的 API，而非过时的逐表 `refreshData()`。它们能够感知共享缓存，可避免冗余的源数据获取，并允许您选择满足刷新需求的最小范围。

## 常见陷阱
- **保存前忘记刷新。** 数据透视表仅在刷新其数据链后才会将呈现后的值写入工作表。如果您修改了源单元格，请在 `Workbook.save()` 之前调用 `PivotCache.Refresh()`（或 `Workbook.RefreshAll()`），否则保存的文件仍将包含旧的聚合值。
- **对每个表调用过时的 `RefreshData()`。** 在 v26.7 中，`PivotTable.RefreshData()` 已被标记为过时，并且每次调用都会重新获取源数据。当多个数据透视表共享一个缓存时，这意味着存在 N 次冗余的源数据获取。请替换为对缓存的一次 `PivotCache.Refresh()`，再对每个表调用 `CalculateData()`。
- **仅布局更改时仍执行刷新。** 如果您仅更改了数据透视表的视图（列顺序、`ConsolidationFunction` 等），而未触及源数据，则 `PivotCache.Refresh()` 是没有必要且较慢的。应调用 `pivotTable.CalculateData()` 以从现有缓存重新渲染。
- **`PivotCache.Refresh()` 不支持外部数据源。** 如果数据透视表的源数据来自外部连接（数据库、OLAP 多维数据集等），则在 v26.7 中 `PivotCache.Refresh()` 无法刷新它 — 目前仅支持 `Sheet` 和 `Consolidation` 源类型。对于外部源，请重新打开工作簿或从源重建缓存。

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table: source range "A1:C9", destination cell "E3", name "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify several Amount values in the source data to simulate changes
worksheet.getCells().get("C2").putValue(55);
worksheet.getCells().get("C5").putValue(85);
worksheet.getCells().get("C9").putValue(125);
// Refresh every pivot table / pivot cache in the workbook
workbook.refreshAll();
// Save the workbook
workbook.save("output.xlsx");
```

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

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table named "Pivot1" placed at destination cell E3, sourcing from A1:C9
int pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign fields: Fruit to Row, Year to Column, Amount to Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Modify a view/layout property -- this is a presentation-only change,
// so it does NOT require re-reading the source data through PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

{{< app/cells/assistant language="java" >}}