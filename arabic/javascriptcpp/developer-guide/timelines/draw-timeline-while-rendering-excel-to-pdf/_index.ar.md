---
title: رسم مخطط زمني أثناء عرض إكسل كملف PDF باستخدام جافا سكريبت عبر C++
linktitle: رسم الجدول الزمني أثناء تحويل إكسيل إلى PDF
type: docs
weight: 60
url: /ar/javascript-cpp/draw-timeline-while-rendering-excel-to-pdf/
description: إدارة الجداول الزمنية لملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: عرض الجدول الزمني إلى PDF بدون Office 2013، Office 2016، Office 2019 وOffice 365 باستخدام جافا سكريبت عبر C++
---

## **رسم الجدول الزمني أثناء تحويل Excel إلى PDF**
 إذا كان لديك ملف إكسل يحتوي على جدول زمني وتريد تصديره إلى PDF مع إعدادات الجدول الزمني، يدعم Aspose.Cells for JavaScript عبر C++ ذلك بشكل افتراضي. ببساطة، صدر ملف إكسل مع جدول زمني إلى PDF، وسيعرض PDF الناتج الجدول الزمني المطبق.

الكود النموذجي التالي يحمل [ملف Excel عيني](input.xlsx) الذي يحتوي على جدول زمني موجود. ثم يحفظ المصنف كـ [ملف PDF الناتج](out.pdf). اللقطة الشاشية التالية تقارن ملف Excel المصدر بالملف PDF المعدل.

<img src="out.png" width="60%">

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook to PDF format (browser)
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
