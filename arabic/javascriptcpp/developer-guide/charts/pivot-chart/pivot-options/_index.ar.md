---
title: كيفية إدارة PivotChart باستخدام خيارات Pivot لل JavaScript عبر C++
linktitle: Pivot Options
type: docs
weight: 10
url: /ar/javascript-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: كيفية إدارة PivotChart مع خيارات Pivot في JavaScript عبر C++.
keywords: PivotChart JavaScript عبر C++
---

## ما هو PivotChart

PivotChart في Excel هو تمثيل رسومي للبيانات تم إنشاؤه من PivotTable. يتيح للمستخدمين تصور البيانات وتحليلها ديناميكيًا من خلال تلخيص وعرض المعلومات في شكل رسوم بيانية. تكون PivotCharts تفاعلية ويمكن تعديلها بسهولة لعرض وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات والعرض في Excel.

## كيفية إدارة PivotChart مع PivotOptions

باستخدام Aspose.Cells for JavaScript عبر C++، يمكنك استخدام [**PivotOptions**](https://reference.aspose.com/cells/javascript-cpp/pivotoptions/) لإدارة PivotChart.

ملف وكود مثالي:
[ملف المثال](Sample.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide PivotChart ZoneFilter Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and the first chart
            const worksheet = workbook.worksheets.get(0);
            const chart = worksheet.charts.get(0);
            const opt = chart.pivotOptions;

            // Hide ZoneFilter in PivotChart
            opt.dropZoneFilter = false; // HideZoneFilter

            // Save the file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'HideZoneFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">ZoneFilter hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

مع الكود المثالي أعلاه، يمكنك التحقق من ملف النتيجة بالتأثير التالي، كما هو موضح في الشكل:

**![النتيجة](الناتج.png)**
