---
title: Ottieni il massimo intervallo in un foglio di lavoro con JavaScript tramite C++
linktitle: Ottieni Max Range In Un Foglio di Lavoro
type: docs
weight: 360
url: /it/javascript-cpp/get-max-range-in-a-worksheet/
description: Questo articolo descrive come ottenere l intervallo massimo, l intervallo massimo di dati e l intervallo massimo di visualizzazione dei file Excel usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}

Quando si leggono i dati dal foglio di lavoro, è necessario conoscere l'area massima.

Quando si copiano tutti i dati da un foglio di lavoro, è necessario conoscere l'area massima.

Quando esportiamo un'area specificata in HTML e PDF, dobbiamo conoscere l'area massima.

Aspose.Cells for JavaScript tramite C++ contiene diversi modi per trovare l'intervallo massimo in un foglio di lavoro.

{{% /alert %}}

## **Ottenere l'intervallo massimo**
In Aspose.Cells, se gli oggetti [**row**](https://reference.aspose.com/cells/javascript-cpp/row/) e [**column**](https://reference.aspose.com/cells/javascript-cpp/column/) sono inizializzati, queste righe e colonne verranno conteggiate per l'area massima, anche se non ci sono dati nelle righe o colonne vuote.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxRow;
            let maxColumn = sheet.cells.maxColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate maxRow/maxColumn after clearing
            maxRow = sheet.cells.maxRow;
            maxColumn = sheet.cells.maxColumn;
            // The range is updated (e.g., A1:B10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ottieni il massimo intervallo di dati**
Nella maggior parte dei casi, abbiamo solo bisogno di ottenere tutti i range contenenti tutti i dati, anche se le celle vuote al di fuori del range sono formattate.
E le impostazioni su forme, tabelle e tabelle pivot verranno ignorate.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;
            const sheet = worksheets.get(0);

            // Gets the max data range.
            let maxRow = sheet.cells.maxDataRow;
            let maxColumn = sheet.cells.maxDataColumn;
            // The range is A1:B3 (based on maxRow/maxColumn).
            let range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Clear cell A10 by setting its value to null
            const cell = sheet.cells.get("A10");
            cell.value = null;

            // Recalculate max data range after clearing the cell
            maxRow = sheet.cells.maxDataRow;
            maxColumn = sheet.cells.maxDataColumn;
            // The range is still A1:B3 (after clearing A10).
            range = sheet.cells.createRange(0, 0, maxRow + 1, maxColumn + 1);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Ottieni l'intervallo massimo di visualizzazione**
Quando esportiamo tutti i dati dal foglio di lavoro in HTML, PDF o immagini, dobbiamo ottenere un'area che contenga tutti gli oggetti visibili, inclusi dati, stili, grafici, tabelle e tabelle pivot.
I seguenti codici mostrano come rendere l'intervallo di visualizzazione massimo in HTML:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Export Range to HTML</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Gets the max display range.
            const range = worksheets.get(0).cells.maxDisplayRange;

            // Save the range to html
            const saveOptions = new AsposeCells.HtmlSaveOptions();
            saveOptions.exportActiveWorksheetOnly = true;
            saveOptions.exportArea = AsposeCells.CellArea.createCellArea(
                range.firstRow,
                range.firstColumn,
                range.firstRow + range.rowCount - 1,
                range.firstColumn + range.columnCount - 1
            );

            // Save the range to HTML format and provide download link
            const outputData = workbook.save(SaveFormat.Html, saveOptions);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'html.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Range exported successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```

Ecco il [file excel di origine](Book1.xlsx).
