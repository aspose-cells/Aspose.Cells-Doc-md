---
title: Convert Excel file to PDF format compatible with PDF/A-1a with JavaScript via C++
linktitle: Convert Excel file to PDF format compatible with PDF/A-1a
type: docs
weight: 130
url: /javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Learn how to convert Excel files to PDF/A compliant PDF files using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  

PDF/A is a unique flavor of PDF designed for the long‑term preservation of documents. PDF/A is an ISO‑standardized version of the Portable Document Format (PDF), which is an archival format that embeds all fonts used in the document within the PDF file. PDF/A differs from PDF by prohibiting features, such as font linking (as opposed to font embedding) and encryption. Aspose.Cells for JavaScript via C++ enables you to save Excel files to PDF/A‑compliant PDF files (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab, and PDF/A-3u are supported). This topic describes how to save an Excel workbook to a PDF/A‑compliant (PDF/A-1a) PDF file.  

## **Convert Excel file to PDF Format Compatible with PDF/A-1a**  

Developers may use the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class to set different attributes for the conversion. Setting different properties of the [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) class gives you control over the print, font, security, and compression settings for the output PDF. The most important property is [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) which enables you to save Excel files to PDF/A‑compliant PDF files.  

The following sample code explains how to convert an Excel file to PDF format compatible with PDF/A-1a. Please see its [output PDF](outputCompliancePdfA1a.pdf) as well as the screenshot for reference.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Sample Code**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;
        
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDF/A-1a.";

            // Create PDF save options and set its compliance to PDF/A-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output PDF
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```