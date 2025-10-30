---
title: Formattazione della tabella pivot
type: docs
weight: 10
url: /it/javascript-cpp/formatting-pivot-table/
description: Come formattare una tabella pivot con Aspose.Cells for JavaScript via C++.
keywords: Formattazione tabella pivot.
---

## **Aspetto della tabella pivot**

Come creare una tabella pivot spiega come creare una semplice tabella pivot. Questo articolo descrive come personalizzare l'aspetto di una tabella pivot impostando diverse proprietà:

- Opzioni di formato tabella pivot
- Opzioni di formato dei campi pivot
- Opzioni di formato del campo dati

### **Come impostare le opzioni di formato tabella pivot**

La classe [**PivotTable**](https://reference.aspose.com/cells/javascript-cpp/pivottable/) controlla complessivamente la tabella pivot e può essere formattata in vari modi.

#### **Come impostare il tipo di autoformato**

Microsoft Excel offre diversi formati di report preimpostati. Aspose.Cells for JavaScript via C++ supporta anche queste opzioni di formattazione. Per accedervi:

1. Imposta [**PivotTable.isAutoFormat(value)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#isAutoFormat-boolean-) su **vero**.
1. Assegna un'opzione di formattazione dall'enumerazione [**PivotTableAutoFormatType**](https://reference.aspose.com/cells/javascript-cpp/pivottableautoformattype/).

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

#### **Come impostare le opzioni di formattazione**

Il codice di esempio qui sotto mostra come formattare la tabella pivot per mostrare i totali generali per righe e colonne, e come impostare l'ordine dei campi del report. Mostra inoltre come impostare una stringa personalizzata per i valori nulli.

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

#### **Formattazione Aspetto e Sensazione Manualmente**

Per formattare manualmente l'aspetto del report della tabella pivot, anziché utilizzare formati di report predefiniti, utilizzare i metodi [**PivotTable.formatAll(style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#formatAll-style-) e [**PivotTable.format(row, column, style)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#format-number-number-style-). Creare un oggetto stile per la formattazione desiderata, ad esempio:

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

### **Come impostare le opzioni di formato campo pivot**

La classe [**PivotField**](https://reference.aspose.com/cells/javascript-cpp/pivotfield/) rappresenta un campo in una tabella pivot e può essere formattata in vari modi. Il codice di esempio qui sotto mostra come:

- Accedere ai campi di riga.
- Impostare i subtotali.
- Impostazione dell'ordinamento automatico.
- Impostazione dell'autovisualizzazione.

#### **Come impostare il formato dei campi riga/colonna/pagina**

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

### **Come impostare il formato dei campi dati**

Il campione di codice sottostante mostra come impostare i formati di visualizzazione e il formato numerico per i campi dati.

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

### **Come eliminare i campi di un Pivot**

Il [**PivotFieldCollection**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/) ha un metodo chiamato [**clear()**](https://reference.aspose.com/cells/javascript-cpp/pivotfieldcollection/#clear--) che ti consente di eliminare i campi di un Pivot. Usalo quando vuoi eliminare tutti i campi di un Pivot nelle aree, ad esempio, pagina, colonna, riga o dati.
Il campione di codice sottostante mostra come eliminare tutti i campi di un Pivot in un'area dati.

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
