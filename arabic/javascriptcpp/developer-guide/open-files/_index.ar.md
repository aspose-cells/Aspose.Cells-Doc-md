---
title: تحميل وإدارة ملفات إكسل، OpenOffice، Json، Csv و Html
linktitle: فتح الملفات
type: docs
weight: 20
url: /ar/javascript-cpp/loading-saving-and-managing/
description: مع Aspose.Cells، من السهل إنشاء وفتح وإدارة ملفات إكسل وCSV وTSV وODS وHTML وNumbers وJson وXML وPdf وJpg وTiff والصور وMht وXPS باستخدام جافاسكريبت عبر C++.
---

{{% alert color="primary" %}}

 مع Aspose.Cells، من السهل إنشاء، فتح، وإدارة ملفات إكسل، على سبيل المثال، لاسترجاع البيانات، أو استخدام قالب مصمم لتسريع عملية التطوير.

{{% /alert %}}

## **إنشاء مصنف جديد**
يُظهر المثال التالي إنشاء دفتر عمل جديد من الصفر.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/Aspose.Cells.lic",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a Workbook object (new blank workbook)
            const wb = new Workbook();

            // Access the first worksheet in the workbook
            const sheet = wb.worksheets.get(0);

            // Access the "A1" cell in the sheet
            const cell = sheet.cells.get("A1");

            // Input the "Hello World!" text into the "A1" cell
            cell.value = "Hello World!";

            // Save the Excel file and prepare download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MyBook_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell updated. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **فتح وحفظ ملف**
 مع Aspose.Cells، من السهل فتح، حفظ، وإدارة ملفات إكسل.

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Creating a Workbook object and opening an Excel file using its file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Adding new sheet
            const sheetIndex = workbook.worksheets.add("MySheet");
            const sheet = workbook.worksheets.get(sheetIndex);

            // Setting active sheet
            workbook.worksheets.activeSheetIndex = 1;

            // Setting values.
            const cells = sheet.cells;

            // Setting text
            cells.get("A1").putValue("Hello!");

            // Setting number
            cells.get("A2").putValue(1000);

            // Setting Date Time
            const cell = cells.get("A3");
            cell.putValue(new Date());
            const style = cell.style;
            style.number = 14;
            cell.style = style;

            // Setting formula
            cells.get("A4").formula = "=SUM(A1:A3)";

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [طرق مختلفة لفتح الملفات](/cells/ar/javascript-cpp/different-ways-to-open-files/)
- [تصفية أسماء محددة أثناء تحميل المصنف](/cells/ar/javascript-cpp/filter-defined-names-while-loading-workbook/)
- [تصفية الكائنات أثناء تحميل مصنف العمل أو ورقة العمل](/cells/ar/javascript-cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [تصفية نوع البيانات أثناء تحميل مصنف العمل من ملف القالب](/cells/ar/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [الحصول على تحذيرات أثناء تحميل ملف إكسل](/cells/ar/javascript-cpp/get-warnings-while-loading-excel-file/)
- [تحميل ملف Excel المصدر دون الرسوم البيانية](/cells/ar/javascript-cpp/load-source-excel-file-without-charts/)
- [تحميل الأوراق العمل المحددة في كتيب عمل](/cells/ar/javascript-cpp/load-specific-worksheets-in-a-workbook/)
- [تحميل الدفتر بحجم ورقة الطابعة المحدد](/cells/ar/javascript-cpp/load-workbook-with-specified-printer-paper-size/)
- [فتح ملفات Microsoft Excel مختلفة الإصدارات](/cells/ar/javascript-cpp/opening-different-microsoft-excel-versions-files/)
- [فتح الملفات بتنسيقات مختلفة](/cells/ar/javascript-cpp/opening-files-with-different-formats/)
- [تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة](/cells/ar/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [قراءة جدول بيانات الأرقام المطور من قبل Apple Inc. باستخدام Aspose.Cells](/cells/ar/javascript-cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [توقّف عن التحويل أو التحميل باستخدام InterruptMonitor عندما يستغرق وقتًا طويلاً](/cells/ar/javascript-cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [استخدام واجهة برمجة التطبيقات LightCells](/cells/ar/javascript-cpp/using-lightcells-api/)
- [تحويل CSV إلى JSON](/cells/ar/javascript-cpp/convert-csv-to-json/)
- [تحويل إكسل إلى JSON](/cells/ar/javascript-cpp/convert-excel-to-json/)
- [تحويل JSON إلى CSV](/cells/ar/javascript-cpp/convert-json-to-csv/)
- [تحويل JSON إلى إكسل](/cells/ar/javascript-cpp/convert-json-to-excel/)
- [تحويل إكسل إلى Html](/cells/ar/javascript-cpp/convert-excel-to-html/)
