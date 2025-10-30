---
title: Ignorera fel vid renderering av Excel till PDF med JavaScript via C++
linktitle: Ignorera fel vid rendering av Excel till PDF
type: docs
weight: 80
url: /sv/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Lär dig hur man ignorerar fel under konvertering av Excel filer till PDF med Aspose.Cells for JavaScript via C++.
---

## **Möjliga användningsscenario**  

Ibland när du konverterar din Excel-fil till PDF uppstår fel eller undantag och konverteringsprocessen avbryts. Du kan ignorera alla dessa fel under konverteringsprocessen genom att använda [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) egenskapen. På detta sätt kommer konverteringsprocessen att slutföras smidigt utan att kasta något fel eller undantag, men datatapp kan inträffa. Använd därför denna egenskap bara om datatapp inte är kritiskt för dig.  

## **Ignorera fel vid rendering av Excel till PDF**  

Följande kod laddar [exempel Excel-fil](55541778.xlsx), men filen är felaktig och kastar ett fel under [konvertering till PDF](55541779.pdf) i 17.11, men eftersom vi använder [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) egenskapen, kastas inget fel. Men en *rundad röd pil-liknande form* som visas i skärmdumpen förloras.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Exempelkod**  

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
