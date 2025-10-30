---
title: Konvertera JSON till Excel med JavaScript via C++
linktitle: Konvertera JSON till Excel
type: docs
weight: 300
url: /sv/javascript-cpp/convert-json-to-excel/
description: Lär dig hur man konverterar JSON till Excel fil med Aspose.Cells for JavaScript via C++.
keywords: Importera JSON utan Office 2013, Office 2016, Office 2019 och Office 365 med JavaScript via C++.
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av en JSON (JavaScript-objektnotation) fil till en Excel-arbetsbok.

{{% /alert %}}

## **Konvertera JSON till Excel-arbetsbok**
Behöver inte undra hur man konverterar JSON till Excel-fil, eftersom Aspose.Cells for JavaScript via C++ ger den bästa lösningen. Aspose.Cells API stödjer konvertering av JSON-format till kalkylblad. Du kan använda [**JsonLoadOptions**](https://reference.aspose.com/cells/javascript-cpp/jsonloadoptions)-klassen för att specificera ytterligare inställningar för att importera JSON till arbetsbok.

Följande kodexempel visar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfilen](sample.json) till den xlsx-fil som genereras av koden som referens.

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

Följande kodexempel, som använder JsonLoadOptions-klassen för att specificera ytterligare inställningar, demonstrerar import av JSON till Excel-arbetsbok. Se koden för att konvertera [källfil](sample.json) till xlsx-filen som genereras av koden för referens.

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

Följande kodexempel visar import av en JSON-sträng till Excel-arbetsbok. Du kan också specificera platsen för layouten vid import av JSON. Se koden för att konvertera en JSON-sträng till xlsx-filen som genereras av koden för referens.

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
