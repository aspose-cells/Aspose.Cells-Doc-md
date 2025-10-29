---
title: تغيير مصدر بيانات الرسم البياني إلى ورقة عمل وجهة أثناء نسخ الصفوف أو النطاق باستخدام JavaScript عبر C++
linktitle: تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق
description: تعلم كيفية تغيير مصدر بيانات الرسم البياني إلى ورقة عمل وجهة أثناء نسخ الصفوف أو نطاق في Aspose.Cells for Javaسكريبت عبر C++. يوضح هذا الدليل كيفية تحديث نطاق بيانات الرسم البياني وربطه بورقة العمل الوجهة.
keywords: Aspose.Cells for Javaسكريبت عبر C++، الرسم البياني، مصدر البيانات، ورقة العمل الوجهة، الصفوف، النطاق، النسخ، التحديث، نطاق البيانات، الربط.
type: docs
weight: 440
url: /ar/javascript-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **سيناريوهات الاستخدام المحتملة**

عند نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة، فإن مصدر بيانات المخطط لا يتغير. على سبيل المثال، إذا كان مصدر البيانات للمخطط هو `=Sheet1!$A$1:$B$4`، فبعد نسخ الصفوف أو النطاق إلى ورقة عمل جديدة، سيظل مصدر البيانات كما هو، أي `=Sheet1!$A$1:$B$4`. لا يزال يشير إلى ورقة العمل القديمة، أي Sheet1. وهذا هو السلوك أيضًا في Microsoft Excel. إذا كنت ترغب في أن يشير إلى ورقة العمل الجديدة، يرجى استخدام الخاصية [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) وضبطها على **true** عند استدعاء الطريقة [**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#copyRows-cells-number-number-number-). الآن، إذا كانت ورقة العمل الوجهة الخاصة بك هي DestSheet، فسيتم تغيير مصدر البيانات للمخطط من `=Sheet1!$A$1:$B$4` إلى `=DestSheet!$A$1:$B$4`.

## **تغيير مصدر البيانات للرسم البياني إلى ورقة العمل الوجهة أثناء نسخ الصفوف أو النطاق**

يوضح الكود النموذجي التالي استخدام الخاصية [**CopyOptions.referToDestinationSheet**](https://reference.aspose.com/cells/javascript-cpp/copyoptions/#referToDestinationSheet--) أثناء نسخ الصفوف أو النطاق الذي يحتوي على مخططات إلى ورقة عمل جديدة. يستخدم الكود ملف Excel النموذجي (5113699.xlsx) ويولد ملف Excel الناتج (5113697.xlsx).

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Worksheet with Charts</title>
    </head>
    <body>
        <h1>Copy Worksheet with Charts Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first sheet which contains chart
            const source = wb.worksheets.get(0);

            // Add another sheet named DestSheet
            const destination = wb.worksheets.add("DestSheet");

            // Set CopyOptions.referToDestinationSheet to true
            const options = new AsposeCells.CopyOptions();
            options.referToDestinationSheet = true;

            // Copy all the rows of source worksheet to destination worksheet which includes chart as well
            // The chart data source will now refer to DestSheet
            destination.cells.copyRows(source.cells, 0, 0, source.cells.maxDisplayRange.rowCount, options);

            // Save workbook in xlsx format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
