---
title: الحصول على مجموعات الرموز، شرائط البيانات، أو كائنات المقياس اللوني المستخدمة في التنسيق الشرطي
linktitle: الحصول على مجموعات الرموز، شرائط البيانات، أو كائنات المقياس اللوني المستخدمة في التنسيق الشرطي
description: تعلم كيفية استخدام Aspose.Cells for JavaScript عبر C++ لاسترداد مجموعات الأيقونات وأعمدة البيانات ومقاييس الألوان في التنسيق الشرطي من ملفات الجدول.
keywords: Aspose.Cells، التنسيق الشرطي، مجموعة الأيقونات، عمود البيانات، مقياس الألوان، الجدول، جافا سكريبت عبر C++
type: docs
weight: 10
url: /ar/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}}  

أحيانًا ، تحتاج إلى استرداد مجموعات الرموز التي تستخدم في التنسيق الشرطي لخلية أو مجموعة من الخلايا وترغب في إنشاء ملف صور استنادًا إلى ذلك. قد تحتاج إلى قراءة شرائط البيانات أو مقاييس الألوان المستخدمة في التنسيق الشرطي. تدعم Aspose.Cells هذه الميزة.

{{% /alert %}}  

يظهر نموذج الشفرة التالي كيفية قراءة مجموعات الأيقونات المستخدمة للتنسيق الشرطي. بواسطة واجهة برمجة التطبيقات البسيطة لـ Aspose.Cells، يتم حفظ بيانات صورة مجموعة الأيقونات كصورة.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Extract Conditional Formatting Icon</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultEl = document.getElementById('result');

            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon and create a downloadable blob
            const imageData = icon.imageData;
            const blob = new Blob([imageData], { type: 'image/jpeg' });

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Extracted Icon Image';

            resultEl.innerHTML = '<p style="color: green;">Icon image extracted. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
