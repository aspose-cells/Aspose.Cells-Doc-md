---
title: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/javascript-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells for JavaScript عبر C++ الآن تحديث وحساب جدول محوري يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.refreshData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#refreshdata--) و[**PivotTable.calculateData**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#calculatedata--) كما هو معتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

يحمّل الرمز النموذجي التالي ملف Excel المصدر [ملف المصدر](5115238.xlsx) الذي يحتوي على جدول محوري به ثلاثة عناصر محسوبة مثل "إضافة", "قسمة" و"قسمة 2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب جدول المحوري باستخدام APIات Aspose.Cells for JavaScript عبر C++ وحفظ المصنف بصيغة PDF. تظهر النتائج في [ملف PDF الخارج](5115229.pdf) أن Aspose.Cells for JavaScript عبر C++ قام بتحديث وحساب جدول المحوري بنجاح. يمكنك التحقق من ذلك عبر برنامج Microsoft Excel بوضع القيمة 20 يدويًا في الخلية D2 ثم تحديث جدول المحوري عبر اختصار Alt+F5 أو بالنقر على زر تحديث جدول المحوري.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh and Calculate Pivot Table Items</title>
    </head>
    <body>
        <h1>Refresh and Calculate Pivot Table Items</h1>
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Change the value of cell D2
            const cell = sheet.cells.get("D2");
            cell.value = 20;

            // Refresh and calculate all the pivot tables inside this sheet
            sheet.refreshPivotTables();

            // Save the workbook as PDF and provide a download link
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshAndCalculateItems_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            result.innerHTML = '<p style="color: green;">Pivot tables refreshed and calculated. Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
