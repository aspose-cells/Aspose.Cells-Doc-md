---
title: Conta il numero di celle nel foglio di lavoro con JavaScript tramite C++
linktitle: Contare il numero di celle nel foglio di lavoro
type: docs
weight: 110
url: /it/javascript-cpp/count-number-of-cells-in-the-worksheet/
description: Scopri come contare automaticamente il numero di celle in un foglio di lavoro di Excel usando Aspose.Cells for JavaScript tramite C++.
keywords: conta il numero di celle nei fogli di lavoro di Excel JavaScript tramite C++, fogli di lavoro di Excel JavaScript tramite C++
---

Puoi contare il numero di celle nel foglio di lavoro utilizzando le proprietà [**Cells.count**](https://reference.aspose.com/cells/javascript-cpp/cells/#count--) o [**Cells.countLarge**](https://reference.aspose.com/cells/javascript-cpp/cells/#countLarge--) come mostrato nell'esempio di codice riportato di seguito.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cells Count Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get number of cells (regular Count)
            const numberOfCells = worksheet.cells.count;

            // If very large, use CountLarge
            const numberOfCellsLarge = worksheet.cells.countLarge;

            console.log("Number of Cells: " + numberOfCells);
            console.log("Number of Cells (CountLarge): " + numberOfCellsLarge);

            resultDiv.innerHTML = '<p style="color: green;">Number of Cells: ' + numberOfCells + '</p>'
                + '<p style="color: green;">Number of Cells (CountLarge): ' + numberOfCellsLarge + '</p>';
        });
    </script>
</html>
```
