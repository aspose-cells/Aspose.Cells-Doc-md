---
title: قراءة وكتابة جدول الاستعلام في ورقة العمل باستخدام جافا سكريبت عبر C++
linktitle: قراءة وكتابة جدول الاستعلام لورقة العمل
type: docs
weight: 40
url: /ar/javascript-cpp/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}}

توفر Aspose.Cells مجموعة Worksheet.QueryTables التي تعيد كائن نوع QueryTable عن طريق الفهرس. لديها الخاصيةان التالية

- QueryTable.adjustColumnWidth
- QueryTable.preserveFormatting

هذه قيم بوليانيتين. يمكنك مشاهدتها في Microsoft Excel عبر Data > Connections > Properties.

{{% /alert %}}

## قراءة وكتابة جدول الاستعلام لورقة العمل

يقرأ المثال التالي أول جدول استعلام من أول ورقة عمل ثم يطبع خصائص جدول الاستعلام. ثم يضبط خاصية preserveFormatting إلى true.

يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج الذي تم إنشاؤه بواسطة الكود من الروابط التالية.

- [ملف Excel المصدر](5115533.xlsx)
- [ملف Excel الناتج](5115537.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells QueryTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
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
            document.getElementById('runExample').disabled = false;
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

            // Create workbook from source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first Query Table
            const qt = worksheet.queryTables.get(0);

            // Read Query Table Data (properties converted from getters)
            const adjustColumnWidth = qt.adjustColumnWidth;
            const preserveFormatting = qt.preserveFormatting;

            resultDiv.innerHTML = `<p>Adjust Column Width: ${adjustColumnWidth}</p><p>Preserve Formatting: ${preserveFormatting}</p>`;

            // Now set Preserve Formatting to true (setter converted to property assignment)
            qt.preserveFormatting = true;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += '<p style="color: green;">PreserveFormatting set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### إخراج الكونسول



{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## استرداد نطاق نتيجة جدول الاستعلام

توفر Aspose.Cells خيار قراءة العنوان أي نطاق نتائج الخلايا لجدول الاستعلام. يُظهر الكود التالي هذه الميزة من خلال قراءة عنوان نطاق النتائج لجدول الاستعلام. يمكن تنزيل الملف النموذجي من [هنا](72417290.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const queryTable = worksheet.queryTables.get(0);
            const resultRange = queryTable.resultRange;
            const address = resultRange.address;

            const addressText = (address && typeof address.toString === 'function') ? address.toString() : String(address);
            console.log(addressText);
            document.getElementById('result').innerHTML = `<p>Query table result range address: ${addressText}</p>`;
        });
    </script>
</html>
```
