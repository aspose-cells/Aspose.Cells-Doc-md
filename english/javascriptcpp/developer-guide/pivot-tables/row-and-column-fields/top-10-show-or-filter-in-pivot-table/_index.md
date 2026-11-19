---
title: Top 10 Show or Filter in Pivot Table
description: Learn how to show only the top or bottom ranked items of a pivot field in Aspose.Cells for JavaScript via C++. This article covers the Excel 97-2003 top10AutoShow method, reading the options back with top10AutoShowSettings, and the Excel 2007-365 Top 10 Filter via filterTop10.
linktitle: Top 10 Show or Filter
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, pivot table, top 10, auto show, top10AutoShow, top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
A pivot table that lists every item of a row field can be hard to read when the field has dozens of members. A Top 10 report keeps only the highest or lowest ranked items, which is exactly what ranking reports need — "top 5 products by revenue" or "bottom 3 regions by sales count". Aspose.Cells supports two mechanisms for this, and they correspond to two generations of Microsoft Excel.
- **Excel 97-2003 AutoShow** — the `PivotField.top10AutoShow()` method. This is the classic "Show the top/bottom N items" setting stored directly on the pivot field. It works in every Excel version, old and new, because it is part of the original pivot table format.
- **Excel 2007-365 Top 10 Filter** — the `PivotField.filterTop10()` method. This is the modern Top 10 value filter found under the field menu's Value Filters. It is stored as a `PivotFilter` object attached to the field and offers item-count and percentage based ranking.

## **Top 10 Show in Excel 97-2003 (top10AutoShow)**
The classic AutoShow is configured with a single call to `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, number count, number rankBy)`:
- `isAutoShow` — enables or disables the AutoShow setting on the field.
- `isTop` — `true` keeps the highest ranked items (Top), `false` keeps the lowest (Bottom).
- `count` — how many items to keep, for example 10 for a classic Top 10 report.
- `rankBy` — the zero-based index of the **data field** whose values rank the items. Pass -1 to rank the items by the field itself.
The ranking can be driven by a value field or by the field itself. Two natural variants exist, shown below.

### **Rank by a Value Field**
Rank the row field's items by an ordinary value field such as Sum of Sales. The following example builds a pivot table with one row field (`Sport`) and one data field (`Sales`), then shows the top 2 sports by sales. `rankBy` is 0 because "Sum of Sales" is the data field at index 0.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Show the top 2 items ranked by "Sum of Sales" (data field index 0)
            sportField.top10AutoShow(true, true, 2, 0);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Rank by the Field Itself**
A field can also be ranked by itself — pass -1 to `rankBy`. No extra data field is needed for this variant; the field only has to sit in the row (or column) area. The following example shows the bottom 3 sports ranked by the field itself. When this setting is saved, the `rankBy` attribute is omitted from the pivot table XML because -1 is the format's default value, and `rankBy` reads -1 back.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Show the bottom 3 items ranked by the field itself (rankBy = -1)
            sportField.top10AutoShow(true, false, 3, -1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Reading the Current AutoShow Options**
The `PivotField.top10AutoShowSettings` property returns a `PivotFieldTop10AutoShowSettings` object that exposes the AutoShow options currently stored on the field. Use it to inspect how an existing workbook, or a pivot table you just configured, will present its items — including workbooks loaded from file.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const settings = sportField.top10AutoShowSettings;
                const autoShowEnabled = settings.isAutoShow;
                const direction = settings.isTop ? "Top" : "Bottom";
                const itemCount = settings.autoShowCount;
                const rankingDataFieldIndex = settings.rankBy;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

The settings map to the classic AutoShow attributes written into the pivot table XML (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), so the values read back are the values every Excel version will honor.

## **Note**

{{% alert color="primary" %}}
- After calling `top10AutoShow()`, call `pivotTable.calculateData()` again — the settings only take effect in the rendered layout on the next recalculation.
- The AutoShow settings work with row and column fields. A field that is only in the page (filter) area cannot be ranked this way because its items are not laid out in the pivot body.
{{% /alert %}}

## **Excel 2007-365: Top 10 Filter (filterTop10)**
Modern Excel versions expose Top 10 as a value filter on the field menu (Value Filters, Top 10...). Aspose.Cells models it with the `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)` method, which returns the created `PivotFilter`:
- `valueFieldIndex` — the zero-based index of the data field whose aggregated values rank the items.
- `type` — what `itemCount` means. `PivotFilterType.Count` keeps a fixed number of items (the dialog's Items option). `PivotFilterType.Percent` keeps a percentage of the items, so `itemCount` is the percentage itself — 30 keeps the top 30 percent. `PivotFilterType.Sum` ranks by cumulative value coverage.
- `isTop` — `true` for Top, `false` for Bottom.
- `itemCount` — the N in Top N; its unit depends on `type`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            });
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Keep the top 3 items ranked by "Sum of Sales" (data field index 0)
            sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 3);
            pivotTable.pivotCache.refresh();
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-filter.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
The AutoShow properties and `filterTop10` are two separate features. AutoShow writes the classic `autoShow` attribute set on the pivot field and is honored by all Excel versions back to Excel 97. `filterTop10` writes a modern `PivotFilter` entry, which requires Excel 2007 or later. When a workbook is opened in an older Excel version, a pivot table that uses the modern filter falls back to showing all items. For documents that must round-trip through legacy tooling, prefer `top10AutoShow`; for modern workbooks, prefer `filterTop10` because it composes with the other value filters.
{{% /alert %}}

## **Related Articles**
- [Group Pivot Fields in the Pivot Table](/cells/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}