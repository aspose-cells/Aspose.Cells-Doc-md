---
title: نسخ Sparkline عن طريق تحديد نطاق البيانات وموقع مجموعة Sparkline باستخدام جافا سكريبت عبر C++
linktitle: نسخة الشرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط
type: docs
weight: 300
url: /ar/javascript-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: تعلم كيفية نسخ Sparkline في إكسل بتحديد نطاق البيانات وموقع مجموعة Sparkline باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}
يسمح Microsoft Excel لك بنسخ شرارة عن طريق تحديد نطاق البيانات وموقع مجموعة الشرائط. تدعم Aspose.Cells هذه الميزة.
{{% /alert %}}

لنسخ الشرارة إلى خلايا أخرى في Microsoft Excel:

1. حدد الخلية التي تحتوي على الشرارة.  
1. حدد **Edit Data** من **قسم Sparkline** من **tDesign** علامة التبويب.  
1. حدد **Edit Group Location & Data**.  
1. حدد نطاق البيانات والموقع.  
1. انقر على **موافق**.

توفر Aspose.Cells طريقة `SparklineCollection.add(dataRange, row, column)` لتحديد نطاق البيانات وموقع مجموعة خطوط الفاصل. ترفع الكود النموذجي التالي ملف إكسل المصدر كما هو موضح في الصورة أعلاه، ثم يصل إلى مجموعة خطوط الفاصل الأولى ويضيف نطاقات البيانات والمواقع في مجموعة خطوط الفاصل. وأخيرًا، يكتب ملف إكسل الناتج على القرص والذي يظهر أيضًا في الصورة أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Sparkline Example</h1>
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

            // Create workbook from uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the first sparkline group
            const group = worksheet.sparklineGroups.get(0);

            // Add Data Ranges and Locations inside this sparkline group
            group.sparklines.add("Sheet1!D5:O5", 4, 15);
            group.sparklines.add("Sheet1!D6:O6", 5, 15);
            group.sparklines.add("Sheet1!D7:O7", 6, 15);
            group.sparklines.add("Sheet1!D8:O8", 7, 15);

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sparklines added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
