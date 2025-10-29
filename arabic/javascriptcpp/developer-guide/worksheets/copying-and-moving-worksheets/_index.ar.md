---
title: نسخ ونقل جداول البيانات باستخدام جافا سكريبت عبر C++
linktitle: نسخ ونقل ورقات العمل
type: docs
weight: 10
url: /ar/javascript-cpp/copying-and-moving-worksheets/
description: يتضمن هذا المقال رمزًا نمطيًا ويصف كيفية نسخ ونقل جداول البيانات برمجيًا داخل دفتر عمل إكسل وعبر دفاتر عمل إكسل باستخدام واجهة برمجة التطبيقات جافا سكريبت عبر C++.
keywords: نسخ جدول بيانات باستخدام جافا سكريبت، نقل جدول بيانات باستخدام جافا سكريبت
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى عدد من ورقات العمل مع تنسيقات وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الفصلية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة لفعل ذلك: من خلال إنشاء ورقة واحدة ثم نسخها.

تدعم الشفرة Aspose.Cells for JavaScript عبر C++ نسخ ونقل جداول البيانات داخل أو بين دفاتر العمل. يتم نسخ الجدول بالكامل بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسوم البيانية والصور والأشياء الأخرى بدقة عالية.

{{% /alert %}}

## **نقل أو نسخ الأوراق باستخدام Microsoft Excel**

فيما يلي الخطوات اللازمة لنسخ ونقل أوراق العمل داخل أو بين دفاتر العمل في Microsoft Excel.

1. لنقل أو نسخ الأوراق إلى دفتر العمل الآخر، افتح دفتر العمل الذي سيتلقى الأوراق.
1. انتقل إلى دفتر العمل الذي يحتوي على الأوراق التي ترغب في نقلها أو نسخها، ثم حدد الأوراق.
1. في قائمة **تحرير**، انقر فوق **نقل أو نسخ الصفحة**.
4. في مربع الحوار **إلى مصنف**، انقر فوق المصنف الذي سيستقبل الصفحات.
5. لنقل أو نسخ الصفحات المحددة إلى مصنف جديد، انقر فوق **مصنف جديد**.
1. في مربع **قبل الصفحة**، انقر فوق الصفحة التي ترغب في إدراج الصفحات المنقولة أو المنسوخة قبلها.
7. لنسخ الصفحات بدلاً من نقلها، حدد مربع الاختيار **إنشاء نسخة**.

### **نسخ جداول البيانات داخل دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++**

توفر Aspose.Cells طريقة متحملة، [**Aspose.Cells.WorksheetCollection.addCopy()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#addCopy-number-)، يتم استخدامها لإضافة ورقة عمل إلى المجموعة ونسخ البيانات من ورقة عمل موجودة. إحدى الإصدارات من الطريقة تأخذ فهرس الورقة المصدر كمعلمة. الإصدار الآخر يأخذ اسم الورقة المصدر.

المثال التالي يظهر كيفية نسخ ورقة عمل موجودة داخل سجل العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Sheet Within Workbook</title>
    </head>
    <body>
        <h1>Copy Sheet Within Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Open an existing Excel file.
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheets object with reference to the sheets of the Workbook.
            const sheets = wb.worksheets;

            // Copy data to a new sheet from an existing sheet within the Workbook.
            sheets.addCopy("Sheet1");

            // Save the Excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWithinWorkbook_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Sheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **نسخ أوراق العمل بين دفاتر العمل**

توفر Aspose.Cells طريقة [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) لنسخ البيانات والتنسيقات من ورقة عمل مصدر إلى ورقة أخرى داخل أو بين المصنفات. تأخذ الطريقة كائن ورقة عمل المصدر كمعامل.

يظهر المثال التالي كيفية نسخ ورقة عمل من دفتر عمل إلى دفتر عمل آخر.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheets Between Workbooks</title>
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
        <p>Select the source Excel file (book1.xls) to copy its first worksheet into a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (book1.xls).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create a Workbook from the uploaded file (source workbook)
            const excelWorkbook0 = new Workbook(new Uint8Array(arrayBuffer));

            // Create another Workbook (destination workbook)
            const excelWorkbook1 = new Workbook();

            // Copy the first sheet of the first book into second book.
            excelWorkbook1.worksheets.get(0).copy(excelWorkbook0.worksheets.get(0));

            // Save the file as Excel 97-2003 (.xls)
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Copied Workbook';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

المثال التالي يوضح كيفية نسخ ورقة عمل من مصنف إلى مصنف آخر.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Between Workbooks Example</h1>
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
            // Create a new Workbook.
            const excelWorkbook0 = new Workbook();

            // Get the first worksheet in the book.
            const ws0 = excelWorkbook0.worksheets.get(0);

            // Put some data into header rows (A1:A4)
            for (let i = 0; i < 5; i++) {
                ws0.cells.get(i, 0).value = `Header Row ${i}`;
            }

            // Put some detail data (A5:A999)
            for (let i = 5; i < 1000; i++) {
                ws0.cells.get(i, 0).value = `Detail Row ${i}`;
            }

            // Define a pagesetup object based on the first worksheet.
            const pagesetup = ws0.pageSetup;

            // The first five rows are repeated in each page...
            // It can be seen in print preview.
            pagesetup.printTitleRows = "$1:$5";

            // Create another Workbook.
            const excelWorkbook1 = new Workbook();

            // Get the first worksheet in the book.
            const ws1 = excelWorkbook1.worksheets.get(0);

            // Name the worksheet.
            ws1.name = "MySheet";

            // Copy data from the first worksheet of the first workbook into the
            // first worksheet of the second workbook.
            ws1.copy(ws0);

            // Saving the modified Excel file
            const outputData = excelWorkbook1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetFromWorkbookToOther_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and worksheet copied successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **نقل أوراق العمل داخل الدفتر**

توفر Aspose.Cells طريقة [**Aspose.Cells.Worksheet.moveTo()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#moveto-number-) التي تُستخدم لنقل ورقة عمل إلى موقع آخر في نفس جدول البيانات. تأخذ الطريقة فهرس ورقة العمل الهدف كمعامل.

المثال التالي يظهر كيفية نقل ورقة عمل إلى موقع آخر داخل سجل العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access worksheets collection
            const sheets = wb.worksheets;

            // Get the first worksheet
            const worksheet = sheets.get(0);

            // Move the first sheet to the third position (index 2)
            worksheet.moveTo(2);

            // Save the modified workbook in Excel97-2003 format
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'MoveWorksheet_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
