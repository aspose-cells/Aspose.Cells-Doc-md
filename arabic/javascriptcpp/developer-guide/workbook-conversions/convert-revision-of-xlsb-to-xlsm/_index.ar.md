---
title: تحويل مراجعة ملفات XLSB إلى XLSM باستخدام جافا سكريبت عبر ++C
linktitle: تحويل مراجعة ملف XLSB إلى ملف XLSM
type: docs
weight: 290
url: /ar/javascript-cpp/convert-revision-of-xlsb-to-xlsm/
description: تعلم كيفية تحويل مراجعات ملفات XLSB بالكامل إلى تنسيق XLSM باستخدام Aspose.Cells for JavaScript عبر ++C
---

{{% alert color="primary" %}}

يدعم Aspose.Cells الآن التحويل الكامل لمراجعات ملفات XLSB إلى ملفات XLSM. تُوجد المراجعات داخل المسار \xl\revisions. يمكنك عرضها عن طريق تغيير امتداد ملف XLSB الخاص بك إلى ZIP. يحتوي مسار \xl\revisions على ملفات تنتهي بامتداد .bin.

عند تحويل ملف XLSB الخاص بك إلى ملف XLSM باستخدام Aspose.Cells، يتم تحويل هذه ملفات .bin بنجاح إلى ملفات .xml كما هو موضح في هاتين اللقطتين.

{{% /alert %}}

يعرض مثال الكود التالي كيفية تحويل ملف XLSB إلى تنسيق XLSM باستخدام Aspose.Cells for JavaScript عبر ++C

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert XLSB to XLSM Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb, .xls, .xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save Workbook to XLSM format
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted XLSM File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook converted to XLSM successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
