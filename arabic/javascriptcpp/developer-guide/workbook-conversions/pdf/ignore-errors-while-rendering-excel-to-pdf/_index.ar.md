---
title: تجاهل الأخطاء أثناء تصيير إكسل إلى PDF باستخدام JavaScript عبر C++
linktitle: تجاهل الأخطاء أثناء تحويل Excel إلى PDF
type: docs
weight: 80
url: /ar/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: تعلم كيفية تجاهل الأخطاء أثناء تحويل ملفات إكسل إلى PDF باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

أحيانًا عند تحويل ملف إكسيل إلى PDF، تحدث أخطاء أو استثناءات وتنتهي عملية التحويل. يمكنك تجاهل جميع هذه الأخطاء أثناء عملية التحويل باستخدام خاصية [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--). وبهذا، ستكتمل عملية التحويل بسلاسة دون إظهار أي خطأ أو استثناء، ولكن قد يحدث فقدان للبيانات. لذا، يرجى استخدام هذه الخاصية فقط إذا لم يكن فقدان البيانات مهمًا بالنسبة لك.  

## **تجاهل الأخطاء أثناء تحويل Excel إلى PDF**  

الكود التالي يحمل ملف إكسيل نمونه (sample Excel file) ولكن الملف يحتوي على أخطاء ويثير خطأ أثناء التحويل إلى PDF في 17.11، ولكن نظرًا لاستخدامنا خاصية [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--)، فلا يثير الخطأ. ومع ذلك، فإن شكل سهم أحمر مستدير مماثل كما في لقطة الشاشة يُفقد.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
