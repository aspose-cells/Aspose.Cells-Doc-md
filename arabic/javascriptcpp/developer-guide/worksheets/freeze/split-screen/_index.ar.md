---
title: تقسيم شاشة ورقة عمل إكسل باستخدام جافا سكريبت عبر C++
linktitle: شاشة مقسمة
type: docs
weight: 190
url: /ar/javascript-cpp/how-to-split-screen-of-excel-worksheet
description: في هذا المقال، ستتعلم كيفية عرض صفوف و/أو أعمدة معينة في لوحات منفصلة عن طريق تقسيم الورقة إلى جزأين أو أربعة أجزاء برمجياً باستخدام جافا سكريبت عبر مكون إضافي لـ C++.
keywords: تجميد الصفوف العليا، تجميد الصف العلوي.
---

## **مقدمة**

في هذا المقال، سوف نتعلم كيفية عرض صفوف و/أو أعمدة معينة في ألواح منفصلة عن طريق تقسيم ورقة العمل إلى جزأين أو أربعة أجزاء. عند العمل مع مجموعات البيانات الكبيرة، نحتاج إلى رؤية مناطق معينة من نفس ورقة العمل في وقت واحد للمقارنة بين مجموعات البيانات المختلفة. يمكن أن تلبي وظيفة تقسيم الشاشة احتياجاتك.

## **كيفية تقسيم الشاشة في إكسيل**
لتقسيم ورقة عمل إلى جزئين أو أربعة أجزاء، اتبع الخطوات التالية:

1. حدد الصف / العمود / الخلية قبل المكان الذي تريد وضع التقسيم فيه.
2. على علامة التبويب عرض، في مجموعة النوافذ، انقر فوق زر التقسيم.

**![شاشة مقسمة](Split-Screen.png)**

## **تقسيم ورقة العمل عمودياً على الأعمدة**

لفصل منطقتين في جدول البيانات بشكل عمودي، حدد العمود إلى اليمين من العمود الذي ترغب في ظهور التقسيم فيه، ثم انقر فوق زر التقسيم في Excel.

من السهل تقسيم ورقة العمل رأسياً على الأعمدة برمجياً باستخدام Aspose.Cells for JavaScript عبر C++، نحن فقط بحاجة إلى تحديد خلية واحدة في الصف العلوي كخلية نشطة، ثم تقسيم باستخدام طريقة [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets C1 cell in the top row as the active cell.
            sheet.activeCell = "C1";

            // Split worksheet vertically on columns
            sheet.split();

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تقسيم ورقة العمل أفقياً على الصفوف**
لفصل نافذة Excel أفقياً، حدد الصف أسفل الصف الذي ترغب في ظهور التقسيم فيه في Excel.

من السهل تقسيم ورقة العمل أفقياً على الصفوف برمجياً باستخدام Aspose.Cells for JavaScript عبر C++، نحتاج فقط إلى تحديد خلية واحدة في العمود الأيسر كخلية نشطة، ثم تقسيم باستخدام طريقة [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Sets A6 cell in the left column as the active cell.
            sheet.activeCell = "A6";

            // Split worksheet horizontally on rows
            sheet.split();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'dest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تقسيم ورقة العمل إلى أربعة أجزاء**
لعرض أربعة أقسام مختلفة من نفس ورقة البيانات بشكل متزامن، قم بتقسيم الشاشة الخاصة بك عمودياً وأفقياً في Excel.

من السهل تقسيم ورقة العمل رأسياً على الأعمدة برمجياً باستخدام Aspose.Cells for JavaScript عبر C++، نحن فقط بحاجة إلى تحديد خلية واحدة غير موجودة في الصف الأول والعمود كنشطة، ثم التقسيم باستخدام طريقة [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Active Cell and Split Worksheet Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Sets E6 cell as the active cell.
            sheet.activeCell = "E6";

            // Split worksheet into four parts
            sheet.split();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet updated successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **كيفية إزالة التقسيم**
لإزالة تقسيم ورقة العمل، فقط انقر مرة أخرى فوق زر التقسيم.

يوفر Aspose.Cells for JavaScript عبر C++ طريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--) لإزالة إعداد التقسيم.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Worksheet Example</title>
    </head>
    <body>
        <h1>Split Worksheet Example</h1>
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

            // Instantiate a new Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const sheet = workbook.worksheets.get(0);

            // Remove split and then split worksheet into four parts
            sheet.removeSplit();
            sheet.split();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet split operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
