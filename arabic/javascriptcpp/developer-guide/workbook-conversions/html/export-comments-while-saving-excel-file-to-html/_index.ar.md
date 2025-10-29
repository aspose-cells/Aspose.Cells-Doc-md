---
title: تصدير التعليقات أثناء حفظ ملف إكسل كـ HTML بواسطة JavaScript عبر C++
linktitle: تصدير التعليقات أثناء حفظ ملف Excel إلى HTML
type: docs
weight: 40
url: /ar/javascript-cpp/export-comments-while-saving-excel-file-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل الخاص بك كـ HTML، لا يتم تصدير التعليقات. ومع ذلك، يوفر Aspose.Cells for JavaScript عبر C++ هذه الميزة باستخدام خاصية [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/). إذا قمت بضبطها على **true**، فسيتم عرض التعليقات الموجودة في ملف إكسل الخاص بك أيضًا في HTML.

## **تصدير التعليقات أثناء حفظ ملف Excel إلى HTML**

يشرح الكود العيني التالي استخدام الخاصية [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/javascript-cpp/export-comments-while-saving-excel-file-to/). توضح اللقطة الشاشية تأثير الكود على الHTML عندما يتم تعيينها إلى **true**. يرجى تحميل [ملف Excel العيني](50528260.xlsx) و[HTML المُنشئ](5052826.txt) للرجوع إليها.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Comments to HTML</title>
    </head>
    <body>
        <h1>Export Comments to HTML Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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

            // Create HTML save options and set IsExportComments to true
            const opts = new HtmlSaveOptions();
            opts.isExportComments = true;

            // Save the workbook to HTML format with the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportCommentsHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
