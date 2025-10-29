---
title: حذف الصفوف والأعمدة الفارغة في ورقة عمل باستخدام جافاسكرابت عبر C++
linktitle: حذف الصفوف والأعمدة الفارغة في ورقة العمل
type: docs
weight: 300
url: /ar/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: تعلم كيفية حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل باستخدام Aspose.Cells for JavaScript عبر C++.  
---

{{% alert color="primary" %}}

من الممكن حذف جميع الصفوف والأعمدة الفارغة من ورقة العمل. هذا مفيد عند إنشاء ملف PDF من ملف Microsoft Excel وترغب في تحويل الصفوف والأعمدة التي تحتوي على بيانات أو كائنات ذات علاقة فقط.

استخدم وسائل Aspose.Cells التالية لحذف الصفوف والأعمدة الفارغة:

1. لحذف الصفوف الفارغة، استخدم الطريقة [**Cells.deleteBlankRows()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankRows--). يرجى ملاحظة أنه من الضروري للصفوف الفارغة التي سيتم حذفها أن يكون [**Row.isBlank()**](https://reference.aspose.com/cells/javascript-cpp/row/#isBlank--) صحيحًا، وأيضًا يجب ألا يكون هناك تعليق مرئي معرف لأي خلية في تلك الصفوف، ولا جدول محوري يتقاطع نطاقه معها.
2. لحذف الأعمدة الفارغة، استخدم الطريقة [**Cells.deleteBlankColumns()**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteBlankColumns--).

{{% /alert %}}

## كود جافاسكرابت لحذف الصفوف الفارغة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Delete Blank Rows Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = workbook.worksheets;

            // Get first worksheet
            const sheet = sheets.get(0);

            // Delete blank rows from the worksheet
            sheet.cells.deleteBlankRows();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Blank rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## كود جافاسكرابت لحذف الأعمدة الفارغة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Blank Columns Example</title>
    </head>
    <body>
        <h1>Delete Blank Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = workbook.worksheets;

            // Get first Worksheet from WorksheetCollection
            const sheet = sheets.get(0);

            // Delete the Blank Columns from the worksheet
            sheet.cells.deleteBlankColumns();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mybook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Blank columns deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
