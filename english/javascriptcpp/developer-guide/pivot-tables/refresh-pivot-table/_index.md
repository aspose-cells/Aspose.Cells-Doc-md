---
title: Refresh Pivot Tables and Pivot Caches in Aspose.Cells for JavaScript via C++
description: Learn how to refresh pivot tables in Aspose.Cells for JavaScript via C++ using the v26.7+ pivot-refresh API. This article covers workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData, and pivotCache.getPivotTables with practical code examples.
linktitle: Refresh Pivot Tables
keywords: Aspose.Cells, JavaScript via C++, pivot table, refresh, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells provides a layered refresh API that lets you reload pivot data at four different scopes — from the entire workbook down to a single pivot table. Starting with **Aspose.Cells for JavaScript via C++ v26.7**, the legacy method `pivotTable.refreshData()` is marked obsolete and should be replaced with the more efficient, cache-aware APIs described in this article.
{{% /alert %}}

## Introduction
Refreshing a pivot table is rarely a single operation. Behind the scenes, Aspose.Cells maintains a layered data chain that connects your original source data to the rendered values you see in the worksheet. Understanding this chain is the key to choosing the right refresh API for any situation.
The four-layer data chain is:
1. **Data Source** — the original worksheet ranges, database query, or consolidation range where the raw values live.
2. **PivotCache** — the in-memory snapshot of the source data. Every pivot table is built on top of a `PivotCache`; this is where all data is gathered and aggregated.
3. **PivotTable** — the view object that defines row, column, value, and filter fields. A `PivotTable` reads *only* from its `PivotCache`, never directly from the data source.
4. **Cells** — the worksheet cells returned by `getCells()`, where the `PivotTable` renders its computed values and styles.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (enum `PivotTableSourceType`) indicates where the cache data came from. As of v26.7, `pivotCache.refresh()` supports only the **`SHEET`** and **`CONSOLIDATION`** source types — that is, data that lives in worksheet ranges. External sources (databases, external connections, etc.) are not yet refreshable through the cache API.
Because of this chain, there are two fundamental refresh paths in Aspose.Cells:
- **`pivotTable.calculateData()`** — recalculates one `PivotTable`'s display from already-cached data, with no round-trip back to the data source.
All scenarios in this article use worksheet-cell source data, so the source type is `SHEET` and refresh operations behave as described.
{{% /alert %}}

## Quick Start
If you just need the shortest possible code that refreshes every pivot in the workbook, a single call is enough:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Everything else in this article explains when to choose a narrower API instead.

## Required Imports
All JavaScript examples in this article begin with the following module import because the pivot types are exposed through the `Aspose.Cells.Pivot` namespace:
- `const Aspose = require('aspose.cells');`

## Refresh All Pivot Tables in the Workbook
When you need to ensure that every pivot cache and every pivot table in the workbook reflects the latest source data, the simplest and most comprehensive API is `workbook.refreshAll()`. A single call traverses the entire workbook — refreshing each `PivotCache` from its source and then recalculating every dependent `PivotTable`. This is the recommended approach for general, full-document refreshes where performance is not a concern.
The following example builds a workbook with a Fruit/Year/Amount source range, creates one pivot table, modifies some source values, and then uses `refreshAll()` to bring everything up to date in a single call.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // Write header row into cells A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Write data rows into cells A2:C9 (8 rows of fruit data across 2020 and 2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Add a pivot table: source range "A1:C9", destination cell "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // Assign pivot fields: Fruit to Rows, Year to Columns, Amount to Data
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Modify several Amount values in the source data to simulate changes
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Refresh every pivot table / pivot cache in the workbook
            workbook.refreshAll();
            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Refresh All Pivot Tables on a Single Worksheet
Sometimes you only need to refresh the pivot tables that live on one specific worksheet — for example, when pivot tables on other worksheets are known to be unrelated and shouldn't be touched. For this case, Aspose.Cells provides `worksheet.refreshPivotTables()`, which is scoped to a single `Worksheet` instance.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## Refresh a Single Pivot Table
When you want fine-grained control over a single pivot table, the cache-based API gives you two options. The choice between them depends on what actually changed: the underlying source data, or just the view/layout settings of the pivot table itself.

### Source Data Changed — Use `pivotCache.refresh()`
If the underlying source data has changed, the right entry point is `pivotTable.getPivotCache().refresh()`. This call re-reads the source data into the cache and then recalculates every `PivotTable` that depends on that cache.

### Only View/Layout Changed — Use `pivotTable.calculateData()`
If the source data has *not* changed but only the pivot table's view or layout settings have been modified (for example, a field has been moved to a different area, or a refresh-on-open setting has been toggled), there is no need to round-trip back to the data source. The cache already holds the right data; only the rendered `PivotTable` needs recalculation. In this case, `pivotTable.calculateData()` is the right choice.
The following example modifies a non-source property of the pivot table and then calls `calculateData()` to re-render it from the existing cache.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Write Fruit / Year / Amount header row
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // Add a pivot table placed at destination cell E3, sourcing from A1:C9
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // Assign fields: Fruit to Row, Year to Column, Amount to Data
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Modify a view/layout property — this is a presentation-only change,
                // so it does NOT require re-reading the source data through PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData() re-renders THIS pivot table's display (data + style) from the
                // data already held in the PivotCache. Because the source data did not change,
                // no round-trip to the source is performed — only the cached values are recalculated
                // into worksheet cells.
                pivotTable.calculateData();
                // Save the workbook to disk
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

A workbook often contains many pivot tables that all sit on top of one shared cache. To enumerate them — for example, before performing a batch refresh, or to diagnose shared-cache impact — use `pivotCache.getPivotTables()`. This method returns the collection of every `PivotTable` that depends on the given cache.

## Migrating from the Obsolete `pivotTable.refreshData()`
Prior to Aspose.Cells for JavaScript via C++ v26.7, the standard way to refresh a pivot table was to call `pivotTable.refreshData()` on each pivot table individually. As of v26.7, that method is marked **obsolete** and should be replaced with the cache-aware APIs described above.
There are two reasons the per-table `refreshData()` approach is problematic in real-world workbooks:
- It re-fetches data from the source *every* time it is called, even when the source has not changed.
The recommended replacements are:
The following example demonstrates the new efficient pattern for workbooks with multiple pivot tables sharing a single cache.

## Which Refresh API Should I Use?
The table below summarizes the available refresh APIs and when to choose each one.
| Goal | Recommended API | Notes |
|------|-----------------|-------|
| Refresh everything in the workbook | `workbook.refreshAll()` | One call; covers all caches and tables. |
| Refresh only pivot tables on a single sheet | `worksheet.refreshPivotTables()` | Scoped to one worksheet. |
| Source data changed for one cache | `pivotTable.getPivotCache().refresh()` | Refreshes ALL pivot tables on that shared cache. |
| Only view/layout settings changed | `pivotTable.calculateData()` | Skips unnecessary source round-trip. |
| List all pivot tables on a shared cache | `pivotCache.getPivotTables()` | Use to enumerate before bulk refresh. |
In practice, prefer the cache-based APIs over the obsolete per-table `refreshData()`. They are aware of shared caches, they avoid redundant source fetches, and they let you choose the smallest scope that satisfies your refresh requirement.

## Common Pitfalls
- **Forgetting to refresh before saving.** A pivot table only writes its rendered values into the worksheet when its data chain is refreshed. If you modify source cells, call `pivotCache.refresh()` (or `workbook.refreshAll()`) before `workbook.save()`, otherwise the saved file still contains the old aggregated values.
- **Calling the obsolete `refreshData()` per table.** In v26.7, `pivotTable.refreshData()` is marked obsolete and re-fetches the source for every call. With multiple pivot tables sharing a cache this means N redundant source fetches. Replace with a single `pivotCache.refresh()` followed by `pivotTable.calculateData()` per table.
- **Refreshing when only the layout changed.** If you only changed a pivot table's view (column order, `getConsolidationFunction()`, etc.) without touching source data, `pivotCache.refresh()` is unnecessary and slow. Call `pivotTable.calculateData()` to re-render from the existing cache.
- **External source not supported by `pivotCache.refresh()`.** If the pivot table's source comes from an external connection (database, OLAP cube, etc.), `pivotCache.refresh()` cannot refresh it in v26.7 — it currently only supports `SHEET` and `CONSOLIDATION` source types. For external sources, re-open the workbook or rebuild the cache from the source.

{{< app/cells/assistant language="javascript-cpp" >}}