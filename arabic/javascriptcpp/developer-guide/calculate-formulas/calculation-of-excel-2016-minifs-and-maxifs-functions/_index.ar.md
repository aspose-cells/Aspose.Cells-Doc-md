---
title: حساب وظائف MINIFS و MAXIFS في Excel 2016 باستخدام JavaScript عبر C++
description: تقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لحساب وظائف MINIFS و MAXIFS في Excel 2016 باستخدام JavaScript عبر C++. تحميل ملف Excel موجود أو إنشائه، ثم استخدام طرق Aspose.Cells لحساب هذه الوظائف وحفظ النتائج على القرص.
keywords: Aspose.Cells، Excel، 2016، وظيفة MINIFS، وظيفة MAXIFS، الحسابات JavaScript عبر C++
type: docs
weight: 300
url: /ar/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/
---

## **سيناريوهات الاستخدام المحتملة**
 يدعم Microsoft Excel 2016 وظائف MINIFS و MAXIFS. هذه الوظائف غير مدعومة في Excel 2013 أو الإصدارات الأقدم. كما تدعم Aspose.Cells for JavaScript عبر C++ حساب هذه الوظائف. يوضح لقطة الشاشة التالية استخدام هذه الوظائف. يرجى قراءة التعليقات الحمراء داخل لقطة الشاشة لمعرفة كيفية عمل هذه الوظائف.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **حساب وظائف MINIFS و MAXIFS في Excel 2016**
يحمّل رمز العينة التالي [ملف إكسل النموذجي](5115149.xlsx) ويستدعي طريقة [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) لأداء حساب الصيغة عبر Aspose.Cells for JavaScript باستخدام C++، ثم يحفظ النتائج في [ملف PDF الناتج](5115154.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>MINIFS and MAXIFS Calculation to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Load your source workbook containing MINIFS and MAXIFS functions
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Perform Aspose.Cells formula calculation
            workbook.calculateFormula();

            // Save the calculations result in pdf format
            const options = new PdfSaveOptions();
            options.onePagePerSheet = true;

            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputMINIFSAndMAXIFS.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculation and conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
