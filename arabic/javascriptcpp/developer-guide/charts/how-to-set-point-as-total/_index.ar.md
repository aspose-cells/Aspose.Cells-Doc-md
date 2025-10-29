---
title: كيفية تعيين النقطة كإجمالي باستخدام JavaScript عبر C++
linktitle: كيفية تعيين نقطة كمجموع
description: تعلم كيفية تعيين النقاط كإجمالي في مخططات الماء باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: مخطط WaterFall، نقطة، تعيين كإجمالي، JavaScript عبر C++
type: docs
weight: 72
url: /ar/javascript-cpp/how-to-set-point-as-total/
---

## ما هو "تعيين نقطة كمجموع" في مخطط إكسل

في بعض مخططات إكسل، مثل مخطط WaterFall، تكون بعض نقاط البيانات مجموع النقاط السابقة، وقد تحتاج إلى "تعيين نقطة كمجموع". سنوضح رمز النموذج والتوضيح أدناه.

## يحتاج مخطط WaterFall إلى "تعيين نقطة كمجموع" 

![todo:image_alt_text](set-as-total1.png)

تُظهر هذه الصورة مخطط WaterFall في Excel. يمكننا أن نرى أن هناك أربع نقاط بيانات تبدأ بـ "إجمالي"، وتُستخدم لحساب جميع نقاط البيانات السابقة. في هذه الصورة، الإعدادات ليست صحيحة تمامًا. عندما نختار نقطة "إجمالي 2024"، يمكننا أن نرى أن خيار "تعيين كإجمالي" غير محدد في Excel. مرفق أدناه هو [ملف Excel النموذجي](SampleSheet.xlsx) الذي يحتاج إلى تعديل، وسنستخدم Aspose.Cells for JavaScript عبر C++ لإعداده بشكل صحيح.

## استخدام Aspose.Cells for JavaScript عبر C++ لـ "تعيين نقطة كإجمالي" 

نستخدم الكود التالي لضبط الملف بشكل صحيح:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Chart Subtotals Example</title>
    </head>
    <body>
        <h1>Set Chart Subtotals Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the chart named "Graphiq5"
            const chart = worksheet.charts.get("Graphiq5");

            // set some points as total column 
            // In this example, we set points 0, 4, 8, 12 as total
            chart.nSeries.get(0).layoutProperties.subtotals = [0, 4, 8, 12];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

يمكنك الحصول على [ملف الناتج الصحيح](output.xlsx) التالي

كما هو موضح في الشكل أدناه، تم ضبط النقاط الأربعة "مجموع" بشكل صحيح، ويمكنك رؤية الفرق عن المخطط السابق.

![todo:image_alt_text](set-as-total2.png)
