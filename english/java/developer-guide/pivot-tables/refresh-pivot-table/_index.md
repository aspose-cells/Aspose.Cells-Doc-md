---
title: Refresh Pivot Tables and Pivot Caches in Aspose.Cells for Java
linktitle: Refresh Pivot Tables
description: Learn how to refresh pivot tables in Aspose.Cells for Java using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
keywords: Aspose.Cells, Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells provides a layered refresh API that lets you reload pivot data at four different scopes — from the entire workbook down to a single pivot table. Starting with **Aspose.Cells for Java v26.7**, the legacy method `PivotTable.refreshData()` is marked obsolete and should be replaced with the more efficient, cache-aware APIs described in this article.

{{% /alert %}}

## Introduction

Refreshing a pivot table is rarely a single operation. Behind the scenes, Aspose.Cells maintains a layered data chain that connects your original source data to the rendered values you see in the worksheet. Understanding this chain is the key to choosing the right refresh API for any situation.

The four-layer data chain is:

1. **Data Source** — the original worksheet ranges, database query, or consolidation range where the raw values live.
2. **PivotCache** — the in-memory snapshot of the source data. Every pivot table is built on top of a `PivotCache`; this is where all data is gathered and aggregated.
3. **PivotTable** — the view object that defines row, column, value, and filter fields. A `PivotTable` reads *only* from its `PivotCache`, never directly from the data source.
4. **Cells** — the worksheet `Cells` that the `PivotTable` renders its computed values and styles into.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indicates where the cache data came from. As of v26.7, `PivotCache.refresh()` supports only the **`Sheet`** and **`Consolidation`** source types — that is, data that lives in worksheet ranges. External sources (databases, external connections, etc.) are not yet refreshable through the cache API.

{{% /alert %}}

Because of this chain, there are two fundamental refresh paths in Aspose.Cells:

- **`PivotCache.refresh()`** — reloads source → cache AND recalculates all dependent `PivotTable`s in a single operation.
- **`PivotTable.calculateData()`** — recalculates one `PivotTable`'s display from already-cached data, with no round-trip back to the data source.

All scenarios in this article use worksheet-cell source data, so the source type is `Sheet` and refresh operations behave as described.

## Quick Start

If you just need the shortest possible code that refreshes every pivot in the workbook, a single call is enough:

```csharp
using Aspose.Cells;

Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

Everything else in this article explains when to choose a narrower API instead.

## Required Import Statements

All Java examples in this article begin with the following import statements because the pivot types live in the `com.aspose.cells.pivot` package:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook

When you need to ensure that every pivot cache and every pivot table in the workbook reflects the latest source data, the simplest and most comprehensive API is `Workbook.refreshAll()`. A single call traverses the entire workbook — refreshing each `PivotCache` from its source and then recalculating every dependent `PivotTable`. This is the recommended approach for general, full-document refreshes where performance is not a concern.

The following example builds a workbook with a Fruit/Year/Amount source range, creates one pivot table, modifies some source values, and then uses `refreshAll()` to bring everything up to date in a single call.

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

Sometimes you only need to refresh the pivot tables that live on one specific worksheet — for example, when pivot tables on other worksheets are known to be unrelated and shouldn't be touched. For this case, Aspose.Cells provides `Worksheet.refreshPivotTables()`, which is scoped to a single `Worksheet` instance.

This is more selective than `Workbook.refreshAll()`: only the pivot tables on the targeted worksheet are refreshed, leaving any pivot tables on other worksheets untouched.

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

When you want fine-grained control over a single pivot table, the cache-based API gives you two options. The choice between them depends on what actually changed: the underlying source data, or just the view/layout settings of the pivot table itself.

### Source Data Changed — Use `PivotCache.refresh()`

If the underlying source data has changed, the right entry point is `pivotTable.getPivotCache().refresh()`. This call re-reads the source data into the cache and then recalculates every `PivotTable` that depends on that cache.

{{% alert color="primary" %}}

{{% /alert %}}

### Only View/Layout Changed — Use `calculateData()`

If the source data has *not* changed but only the pivot table's view or layout settings have been modified (for example, a field has been moved to a different area, or a refresh-on-open setting has been toggled), there is no need to round-trip back to the data source. The cache already holds the right data; only the rendered `PivotTable` needs recalculation. In this case, `pivotTable.calculateData()` is the right choice.

The following example modifies a non-source property of the pivot table and then calls `calculateData()` to re-render it from the existing cache.

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

A workbook often contains many pivot tables that all sit on top of one shared cache. To enumerate them — for example, before performing a batch refresh, or to diagnose shared-cache impact — use `PivotCache.getPivotTables()`. This method returns the collection of every `PivotTable` that depends on the given cache.

## Migrating from the Obsolete `PivotTable.refreshData()`

Prior to Aspose.Cells for Java v26.7, the standard way to refresh a pivot table was to call `PivotTable.refreshData()` on each pivot table individually. As of v26.7, that method is marked **obsolete** and should be replaced with the cache-aware APIs described above.

There are two reasons the per-table `refreshData()` approach is problematic in real-world workbooks:

- It re-fetches data from the source *every* time it is called, even when the source has not changed.

The recommended replacements are:

- **Refresh ALL pivot tables in the workbook** → use `workbook.refreshAll();`
- **Refresh SOME of them** → use `pivotTable.getPivotCache().refresh();` for one cache. Because the cache is shared, this single call updates every pivot table built on top of that cache. Other pivot tables that sit on an already-refreshed cache can be safely skipped.
- **Only the pivot view/layout changed** → use `pivotTable.calculateData();` to re-render from the existing cache without any source round-trip.

The following example demonstrates the new efficient pattern for workbooks with multiple pivot tables sharing a single cache.


## Which Refresh API Should I Use?

The table below summarizes the available refresh APIs and when to choose each one.

| Goal | Recommended API | Notes |
|------|-----------------|-------|
| Refresh everything in the workbook | `Workbook.refreshAll()` | One call; covers all caches and tables. |
| Refresh only pivot tables on a single sheet | `Worksheet.refreshPivotTables()` | Scoped to one worksheet. |
| Source data changed for one cache | `pivotTable.getPivotCache().refresh()` | Refreshes ALL pivot tables on that shared cache. |
| Only view/layout settings changed | `pivotTable.calculateData()` | Skips unnecessary source round-trip. |
| List all pivot tables on a shared cache | `pivotCache.getPivotTables()` | Use to enumerate before bulk refresh. |

In practice, prefer the cache-based APIs over the obsolete per-table `refreshData()`. They are aware of shared caches, they avoid redundant source fetches, and they let you choose the smallest scope that satisfies your refresh requirement.



## Common Pitfalls

- **Forgetting to refresh before saving.** A pivot table only writes its rendered values into the worksheet when its data chain is refreshed. If you modify source cells, call `PivotCache.Refresh()` (or `Workbook.RefreshAll()`) before `Workbook.Save()`, otherwise the saved file still contains the old aggregated values.
- **Calling the obsolete `RefreshData()` per table.** In v26.7, `PivotTable.RefreshData()` is marked obsolete and re-fetches the source for every call. With multiple pivot tables sharing a cache this means N redundant source fetches. Replace with a single `PivotCache.Refresh()` followed by `CalculateData()` per table.
- **Refreshing when only the layout changed.** If you only changed a pivot table's view (column order, `ConsolidationFunction`, etc.) without touching source data, `PivotCache.Refresh()` is unnecessary and slow. Call `pivotTable.CalculateData()` to re-render from the existing cache.
- **External source not supported by `PivotCache.Refresh()`.** If the pivot table's source comes from an external connection (database, OLAP cube, etc.), `PivotCache.Refresh()` cannot refresh it in v26.7 — it currently only supports `Sheet` and `Consolidation` source types. For external sources, re-open the workbook or rebuild the cache from the source.

{{< app/cells/assistant language="java" >}}
