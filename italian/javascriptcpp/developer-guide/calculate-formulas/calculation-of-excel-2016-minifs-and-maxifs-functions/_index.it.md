---
title: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016 con JavaScript tramite C++
description: Questo articolo introduce come usare la libreria Aspose.Cells per calcolare le funzioni MINIFS e MAXIFS in Microsoft Excel 2016 usando JavaScript tramite C++. Carica un file Excel esistente o creane uno nuovo, quindi usa i metodi Aspose.Cells per calcolare queste funzioni e salva i risultati su disco.
keywords: Aspose.Cells, Excel, 2016, funzione MINIFS, funzione MAXIFS, calcolo JavaScript tramite C++
type: docs
weight: 300
url: /it/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel 2016 supporta le funzioni MINIFS e MAXIFS. Queste funzioni non sono supportate in Excel 2013 o versioni precedenti. Aspose.Cells for JavaScript tramite C++ supporta anche il calcolo di queste funzioni. La schermata seguente mostra come vengono utilizzate queste funzioni. Si prega di leggere i commenti rossi all’interno della schermata per sapere come funzionano queste funzioni.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016**
Il codice di esempio seguente carica il [file excel di esempio](5115149.xlsx) e chiama il metodo [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) per eseguire il calcolo della formula tramite Script Aspose.Cells for Java via C++, e poi salva i risultati nel [PDF output](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
