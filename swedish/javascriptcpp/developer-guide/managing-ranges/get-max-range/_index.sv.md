---
title: Hämta det maximala området i ett kalkylblad med JavaScript via C++
linktitle: Få maxintervall i ett arbetsblad
type: docs
weight: 360
url: /sv/javascript-cpp/get-max-range-in-a-worksheet/
description: Denna artikel beskriver hur man får det maximala området, det maximala datamrådet och det maximala visningsområdet för Excel filer med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

När vi läser data från arket behöver vi känna till det maximala området.

När vi kopierar all data från ett ark behöver vi känna till det maximala området.

När du exporterar ett specificerat område till HTML och PDF behöver vi känna till det maximala området.

Aspose.Cells for JavaScript via C++ innehåller olika sätt att hitta det maximala området i ett kalkylblad.

{{% /alert %}}

## **Får maximalt intervall**
I Aspose.Cells, om objekten [**row**](https://reference.aspose.com/cells/javascript-cpp/row/) och [**column**](https://reference.aspose.com/cells/javascript-cpp/column/) är initialiserade, kommer dessa rader och kolumner att räknas till det maximala området, även om det inte finns någon data i tomma rader eller kolumner.

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

## **Får maximalt datointervall**
I de flesta fall behöver vi bara få alla intervall som innehåller all data, även om de tomma cellerna utanför intervallet är formaterade.
Och inställningarna för former, tabeller och pivottabeller kommer att ignoreras.

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

## **Får maximalt visningsintervall**
När vi exporterar all data från arket till HTML, PDF eller bilder behöver vi få ett område som innehåller alla synliga objekt, inklusive data, stilar, grafik, tabeller och pivottabeller.
Följande kodexempel visar hur man renderar det maximala visningsområdet till HTML:

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

Här är [källa excel-fil](Book1.xlsx).
