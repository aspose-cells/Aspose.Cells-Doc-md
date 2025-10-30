---
title: Nascondere e ordinare i dati della tabella pivot
type: docs
weight: 120
url: /it/javascript-cpp/pivot-table-hide-and-sort-data/
---

## **Nascondi e ordina i datidelle tabelle pivot**
Aspose.Cells for JavaScript tramite C++ supporta la visualizzazione e l’ordinamento dei dati nella tabella pivot. Il seguente frammento di codice dimostra questa funzione ordinando la colonna Score in ordine decrescente e nascondendo poi le righe con un punteggio inferiore a 60.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Hide and Sort Example</title>
    </head>
    <body>
        <h1>PivotTable Hide and Sort Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first pivot table in the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Getting data body range and determining rows used
            const dataBodyRange = pivotTable.dataBodyRange;
            let currentRow = 3;
            const rowsUsed = dataBodyRange.endRow;

            // Sorting score in descending
            const field = pivotTable.rowFields.get(0);
            field.isAutoSort = true;
            field.isAscendSort = false;
            field.autoSortField = 0;
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Hiding rows with score less than 60
            while (currentRow < rowsUsed) {
                const cell = worksheet.cells.get(currentRow, 1);
                const score = cell.floatValue;
                if (score < 60) {
                    worksheet.cells.hideRow(currentRow);
                }
                currentRow = currentRow + 1;
            }

            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PivotTableHideAndSort_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

I file excel di origine e di output utilizzati nello snippet di codice sono allegati per riferimento.

[File di origine](96928093.xlsx)

[File di output](96928094.xlsx)
