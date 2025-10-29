---
title: كيفية إخفاء السلسلة باستخدام جافا سكريبت عبر C++
linktitle: كيفية إخفاء سلسلة
description: تعلم كيفية جعل السلسلة غير مرئية في مخطط إكسل باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: مخطط إكسل، السلسلة، غير مرئي، IsFiltered جافا سكريبت عبر C++.
type: docs
weight: 74
url: /ar/javascript-cpp/how-to-set-series-invisible/
---

## كيفية إخفاء سلسلة في مخطط إكسل

في مخطط إكسل، يمكنك النقر بزر الماوس الأيمن على مخطط، ثم اختيار "تحديد البيانات"، وفي النافذة المنبثقة، يمكنك تحديد ما إذا كانت السلسلة مرئية عبر الاختيار أو إلغاء الاختيار. يمكنك تحميل [ملف النموذج](SeriesFiltered.xlsx) التالي واستخدامه في إكسل لتحقيق هذه الوظيفة، وسنشرح لاحقًا كيفية تحقيق ذلك باستخدام مكتبة Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## كيفية إخفاء سلسلة باستخدام Aspose.Cells 

نستخدم الكود التالي لإخفاء سلسلة باستخدام Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify Chart Series Color Variation</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Access the first worksheet and its charts
            const charts = workbook.worksheets.get(0).charts;
            const chart = charts.get("Chart 1");

            // Access filtered NSeries and NSeries collections (properties instead of getters)
            const nSeriesFiltered = chart.filteredNSeries;
            const nSeries = chart.nSeries;

            // Set IsColorVaried on series (converted from setIsColorVaried to property assignment)
            nSeries.get(1).isColorVaried = true;
            nSeries.get(0).isColorVaried = true;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

يمكنك الحصول على الملف المدخل التالي [Input file](SeriesFiltered.xlsx) وملف الإخراج [output file](output.xlsx).

كما هو موضح في الشكل أدناه، السلسلتان الأوليان اللتان كانتا مرئيتين أصلاً، أصبحتا غير مرئيتين في ملف الإخراج.
![todo:image_alt_text](output.png)
