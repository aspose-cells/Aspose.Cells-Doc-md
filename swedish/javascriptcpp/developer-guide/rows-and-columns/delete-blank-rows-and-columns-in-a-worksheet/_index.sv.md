---
title: Ta bort tomma rader och kolumner i ett kalkylblad med JavaScript via C++
linktitle: Radera tomma rader och kolumner i ett kalkylblad
type: docs
weight: 300
url: /sv/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: Lär dig hur man tar bort alla tomma rader och kolumner från ett kalkylblad med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Det är möjligt att ta bort alla tomma rader och kolumner från ett kalkylblad. Detta är användbart när man, till exempel, genererar en PDF-fil från en Microsoft Excel-fil och vill konvertera endast rader och kolumner som innehåller data eller relaterade objekt.

Använd följande Aspose.Cells-metoder för att ta bort tomma rader och kolumner:

1. För att ta bort tomma rader, använd metoden [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankRows--). Observera, för tomma rader som kommer att tas bort, krävs det inte bara att [**Row.isBlank()**](https://reference.aspose.com/cells/javascript-cpp/row/#isBlank--) ska vara sant, utan det får inte heller finnas någon synlig kommentar definierad för någon cell i dessa rader, och ingen pivottabell vars omfång korsar dem.
2. För att ta bort tomma kolumner, använd [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankColumns--)-metoden.

{{% /alert %}}

## JavaScript-kod för att ta bort tomma rader

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;

            // Get first worksheet
            const sheet = sheets.get(0);

            // Delete blank rows from the worksheet
            sheet.cells.deleteBlankRows();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Blank rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## JavaScript-kod för att ta bort tomma kolumner

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Blank Columns Example</title>
    </head>
    <body>
        <h1>Delete Blank Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = workbook.worksheets;

            // Get first Worksheet from WorksheetCollection
            const sheet = sheets.get(0);

            // Delete the Blank Columns from the worksheet
            sheet.cells.deleteBlankColumns();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Blank columns deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
