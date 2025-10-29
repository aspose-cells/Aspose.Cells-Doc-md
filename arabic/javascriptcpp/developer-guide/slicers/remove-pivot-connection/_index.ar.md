---
title: إزالة اتصال المحور باستخدام جافا سكريبت عبر C++
linktitle: إزالة اتصال الجدول المحوري
type: docs
weight: 30
url: /ar/javascript-cpp/remove-pivot-connection/
description: تعلم كيفية إزالة اتصال المحور باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: إزالة اتصال المحور دون Office 2013، Office 2016، Office 2019 و Office 365 باستخدام جافا سكريبت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تريد فك ارتباط قطعة الفاصل وجدول المحور في إكسل، تحتاج إلى النقر بزر الماوس الأيمن على القطعة واختيار "ارتباط التقرير...". يمكنك استخدام خانة الاختيار في قائمة الخيارات. بالمثل، إذا كنت تريد فك ارتباط قطعة الفاصل وجدول المحور باستخدام Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات (API) برمجياً، يرجى استخدام طريقة [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/javascript-cpp/slicer/#removePivotConnection-pivottable-). ستفصل قطعة الفاصل وجدول المحور.

## **فصل قالب التصفية عن جدول المحور**

الكود النموذجي التالي يحمل [ملف Excel النموذجي](remove-pivot-connection.xlsx) الذي يحتوي على مقسم موجود. يصل إلى المقسم ثم يفكه. أخيرًا، يحفظ المصنف كـ [ملف Excel المخرجي](remove-pivot-connection-out.xlsx).

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Pivot Connection</title>
    </head>
    <body>
        <h1>Remove Pivot Connection Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access the first PivotTable inside the PivotTable collection.
            const pivotTable = worksheet.pivotTables.get(0);

            // Access the first slicer inside the slicer collection.
            const slicer = worksheet.slicers.get(0);

            // Remove PivotTable connection.
            slicer.removePivotConnection(pivotTable);

            // Save the workbook in output XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'remove-pivot-connection-out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Pivot connection removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
