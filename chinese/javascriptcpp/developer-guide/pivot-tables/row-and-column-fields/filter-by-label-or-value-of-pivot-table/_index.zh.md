---
title: 按标签或值筛选数据透视表
linktitle: 按标签或值筛选数据透视表
description: Aspose.Cells for JavaScript via C++ 提供全面的数据透视表筛选功能。本文介绍如何使用标签筛选、日期筛选、值筛选和前 10 项筛选对数据透视表数据进行筛选，以及如何通过隐藏或取消隐藏数据透视项来控制显示内容。
keywords: Aspose.Cells, JavaScript via C++ 库, 电子表格, 数据透视表, 筛选, 标签筛选, 值筛选, 日期筛选, 前 10 项筛选, 数据透视项, 隐藏数据透视项
type: docs
weight: 10
url: /zh/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供五种实用的筛选策略，用于筛选数据透视表中显示的数据。您可以对基于文本的行字段或列字段应用标签筛选；当字段仅包含日期时间单元格或空白值时使用日期筛选；针对汇总数值应用值筛选；使用前 10 项筛选，依据值字段对项目进行排名；或者使用 `isHidden` 属性手动隐藏和取消隐藏单个数据透视项。每种策略均由 `PivotField` 和 `PivotItem` 类上的专用 API 实现。
{{% /alert %}}

## **简介**
数据透视表是强大的分析工具，但原始汇总数据通常包含远超实际展示需求的信息。筛选是将数据透视表缩减至特定报告所需行、列或值的主要机制。Aspose.Cells for JavaScript via C++ 通过 API 提供与 Microsoft Excel 相同的筛选功能，从而支持完全自动化的报告生成。
本文涵盖以下筛选策略：
1. **标签筛选** — 根据文本标签筛选行字段或列字段中的项目。
2. **日期筛选** — 筛选仅包含日期时间值（或空白值）的行字段或列字段。
3. **值筛选** — 根据数据字段的汇总值筛选项目。
4. **前 10 项筛选** — 仅显示按值字段排名的前 N 项或后 N 项。
5. **隐藏/取消隐藏数据透视项** — 手动控制字段中每个数据透视项的可见性。
每种筛选方式均使用 `PivotField` 类上的不同方法，或使用 `PivotItem` 类上的属性。应用任一筛选后，必须在数据透视表上调用 `pivotCache.refresh()`，以便缓存数据和计算值反映新的筛选状态。

## **标签筛选**
标签筛选允许您通过将文本标签与模式进行比较来筛选行字段或列字段中的项目。当您只想显示名称以特定字母开头、包含特定单词或符合其他基于标签条件的项目时，此功能非常有用。
Aspose.Cells 通过 `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` 方法提供标签筛选功能。`filterType` 参数用于选择比较模式（`CaptionBeginsWith`、`CaptionContains`、`CaptionEndsWith`、`CaptionDoesNotContain`、`CaptionIsNotBlank`、`CaptionIsBlank` 等）。`label1` 和 `label2` 参数提供比较文本；当您只需使用单个比较值时（例如“开头为”或“包含”），为 `label2` 传入 `""`。
以下示例加载包含现有数据透视表的工作簿，应用标签筛选，使仅标签以指定前缀开头的项目可见，刷新数据透视表并保存结果。

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
                    // 加载包含数据透视表的现有工作簿
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // 通过索引访问工作表（第一个工作表）
                    const worksheet = workbook.worksheets.get(0);
                    // 通过索引访问数据透视表
                    const pivotTable = worksheet.pivotTables.get(0);
                    // 获取第一个行 PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // 应用标签筛选器——仅显示标签以指定前缀开头的行项
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // 刷新并重新计算数据透视表数据，使筛选器生效
                    pivotTable.refreshData();
                    // 将工作簿保存回磁盘
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
日期筛选允许您按今天、上周、本月、下个季度或特定日期区间等日期条件筛选数据透视表。此类筛选仅适用于存储日期时间信息的字段。

{{% alert color="primary" %}}
仅当行区域或列区域只包含日期时间单元格或空白值时，日期筛选才会生效。如果底层字段包含数字或文本等其他数据类型，日期筛选将不会产生预期结果。在应用此筛选之前，请确保该字段已设置为日期格式，且所有值均为有效的 `DateTime` 实例或空单元格。
Aspose.Cells 通过 `pivotField.filterByDate(PivotFilterType, DateTime[] values)` 方法提供日期筛选功能。`PivotFilterType` 枚举包含日期筛选专用的枚举值，例如 `Today`、`Yesterday`、`LastWeek`、`ThisWeek`、`NextWeek`、`LastMonth`、`ThisMonth`、`NextMonth`、`LastQuarter`、`ThisQuarter`、`NextQuarter`、`LastYear`、`ThisYear`、`NextYear` 和 `Between`。根据所选筛选类型，传入一个或两个 `DateTime` 值（对于 `Between`，传入开始日期和结束日期）。
以下示例加载包含数据透视表的工作簿（其行区域包含日期字段），应用日期筛选以将可见项目限制在特定日期区间内，然后刷新数据透视表并保存工作簿。
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
                // 加载包含数据透视表的现有工作簿
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // 按索引访问包含数据透视表的工作表
                const worksheet = workbook.worksheets.get(0);
                // 按索引访问数据透视表
                const pivotTable = worksheet.pivotTables.get(0);
                // 从行区域获取日期透视字段
                //（日期筛选仅在行/列区域仅包含日期时间单元格或空白单元格时有效）
                const dateField = pivotTable.rowFields.get(0);
                // 定义“介于”筛选条件的日期范围
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // 在透视字段上应用日期筛选
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // 刷新并重新计算数据透视表，使筛选生效
                pivotTable.refreshData();
                // 保存工作簿
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
值筛选基于数据透视表在数据区域中计算的汇总值工作。与匹配文本标签不同，值筛选会将数值总计与阈值进行比较。典型用例包括仅显示销售总额超过目标金额的产品，或仅显示交易次数落在某个区间内的区域。
Aspose.Cells 通过 `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` 方法提供值筛选功能。`valueFieldIndex` 参数指定要评估的数据字段（可使用 `pivotTable.getDataFields().indexOf(dataField)`，或遍历该集合以查找其位置）。`filterType` 参数可使用 `ValueGreaterThan`、`ValueLessThan`、`ValueBetween`、`ValueEqual`、`ValueNotEqual`、`ValueGreaterThanOrEqual` 和 `ValueLessThanOrEqual` 等值。两个 `double` 参数用于指定阈值。
以下示例加载包含数据透视表的工作簿，应用值筛选以仅保留汇总销售额超过数值阈值的项目，然后刷新数据透视表并保存工作簿。

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
                // 由于 PivotFieldCollection 没有 IndexOf，因此手动查找数据字段索引
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
                pivotTable.refreshData();
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
前 10 项筛选是值筛选的一种专用形式，根据选定的值字段仅保留汇总值最高或最低的 N 个项目。常用于生成“按收入排名前 10 的产品”或“按销售量排名后 5 的区域”等排名报告。

{{% alert color="primary" %}}
仅当数据透视表的数据区域中包含一个或多个值字段时，前 10 项筛选才有效。如果数据区域中没有任何值字段，就没有可用于对项目进行排名的汇总度量，因而无法应用此筛选。
Aspose.Cells 通过 `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` 方法提供前 10 项筛选功能。`valueFieldIndex` 参数是数据字段的索引，该字段的汇总值用于对项目进行排名；`filterType` 用于选择 `itemCount` 的单位（`Count` 保留固定数量的项目，`Percent` 保留项目的一定百分比，此时 `itemCount` 本身即为该百分比）；`isTop` 指示是否保留排名靠前的项目（true）或排名靠后的项目（false）；`itemCount` 指定要保留的项目数量或百分比。
以下示例加载包含数据透视表的工作簿（其中包含一个值字段），随后应用前 10 项筛选，仅保留按销售总额排名前 10 的项目，刷新数据透视表并保存工作簿。
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
                // 加载包含数据透视表的工作簿
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // 获取包含数据透视表的工作表（索引 0）
                const worksheet = workbook.worksheets.get(0);
                // 按索引获取数据透视表
                const pivotTable = worksheet.pivotTables.get(0);
                // 确认数据区域中至少有一个值 PivotField
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // 获取目标行 PivotField（要应用前 10 筛选的字段）
                const rowField = pivotTable.rowFields.get(0);
                // 第一个（也是唯一的）数据字段位于索引 0；前 10 筛选按该字段排名。
                const valueFieldIndex = 0;
                // 对行字段应用前 10 筛选：
                //   - valueFieldIndex = 0 — 用于对项目进行排名的数据字段
                //   - filterType = PivotFilterType.Count（保留固定数量的项目；
                //     PivotFilterType.Percent 会将 10 解释为“前 10%”）
                //   - isTop = true（前 N；false 表示后 N）
                //   - itemCount = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // 刷新数据透视表数据并重新计算，使筛选生效
                pivotTable.refreshData();
                // 保存工作簿
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
除了结构化筛选 API 之外，Aspose.Cells 允许您直接控制各个数据透视项的可见性。通过遍历 `PivotField` 的 `pivotField.getPivotItems()` 集合并切换 `isHidden` 属性，您可以在不应用基于公式的筛选的情况下，选择性地隐藏特定项目。设置 `pivotItem.isHidden = true` 会将该项目从数据透视表中隐藏；设置 `pivotItem.isHidden = false` 会取消隐藏并使其重新可见。
当筛选规则不规则或需要针对特定项目分别处理时，此方法非常有用，例如隐藏特定报告中不应出现的少量具有指定名称的类别。以下示例加载数据透视表，按名称隐藏特定项目，演示如何取消隐藏，然后刷新数据透视表并保存工作簿。

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
                // 加载包含数据透视表的现有工作簿
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // 访问包含数据透视表的第一个工作表
                const sheet = workbook.worksheets.get(0);
                // 按索引访问数据透视表（工作表上的第一个数据透视表）
                const pivotTable = sheet.pivotTables.get(0);
                // 获取目标 PivotField（我们将隐藏或取消隐藏其项目的第一个行标签字段）
                const pivotField = pivotTable.rowFields.get(0);
                // 遍历所选 PivotField 的 PivotItems 集合
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // 隐藏名称符合特定条件的数据透视项
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // 演示取消隐藏：重新显示先前隐藏的数据透视项
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // 刷新并重新计算数据透视表，使更改生效
                pivotTable.refreshData();
                // 保存工作簿——隐藏的项目仍保留在底层数据中
                // 但不会显示在数据透视表输出结果中
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
Aspose.Cells for JavaScript via C++ 提供了与 Microsoft Excel 中相应功能相匹配的一整套数据透视表筛选功能。标签筛选、日期筛选和值筛选涵盖了最常见的分析场景，而前 10 项筛选则用于处理排名报告。当筛选规则不规则时，`pivotItem.isHidden` 属性可作为灵活的项目级备选方案。组合使用这些策略（例如先应用标签筛选，再隐藏特定项目），即可完全通过代码构建精准呈现所需内容的数据透视表报告。

{{< app/cells/assistant language="javascript-cpp" >}}