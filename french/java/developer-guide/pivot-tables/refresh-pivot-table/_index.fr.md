---
title: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Java
linktitle: Actualisation des tableaux croisés dynamiques dans Aspose.Cells for Java
description: Apprenez à actualiser les tableaux croisés dynamiques dans Aspose.Cells for Java à l'aide de l'API pivot-refresh de la version 26.7+. Cet article couvre RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData et GetPivotTables avec des exemples de code pratiques.
keywords: Aspose.Cells, Java, tableau croisé dynamique, actualisation, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /fr/java/refresh-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
```
For the body content:

{{% alert color="primary" %}}
Aspose.Cells provides a layered refresh API that lets you reload pivot data at four different scopes — from the entire workbook down to a single pivot table. Starting with **Aspose.Cells for Aspose.Cells for Java v26.7**, the legacy method `PivotTable.refreshData()` is marked obsolete and should be replaced with the more efficient, cache-aware APIs described in this article.
{{% /alert %}}

Translation:
{{% alert color="primary" %}}
Aspose.Cells fournit une API d'actualisation en couches qui vous permet de recharger les données de tableau croisé dynamique à quatre portées différentes — du classeur entier à un seul tableau croisé dynamique. À partir de **Aspose.Cells for Aspose.Cells for Java v26.7**, la méthode héritée `PivotTable.refreshData()` est marquée comme obsolète et doit être remplacée par les API plus efficaces et conscientes du cache décrites dans cet article.
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
`PivotCache.getSourceType()` (enum `PivotTableSourceType`) indicates where the cache data came from. As of v26.7, `PivotCache.refresh()` supports only the **`Sheet`** and **`Consolidation`** source types — that is, data that lives in worksheet ranges. External sources (databases, external connections, etc.) are not yet refreshable through the cache API.
{{% /alert %}}

Because of this chain, there are two fundamental refresh paths in Aspose.Cells:

- **`PivotCache.refresh()`** — reloads source → cache AND recalculates all dependent `PivotTable`s in a single operation.
- **`PivotTable.calculateData()`** — recalculates one `PivotTable`'s display from already-cached data, with no round-trip back to the data source.

All scenarios in this article use worksheet-cell source data, so the source type is `Sheet` and refresh operations behave as described.

## Required Import Statements

All Java examples in this article begin with the following import statements because the pivot types live in the `com.aspose.cells.pivot` package:

- `import java.lang.System;`
- `import com.aspose.cells.Workbook;`
- `import com.aspose.cells.pivot.*;`

## Refresh All Pivot Tables in the Workbook

When you need to ensure that every pivot cache and every pivot table in the workbook reflects the latest source data, the simplest and most comprehensive API is `Workbook.refreshAll()`. A single call traverses the entire workbook — refreshing each `PivotCache` from its source and then recalculating every dependent `PivotTable`. This is the recommended approach for general, full-document refreshes where performance is not a concern.

The following example builds a workbook with a Fruit/Year/Amount source range, creates one pivot table, modifies some source values, and then uses `refreshAll()` to bring everything up to date in a single call.

## Refresh All Pivot Tables on a Single Worksheet

Sometimes you only need to refresh the pivot tables that live on one specific worksheet — for example, when pivot tables on other worksheets are known to be unrelated and shouldn't be touched. For this case, Aspose.Cells provides `Worksheet.refreshPivotTables()`, which is scoped to a single `Worksheet` instance.

This is more selective than `Workbook.refreshAll()`: only the pivot tables on the targeted worksheet are refreshed, leaving any pivot tables on other worksheets untouched.

The following example populates the same Fruit/Year/Amount source data, adds a pivot table on the first worksheet, modifies some source values, and then refreshes only the pivot tables on that worksheet.

## Refresh a Single Pivot Table

When you want fine-grained control over a single pivot table, the cache-based API gives you two options. The choice between them depends on what actually changed: the underlying source data, or just the view/layout settings of the pivot table itself.

### Source Data Changed — Use `PivotCache.refresh()`

If the underlying source data has changed, the right entry point is `pivotTable.getPivotCache().refresh()`. This call re-reads the source data into the cache and then recalculates every `PivotTable` that depends on that cache.

{{% alert color="primary" %}}
Because pivot tables share a single `PivotCache` instance, calling `PivotCache.refresh()` recalculates **all** pivot tables built on that same cache — not just the one you reference. If two pivot tables share the same source range, refreshing one cache refreshes both.
{{% /alert %}}

The following example creates two pivot tables on the same source range to demonstrate this shared-cache behavior, modifies some source values, and then refreshes through one cache reference.

### Only View/Layout Changed — Use `calculateData()`

If the source data has *not* changed but only the pivot table's view or layout settings have been modified (for example, a field has been moved to a different area, or a refresh-on-open setting has been toggled), there is no need to round-trip back to the data source. The cache already holds the right data; only the rendered `PivotTable` needs recalculation. In this case, `pivotTable.calculateData()` is the right choice.

This avoids the unnecessary source fetch and is significantly faster when many pivot tables share the same cache.

The following example modifies a non-source property of the pivot table and then calls `calculateData()` to re-render it from the existing cache.

## Get All Pivot Tables Sharing the Same PivotCache

A workbook often contains many pivot tables that all sit on top of one shared cache. To enumerate them — for example, before performing a batch refresh, or to diagnose shared-cache impact — use `PivotCache.getPivotTables()`. This method returns the collection of every `PivotTable` that depends on the given cache.

This is also the most direct way to confirm that two pivot tables indeed share the same `PivotCache` instance: you can compare cache references (using the `==` operator), or simply iterate the collection returned by `getPivotTables()` and observe which pivot tables appear in it.

The following example creates two pivot tables on the same source range, verifies that they share the same cache instance, and then enumerates the cache's pivot tables.

## Migrating from the Obsolete `PivotTable.refreshData()`

Prior to Aspose.Cells for Aspose.Cells for Java v26.7, the standard way to refresh a pivot table was to call `PivotTable.refreshData()` on each pivot table individually. As of v26.7, that method is marked **obsolete** and should be replaced with the cache-aware APIs described above.

There are two reasons the per-table `refreshData()` approach is problematic in real-world workbooks:

- It re-fetches data from the source *every* time it is called, even when the source has not changed.
- Each call refreshes the entire shared cache. When many pivot tables share one cache, repeatedly calling `refreshData()` per pivot table causes the same cache to be re-fetched over and over again, which is very slow.

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

{{< app/cells/assistant language="java" >}}