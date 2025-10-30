---
title: Nascondere la visualizzazione di valori Zero nel Foglio di Lavoro con JavaScript tramite C++
linktitle: Nascondere la Visualizzazione dei Valori Zero nel Foglio di Lavoro
type: docs
weight: 50
url: /it/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Questo articolo ti mostrerà un esempio di codice che spiega come nascondere programmaticamente i valori zero in un foglio Excel utilizzando la libreria JavaScript tramite C++.
keywords: nascondere valori zero del foglio di lavoro di Excel in JavaScript tramite C++
---

{{% alert color="primary" %}} 

A volte è necessario nascondere i valori zero in un foglio di calcolo. Potrebbe essere una preferenza personale o uno standard di formattazione.

{{% /alert %}} 

Per nascondere i valori zero in un foglio di lavoro in Microsoft Excel (ad esempio Microsoft Excel 2003):

1. Dal menu **Strumenti**, selezionare **Opzioni**, e quindi selezionare la scheda **Visualizza**.
1. Deselezionare l'opzione **Valori zero**.
1. Fai clic su **OK**.

Vedi il seguente esempio di codice che dimostra come nascondere gli zeri usando Aspose.Cells for JavaScript tramite C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
