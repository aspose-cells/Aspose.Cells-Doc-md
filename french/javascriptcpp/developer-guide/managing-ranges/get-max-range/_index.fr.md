---
title: Obtenir la plage maximale dans une feuille de calcul avec JavaScript via C++
linktitle: Obtenir la plage maximale dans une feuille de calcul
type: docs
weight: 360
url: /fr/javascript-cpp/get-max-range-in-a-worksheet/
description: Cet article décrit comment obtenir la plage max, la plage de données max, et la plage d affichage max des fichiers Excel en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

Lors de la lecture de données de la feuille de calcul, nous devons connaître la zone maximale.

Lors de la copie de toutes les données d'une feuille de calcul, nous devons connaître la zone maximale.

Lors de l'exportation d'une zone spécifiée en HTML et PDF, nous devons connaître la zone maximale.

Aspose.Cells for JavaScript via C++ propose différentes manières de trouver la plage maximale dans une feuille de calcul.

{{% /alert %}}

## **Obtenir la plage maximale**
Dans Aspose.Cells, si les objets [**row**](https://reference.aspose.com/cells/javascript-cpp/row/) et [**column**](https://reference.aspose.com/cells/javascript-cpp/column/) sont initialisés, ces lignes et colonnes seront comptabilisées jusqu'à la zone maximale, même s'il n'y a aucune donnée dans les lignes ou colonnes vides.

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

## **Obtenir la plage de données maximale**
Dans la plupart des cas, nous n'avons besoin d'obtenir que toutes les plages contenant toutes les données, même si les cellules vides en dehors de la plage sont formatées.
Et les paramètre concernant les formes, les tableaux et les tableaux croisés dynamiques seront ignorés.

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

## **Obtenir la plage d'affichage maximale**
Lorsque nous exportons toutes les données de la feuille de calcul vers HTML, PDF ou images, nous devons obtenir une zone contenant tous les objets visibles, y compris les données, les styles, les graphiques, les tableaux et les tableaux croisés dynamiques.
Les codes suivants montrent comment rendre la plage d'affichage maximale en HTML :

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

Voici le [fichier excel source](Book1.xlsx).
