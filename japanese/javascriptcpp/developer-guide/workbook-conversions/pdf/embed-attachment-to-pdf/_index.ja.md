---
title: C++経由でJavaScriptを使ってPDFに添付ファイルを埋め込む
linktitle: PDFに添付を埋め込む
type: docs
weight: 380
url: /ja/javascript-cpp/embed-attachment-to-pdf/
description: C++経由のAspose.Cells for JavaScriptを使用して、OLEオブジェクトを添付ファイルとしてPDFに埋め込む方法を学ぶ。
---

Excelでは、ソースデータを持つOleオブジェクトを挿入できます（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。Oleオブジェクトをダブルクリックすると、埋め込まれたファイルが開きます。

一般的に、PDFに変換する際、OLEオブジェクトはアイコンやサムネイルとして表示され、OLEオブジェクトのソースデータは表示されません。オプション[PdfSaveOptions.embedAttachments()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#embedAttachments--)を使用すると、OLEオブジェクトのソースデータを添付ファイルとしてPDFに埋め込むことができます。PDF内のアイコンまたはサムネイルをダブルクリックすると、OLEオブジェクトのソースファイルを開くことができます。

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
