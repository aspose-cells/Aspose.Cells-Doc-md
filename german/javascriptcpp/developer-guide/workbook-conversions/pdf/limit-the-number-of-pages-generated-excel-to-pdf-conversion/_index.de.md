---
title: Begrenzung der Anzahl der generierten Seiten  Excel in PDF Konvertierung mit JavaScript über C++
linktitle: Begrenzen der Anzahl der generierten Seiten  Umsetzung von Excel in PDF
type: docs
weight: 180
url: /de/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lernen Sie, wie Sie die Anzahl der Seiten bei der Umwandlung eines Excel Arbeitsblatts in PDF mit Aspose.Cells for JavaScript über C++ begrenzen. 
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Seitenbereich in eine Ausgabedatei PDF drucken. Aspose.Cells for JavaScript via C++ bietet die Möglichkeit, eine Begrenzung festzulegen, wie viele Seiten bei der Konvertierung eines Excel-Tabellenblatts in das PDF-Format generiert werden.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, kurz vor dem Rendern in PDF [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) aufzurufen. Dies stellt sicher, dass formelabhängige Werte neu berechnet werden und die korrekten Werte in der Ausgabedatei angezeigt werden.

{{% /alert %}}
