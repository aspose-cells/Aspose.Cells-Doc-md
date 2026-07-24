---
title: Refreshing Pivot Tables in Aspose.Cells for Python via Java
description: Learn how to refresh pivot tables in Aspose.Cells for Python via Java using the v26.7+ pivot-refresh API. This article covers RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData, and GetPivotTables with practical code examples.
keywords: Aspose.Cells, Python via Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /python-java/refresh-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells provides a layered refresh API that lets you reload pivot data at four different scopes — from the entire workbook down to a single pivot table. Starting with **Aspose.Cells for Aspose.Cells for Python via Java v26.7**, the legacy method `PivotTable.refreshData()` is marked obsolete and should be replaced with the more efficient, cache-aware APIs described in this article.

{{% /alert %}}

## Introduction

Refreshing a pivot table is rarely a single operation. Behind the scenes, Aspose.Cells maintains a layered data chain that connects your original source data to the rendered values you see in the worksheet. Understanding this chain is the key to choosing the right refresh API for any situation.

The four-layer data chain is:

1. **Data Source** — the original worksheet ranges, database query, or consolidation range where the raw values live.
2. **PivotCache** — the in-memory snapshot of the source data. Every pivot table is built on top of a `PivotCache`; this is where all data is gathered and aggregated.
3. **PivotTable** — the view object that defines row, column, value, and filter fields. A `PivotTable` reads *only* from its `PivotCache`, never directly from the data source.
4. **Cells** — the worksheet `Cells` that the `PivotTable` renders its computed values and styles into.

A particularly important concept is the **shared cache**. When multiple pivot tables in a workbook reference the same source range, they share *one* `PivotCache` instance. A single `PivotCache` can be referenced by many pivot tables, and refreshing that cache refreshes every dependent `PivotTable` at once.

{{% alert color="primary" %}}

`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indicates where the cache data came from. As of v26.7, `PivotCache.refresh()` supports only the **`SHEET`** and **`CONSOLIDATION`** source types — that is, data that lives in worksheet ranges. External sources (databases, external connections, etc.) are not yet refreshable through the cache API.

{{% /alert %}}

Because of this chain, there are two fundamental refresh paths in Aspose.Cells:

- **`PivotCache.refresh()`** — reloads source → cache AND recalculates all dependent `PivotTable`s in a single operation.
- **`PivotTable.calculateData()`** — recalculates one `PivotTable`'s display from already-cached data, with no round-trip back to the data source.

All scenarios in this article use worksheet-cell source data, so the source type is `SHEET` and refresh operations behave as described.

## Required Imports

All Python examples in this article rely on the following imports because the pivot types live in the `aspose.cells.pivot` namespace:

- `import jpype`
- `import aspose.cells as cells`

The `jpype` module is used to bootstrap the JVM, while `aspose.cells` exposes the workbook/worksheet/cell/pivot types used throughout.

## Refresh All Pivot Tables in the Workbook

When you need to ensure that every pivot cache and every pivot table in the workbook reflects the latest source data, the simplest and most comprehensive API is `Workbook.refreshAll()`. A single call traverses the entire workbook — refreshing each `PivotCache` from its source and then recalculating every dependent `PivotTable`. This is the recommended approach for general, full-document refreshes where performance is not a concern.

The following example builds a workbook with a Fruit/Year/Amount source range, creates one pivot table, modifies some source values, and then uses `refreshAll()` to bring everything up to date in a single call.

<!-- CODE_BLOCK:0:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a header row Fruit/Year/Amount into cells A1:C1 using worksheet.getCells().get("A1").put_value("Fruit") and similar calls for "Year" and "Amount"; writes approximately 9 data rows containing fruits (grape, blueberry, kiwi, cherry) across years 2020 and 2021 with corresponding Amount values into cells A2:C10; adds a pivot table via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1") where the first string is the source range, the second is the destination cell, and the third is the pivot table name; assigns fields using addFieldToArea(cells.pivot.PivotFieldType.ROW, "Fruit"), addFieldToArea(cells.pivot.PivotFieldType.COLUMN, "Year"), and addFieldToArea(cells.pivot.PivotFieldType.DATA, "Amount"); modifies several Amount cell values in the source data to simulate changes; calls workbook.refreshAll() to refresh every pivot cache and pivot table in the workbook; calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

## Refresh All Pivot Tables on a Single Worksheet

Sometimes you only need to refresh the pivot tables that live on one specific worksheet — for example, when pivot tables on other worksheets are known to be unrelated and shouldn't be touched. For this case, Aspose.Cells provides `Worksheet.refreshPivotTables()`, which is scoped to a single `Worksheet` instance.

This is more selective than `Workbook.refreshAll()`: only the pivot tables on the targeted worksheet are refreshed, leaving any pivot tables on other worksheets untouched.

The following example populates the same Fruit/Year/Amount source data, adds a pivot table on the first worksheet, modifies some source values, and then refreshes only the pivot tables on that worksheet.

<!-- CODE_BLOCK:1:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a Fruit/Year/Amount header row into A1:C1 and approximately 9 data rows containing fruits (grape, blueberry, kiwi, cherry) across years 2020 and 2021 with Amount values into A2:C10; adds a pivot table via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1"); assigns Fruit to the Row area, Year to the Column area, and Amount to the Data area; modifies several Amount cell values in the source data; gets a reference to the worksheet and calls worksheet.refreshPivotTables() to refresh only that worksheet's pivot tables; calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

## Refresh a Single Pivot Table

When you want fine-grained control over a single pivot table, the cache-based API gives you two options. The choice between them depends on what actually changed: the underlying source data, or just the view/layout settings of the pivot table itself.

### Source Data Changed — Use `PivotCache.refresh()`

If the underlying source data has changed, the right entry point is `pivotTable.getPivotCache().refresh()`. This call re-reads the source data into the cache and then recalculates every `PivotTable` that depends on that cache.

{{% alert color="primary" %}}

Because pivot tables share a single `PivotCache` instance, calling `PivotCache.refresh()` recalculates **all** pivot tables built on that same cache — not just the one you reference. If two pivot tables share the same source range, refreshing one cache refreshes both.

{{% /alert %}}

The following example creates two pivot tables on the same source range to demonstrate this shared-cache behavior, modifies some source values, and then refreshes through one cache reference.

<!-- CODE_BLOCK:2:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a Fruit/Year/Amount header row into A1:C1 and approximately 9 data rows into A2:C10; adds the first pivot table named Pivot1 at destination cell E3 via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1"); assigns Fruit to the Row area, Year to the Column area, and Amount to the Data area; adds a second pivot table named Pivot2 at destination cell E15 via worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2") using the same source range A1:C9 to demonstrate the shared-cache scenario; assigns the same Fruit/Year/Amount fields to Pivot2; modifies several Amount cell values in the source data; calls pivotTable1.getPivotCache().refresh(); the code should include a brief comment noting that this single call refreshes BOTH pivot tables because they share the same PivotCache; calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

### Only View/Layout Changed — Use `calculateData()`

If the source data has *not* changed but only the pivot table's view or layout settings have been modified (for example, a field has been moved to a different area, or a refresh-on-open setting has been toggled), there is no need to round-trip back to the data source. The cache already holds the right data; only the rendered `PivotTable` needs recalculation. In this case, `pivotTable.calculateData()` is the right choice.

This avoids the unnecessary source fetch and is significantly faster when many pivot tables share the same cache.

The following example modifies a non-source property of the pivot table and then calls `calculateData()` to re-render it from the existing cache.

<!-- CODE_BLOCK:3:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a Fruit/Year/Amount header row into A1:C1 and approximately 9 data rows into A2:C10; adds a pivot table named Pivot1 at destination cell E3 via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1"); assigns Fruit to the Row area, Year to the Column area, and Amount to the Data area; modifies a view/layout property of the pivot table that does NOT require a source refresh (such as setting pivotTable.setRefreshDataOnOpeningFile(False) or moving a field to a different area); calls pivotTable.calculateData() to re-render the pivot table from the existing cache; the code should include a brief comment explaining that no source round-trip occurred; calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

## Get All Pivot Tables Sharing the Same PivotCache

A workbook often contains many pivot tables that all sit on top of one shared cache. To enumerate them — for example, before performing a batch refresh, or to diagnose shared-cache impact — use `PivotCache.getPivotTables()`. This method returns the collection of every `PivotTable` that depends on the given cache.

This is also the most direct way to confirm that two pivot tables indeed share the same `PivotCache` instance: you can compare cache references, or simply iterate the collection returned by `getPivotTables()` and observe which pivot tables appear in it.

The following example creates two pivot tables on the same source range, verifies that they share the same cache instance, and then enumerates the cache's pivot tables.

<!-- CODE_BLOCK:4:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a Fruit/Year/Amount header row into A1:C1 and approximately 9 data rows into A2:C10; adds the first pivot table named Pivot1 at destination cell E3 via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1"); assigns Fruit to the Row area, Year to the Column area, and Amount to the Data area; adds a second pivot table named Pivot2 at destination cell E15 via worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2") using the same source range; assigns the same Fruit/Year/Amount fields to Pivot2; demonstrates shared-cache equality by printing that pivotTable1.getPivotCache() is pivotTable2.getPivotCache() (object identity comparison); calls pivotTable1.getPivotCache().getPivotTables() to retrieve the collection of pivot tables sharing this cache; iterates the returned collection and demonstrates that it contains BOTH Pivot1 and Pivot2 (for example, by printing each pivot table's name); calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

## Migrating from the Obsolete `PivotTable.refreshData()`

Prior to Aspose.Cells for Aspose.Cells for Python via Java v26.7, the standard way to refresh a pivot table was to call `PivotTable.refreshData()` on each pivot table individually. As of v26.7, that method is marked **obsolete** and should be replaced with the cache-aware APIs described above.

There are two reasons the per-table `refreshData()` approach is problematic in real-world workbooks:

- It re-fetches data from the source *every* time it is called, even when the source has not changed.
- Each call refreshes the entire shared cache. When many pivot tables share one cache, repeatedly calling `refreshData()` per pivot table causes the same cache to be re-fetched over and over again, which is very slow.

The recommended replacements are:

- **Refresh ALL pivot tables in the workbook** → use `workbook.refreshAll();`
- **Refresh SOME of them** → use `pivotTable.getPivotCache().refresh();` for one cache. Because the cache is shared, this single call updates every pivot table built on top of that cache. Other pivot tables that sit on an already-refreshed cache can be safely skipped.
- **Only the pivot view/layout changed** → use `pivotTable.calculateData();` to re-render from the existing cache without any source round-trip.

The following example demonstrates the new efficient pattern for workbooks with multiple pivot tables sharing a single cache.

<!-- CODE_BLOCK:5:A complete, self-contained Python script that uses Aspose.Cells for Python via Java; begins with the imports import jpype and import aspose.cells as cells; bootstraps the JVM via jpype.startJVM(); creates a new Workbook via cells.Workbook(); gets workbook.getWorksheets().get(0); writes a Fruit/Year/Amount header row into A1:C1 and approximately 9 data rows into A2:C10; adds the first pivot table named Pivot1 at destination cell E3 via worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1"); assigns Fruit to the Row area, Year to the Column area, and Amount to the Data area; adds a second pivot table named Pivot2 at destination cell E15 via worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2") using the same source range; assigns the same Fruit/Year/Amount fields to Pivot2 to simulate the many-tables-share-one-cache scenario; modifies several Amount cell values in the source data; demonstrates the efficient v26.7+ pattern by calling pivotTable1.getPivotCache().refresh() once (which refreshes both shared-cache tables because they share the same PivotCache) and then calling pivotTable2.calculateData() to show that the second table can be re-rendered from the already-updated cache without re-fetching from source; the code should include comments contrasting the new pattern with the obsolete per-table refreshData() approach and explaining why only one cache refresh is needed; calls workbook.save("output.xlsx"); the code must run against Aspose.Cells for Python via Java 26.7.0 -->

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

## Related Articles

- [Inserting an Image into a Cell](/cells/python-java/inserting-an-image-into-a-cell/)
- [Reading and Writing DBF Files](/cells/python-java/dbf/)
- [Splitting Excel Files into Multiple Files](/cells/python-java/splitting-excel-files-into-multiple-files/)
- [Sparklines in Aspose.Cells for Aspose.Cells for Python via Java](/cells/python-java/sparkline/)

{{< app/cells/assistant language="python" >}}