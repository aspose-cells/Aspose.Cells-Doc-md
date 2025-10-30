---
title: Inkludera bilaga i PDF med JavaScript via C++
linktitle: Inbädda bilaga till PDF
type: docs
weight: 380
url: /sv/javascript-cpp/embed-attachment-to-pdf/
description: Lär dig hur man inkluderar en Ole objekt som en bilaga i en PDF med Aspose.Cells for JavaScript via C++.
---

I Excel kan du infoga ett Ole-objekt med källdata ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Dubbelklicka på Ole-objektet, och den inbäddade filen öppnas.

Generellt, vid konvertering till PDF, kommer Ole-objektet att visas som en ikon eller miniatyrbild utan källinformation för Ole-objektet. Med alternativet [PdfSaveOptions.embedAttachments()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#embedAttachments--) kan du bädda in Ole-objektets källinformation som en bilaga i PDF:en. Dubbelklicka på ikonen eller miniatyrbilden i PDF för att öppna källfilen för Ole-objektet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Embed Attachments to PDF</title>
    </head>
    <body>
        <h1>Embed Attachments to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Set to embed Ole Object attachment.
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.embedAttachments = true;

            // Save the pdf file with PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

![embedded-attachment.png](embedded-attachment.png)
