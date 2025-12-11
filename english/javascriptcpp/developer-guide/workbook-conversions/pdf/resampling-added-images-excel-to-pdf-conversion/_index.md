---
title: Resampling Added Images - Excel to PDF Conversion with JavaScript via C++
linktitle: Resampling Added Images
type: docs
weight: 150
url: /javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Learn how to compress images added in Excel files to reduce PDF size and improve conversion performance using Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

While working with large Microsoft Excel files that contain many images, you might need to compress the images to reduce the output PDF file size and improve overall conversion performance. Aspose.Cells for JavaScript via C++ supports resampling added images to reduce the output PDF file size and improve performance somewhat.

{{% /alert %}}

Please see the following sample code that describes how to perform the task using the Aspose.Cells API. The example converts a Microsoft Excel file to a PDF file while compressing the images in the file.

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

Using the [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) option minimizes the size of the output PDF, but it may affect image quality slightly.

{{% /alert %}} {{% alert color="primary" %}}

If your spreadsheet contains formulas, it is best to call [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) just before rendering the spreadsheet to PDF format. Doing so will ensure that the formula‑dependent values are recalculated and the correct values are rendered in the PDF.

{{% /alert %}}