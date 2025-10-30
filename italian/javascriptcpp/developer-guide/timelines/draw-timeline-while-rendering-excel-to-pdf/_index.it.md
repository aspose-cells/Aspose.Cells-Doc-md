---
title: Disegna la Timeline durante il rendering di Excel in PDF con JavaScript tramite C++
linktitle: Disegna la Timeline durante la rappresentazione di Excel in PDF
type: docs
weight: 60
url: /it/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gestisci le timeline dei file Excel con Aspose.Cells for JavaScript tramite C++.
keywords: Rendering della timeline in pdf senza Office 2013, Office 2016, Office 2019 e Office 365 JavaScript tramite C++
---

## **Disegna la Timeline durante la rappresentazione di Excel in PDF**
Se hai un file Excel a cui è applicata una timeline e vuoi esportare l'Excel in PDF con le impostazioni della timeline, Aspose.Cells for JavaScript tramite C++ supporta ora questa funzione di default. Basta esportare il file Excel con timeline in PDF, e il PDF generato mostrerà la timeline applicata.

Il seguente codice di esempio carica il [file di Excel di esempio](input.xlsx) che contiene un timeline esistente. Salva poi il workbook come [file PDF di output](out.pdf). La seguente schermata confronta il file di Excel di origine e il file PDF generato.

<img src="out.png" width="60%">

## **Codice di Esempio**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
