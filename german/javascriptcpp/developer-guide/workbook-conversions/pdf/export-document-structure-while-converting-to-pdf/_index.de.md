---
title: Exportieren der Dokumentenstruktur beim Konvertieren in PDF mit JavaScript via C++
linktitle: Exportieren der Dokumentstruktur beim Konvertieren in PDF
type: docs
weight: 360
url: /de/javascript-cpp/export-document-structure-while-converting-to-pdf/
description: Erfahren Sie, wie Sie die Dokumentenstruktur beim Konvertieren einer Excel Datei in ein getaggtes PDF mit Aspose.Cells for JavaScript via C++ exportieren.
---

Die logisch-strukturellen PDF-Funktionen bieten einen Mechanismus zur Integration von Informationen über die Dokumenteninhaltstruktur in eine PDF-Datei. Aspose.Cells for JavaScript via C++ erhält Informationen über die Struktur aus einem Microsoft Excel-Dokument, z.B. Zellen, Zeilen, Tabellen, Arbeitsblätter, Bilder, Formen, Kopf- und Fußzeilen usw.

Mit der Option [PdfSaveOptions.exportDocumentStructure()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#exportDocumentStructure--) können Sie die exportierte, strukturierte, getaggte PDF speichern.

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
