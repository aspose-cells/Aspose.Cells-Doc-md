---
title: تضمين مرفق في PDF باستخدام JavaScript عبر C++
linktitle: تضمين مرفق في ملف PDF
type: docs
weight: 380
url: /ar/javascript-cpp/embed-attachment-to-pdf/
description: تعلم كيفية تضمين كائن Ole كمرفق في ملف PDF باستخدام Aspose.Cells for JavaScript عبر C++.
---

في Excel، يمكنك إدراج كائن Ole بمصدر البيانات ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). انقر نقرًا مزدوجًا على كائن Ole، وسيتم فتح الملف المضمن.

 بشكل عام، عند التحويل إلى PDF، سيتم عرض كائن Ole كرمز أو صورة مصغرة بدون بيانات مصدر كائن Ole. مع خيار [PdfSaveOptions.embedAttachments()](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#embedAttachments--) يمكنك دمج بيانات مصدر كائن Ole كمرفق في PDF. يمكنك النقر المزدوج على الرمز أو الصورة المصغرة في PDF لفتح ملف المصدر الخاص بكائن Ole.

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
