---
title: الوصول إلى الجدول من خلية وإضافة القيم بداخله باستخدام إزاحة الصف والعمود مع جافا سكريبت عبر C++
linktitle: الوصول إلى الجدول من الخلية وإضافة القيم داخله باستخدام إزاحة الصف والعمود
type: docs
weight: 230
url: /ar/javascript-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/
---

{{% alert color="primary" %}}  

عادةً ما تضيف القيم داخل الجدول أو كائن القائمة باستخدام الطريقة [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-). ولكن في بعض الأحيان، قد تحتاج إلى إضافة القيم داخل الجدول أو كائن القائمة باستخدام إزاحة الصف والعمود.  

للوصول إلى جدول أو كائن قائمة من خلية معينة، استخدم الخاصية [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--). ولإضافة قيم بداخله باستخدام إزاحات الصف والعمود، استخدم الطريقة [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-).  

{{% /alert %}}  

يُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم داخل الكود. يحتوي على الجدول الفارغ ويبرز الخلية D5 التي تقع داخل الجدول. سنقوم بالوصول إلى هذا الجدول من الخلية D5 باستخدام خاصية [**Cell.table**](https://reference.aspose.com/cells/javascript-cpp/cell/#table--) ثم نضيف القيم بداخله باستخدام كل من طريقتي [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/javascript-cpp/cell/#putValue-boolean-) و [**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/javascript-cpp/listobject/#putCellValue-number-number-object-).  

## مثال  

### لقطات شاشة تقارن الملفات المصدرية والإخراجية  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

اللقطة الشاشية التالية تُظهر ملف Excel الناتج الذي تم إنشاؤه بواسطة الكود. كما يمكنك رؤية الخلية D5 التي تحتوي على قيمة والخلية F6 والتي تقع في الإزاحة 2،2 من الجدول وتحتوي على قيمة.  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### كود JavaScript للوصول إلى الجدول من الخلية وإضافة القيم بداخله باستخدام إزاحات الصف و العمود  

يقوم الكود النموذجي التالي باستخدام ملف Excel المصدر كما هو موضح في اللقطة الشاشية أعلاه ويضيف القيم داخل الجدول ويولد ملف Excel الناتج كما هو موضح أعلاه.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Accessing Table Example</h1>
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

            // Access cell D5 which lies inside the table
            const cell = worksheet.cells.get("D5");

            // Put value inside the cell D5
            cell.value = "D5 Data";

            // Access the Table from this cell
            const table = cell.table;

            // Add some value using Row and Column Offset
            table.putCellValue(2, 2, "Offset [2,2]");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
