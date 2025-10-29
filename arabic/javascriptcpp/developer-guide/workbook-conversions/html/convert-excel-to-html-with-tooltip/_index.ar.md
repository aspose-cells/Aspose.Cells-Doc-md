---
title: تحويل إكسل إلى HTML مع أداة شرح باستخدام JavaScript عبر C++  
linktitle: تحويل Excel إلى HTML مع تلميح سريع  
type: docs  
weight: 200  
url: /ar/javascript-cpp/convert-excel-to-html-with-tooltip/  
description: تعرف على كيفية تحويل ملفات إكسل إلى تنسيق HTML مع أدوات شرح لعرض النص بالكامل باستخدام Aspose.Cells for JavaScript عبر C++.  
---

## **تحويل Excel إلى HTML مع تلميحة**

قد تكون هناك حالات يتم فيها قطع النص في HTML المُنتج وترغب في عرض النص الكامل كأداة شرح عند التحويم. يدعم Aspose.Cells for JavaScript عبر C++ ذلك من خلال توفير خاصية [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--). تعيين الخاصية [**HtmlSaveOptions.addTooltipText**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#addTooltipText--) إلى **true** سيضيف النص الكامل كأداة شرح في HTML المُنتج.

تُظهر الصورة التالية التلميح السريع في ملف HTML المولد.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

الرمز التالي يحمل ملف Excel [المصدر](98107416.xlsx) ويولد ملف HTML [الناتج](98107417.zip) مع أداة التلميح.

الكود المثالي

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Tooltip to HTML Example</title>
    </head>
    <body>
        <h1>Add Tooltip to HTML Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create HtmlSaveOptions and enable tooltip text
            const options = new HtmlSaveOptions();
            options.addTooltipText = true;

            // Save workbook as HTML with the specified options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddTooltipToHtmlSample_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
