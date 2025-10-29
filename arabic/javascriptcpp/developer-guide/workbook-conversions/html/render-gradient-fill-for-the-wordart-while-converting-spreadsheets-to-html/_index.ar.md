---
title: عرض تدرج ملء لWordArt أثناء تحويل الجداول إلى HTML باستخدام JavaScript عبر C++
linktitle: عرض تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى صيغة HTML
type: docs
weight: 90
url: /ar/javascript-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/
description: تعلم كيفية عرض تدرج ملء لـWordArt عند تحويل جداول البيانات إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  
قبل إصدار Aspose.Cells 17.1، لم يكن يدعم عرض تدرج ملء WordArt عند تحويل ملف إكسل إلى تنسيق HTML. منذ إصدار Aspose.Cells 17.1، يُدعم تدرج ملء WordArt. تُقارن لقطة الشاشة التالية تأثير التدرج عند تحويل ملف إكسل باستخدام Aspose.Cells 17.1 والإصدار الأقدم.  

![todo:image_alt_text](render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to-html_1.png)  

## **عرض تعبئة التدرج لكلمة WordArt أثناء تحويل جداول البيانات إلى صيغة HTML**  
يُحوِّل الكود النموذجي التالي [ملف الإكسل المصدر](22774111.xlsx) إلى [صيغة HTML المخرجة](22774109.zip) إنّ مصدر ملف الإكسل يتضمن كائن WordArt مع تدرج ملء كما هو موضح في لقطة الشاشة أعلاه.  

## **الكود المثالي**  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Source Gradient Fill</title>
    </head>
    <body>
        <h1>Source Gradient Fill to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to HTML</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xls, .xlsx, .csv).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save workbook to HTML format
            const outputData = workbook.save(SaveFormat.Html);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sourceGradientFill.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
