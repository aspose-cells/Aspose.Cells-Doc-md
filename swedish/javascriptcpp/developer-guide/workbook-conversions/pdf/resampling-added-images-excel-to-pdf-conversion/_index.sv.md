---
title: Resampling av tillagda bilder  Excel till PDF konvertering med JavaScript via C++
linktitle: Resampling tillagda bilder
type: docs
weight: 150
url: /sv/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Lär dig hur man komprimerar bilder som lagts till i Excel filer för att minska PDF storleken och förbättra konverteringsprestandan med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

När du arbetar med stora Microsoft Excel-filer med många bilder kan du behöva komprimera bilder som lagts till för att minska storleken på den exporterade PDF-filen och förbättra den totala konverteringsprestandan. Aspose.Cells for JavaScript via C++ stöder återresampling av tillagda bilder för att minska PDF-filens storlek och förbättra prestanda.

{{% /alert %}}

Se följande exempelkod som beskriver hur man utför uppgiften med hjälp av Aspose.Cells API. Exemplet konverterar en Microsoft Excel-fil till en PDF-fil samtidigt som bilderna i filen komprimeras.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Genom att använda alternativet [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) minimerar storleken på utdata-PDF men kan påverka bildkvaliteten något.

{{% /alert %}} {{% alert color="primary" %}}

Om ditt kalkylblad innehåller formler, är det bäst att anropa [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
