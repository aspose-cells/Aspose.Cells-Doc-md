---
title: تعطيل CSS أثناء الحفظ إلى HTML باستخدام JavaScript عبر C++
linktitle: تعطيل CSS عند الحفظ إلى HTML
type: docs
weight: 320
url: /ar/javascript-cpp/disable-css-while-saving-to-html/
description: تعلم كيفية تعطيل CSS عند حفظ ملفات Excel إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف Excel الخاص بك كصفحة HTML واحدة، عادةً ستكون عناصر CSS مضمنة داخل ملف HTML وستكون موجودة في قسم HEAD. إذا قمت بإرفاق هذا الملف كمحتوى/جسم لرسالة بريد إلكتروني، فسيتم مسح عناصر CSS بواسطة معظم عملاء البريد الإلكتروني، مما يؤدي إلى عرض غير صحيح. تقدم نسخة 24.12 من Aspose.Cells خيارًا يسمح بك إلغاء تفعيل CSS بشكل اختياري، مما يتيح تطبيق الأنماط مباشرة داخل عناصر HTML نفسها. إذا كنت تريد تعيين HTML كمحتوى/جسم للبريد الإلكتروني، يرجى استخدام الخاصية [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) وتعيينها إلى **true**.

## **تعطيل CSS عند الحفظ إلى HTML**

يعرض مثال الكود التالي استخدام الخاصية [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
