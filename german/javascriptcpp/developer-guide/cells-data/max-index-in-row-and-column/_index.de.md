---
title: Maximalen Spaltenindex in Zeile und maximalen Zeilenindex in Spalte erhalten
type: docs
weight: 600
url: /de/javascript-cpp/get-max-index-in-row-and-column/
description: Erfahren Sie, wie man die maximale Spaltenindex in einer Zeile und die maximale Zeilennummer in einer Spalte über das Aspose.Cells for JavaScript via C++ API erhält.
keywords: Maximalen Spaltenindex in einer Zeile JavaScript via C++, Maximalen Zeilennummer in einer Spalte JavaScript via C++, Maximalen Daten Spaltenindex in einer Zeile JavaScript via C++, Maximalen Daten Zeilennummer in einer Spalte JavaScript via C++
---

## **Mögliche Verwendungsszenarien**
Wenn Sie nur einzelne Daten in Zeilen oder Spalten manipulieren möchten, müssen Sie den Datenbereich der Zeilen und Spalten kennen. Das Aspose.Cells for JavaScript via C++ bietet diese Funktion. Um den maximalen Spaltenindex in einer Zeile zu erhalten, können Sie die Methoden [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--) und [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--) verwenden und dann die Methode [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--), um den maximalen Spaltenindex und den maximalen Daten-Spaltenindex zu erhalten. Um den maximalen Zeilenindex und den maximalen Zeilendatenindex in einer Spalte zu erhalten, müssen Sie einen Bereich auf der Spalte erstellen, dann den Bereich durchlaufen, um die letzte Zelle zu finden, und schließlich die Methode [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) auf der Zelle aufrufen.

Aspose.Cells for JavaScript via C++ stellt die folgenden Eigenschaften und Methoden bereit, um Ihre Ziele zu erreichen.
- [**Row.lastCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastCell--)
- [**Row.lastDataCell**](https://reference.aspose.com/cells/javascript-cpp/row/#lastDataCell--)
- [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--)
- [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--)

## **Maximalen Spaltenindex in einer Zeile und Maximalen Zeilenindex in einer Spalte ermitteln**
Dieses Beispiel zeigt, wie Sie:

1. Laden Sie die [Beispieldatei](sample.xlsx).
1. Die Zeile abrufen, für die der maximale Spaltenindex und der maximale Daten-Spaltenindex benötigt werden.
1. Rufen Sie die [**Cell.column**](https://reference.aspose.com/cells/javascript-cpp/cell/#column--) Methode auf der Zelle auf.
1. Basierend auf der Spalte einen Bereich erstellen.
1. Iterator abrufen und den Bereich durchlaufen.
1. Rufen Sie die [**Cell.row**](https://reference.aspose.com/cells/javascript-cpp/cell/#row--) Methode auf der Zelle auf.

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
