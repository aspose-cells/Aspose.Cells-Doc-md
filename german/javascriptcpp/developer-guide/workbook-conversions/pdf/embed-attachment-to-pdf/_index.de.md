---
title: Anfügen eines Objekts an PDF mit JavaScript via C++
linktitle: Anhang in PDF einbetten
type: docs
weight: 380
url: /de/javascript-cpp/embed-attachment-to-pdf/
description: Erfahren Sie, wie man ein Ole Objekt als Anhang in einer PDF mit Aspose.Cells for JavaScript via C++ einbettet.
---

In Excel können Sie ein Ole-Objekt mit Quelldaten einfügen ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Klicken Sie doppelt auf das Ole-Objekt, und die eingebettete Datei wird geöffnet.

Im Allgemeinen wird beim Konvertieren in PDF das Ole-Objekt als Symbol oder Miniaturbild ohne die Quelldaten des Ole-Objekts dargestellt. Mit der Option [PdfSaveOptions.embedAttachments()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#embedAttachments--) können Sie die Quelldaten des Ole-Objekts als Anhang in der PDF einbetten. Klicken Sie doppelt auf das Symbol oder die Miniatur in der PDF, um die Quelldatei des Ole-Objekts zu öffnen.

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
