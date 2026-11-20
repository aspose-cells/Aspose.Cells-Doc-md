---
title: 在数据透视表中对字段分组
linktitle: 在数据透视表中对字段分组
description: 了解如何使用 Aspose.Cells for JavaScript via C++ 中的 PivotField.group 和 PivotFieldGroupOptions 将数据透视表的行和列字段分组为月份、季度等日期期间以及数值范围。
keywords: Aspose.Cells, 数据透视表, 分组数据透视字段, PivotField.group, PivotFieldGroupOptions, 日期分组, 数值分组, 月份, 季度, 数值范围, JavaScript via C++
type: docs
weight: 80
url: /zh/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **可能的使用场景**
- 当数据透视表的行或列字段包含大量不同项时（例如包含数百个日期的日期字段或包含许多离散数值的数值字段），对数据透视字段进行分组非常有用。分组会将这些项折叠为有意义的部分：日期可归为月份、季度和年份，数值可归为 0-1、2-3、4-5 等区间。这样可以让大型数据透视表更紧凑、更易于分析。Aspose.Cells 通过 `PivotField.group()` 方法（按数据类型自动分组）和 `PivotField.group(PivotFieldGroupOptions)`（自定义分组选项）提供此功能。
- 日期分组会将单个日期提升为更大的时间段，例如天、月、季度和年，并构建时间层级（例如 年 → 季度 → 月份）。时间趋势一目了然，每个层级都会成为数据透视表行或列区域中的独立字段。
- 仅对放置在 ROW 或 COLUMN 区域的字段可进行分组。数据（数值）字段不能直接分组。若要对该字段分组，需要先将其添加到数据透视表的行或列区域。

## **自动分组数据透视字段**
无参的 `PivotField.group()` 重载会检查字段的数据类型并自动完成分组。仅包含日期（以及空值）的字段会按月份分组；仅包含数字（以及空值）的字段会使用自动间隔划分为数值区间。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **使用自定义选项分组数据透视字段**
`PivotFieldGroupOptions` 类提供自定义分组配置。对于日期字段，设置 `startDate`、`endDate` 和 `groupTypes`；对于数值字段，设置 `startNumber`、`endNumber` 和 `interval`。`newPivotField` 属性控制分组是创建新数据透视字段还是替换原字段（详见本文末的 Note 部分）。

### **按月份和季度分组日期字段**
以下示例将示例数据透视表的日期行字段在指定的开始和结束日期之间按月份和季度分组。代码加载 [sample Excel file](sampleGroupPivotFieldsInPivotTable.xlsx)，执行分组，计算数据透视表数据，并保存分组结果。截图展示了效果：日期行字段已按季度和月份分组。请注意，`options.groupTypes` 中值的顺序会被忽略。无论以何种顺序列出分组类型，分组字段始终按照从大到小的时间层级显示：年、季度、月份、天、小时、分钟、秒。在本例中，`options.groupTypes` 将月份放在季度之前，但最终显示时季度位于外层，月份位于内层。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![按月份和季度分组的数据透视表](group-pivot-fields-in-the-pivot-table_1.png)

### **将数值字段分组为范围**
示例数据透视表的 `FieldTwo` 最初是一个数据（数值）字段。由于只能对行或列字段进行分组，代码首先调用 `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` 将 `FieldTwo` 移动到行区域，刷新数据透视表，然后使用 `startNumber = 0`、`endNumber = 5`、`interval = 2` 将该数值字段分组为 0-1、2-3、4-5 三个区间。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **注意事项**

{{% alert color="primary" %}}
- `PivotField.groupBy()` 方法的重载已被弃用并从 API 中移除。请使用 `PivotField.group()` 和 `PivotField.group(PivotFieldGroupOptions)` 替代。
- 在 Microsoft Excel 中，对数值字段进行分组会 **替换** 原数据透视字段为分组后的区间；而对日期字段进行分组会在原字段旁创建 **新** 的数据透视字段（每个分组层级对应一个字段，例如季度和月份）。从 Aspose.Cells 26.10 开始，`PivotField.group()` 方法遵循相同的行为。`PivotFieldGroupOptions.newPivotField` 属性为兼容旧版本而保留：数值分组默认 `false`，日期时间分组默认 `true`；若希望日期分组 **替换** 原字段而不是创建新字段，可将其设为 `false`。
- `PivotFieldGroupOptions.interval` 属性仅在数值分组以及按天进行的日期分组时生效（例如将日期划分为 7 天的区间）；在按月份、季度或年份进行日期分组时会被忽略。
{{% /alert %}}

## **相关文档**
- [在数据透视表中添加行和列字段](/cells/zh/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [按标签或数值过滤数据透视表](/cells/zh/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [在数据透视表中添加页面字段](/cells/zh/javascript-cpp/add-page-field-in-pivot-table/)
- [对数据透视表应用样式](/cells/zh/javascript-cpp/apply-style-to-pivot-table/)
- [刷新数据透视表](/cells/zh/javascript-cpp/refresh-pivot-table/)
- [数据透视表字段项的离散分组](/cells/zh/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}