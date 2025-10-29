---
title: إدراج الجدول الزمني
linktitle: الجداول الزمنية
type: docs
weight: 170
url: /ar/javascript-cpp/create-timeline/
description: تعرف على كيفية إنشاء مخطط زمني باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

بدلاً من تعديل الفلاتر لعرض التواريخ، يمكنك استخدام جدول PivotTable Timeline——خيار تصفية ديناميكي يسمح لك بسهولة تصفية حسب التاريخ/الوقت، والتكبير في الفترة التي تريدها باستخدام عنصر تحكم الشرائح. يسمح لك Microsoft Excel بإنشاء مخطط زمني عن طريق تحديد جدول محوري ثم النقر على *إدراج > مخطط زمني*. كما يتيح Aspose.Cells for JavaScript عبر C++ إنشاء مخطط زمني باستخدام طريقة [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/javascript-cpp/timelinecollection/#add-pivottable-number-number-string-).

## **إنشاء الجدول الزمني لجدول البيفوت**

يرجى الاطلاع على الكود التالي. يحمل ملف إكسل عياري يحتوي على جدول محوري. ثم ينشئ المخطط الزمني بناءً على أول حقل جدول محوري أساسي. أخيرًا، يحفظ المصنف بصيغة [XLSX المخرجة](output.xlsx). تُظهر لقطة الشاشة التالية المخطط الزمني الذي أنشأه Aspose.Cells for JavaScript عبر C++ في ملف إكسل الناتج.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Timeline to Pivot Table</title>
    </head>
    <body>
        <h1>Add Timeline to Pivot Table</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access second worksheet (index 1)
            const sheet = workbook.worksheets.get(1);

            // Access first pivot table inside the worksheet
            const pivot = sheet.pivotTables.get(0);

            // Add timeline relating to pivot table (positioned at column 15, row 1) with caption "Ship Date"
            const index = sheet.timelines.add(pivot, 15, 1, "Ship Date");

            // Access the newly added timeline from timeline collection
            const timeline = sheet.timelines.get(index);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Timeline added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
