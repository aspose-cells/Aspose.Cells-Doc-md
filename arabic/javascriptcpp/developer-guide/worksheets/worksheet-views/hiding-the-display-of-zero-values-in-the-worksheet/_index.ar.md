---
title: إخفاء عرض القيم الصفرية في ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: إخفاء عرض القيم الصفرية في ورقة العمل
type: docs
weight: 50
url: /ar/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: ستوضح لك هذه المقالة رمز عينة يشرح كيفية إخفاء القيم الصفرية بشكل برمجي في جدول بيانات إكسل باستخدام مكتبة جافا سكريبت عبر C++.
keywords: إخفاء القيم الصفرية في ورقة عمل إكسل باستخدام جافا سكريبت عبر C++
---

{{% alert color="primary" %}} 

في بعض الأحيان، تحتاج إلى إخفاء القيم الصفرية في جدول بيانات. قد يكون اختيار شخصي أو معيار تنسيق.

{{% /alert %}} 

لإخفاء القيم الصفرية في ورقة العمل في Microsoft Excel (على سبيل المثال Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**، ثم حدد علامة تبويب **العرض**.
1. ألغِ تحديد خيار **قيم الصفر**.
1. انقر على **موافق**.

 يرجى الاطلاع على رمز العينة التالي الذي يوضح إخفاء الأصفار باستخدام Aspose.Cells for JavaScript عبر C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Zero Values Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get First worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Hide the zero values in the sheet
            sheet.displayZeros = false;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputfile.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
