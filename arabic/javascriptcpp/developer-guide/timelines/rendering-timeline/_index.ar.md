---
title: تقديم الجدول الزمني
type: docs
weight: 40
url: /ar/javascript-cpp/rendering-timeline/
description: إدارة الجداول الزمنية لملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: تحويل الجدول الزمني بدون Office 2013، Office 2016، Office 2019 وOffice 365
---

## **سيناريوهات الاستخدام المحتملة**
 يدعم Aspose.Cells for JavaScript عبر C++ عرض شكل الجدول الزمني بدون استخدام Office 2013، Office 2016، Office 2019 و Office 365. إذا حولت ورقتك إلى صورة أو حفظت الملف كملف PDF أو HTML، ستظهر الجداول الزمنية بشكل صحيح.

## **تقديم الجدول الزمني**
 يقوم الكود النموذجي التالي بتحميل ملف إكسل [مثالي](input.xlsx) يحتوي على جدول زمني موجود. احصل على كائن الشكل حسب اسم الجدول الزمني، ثم قم بعرضه كصورة عبر طريقة Shape.ToImage(). الصورة التالية هي [صورة المخرجات](out.png) التي تظهر الجدول الزمني المعروض. كما ترى، تم عرض الجدول الزمني بشكل صحيح ويبدو كما في ملف إكسل النموذجي.

![todo:image_alt_text](out.png)
### **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export Timeline Shape as Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Add timeline relating to pivot table (access first timeline)
            const timeline = sheet.timelines.get(0);

            // Prepare image options
            const options = new ImageOrPrintOptions();
            options.imageType = ImageType.Png;

            // Get timeline shape object by timeline's name
            const timeLineShape = sheet.shapes.get(timeline.name);

            // Export shape to image (browser returns image bytes)
            const imageData = timeLineShape.toImage(options);

            // Create blob and provide download link
            const blob = new Blob([imageData], { type: 'image/png' });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Timeline Image';

            resultDiv.innerHTML = '<p style="color: green;">Timeline image generated successfully. Click the download link to save the image.</p>';
        });
    </script>
</html>
```
