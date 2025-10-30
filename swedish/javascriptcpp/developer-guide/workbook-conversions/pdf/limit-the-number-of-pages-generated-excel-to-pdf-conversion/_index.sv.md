---
title: Begränsa antalet genererade sidor  Excel till PDF konvertering med JavaScript via C++
linktitle: Begränsa antalet genererade sidor  Excel till PDF konvertering
type: docs
weight: 180
url: /sv/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lär dig hur man begränsar antalet sidor som genereras vid konvertering av ett Excel ark till PDF med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Ibland vill du skriva ut ett urval av sidor till en utdata-PDF-fil. Aspose.Cells for JavaScript via C++ har möjlighet att sätta en gräns för hur många sidor som genereras vid konvertering av ett Excel-ark till PDF-format.

{{% /alert %}}

## **Begränsning av antalet genererade sidor**

Följande exempel visar hur man renderar en rad sidor (3 och 4) i en Microsoft Excel-fil till PDF.

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

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) precis innan du renderar det till PDF. Det säkerställer att värden som är beroende av formler omberäknas och att de rätta värdena visas i output-filen.

{{% /alert %}}
