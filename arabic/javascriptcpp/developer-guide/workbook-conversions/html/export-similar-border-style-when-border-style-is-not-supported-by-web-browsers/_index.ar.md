---
title: تصدير نمط الحدود المشابه عندما لا يدعم متصفحات الويب نمط الحدود باستخدام JavaScript عبر C++  
linktitle: تصدير نفس نمط الحدود عندما لا يتم دعم نمط الحدود بواسطة متصفحات الويب  
type: docs  
weight: 70  
url: /ar/javascript-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: تعرّف على كيفية تصدير الحدود التي لا يدعمها متصفحات الويب عند تحويل ملفات إكسل إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يدعم مايكروسوفت إكسل بعض أنواع الحدود المنقطه التي لا تدعمها متصفحات الويب. عند تحويل مثل هذا الملف إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++، تتم إزالة هذه الحدود. ومع ذلك، يمكن أيضًا أن يدعم Aspose.Cells عرض مثل هذه الحدود مع خاصية [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--). يرجى تعيين قيمتها على **true**، وسيتم تصدير الحدود غير المدعومة إلى ملف HTML.  

## **تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب**  

يوضح الكود النموذجي التالي تحميل [ملف إكسل النموذجي](64716806.xlsx) الذي يحتوي على بعض الحواف غير المدعومة كما هو موضح في لقطة الشاشة التالية. توضح لقطة الشاشة بشكل إضافي تأثير خاصية [**HtmlSaveOptions.exportSimilarBorderStyle**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportSimilarBorderStyle--) داخل [ملف HTML الناتج](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Export Similar Border Style Example</title>
    </head>
    <body>
        <h1>Export Similar Border Style Example</h1>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options - Export Similar Border Style
            const opts = new HtmlSaveOptions();
            opts.exportSimilarBorderStyle = true;

            // Save the workbook in Html format with specified Html Save Options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportSimilarBorderStyle.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
