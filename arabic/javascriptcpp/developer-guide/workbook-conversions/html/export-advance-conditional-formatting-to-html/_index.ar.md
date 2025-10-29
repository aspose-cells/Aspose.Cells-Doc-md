---
title: تصدير تنسيق الشرط DataBar، وColorScale وIconSet أثناء تحويل Excel إلى HTML باستخدام JavaScript عبر C++
linktitle: تصدير تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز أثناء تحويل ملف Excel إلى HTML
type: docs
weight: 30
url: /ar/javascript-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/
---

{{% alert color="primary" %}} 

 يمكنك تصدير تنسيق الشرط DataBar، وColorScale وIconSet أثناء تحويل ملف Excel إلى HTML. هذه الميزة مدعومة جزئيًا من قبل Microsoft Excel ولكن Aspose.Cells for JavaScript عبر C++ يدعمها بشكل كامل.

{{% /alert %}}  

## **تصدير DataBar، ColorScale و IconSet لتنسيق الشروط أثناء تحويل Excel إلى HTML**  
توضح اللقطة الشاشية التالية [ملف Excel عينة](5115558.xlsx) مع تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز. يمكنك تنزيل [ملف Excel العينة](5115558.xlsx) من الرابط المعطى.  

![todo:image_alt_text](conversion_1.png)  

توضح اللقطة الشاشية التالية ملف HTML الناتج من Aspose.Cells الذي يظهر تنسيق البيانات الشريطية ومقياس الألوان وتنسيق الرموز. كما يمكنك رؤية أنه يبدو تمامًا مثل [ملف Excel العينة](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **الكود المثالي**  
الشفرة النموذجية التالية تحول ملف Excel النموذجي إلى HTML وهو مجرد تحويل عادي [Excel إلى HTML](/cells/ar/javascript-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Converting Excel to HTML Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load your sample excel file in a workbook object
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save it in HTML format
            const outputData = workbook.save(SaveFormat.Html);

            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ConvertingToHTMLFiles_out.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
