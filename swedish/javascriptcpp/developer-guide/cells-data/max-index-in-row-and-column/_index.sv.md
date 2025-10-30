---
title: Hämta maximal kolumnindex i rad och maximal radindex i kolumn
type: docs
weight: 600
url: /sv/javascript-cpp/get-max-index-in-row-and-column/
description: Lär dig hur man får Max kolumnindex i rad och Max radindex i kolumn via Aspose.Cells for JavaScript med C++ API.
keywords: Få Max kolumnindex i rad JavaScript via C++, Få Max radindex i kolumn JavaScript via C++, Få Max datakolumnindex i rad JavaScript via C++, Få Max dataradindex i kolumn JavaScript via C++.
---

## **Möjliga användningsscenario**
När du bara behöver manipulera vissa data på rader eller kolumner, måste du känna till dataintervallet för rader och kolumner. Aspose.Cells for JavaScript via C++ erbjuder denna funktion. För att få maksimal kolumnindex på en rad kan du använda metoderna [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) och [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--), och sedan använda metoden [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) för att få det maximala kolumnindexet och maximala datakolumnindexet. Men för att få det maximala radindexet och maximala dataradindexet på en kolumn, måste du skapa ett intervall på kolumnen, traversera det för att hitta den sista cellen, och slutligen anropa [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) metoden på cellen.

Aspose.Cells for JavaScript via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att nå dina mål.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Få Max kolumnindex i rad och Max radindex i kolumn**
Detta exempel visar hur man:

1. Ladda in [provfilen](sample.xlsx).
1. Hämta raden som behöver få det maximala kolumnindexet och det maximala datakolumnindexet.
1. Anropa [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) metoden på cellen.
1. Skapa ett intervall baserat på kolumn.
1. Hämta iteratorn och traversera intervallen.
1. Anropa [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) metoden på cellen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result pre { background: #f4f4f4; padding: 10px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>Get Max Row/Column Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Accessing cells collection
            const cells = sheet.cells;

            // Check row at index 1
            const row = cells.checkRow(1);
            const outputLines = [];

            if (row != null) {
                // get Maximum column index of Row which contains data or style.
                outputLines.push("Max column index in row: " + row.lastCell.column);

                // get Maximum column index of Row which contains data.
                outputLines.push("Max data column index in row: " + row.lastDataCell.column);
            } else {
                outputLines.push("Row 1 is empty (checkRow returned null).");
            }

            // create the range of column B (index 1)
            const columnRange = cells.createRange(1, 1, true);

            var max_row_index  = cells.maxRow + 1;
            var maxRow = 0;
            var maxDataRow = 0;

            for (let row_index = 0; row_index < max_row_index; row_index++) {
                var curr_cell = cells.get(row_index, 1);

                if (curr_cell) {
                    if (curr_cell.stringValue) {
                        maxDataRow = curr_cell.row;
                    }

                    if (curr_cell.stringValue || curr_cell.hasCustomStyle) {
                        maxRow = curr_cell.row;
                    }
                }
            }

            // Maximum row index of Column which contains data or style.
            outputLines.push("Max row index in Column: " + maxRow);

            // Maximum row index of Column which contains data.
            outputLines.push("Max data row index in Column: " + maxDataRow);

            resultDiv.innerHTML = '<pre>' + outputLines.join('\n') + '</pre>';
        });
    </script>
</html>
```
