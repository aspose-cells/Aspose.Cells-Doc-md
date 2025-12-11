---
title: Ignore Errors while Rendering Excel to PDF with JavaScript via C++
linktitle: Ignore Errors while Rendering Excel to PDF
type: docs
weight: 80
url: /javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Learn how to ignore errors during the conversion of Excel files to PDF using Aspose.Cells for JavaScript via C++.
---

## **Possible Usage Scenarios**  

Sometimes when you convert your Excel file to PDF, errors or exceptions occur and the conversion process terminates. You can ignore all such errors during the conversion process by using the [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) property. This way, the conversion process will complete smoothly without throwing any error or exception, but data loss may occur. Therefore, please use this property only if the loss of data is not critical for you.  

## **Ignore Errors while Rendering Excel to PDF**  

The following code loads the [sample Excel file](55541778.xlsx), which is erroneous and throws an error during [conversion to PDF](55541779.pdf) in version 17.11. However, because we are using the [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--) property, the error is not thrown. One *rounded red arrow‑like shape*, as shown in this screenshot, is lost.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Sample Code**  

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