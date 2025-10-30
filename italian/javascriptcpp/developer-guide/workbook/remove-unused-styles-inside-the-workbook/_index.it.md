---
title: Rimuovi stili inutilizzati all interno del Workbook con JavaScript tramite C++
linktitle: Rimuovere gli Stili Non Utilizzati all interno del Workbook
type: docs
weight: 340
url: /it/javascript-cpp/remove-unused-styles-inside-the-workbook/
description: Impara come rimuovere stili inutilizzati da un workbook usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}  
 Gli stili inutilizzati nei file Excel non solo occupano spazio ma causano anche problemi di prestazioni durante la conversione in formati diversi come PDF, HTML, ecc. Aspose.Cells fornisce il funzionalità [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#removeUnusedStyles--) per rimuovere tutti gli stili inutilizzati all’interno del libro di lavoro.  
{{% /alert %}}  

 Il seguente codice spiega l'uso di {0}. Il codice carica il {1} file Excel modello che puoi scaricare dal link fornito. Contiene uno stile inutilizzato chiamato **AsposeStyle**; questo stile e tutti gli altri stili inutilizzati verranno rimossi dopo l'esecuzione del codice.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Unused Styles</title>
    </head>
    <body>
        <h1>Remove Unused Styles Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Remove all unused styles inside the workbook
            workbook.removeUnusedStyles();

            // Save the modified workbook as XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Unused styles removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
