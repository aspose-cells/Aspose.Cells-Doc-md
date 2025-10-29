---
title: تقديم نمط تاريخ مخصص g وge mm dd
linktitle: تقديم نمط تاريخ مخصص g وge mm dd  
description: تعلم كيفية عرض أنماط تنسيق التاريخ المخصصة "g" و "ge" في Aspose.Cells for JavaScript عبر C++ للتحكم في عرض التاريخ في جداول البيانات.  
keywords: Aspose.Cells، مكتبة جافا سكريبت، جدول بيانات إلكتروني، صيغة تاريخ مخصصة، العرض، نمط g ، نمط ge ، عرض التحكم    
type: docs  
weight: 160  
url: /ar/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

أصبح بإمكان Aspose.Cells الآن تقديم أنماط صيغ التاريخ المخصصة مثل g، ge.mm.dd وما شابه. يرجى التحقق من ملف جدول البيانات المرفق [ملف Excel المصدر] (5112361.xlsx) و [ملف PDF المحول] (5112360.pdf) بواسطة Aspose.Cells للرجوع إليه.

{{% /alert %}}  

يقوم الكود النموذجي التالي بتحويل [ملف Excel المصدر] (5112361.xlsx) الذي يحتوي على قيم تاريخية بأنماط صيغ مخصصة مثل g و ge.mm.dd إلى [PDF الناتج] (5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
