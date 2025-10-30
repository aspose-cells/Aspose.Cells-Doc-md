---
title: Exportera dokumentstruktur vid konvertering till PDF med JavaScript via C++
linktitle: Exportera dokumentstruktur vid konvertering till PDF
type: docs
weight: 360
url: /sv/javascript-cpp/export-document-structure-while-converting-to-pdf/
description: Lär dig hur man exporterar dokumentstrukturen vid konvertering av en Excel fil till en märkt PDF med Aspose.Cells for JavaScript via C++.
---

PDF-logiska strukturfaciliteter ger en mekanism för att införliva information om dokumentinnehållets struktur i en PDF-fil. Aspose.Cells for JavaScript via C++ behåller information om strukturen från ett Microsoft Excel-dokument, såsom cell, rad, tabell, arbetsblad, bild, form, sidhuvud-/sidfot m.m.

Med alternativet [PdfSaveOptions.exportDocumentStructure()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#exportDocumentStructure--) kan du spara till en märkt PDF med den exporterade dokumentstrukturen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export PDF with Document Structure</title>
    </head>
    <body>
        <h1>Export PDF with Document Structure</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set to export document structure.
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.exportDocumentStructure = true;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF exported successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
