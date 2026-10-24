---
title: 刷新 Aspose.Cells for Java 中的数据透视表和数据透视缓存
linktitle: 刷新 Aspose.Cells for Java 中的数据透视表和数据透视缓存
description: 了解如何使用 v26.7+ 数据透视表刷新 API 刷新 Aspose.Cells for Java 中的数据透视表。本文介绍 RefreshAll、RefreshPivotTables、PivotCache.Refresh、CalculateData 和 GetPivotTables，并提供实用的代码示例。
keywords: Aspose.Cells, Java, 数据透视表, 刷新, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /zh/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供分层刷新 API，可让你在四个不同层级重新加载数据透视数据，范围从整个工作簿到单个数据透视表。自 **Aspose.Cells for Java v26.7** 起，旧版方法 `PivotTable.refreshData()` 已标记为过时，应替换为本文介绍的更高效且基于缓存的 API。
{{% /alert %}}

## Introduction
刷新数据透视表很少只涉及一个操作。在幕后，Aspose.Cells 维护着一个分层数据链，将原始源数据与工作表中呈现的值连接起来。理解此数据链，是针对各种情况选择合适刷新 API 的关键。
四层数据链如下：
1. **数据源**——保存原始值的原始工作表区域、数据库查询或合并区域。
2. **`PivotCache`**——源数据的内存快照。每个数据透视表都构建在一个 `PivotCache` 之上；所有数据都在此汇总并进行聚合。
3. **`PivotTable`**——定义行字段、列字段、值字段和筛选字段的视图对象。`PivotTable` *仅*从其 `PivotCache` 读取数据，绝不直接从数据源读取。
4. **`Cells`**——工作表中的 `Cells` 集合，`PivotTable` 会将计算后的值和样式呈现到其中。

{{% alert color="primary" %}}
`PivotCache.getSourceType()`（枚举 `PivotTableSourceType`）指示缓存数据的来源。截至 v26.7，`PivotCache.refresh()` 仅支持 **`Sheet`** 和 **`Consolidation`** 源类型，即位于工作表区域中的数据。外部数据源（数据库、外部连接等）尚无法通过缓存 API 刷新。
由于存在此数据链，Aspose.Cells 中有两种基本刷新路径：
- **`PivotTable.calculateData()`**——根据已缓存的数据重新计算一个 `PivotTable` 的显示结果，无需往返数据源。
本文中的所有场景都使用工作表单元格作为源数据，因此源类型为 `Sheet`，刷新操作的行为与上述说明一致。
{{% /alert %}}

## Quick Start
如果只需使用尽可能短的代码刷新工作簿中的每个数据透视表，一次调用即可完成：

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("input.xlsx");
workbook.refreshAll();
workbook.save("output.xlsx");
```

本文其余内容将说明何时应改用范围更窄的 API。

## Required Import Statements
本文中的所有 Java 示例都以下列导入语句开头，因为数据透视类型位于 `com.aspose.cells.pivot` 包中：
- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook
当需要确保工作簿中的每个数据透视缓存和每个数据透视表都反映最新源数据时，最简单且最全面的 API 是 `Workbook.refreshAll()`。一次调用即可遍历整个工作簿，从源数据刷新每个 `PivotCache`，然后重新计算所有依赖这些缓存的 `PivotTable`。对于不特别关注性能的一般整文档刷新，推荐使用此方法。
以下示例创建一个包含 Fruit/Year/Amount 源区域的工作簿，创建一个数据透视表，修改部分源值，然后通过一次 `refreshAll()` 调用使所有内容保持最新。

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

## Refresh All Pivot Tables on a Single Worksheet
有时只需刷新位于特定工作表上的数据透视表，例如其他工作表上的数据透视表已知与当前任务无关，不应被修改。对于这种情况，Aspose.Cells 提供了 `Worksheet.refreshPivotTables()`，其作用范围限定为单个 `Worksheet` 实例。

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

## Refresh a Single Pivot Table
如果需要精细控制单个数据透视表，基于缓存的 API 提供了两种选择。具体选择取决于实际发生变化的内容：底层源数据，还是数据透视表自身的视图或布局设置。

### Source Data Changed — Use `PivotCache.refresh()`
如果底层源数据已更改，正确的入口点是 `pivotTable.getPivotCache().refresh()`。此调用会将源数据重新读取到缓存中，然后重新计算所有依赖该缓存的 `PivotTable`。

### Only View/Layout Changed — Use `calculateData()`
如果源数据*未*发生更改，而只是修改了数据透视表的视图或布局设置，例如将字段移至其他区域，或者切换“打开时刷新”设置，则无需往返数据源。缓存中已经包含正确的数据，只需重新计算呈现出来的 `PivotTable`。在这种情况下，`pivotTable.calculateData()` 是正确的选择。
以下示例修改数据透视表的非源属性，然后调用 `calculateData()`，根据现有缓存重新呈现数据透视表。

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
// so it does NOT require re-reading the source data through PivotCache.refresh().
pivotTable.setRefreshDataOnOpeningFile(false);
// calculateData() re-renders THIS pivot table's display (data + style) from the
// data already held in the PivotCache. Because the source data did not change,
// no round-trip to the source is performed -- only the cached values are recalculated
// into worksheet cells.
pivotTable.calculateData();
// Save the workbook to disk
workbook.save("output.xlsx");
```

一个工作簿通常包含多个数据透视表，而这些数据透视表都基于同一个共享缓存构建。如果需要枚举它们，例如在执行批量刷新之前，或者诊断共享缓存造成的影响，请使用 `PivotCache.getPivotTables()`。此方法返回所有依赖给定缓存的 `PivotTable` 集合。

## Migrating from the Obsolete `PivotTable.refreshData()`
在 Aspose.Cells for Java v26.7 之前，刷新数据透视表的标准方式是对每个数据透视表分别调用 `PivotTable.refreshData()`。自 v26.7 起，该方法已标记为**过时**，应替换为上述基于缓存的 API。
在实际工作簿中，按表调用 `refreshData()` 的方式存在两个问题：
- 即使源数据未发生更改，每次调用时它也会重新从数据源获取数据。
推荐的替代方案如下：
以下示例演示了多个数据透视表共享单个缓存时的新高效模式。

## Which Refresh API Should I Use?
下表汇总了可用的刷新 API，以及每种 API 的适用场景。
| 目标 | 推荐的 API | 说明 |
|------|-----------------|-------|
| 刷新工作簿中的全部内容 | `Workbook.refreshAll()` | 一次调用即可覆盖所有缓存和表。 |
| 仅刷新单个工作表上的数据透视表 | `Worksheet.refreshPivotTables()` | 作用范围限定为一个工作表。 |
| 一个缓存的源数据已更改 | `pivotTable.getPivotCache().refresh()` | 刷新该共享缓存上的所有数据透视表。 |
| 仅视图或布局设置发生更改 | `pivotTable.calculateData()` | 跳过不必要的数据源往返。 |
| 列出共享缓存上的所有数据透视表 | `pivotCache.getPivotTables()` | 用于在批量刷新前进行枚举。 |
在实际应用中，应优先使用基于缓存的 API，而不是已弃用的按表 `refreshData()`。这些 API 能够识别共享缓存，避免重复获取源数据，并允许选择满足刷新需求的最小范围。

## Common Pitfalls
- **忘记在保存前刷新。** 只有刷新数据透视表的数据链后，数据透视表才会将呈现的值写入工作表。如果修改了源单元格，请在 `Workbook.save()` 之前调用 `PivotCache.refresh()`（或 `Workbook.refreshAll()`），否则保存的文件仍包含旧的聚合值。
- **对每个表调用已弃用的 `refreshData()`。** 在 v26.7 中，`PivotTable.refreshData()` 已标记为过时，并且每次调用都会重新获取源数据。如果多个数据透视表共享一个缓存，这意味着会进行 N 次多余的源数据获取。请改用一次 `PivotCache.refresh()` 来刷新共享缓存；仅当视图或布局发生变化时，才按表调用 `calculateData()`。
- **仅布局发生更改时仍执行刷新。** 如果只修改了数据透视表的视图，例如列顺序、`ConsolidationFunction` 等，而未修改源数据，则无需调用 `PivotCache.refresh()`，否则会拖慢速度。请调用 `pivotTable.calculateData()`，根据现有缓存重新呈现数据透视表。
- **`PivotCache.refresh()` 不支持外部数据源。** 如果数据透视表的源来自外部连接（数据库、OLAP 多维数据集等），则在 v26.7 中 `PivotCache.refresh()` 无法刷新它，目前该方法仅支持 `Sheet` 和 `Consolidation` 源类型。对于外部数据源，请重新打开工作簿或根据源数据重建缓存。

{{< app/cells/assistant language="java" >}}