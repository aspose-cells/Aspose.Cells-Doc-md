---
title: إضافة ارتباط Pivot باستخدام جافا سكريبت عبر C++
linktitle: إضافة اتصال المحور
type: docs
weight: 30
url: /ar/javascript-cpp/add-pivot-connection/
description: تعلم كيفية إضافة ارتباط pivot باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: أضف ارتباط pivot بدون Office 2013، Office 2016، Office 2019 وOffice 365 باستخدام جافا سكريبت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد ربط مقسم وجدول محوري في Excel، تحتاج إلى النقر بزر الماوس الأيمن على المقسم واختيار "اتصالات التقرير...". في قائمة الخيارات، يمكنك العمل على خانة الاختيار. بالمثل، إذا كنت تريد ربط مقسم وجدول محوري باستخدام API الخاص بـ Aspose.Cells برمجيًا، يرجى استخدام [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#addPivotConnection-PivotTable-). سيقوم بربط المقسم والجدول المحوري.

## **ربط المنقي والجدول المحوري**

الكود النموذجي التالي يحمل [ملف Excel النموذجي](add-pivot-connection.xlsx) الذي يحتوي على مقسم موجود. يصل إلى المقسم ثم يربط المقسم والجدول المحوري. أخيرًا، يحفظ المصنف كـ [ملف Excel المخرجي](add-pivot-connection-out.xlsx).

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Pivot Connection Example</title>
    </head>
    <body>
        <h1>Add Pivot Connection Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            const pivotTable = worksheet.pivotTables.get(0);

            const slicer = worksheet.slicers.get(0);

            slicer.addPivotConnection(pivotTable);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'add-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
