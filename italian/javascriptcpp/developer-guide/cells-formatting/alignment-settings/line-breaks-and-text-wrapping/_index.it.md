---
title: Interruzioni di riga e a capo automatico del testo
linktitle: Interruzioni di riga e a capo automatico del testo
description: Come implementare il ritorno a capo del testo e la parola a capo usando la libreria Aspose.Cells in JavaScript tramite C++. Con la libreria Aspose.Cells, puoi facilmente inserire testo nelle celle e impostare il metodo di ritorno a capo, come ad esempio riga manuale, word wrap, ecc. Questo documento illustra come implementare queste funzionalità e fornisce codice di esempio per il tuo riferimento.
keywords: Aspose.Cells, interruzioni di linea, ritorno a capo del testo, layout del testo JavaScript tramite C++
type: docs
weight: 60
url: /it/javascript-cpp/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}
Per garantire che il testo in una cella possa essere letto, possono essere applicati ritorni a capo espliciti e a capo automatico del testo. Il ritorno a capo del testo trasforma una riga in più in una cella, mentre i ritorni a capo espliciti inseriscono spazi esattamente dove si desidera.
{{% /alert %}}

## **Per incapsulare il testo in una cella**
Per avvolgere il testo in una cella, usa il metodo [**Aspose.Cells.Style.isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook
            }

            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cell = ws.cells;

            // Increase the width of First Column Width
            cell.columns.get(0).width = 35;

            // Increase the height of first row
            cell.rows.get(0).height = 36;

            // Add Text to the First Cell
            const firstCell = cell.checkCell(0, 0);
            firstCell.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Per utilizzare ritorni a capo espliciti**
Puoi usare ‘\n’ in JavaScript per inserire interruzioni di riga esplicite in una cella.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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
            let wb;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                wb = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // No file selected - create a new workbook
                wb = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = wb.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 65;

            // Add Text to the First Cell with Explicit Line Breaks
            const firstCell = cells.checkCell(0, 0);
            firstCell.putValue("I am using\nthe latest version of \nAspose.Cells to \ntest this functionality");

            // Make Cell's Text wrap
            const style = firstCell.style;
            style.isTextWrapped = true;
            firstCell.style = style;

            // Save Excel File
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
