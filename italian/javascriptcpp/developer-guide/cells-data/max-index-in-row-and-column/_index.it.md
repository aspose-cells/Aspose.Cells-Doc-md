---
title: Ottenere l Indice Massimo della Colonna nella Riga e l Indice Massimo della Riga nella Colonna
type: docs
weight: 600
url: /it/javascript-cpp/get-max-index-in-row-and-column/
description: Impara come ottenere l indice massimo di colonna in una riga e l indice massimo di riga in una colonna attraverso lo Script Aspose.Cells for Java tramite API C++.
keywords: Ottieni l indice massimo di colonna in una riga JavaScript tramite C++, Ottieni l indice massimo di riga in una colonna JavaScript tramite C++, Ottieni l indice massimo di colonna dati in una riga JavaScript tramite C++, Ottieni l indice massimo di riga dati in una colonna JavaScript tramite C++.
---

## **Possibili Scenari di Utilizzo**
Quando devi manipolare solo alcuni dati sulle righe o colonne, devi conoscere l'intervallo di dati di righe e colonne. Lo Script Aspose.Cells for Java tramite C++ offre questa funzione. Per ottenere l’indice massimo di colonna di una riga, puoi usare i metodi [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) e [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--), e poi usare il metodo [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) per ottenere l’indice massimo di colonna e l’indice massimo di colonna dati. Ma per ottenere l’indice massimo di riga e l’indice massimo di dati di riga su una colonna, devi creare un intervallo sulla colonna, quindi attraversare l’intervallo per trovare l’ultima cella, e infine chiamare il metodo [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) sulla cella.

Lo Script Aspose.Cells for Java tramite C++ fornisce le seguenti proprietà e metodi per aiutarti a raggiungere i tuoi obiettivi.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Ottenere il massimo indice di colonna in riga e il massimo indice di riga in colonna**
Questo esempio mostra come:

1. Caricare il [file di esempio](sample.xlsx).
1. Ottenere la riga che ha bisogno di ottenere l'indice massimo della colonna e l'indice massimo della colonna dei dati.
1. Chiama il metodo [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) sulla cella.
1. Creare un intervallo basato sulla colonna.
1. Ottenere l'iteratore e attraversare l'intervallo.
1. Chiama il metodo [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) sulla cella.

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
