---
title: Форматирование сводной таблицы
type: docs
weight: 10
url: /ru/javascript-cpp/formatting-pivot-table/
description: Как форматировать сводную таблицу с помощью Aspose.Cells for JavaScript для C++.
keywords: Форматирование сводной таблицы.
---

## **Внешний вид сводной таблицы**

Как создать сводную таблицу объясняет, как создать простую сводную таблицу. В этой статье описано, как настроить внешний вид сводной таблицы, устанавливая различные свойства:

- Опции формата сводной таблицы
- Опции формата полей сводной таблицы
- Опции формата данных поля

### **Как установить параметры форматирования сводной таблицы**

Класс [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/) контролирует общую сводную таблицу и может быть отформатирован различными способами.

#### **Как установить тип автоформата**

Microsoft Excel предлагает множество предустановленных форматов отчетов. Aspose.Cells for JavaScript для C++ поддерживает эти параметры форматирования также. Для их доступа:

1. Установите [**PivotTable.isAutoFormat(value)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isAutoFormat-boolean-) в **true**.
1. Назначьте опцию форматирования из перечисления [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/javascript-cpp/pivottableautoformattype/).

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

#### **Как устанавливать параметры форматирования**

Приведенный ниже пример кода показывает, как отформатировать сводную таблицу для отображения общих итогов для строк и столбцов, а также как установить порядок полей отчета. Он также показывает, как установить пользовательскую строку для пустых значений.

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

#### **Форматирование внешнего вида вручную**

Чтобы вручную форматировать отчет сводной таблицы, вместо использования предустановленных форматов отчетов, используйте методы [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) и [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-). Создайте объект стиля для желаемого форматирования, например:

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

### **Как установить параметры форматирования поля сводной таблицы**

Класс [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/) представляет собой поле в сводной таблице и может быть отформатировано несколькими способами. Приведенный ниже образец кода показывает, как:

- Получить строковые поля.
- Настроить итоги.
- Настроить автосортировку.
- Настроить автоотображение.

#### **Как установить формат полей строк/столбцов/страниц**

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

### **Как установить формат полей данных**

Приведенный ниже образец кода показывает, как установить формат отображения и числовой формат для полей данных.

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

### **Как очистить поля сводной таблицы**

У класса [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/) есть метод с именем [**clear()**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/#clear--), который позволяет очистить поля сводной таблицы. Используйте его, когда вам нужно очистить все поля сводной таблицы в областях, например страница, столбец, строка или данные.
Приведенный ниже образец кода показывает, как очистить все поля сводной таблицы в области данных.

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
