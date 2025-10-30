---
title: Dar formato a la tabla dinámica
type: docs
weight: 10
url: /es/javascript-cpp/formatting-pivot-table/
description: Cómo formatear una tabla dinámica con Aspose.Cells for JavaScript vía C++.
keywords: Formato de tabla dinámica
---

## **Apariencia de la tabla dinámica**

Cómo crear una tabla dinámica explica cómo crear una tabla dinámica simple. Este artículo describe cómo personalizar la apariencia de una tabla dinámica estableciendo diversas propiedades:

- Opciones de formato de tabla dinámica
- Opciones de formato de campos de tabla dinámica
- Opciones de formato de campos de datos

### **Cómo establecer opciones de formato de tabla dinámica**

La clase [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/) controla la tabla dinámica general y se puede formatear de varias maneras.

#### **Cómo establecer el tipo de autoformato**

Microsoft Excel ofrece una serie de formatos de informe preestablecidos. Aspose.Cells for JavaScript vía C++ también soporta estas opciones de formato. Para acceder a ellos:

1. Establezca [**PivotTable.isAutoFormat(value)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isAutoFormat-boolean-) en **verdadero**.
1. Asignar una opción de formato de la enumeración [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/javascript-cpp/pivottableautoformattype/).

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

#### **Cómo establecer opciones de formato**

El ejemplo de código a continuación muestra cómo dar formato a la tabla dinámica para mostrar totales generales para filas y columnas, y cómo establecer el orden de los campos del informe. También muestra cómo establecer una cadena personalizada para los valores nulos.

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

#### **Dar formato manualmente al aspecto visual**

Para formatear cómo se ve el informe de tabla dinámica manualmente, en lugar de usar formatos de informe preestablecidos, use los métodos [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) y [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-). Cree un objeto de estilo para su formato deseado, por ejemplo:

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

### **Cómo establecer opciones de formato de campo de tabla dinámica**

La clase [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/) representa un campo en una tabla dinámica y se puede formatear de varias formas. El ejemplo de código a continuación muestra cómo:

- Acceder a los campos de fila.
- Establecer subtotales.
- Establecer orden automático.
- Establecer autover.

#### **Cómo establecer el formato de campos de fila/columna/página.**

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

### **Cómo establecer el formato de campos de datos.**

El ejemplo de código a continuación muestra cómo establecer formatos de visualización y formato numérico para los campos de datos.

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

### **Cómo limpiar los campos de filtro.**

La clase [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/) tiene un método llamado [**clear()**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/#clear--) que te permite borrar campos de tabla dinámica. Úsalo cuando quieras borrar todos los campos de tabla dinámica en las áreas, por ejemplo, página, columna, fila o datos.
El ejemplo de código a continuación muestra cómo borrar todos los campos de tabla dinámica en un área de datos.

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
