---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for JavaScript via C++ 支持全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选、前 10 项筛选，以及通过隐藏或取消隐藏数据透视项来筛选数据透视表中的数据。
keywords: Aspose.Cells, JavaScript via C++ 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供五种实用的策略，用于筛选数据透视表中显示的数据。您可以对基于文本的行或列字段应用标签筛选，在字段仅包含日期时间单元格或空白值时使用日期筛选，对聚合数值应用值筛选，使用前 10 项筛选按值字段进行排名，或使用 `isHidden` 属性手动隐藏和取消隐藏单个数据透视项。每种策略均通过 `PivotField` 和 `PivotItem` 类中的专用 API 实现。
{{% /alert %}}

## **简介**
数据透视表是功能强大的分析工具，但原始汇总通常包含远超实际展示需求的信息。筛选是将数据透视表缩减至特定报告所需行、列或值的主要方式。Aspose.Cells for JavaScript via C++ 提供与 Microsoft Excel 一致的筛选功能，并通过编程方式开放这些功能，从而实现报告生成的全自动化。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行或列字段中的数据透视项。
2. **日期筛选** — 筛选仅包含日期时间值（或空白值）的行或列字段。
3. **值筛选** — 根据数据字段的聚合值筛选数据透视项。
4. **前 10 项筛选** — 仅显示按值字段排名的前 N 个或后 N 个数据透视项。
5. **隐藏/取消隐藏数据透视项** — 手动控制字段中每个数据透视项的可见性。
每种方法均使用 `PivotField` 类中的相应方法或 `PivotItem` 类中的相应属性。应用任何筛选后，必须在数据透视表上调用 `pivotCache.refresh()`，使缓存数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选允许您根据文本标题与指定模式的匹配结果，筛选行或列字段中的数据透视项。当您希望仅显示名称以特定字母开头、包含特定单词或满足其他基于标题的条件的产品时，此功能非常有用。
Aspose.Cells 通过 `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` 方法提供标签筛选功能。`filterType` 参数用于选择比较模式（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等）。`label1` 和 `label2` 参数用于指定比较文本；当只需匹配单个值（例如开头匹配或包含匹配）时，请为 `label2` 传入 `""`。
以下示例加载一个包含现有数据透视表的工作簿，应用标签筛选，仅保留标题以指定前缀开头的数据透视项，刷新数据透视表并保存结果。

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **日期筛选**
日期筛选可按今天、上周、本月、下一季度或特定日期区间等基于日期的条件筛选数据透视表。它们是仅适用于存储日期时间信息的字段的专用筛选器。

{{% alert color="primary" %}}
日期筛选仅在行区域或列区域仅包含日期时间单元格或空白值时有效。如果基础字段包含数字或文本等其他数据类型，日期筛选将不会产生预期结果。应用此筛选器之前，请确保字段的格式设置为日期，并且所有值均为有效的 `DateTime` 实例或空单元格。
Aspose.Cells 通过 `pivotField.filterByDate(PivotFilterType, DateTime[] values)` 方法提供日期筛选功能。`PivotFilterType` 枚举包含专用的日期筛选值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选的筛选器类型，传入一个或两个 `DateTime` 值（对于 `Between`，传入开始日期和结束日期）。
以下示例加载一个工作簿，其中数据透视表的行区域包含日期字段；随后应用日期筛选，将可见数据透视项限定在特定日期区间内，刷新数据透视表并保存工作簿。
{{% /alert %}}

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
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **值筛选**
值筛选用于处理数据透视表在数据区域中计算的聚合值。它不匹配文本标签，而是将数值汇总值与阈值进行比较。典型的使用场景包括仅显示销售额总和超过目标金额的产品，或仅显示交易次数位于某一值区间内的地区。
Aspose.Cells 通过 `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` 方法提供值筛选功能。`valueFieldIndex` 参数指定要对其求值的数据字段（使用 `pivotTable.getDataFields().indexOf(dataField)` 或遍历该集合以确定其位置）。`filterType` 参数可取 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。两个 `double` 参数用于指定一个或两个阈值。
以下示例加载一个包含数据透视表的工作簿，应用值筛选，仅保留聚合销售额超过数值阈值的数据透视项，刷新数据透视表并保存工作簿。

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
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **前 10 项筛选**
前 10 项筛选是值筛选的一种特殊形式，根据所选值字段仅保留排名最高或最低的 N 个数据透视项。它通常用于生成排名报表，例如“按收入排名前 10 的产品”或“按销售量排名后 5 的地区”。

{{% alert color="primary" %}}
前 10 项筛选仅在数据透视表的数据区域中包含一个或多个值数据透视字段时才有效。如果不存在至少一个值字段，就没有可用于对数据透视项进行排名的聚合度量，也无法应用此筛选器。
Aspose.Cells 通过 `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` 方法提供前 10 项筛选功能。`valueFieldIndex` 参数是用于根据聚合值对数据透视项进行排名的数据字段索引；`filterType` 用于选择 `itemCount` 的计量单位（`Count` 保留固定数量的数据透视项，`Percent` 保留数据透视项的指定百分比，此时 `itemCount` 本身即为百分比）；`isTop` 指定保留排名靠前的数据透视项（true）或排名靠后的数据透视项（false）；`itemCount` 则指定要保留的数据透视项数量或百分比。
以下示例加载一个包含数据透视表的工作簿，其中数据透视表含有值字段；随后应用前 10 项筛选，仅保留按销售总额排名前 10 的数据透视项，刷新数据透视表并保存工作簿。
{{% /alert %}}

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
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **通过隐藏或取消隐藏数据透视项进行筛选**
除结构化筛选 API 外，Aspose.Cells 还允许您直接控制每个数据透视项的可见性。通过遍历 `PivotField` 的 `pivotField.getPivotItems()` 集合并切换 `isHidden` 属性，您可以有针对性地隐藏特定数据透视项，而无需使用基于公式的筛选器。设置 `pivotItem.isHidden = true` 会从数据透视表中隐藏该数据透视项；设置 `pivotItem.isHidden = false` 会取消隐藏该数据透视项，使其再次可见。
当筛选规则不规则或需要针对特定数据透视项分别处理时，此方法非常适合。例如，可以隐藏特定报告中不应出现的少量命名类别。以下示例加载一个数据透视表，按名称隐藏特定数据透视项，演示如何取消隐藏该数据透视项，刷新数据透视表并保存工作簿。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **总结**
Aspose.Cells for JavaScript via C++ 提供了一套完整的数据透视表筛选功能，与 Microsoft Excel 中的相应功能相匹配。标签、日期和值筛选涵盖最常见的分析场景，而前 10 项筛选用于处理排名报表。当筛选规则不规则时，`pivotItem.isHidden` 属性提供了一种按数据透视项控制的灵活备用方法。组合使用这些策略——例如先应用标签筛选，再隐藏特定数据透视项——可以完全通过代码生成精准定制的数据透视表报表。

{{< app/cells/assistant language="javascript-cpp" >}}