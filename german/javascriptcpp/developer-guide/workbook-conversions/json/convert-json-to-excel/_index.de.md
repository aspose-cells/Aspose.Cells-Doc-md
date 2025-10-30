---
title: JSON in Excel mit JavaScript über C++ konvertieren
linktitle: Konvertieren Sie JSON nach Excel
type: docs
weight: 300
url: /de/javascript-cpp/convert-json-to-excel/
description: Erfahren Sie, wie Sie JSON mit Aspose.Cells for JavaScript über C++ in Excel Dateien konvertieren.
keywords: JSON ohne Office 2013, Office 2016, Office 2019 und Office 365 mit JavaScript über C++ importieren.
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Konvertierung einer JSON-(JavaScript-Objekt-Notation)-Datei in ein Excel-Arbeitsbuch.

{{% /alert %}}

## **Konvertieren Sie JSON in Excel-Arbeitsmappe**
Sie brauchen sich nicht zu wundern, wie Sie JSON in Excel-Dateien konvertieren, denn Aspose.Cells for JavaScript über C++ bietet die beste Lösung. Die API Aspose.Cells unterstützt die Konvertierung des JSON-Formats in Tabellenkalkulationen. Sie können die Klasse [**JsonLoadOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonloadoptions) verwenden, um zusätzliche Einstellungen für den Import von JSON in die Arbeitsmappe festzulegen.

Das folgende Codebeispiel zeigt, wie man JSON in Excel-Arbeitsmappe importiert. Bitte sehen Sie sich den Code zur Konvertierung der [Quelldatei](sample.json) in die von dem Code generierte xlsx-Datei als Referenz an.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Convert JSON to XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // create a Workbook object from uploaded file (JSON)
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // save file to xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the XLSX file.</p>';
        });
    </script>
</html>
```

Das folgende Codebeispiel, das die JsonLoadOptions-Klasse verwendet, um zusätzliche Einstellungen festzulegen, zeigt den Import von JSON in ein Excel-Arbeitsbuch. Bitte beachten Sie den Code zur Konvertierung der [Quelldatei](sample.json) in die durch den Code generierte xlsx-Datei.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Load JSON into Workbook and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".json" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a JSON file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create an options of loading the file.
            const options = new JsonLoadOptions();
            options.multipleWorksheets = true;

            // Loads the workbook from JSON file
            const book = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save file to xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

Das folgende Codebeispiel demonstriert das Importieren eines JSON-Strings in ein Excel-Arbeitsbuch. Sie können auch die Position des Layouts beim Importieren von JSON festlegen. Bitte beachten Sie den Code zur Konvertierung eines JSON-Strings in die durch den Code generierte xlsx-Datei.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Import JSON as Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, JsonLayoutOptions, JsonUtility, Utils } = AsposeCells;

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

        // Converted logic from JavaScript to browser-compatible code
        const inputJson = JSON.stringify([
            { BEFORE: 'before cell', TEST: 'asd1', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd2', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd3', AFTER: 'after cell' },
            { BEFORE: 'before cell', TEST: 'asd4', AFTER: 'after cell' }
        ]);
        const sheetName = "Sheet1";
        const row = 3;
        const column = 2;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a Workbook object
            const book = new Workbook();
            const worksheet = book.worksheets.get(sheetName);

            // set JsonLayoutOptions to treat Arrays as Table
            const jsonLayoutOptions = new JsonLayoutOptions();
            jsonLayoutOptions.arrayAsTable = true;

            // Import JSON data into worksheet cells at specified row and column
            AsposeCells.JsonUtility.importData(inputJson, worksheet.cells, row, column, jsonLayoutOptions);

            // Save file to xlsx format and prepare download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">JSON imported as table and file generated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
