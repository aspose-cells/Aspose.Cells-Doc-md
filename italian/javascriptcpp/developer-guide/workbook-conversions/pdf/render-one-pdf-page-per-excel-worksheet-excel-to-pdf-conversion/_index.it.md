---
title: Renderizza una pagina PDF per ogni foglio Excel  Conversione da Excel a PDF con JavaScript via C++
linktitle: Rendere una pagina PDF per foglio di lavoro di Excel  Conversione di Excel in PDF
type: docs
weight: 100
url: /it/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Quando si lavora con grandi file Microsoft Excel (ad esempio una cartella di lavoro con molti fogli, ognuno con 50 colonne e 300 o più righe di dati), potresti voler che l'output PDF mostri una pagina per foglio, indipendentemente dalla dimensione del foglio. Ciò significherebbe che ogni pagina potrebbe avere dimensioni molto diverse. Questo può essere ottenuto utilizzando {Aspose.Cells for Java}Script via C++.

{{% /alert %}}

Si prega di vedere il seguente codice di esempio che converte un file di Excel con più fogli di lavoro in PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Se l'opzione [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) è impostata su **true**, tutto il contenuto del foglio verrà reso su una singola pagina PDF.

{{% /alert %}} {{% alert color="primary" %}}

Se il tuo foglio di calcolo contiene formule, è meglio chiamare [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) subito prima di rendere il foglio di calcolo in PDF. Questo assicura che i valori dipendenti dalle formule vengano ricalcolati e che i valori corretti siano visualizzati nel PDF.

{{% /alert %}}
