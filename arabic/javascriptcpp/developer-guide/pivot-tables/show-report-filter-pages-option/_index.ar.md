---
title: خيار إظهار صفحات تصفية التقرير
type: docs
weight: 110
url: /ar/javascript-cpp/show-report-filter-pages-option/
---

## **خيار إظهار صفحات مرشح التقرير**
يدعم Excel إنشاء جداول محورية، إضافة مرشحات التقارير وتمكين خيار "عرض صفحات مرشحات التقرير". يدعم Aspose.Cells for JavaScript عبر C++ أيضًا هذا الميزة لتمكين الخيار "عرض صفحات مرشحات التقرير" على جدول المحوري المنشأ. إليك الشاشة التي تظهر خيار "عرض صفحات مرشحات التقرير" في Excel.

![todo:image_alt_text](show-report-filter-pages-option_1.png)

يمكن تنزيل ملف المصدر وملفات الإخراج التجريبية من هنا لاختبار الشيفرة التجريبية:

`[ملف إكسل المصدر](81920786.xlsx)` 

[ملف إكسل الناتج](81920787.xlsx)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Sample Pivot Table Example</title>
    </head>
    <body>
        <h1>Sample Pivot Table Example</h1>
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

            // Accessing the second worksheet (index 1) and first pivot table
            const worksheet = workbook.worksheets.get(1);
            const pt = worksheet.pivotTables.get(0);

            // Set pivot field - show report filter page for first page field
            pt.showReportFilterPage(pt.pageFields.get(0));

            // Set position index for showing report filter pages
            pt.showReportFilterPageByIndex(pt.pageFields.get(0).position);

            // Set the page field name
            pt.showReportFilterPageByName(pt.pageFields.get(0).name);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSamplePivotTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
