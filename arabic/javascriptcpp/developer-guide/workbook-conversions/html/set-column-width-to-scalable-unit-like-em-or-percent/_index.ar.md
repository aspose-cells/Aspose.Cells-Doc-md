---
title: ضبط عرض العمود كوحدة قابلة للتوسع مثل em أو ٪ باستخدام JavaScript عبر C++
linktitle: ضبط عرض العمود كوحدة قابلة للتكبير مثل em أو النسبة المئوية
type: docs
weight: 130
url: /ar/javascript-cpp/set-column-width-to-scalable-unit-like-em-or-percent/
description: تعلم كيفية ضبط عرض العمود كوحدات قابلة للتوسع مثل em أو ٪ في Aspose.Cells for JavaScript عبر C++. حسن عرض جداول HTML الناتجة.
---

إنشاء ملف HTML من جدول بيانات أمر شائع جدًا. حجم الأعمدة معرف بواسطة "نقطة"، والذي يعمل في العديد من الحالات. ومع ذلك، قد يكون هناك حالة لا يتطلب فيها هذا الحجم الثابت. على سبيل المثال، إذا كان عرض لوحة الحاوية هو 600 بكسل، حيث يتم عرض صفحة HTML هذه، فقد تحصل على شريط تمرير أفقي إذا كان عرض الجدول المولد أكبر. كان من المطلوب تحويل هذا الحجم الثابت إلى وحدة قابلة للتطوير مثل em أو النسبة المئوية للحصول على عرض أفضل. يمكن استخدام الشفرة النموذجية التالية حيث يتم تعيين [**HtmlSaveOptions.widthScalable**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#widthScalable--) إلى **true** لإنشاء عرض قابل للتطوير.

يمكن تنزيل ملف المصدر العيني وملفات الإخراج من الروابط التالية:

[sampleForScalableColumns.xlsx](73990150.xlsx)

[outsampleForScalableColumns.zip](73990151.zip)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Scalable Columns to HTML</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, HtmlSaveOptions, SaveFormat } = AsposeCells;

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

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // Set the property for scalable width (converted from setWidthScalable)
            options.widthScalable = true;

            // Specify image save format (converted from setExportImagesAsBase64)
            options.exportImagesAsBase64 = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outsampleForScalableColumns.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File converted to HTML successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
