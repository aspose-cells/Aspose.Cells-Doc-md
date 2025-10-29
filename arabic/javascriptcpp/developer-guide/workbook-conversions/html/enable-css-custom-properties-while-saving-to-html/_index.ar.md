---
title: تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML باستخدام JavaScript عبر C++
linktitle: تمكين خصائص CSS المخصصة عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/javascript-cpp/enable-css-custom-properties-while-saving-to-html/
description: تعلم كيفية تمكين خصائص CSS المخصصة عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك بتنسيق HTML، في الحالة التي توجد فيها تكرارات متعددة لصورة base64 واحدة، مع الخاصية المخصصة، الحاجة إلى حفظ بيانات الصورة مرة واحدة فقط حتى يتحسن أداء HTML الناتج. يرجى استخدام الخاصية [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--) وتعيينها **true** أثناء الحفظ إلى HTML.
![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg) 


## **تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML**

يوضح رمز المثال التالي استخدام الخاصية [**HtmlSaveOptions.enableCssCustomProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#enableCssCustomProperties--). تُظهر لقطة الشاشة تأثير هذه الخاصية عندما لا تكون مُعينة على **true**. يرجى تنزيل [ملف Excel النموذجي](50528260.xlsx) المستخدم في هذا الرمز و[ملف HTML الناتج](50528261.zip) الذي تم توليده للمراجعة.



## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Enable CSS Custom Properties Example</title>
    </head>
    <body>
        <h1>Enable CSS Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and set properties (converted from setters to property assignments)
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.exportImagesAsBase64 = true;
            opts.enableCssCustomProperties = true;

            // Save the workbook to HTML using SaveFormat.Html and provided options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEnableCssCustomProperties.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML saved successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
