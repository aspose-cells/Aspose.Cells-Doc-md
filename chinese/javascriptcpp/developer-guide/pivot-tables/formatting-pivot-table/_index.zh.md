---
title: 格式化数据透视表
type: docs
weight: 10
url: /zh/javascript-cpp/formatting-pivot-table/
description: 如何用Aspose.Cells for JavaScript通过C++对数据透视表进行格式化。
keywords: 格式化数据透视表。
---

## **数据透视表外观**

如何创建数据透视表介绍了如何创建简单的数据透视表。本文描述了如何通过设置各种属性来自定义数据透视表的外观:

- 数据透视表格式选项
- 数据透视字段格式选项
- 数据字段格式选项

### **如何设置数据透视表格式选项**

[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/)类控制整体数据透视表，可以以多种方式进行格式设置。

#### **如何设置自动格式类型**

Microsoft Excel提供多种预设报告格式。Aspose.Cells for JavaScript通过C++也支持这些格式化选项。访问方法如下：

1. 将[**PivotTable.isAutoFormat(value)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isAutoFormat-boolean-)设置为**true**。
1. 从[**PivotTableAutoFormatType**](https://reference.aspose.com/cells/javascript-cpp/pivottableautoformattype/)枚举中分配一个格式选项。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>PivotTable AutoFormat Example</h1>
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const pivotindex = 0;

            // Accessing the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotindex);

            // Setting the PivotTable report is automatically formatted
            pivotTable.isAutoFormat = true;

            // Setting the PivotTable autoformat type.
            pivotTable.autoFormatType = AsposeCells.PivotTableAutoFormatType.Report5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **如何设置格式选项**

下面的代码示例演示了如何格式化数据透视表以显示行和列的总计，以及如何设置报告的字段顺序。它还显示了如何为空值设置自定义字符串。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Update Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);
            const pivotindex = 0;

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotindex);

            // Setting the PivotTable report shows grand totals for rows.
            pivotTable.rowGrand = true;
            // Setting the PivotTable report shows grand totals for columns.
            pivotTable.columnGrand = true;
            // Setting the PivotTable report displays a custom string in cells that contain null values.
            pivotTable.displayNullString = true;
            pivotTable.nullString = "null";
            // Setting the PivotTable report's layout
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **手动设置外观和感觉格式**

要手动设置数据透视表报告的外观和感觉，而不是使用预设的报告格式，请使用[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-)和[**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-)方法。为所需的格式创建样式对象，例如：

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Style Example</h1>
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first pivot table
            const pivot = worksheet.pivotTables.get(0);

            // Set pivot table style (converted setter -> property)
            pivot.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleDark1;

            // Create and configure a style
            const style = workbook.createStyle();
            style.font.name = "Arial Black";
            style.pattern = AsposeCells.BackgroundType.Solid;
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Apply style to pivot table
            pivot.formatAll(style);

            // Save the modified workbook (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot table styled successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何设置数据透视表字段格式选项**

[**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/)类表示数据透视表中的字段，并可以以多种方式进行格式设置。下面的代码示例演示了如何:

- 访问行字段。
- 设置合计。
- 设置自动排序。
- 设置自动显示。

#### **如何设置行/列/页面字段格式**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Example</title>
    </head>
    <body>
        <h1>PivotTable Example</h1>
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
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pivotindex = 0;

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotindex);

            // Setting the PivotTable report shows grand totals for rows.
            pivotTable.rowGrand = true;

            // Accessing the row fields.
            const pivotFields = pivotTable.rowFields;

            // Accessing the first row field in the row fields.
            const pivotField = pivotFields.get(0);

            // Setting Subtotals.
            pivotField.subtotals = AsposeCells.PivotFieldSubtotalType.Sum, true;
            pivotField.subtotals = AsposeCells.PivotFieldSubtotalType.Count, true;

            // Setting autosort options.
            // Setting the field auto sort.
            pivotField.isAutoSort = true;
            // Setting the field auto sort ascend.
            pivotField.isAscendSort = true;
            // Setting the field auto sort using the field itself.
            pivotField.autoSortField = -5;

            // Setting autoShow options.
            // Setting the field auto show.
            pivotField.isAutoShow = true;
            // Setting the field auto show ascend.
            pivotField.isAscendShow = false;
            // Setting the auto show using field(data field).
            pivotField.autoShowField = 0;

            // Saving the Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PivotTable modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何设置数据字段格式**

以下代码示例显示如何设置数据字段的显示格式和数字格式。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Pivot Field Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PivotFieldDataDisplayFormat, PivotItemPositionType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pivotindex = 0;

            // Accessing the PivotTable
            const pivotTable = worksheet.pivotTables.get(pivotindex);

            // Accessing the data fields.
            const pivotFields = pivotTable.dataFields;

            // Accessing the first data field in the data fields.
            const pivotField = pivotFields.get(0);

            // Setting data display format
            pivotField.showValuesAs(PivotFieldDataDisplayFormat.PercentageOf, 1, PivotItemPositionType.Next, 0);

            // Setting number format (converted from setNumber to property assignment)
            pivotField.number = 10;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **如何清除数据透视字段**

[**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/) 有一个名为 [**clear()**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/#clear--) 的方法，允许您清除数据透视字段。当您想要清除区域中的所有数据透视字段时（例如页、列、行或数据），请使用它。
以下代码示例显示如何清除数据区域中的所有数据透视字段。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the pivot tables in the sheet
            const pivotTables = sheet.pivotTables;

            // Get the first PivotTable
            const pivotTable = pivotTables.get(0);

            // Clear all the data fields
            pivotTable.dataFields.clear();

            // Add new data field
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Betrag Netto FW");

            // Set the refresh data flag on
            pivotTable.refreshDataFlag = true;

            // Refresh and calculate the pivot table data
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Turn off refresh flag
            pivotTable.refreshDataFlag = false;

            // Save the modified Excel file (Excel 97-2003 .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Pivot table updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
