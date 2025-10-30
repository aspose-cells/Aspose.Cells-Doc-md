---
title: ピボットテーブルの書式設定
type: docs
weight: 10
url: /ja/javascript-cpp/formatting-pivot-table/
description: C++を使用したAspose.Cells for JavaScriptによるピボットテーブルの書式設定方法。
keywords: ピボットテーブルのフォーマット。
---

## **ピボットテーブルの外観**

ピボットテーブルの外観をカスタマイズする方法については、「ピボットテーブルの作成」でシンプルなピボットテーブルの作成方法が説明されています。この記事では、さまざまなプロパティを設定してピボットテーブルの外観をカスタマイズする方法について説明します:

- ピボットテーブルの書式オプション
- ピボットフィールドの書式オプション
- データフィールドの書式オプション

### **ピボットテーブルフォーマットオプションの設定方法**

[**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/) クラスは、全体のピボットテーブルを制御し、さまざまな方法で書式設定できます。

#### **自動フォーマットタイプの設定方法**

 Microsoft Excelはさまざまな既定のレポート形式を提供しています。Aspose.Cells for JavaScriptもこれらの書式設定オプションをサポートしています。アクセス方法：

1. [**PivotTable.isAutoFormat(value)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isAutoFormat-boolean-) を **true** に設定します。
1. [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/javascript-cpp/pivottableautoformattype/) 列挙型から書式設定オプションを割り当てます。

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

#### **フォーマットオプションの設定方法**

以下のコードサンプルは、ピボットテーブルを書式設定して行と列の合計を表示する方法、およびレポートのフィールド順序を設定する方法を示しています。また、null 値にカスタム文字列を設定する方法も示しています。

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

#### **見た目と手触りの書式設定**

事前設定されたレポート形式を使用せずに、ピボットテーブルレポートの外観を手動でフォーマットする場合、[**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) メソッドと [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-) メソッドを使用します。所望のフォーマットのためのスタイルオブジェクトを作成します。たとえば：

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

### **ピボットフィールドのフォーマットオプションの設定方法**

[**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/) クラスは、ピボットテーブルのフィールドを表し、さまざまな方法で書式設定できます。以下のコードサンプルは、次のように行います:

- 行フィールドへのアクセス。
- 小計の設定。
- 自動並べ替えの設定。
- 自動表示の設定。

#### **行/列/ページフィールドのフォーマット設定方法**

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

### **データフィールドのフォーマット設定方法**

以下のコードサンプルは、データフィールドの表示形式と数値形式を設定する方法を示しています。

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

### **ピボットフィールドをクリアする方法**

[**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/) には、ピボットフィールドをクリアするための [**clear()**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/#clear--) メソッドがあります。たとえば、ページ、列、行、またはデータなど、領域内のすべてのピボットフィールドをクリアしたい場合に使用します。
以下のコードサンプルは、データ領域内のすべてのピボットフィールドをクリアする方法を示しています。

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
