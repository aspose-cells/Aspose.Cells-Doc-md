---
title: استخراج بيانات النسق من ملف Excel
linktitle: استخراج بيانات النسق من ملف Excel
description: تعلم كيفية استخراج بيانات السمة من ملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++. احصل على معلومات الأسلوب والتنسيق بشكل فعال.
keywords: Aspose.Cells، ملف إكسل، بيانات السمة، الأسلوب، التنسيق، جافا سكريبت عبر C++
type: docs
weight: 120
url: /ar/javascript-cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

تسمح Aspose.Cells للمستخدمين باستخراج بيانات ذات صلة بالموضوع من ملف Excel. على سبيل المثال، يمكنك استخراج اسم الموضوع المطبق على الدفتر ولون الموضوع المطبق على الخلية أو حدود الخلية، إلخ.

يمكنك تطبيق الموضوع على دفتر عملك باستخدام Microsoft Excel عبر الأمر تخطيط الصفحة > الموضوع.

{{% /alert %}}

## رمز JavaScript لاستخراج بيانات الثيم من ملف Excel

يستخرج رمز النموذج التالي اسم السمة المطبقة على دفتر العمل المصدر ثم يستخرج لون السمة المطبق على الخلية A1 ولون السمة المطبق على الحد السفلي للخلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; }
            #result p { margin: 6px 0; }
        </style>
    </head>
    <body>
        <h1>Aspose.Cells Theme & Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, Utils } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Extract theme name applied to this workbook
            const themeName = workbook.theme;
            resultDiv.innerHTML += `<p>Workbook theme: ${themeName}</p>`;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Get the style object
            const style = cell.style;

            if (style.foregroundThemeColor != null) {
                // Extract theme color applied to this cell if theme has foreground theme color defined
                const fgColorType = style.foregroundThemeColor.colorType;
                resultDiv.innerHTML += `<p>Foreground theme color type: ${fgColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not foreground color defined.</p>`;
            }

            // Extract theme color applied to the bottom border of the cell if theme has border color defined
            const bot = style.borders.get(BorderType.BottomBorder);
            if (bot.themeColor != null) {
                const botColorType = bot.themeColor.colorType;
                resultDiv.innerHTML += `<p>Bottom border theme color type: ${botColorType}</p>`;
            } else {
                resultDiv.innerHTML += `<p>Theme has not Border color defined.</p>`;
            }

            // No file is produced here, but keep download link hidden
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.style.display = 'none';
            downloadLink.href = '#';
            downloadLink.textContent = '';
        });
    </script>
</html>
```
