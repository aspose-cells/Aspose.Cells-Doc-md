---
title: Convertire JSON in Excel con JavaScript tramite C++
linktitle: Converti JSON in Excel
type: docs
weight: 300
url: /it/javascript-cpp/convert-json-to-excel/
description: Impara come convertire JSON in file Excel con Aspose.Cells for JavaScript tramite C++.
keywords: Importazione di JSON senza Office 2013, Office 2016, Office 2019 e Office 365 usando JavaScript tramite C++.
---

{{% alert color="primary" %}}

 Aspose.Cells supporta la conversione di un file JSON (JavaScript Object Notation) in un Workbook Excel.

{{% /alert %}}

## **Converti JSON in Excel Workbook**
Non c'è bisogno di chiedersi come convertire JSON in file Excel, perché Aspose.Cells for JavaScript tramite C++ fornisce la soluzione migliore. L'API Aspose.Cells supporta la conversione del formato JSON in fogli di calcolo. È possibile utilizzare la classe [**JsonLoadOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonloadoptions) per specificare impostazioni aggiuntive per l'importazione di JSON in Workbook.

Il seguente esempio di codice dimostra l'importazione del JSON nel foglio di lavoro di Excel. Si prega di vedere il codice per convertire il [file di origine](sample.json) nel file xlsx generato dal codice a titolo di riferimento.

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

 Il seguente esempio di codice, che utilizza la classe JsonLoadOptions per specificare impostazioni aggiuntive, dimostra come importare JSON in un Excel Workbook. Consulta il codice per convertire [file sorgente](sample.json) nel file xlsx generato dal codice come riferimento.

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

 Il seguente esempio di codice dimostra l'importazione di una stringa JSON in un Excel Workbook. Puoi anche specificare la posizione del layout durante l'importazione di JSON. Consulta il codice per convertire una stringa JSON in un file xlsx generato dal codice come riferimento.

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
