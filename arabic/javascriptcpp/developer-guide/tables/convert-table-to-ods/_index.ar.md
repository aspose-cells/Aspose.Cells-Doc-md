---
title: تحويل الجدول إلى ODS باستخدام JavaScript عبر C++
linktitle: تحويل الجدول إلى ملف ODS
type: docs
weight: 70
url: /ar/javascript-cpp/convert-table-to-ods/
description: تعلم كيفية تحويل ملف Excel يحتوي على جدول إلى تنسيق ODS باستخدام Aspose.Cells for JavaScript عبر C++.
---

يدعم Aspose.Cells تحويل ملف Excel يحتوي على جدول إلى ملف ODS. عليك فقط حفظ الملف بتنسيق ODS وسيحتوي ملف ODS الناتج على جدول يعمل بشكل صحيح.

## كود عينة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Table to ODS Example</title>
    </head>
    <body>
        <h1>Convert Table to ODS Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Opening the Excel file from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the file to ODS format and providing download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertTableToOds_out.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted successfully! Click the download link to get the ODS file.</p>';
        });
    </script>
</html>
```

الملف ODS الناتج من كود العينة مرفق للرجوع إليه.

[**Output ODS File**](ConvertTableToOds_out.ods)
