---
title: Ignora errori durante il rendering di Excel in PDF con JavaScript via C++
linktitle: Ignora gli errori durante la conversione di Excel in PDF
type: docs
weight: 80
url: /it/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Impara come ignorare gli errori durante la conversione di file Excel in PDF usando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**  

A volte, quando converti il file Excel in PDF, si verificano errori o eccezioni e il processo di conversione termina. Puoi ignorare tutti questi errori durante il processo di conversione usando la proprietà [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--). In questo modo, il processo di conversione si completerà senza generare errori o eccezioni, ma potrebbe verificarsi perdita di dati. Quindi, utilizza questa proprietà solo se la perdita di dati non è critica per te.  

## **Ignora gli errori durante la conversione di Excel in PDF**  

Il seguente codice carica il [file Excel di esempio](55541778.xlsx) ma il file Excel di esempio è errato e genera un errore durante [conversione in PDF](55541779.pdf) in 17.11, ma poiché utilizziamo la proprietà [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--), non viene generato alcun errore. Tuttavia, una *forma a freccia rossa arrotondata* come mostrato in questa schermata viene persa.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Codice di Esempio**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
