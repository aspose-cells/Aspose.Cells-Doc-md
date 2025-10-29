---
title: تعطيل تصدير سكربتات الإطار وخصائص المستند باستخدام JavaScript عبر C++
linktitle: تعطيل تصدير الإطارات النصية وخصائص المستند
type: docs
weight: 310
url: /ar/javascript-cpp/disable-exporting-frame-scripts-and-document-properties/
description: تعلم كيفية تعطيل تصدير سكربتات الإطار وخصائص المستند عند تحويل كتاب إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
--- 

{{% alert color="primary" %}}

 يقوم Aspose.Cells بتصدير سكربتات الإطار وخصائص المستند أثناء تحويل كتاب إلى HTML. الإصدار 8.6.0 من Aspose.Cells for JavaScript عبر C++ يقدم خيارًا يسمح لك بتعطيل تصدير سكربتات الإطار وخصائص المستند بشكل اختيارى. يرجى استخدام خاصية `HtmlSaveOptions.exportFrameScriptsAndProperties` لتعطيل التصدير.

{{% /alert %}}

## **تعطيل تصدير الإطارات النصية وخصائص المستند**

الشيفرة النموذجية التالية تتيح لك تعطيل تصدير الإطارات النصية وخصائص المستند. بمجرد تحويل دفتر العمل إلى HTML، لن يحتوي الملف الناتج على أي إطارات نصية أو خصائص مستند.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable exporting frame scripts and document properties
            const options = new HtmlSaveOptions();
            options.exportFrameScriptsAndProperties = false;

            // Save workbook as HTML
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
