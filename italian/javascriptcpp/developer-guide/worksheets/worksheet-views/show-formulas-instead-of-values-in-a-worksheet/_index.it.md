---
title: Mostra le formule invece dei valori in un foglio di lavoro con JavaScript tramite C++
linktitle: Mostrare le Formule invece dei Valori in un Foglio di Lavoro
type: docs
weight: 20
url: /it/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/
description: Questo articolo fornisce un esempio di codice per usare l API JavaScript tramite C++ per visualizzare programmaticamente le formule anziché i valori in un foglio di lavoro o spreadsheet Excel.
---

{{% alert color="primary" %}}

È possibile mostrare le formule invece dei valori calcolati in Microsoft Excel utilizzando l'opzione **Mostra formule** nella scheda **Formule**. Quando le formule sono mostrate, Microsoft Excel visualizza le formule nel foglio di lavoro. Puoi ottenere lo stesso risultato usando Aspose.Cells for JavaScript tramite C++.

{{% /alert %}}

Aspose.Cells fornisce una proprietà [**Worksheet.showFormulas**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#showFormulas--). Impostala a **true** per far sì che Microsoft Excel visualizzi le formule.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Show Formulas Example</title>
    </head>
    <body>
        <h1>Show Formulas Example</h1>
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

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Show formulas of the worksheet
            worksheet.showFormulas = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'source.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas are now visible. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
