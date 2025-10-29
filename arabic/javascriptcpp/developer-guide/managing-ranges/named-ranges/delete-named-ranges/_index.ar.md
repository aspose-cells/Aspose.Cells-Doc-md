---
title: حذف النطاقات المسماة باستخدام JavaScript عبر C++
linktitle: حذف المدى المسمى
type: docs
weight: 90
url: /ar/javascript-cpp/Delete-named-ranges/
description: يمكنك تعلم كيفية إزالة الأسماء المحددة أو النطاقات المسماة من ملفات Excel أو OpenOffice باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **مقدمة**
إذا كان هناك الكثير من الأسماء المحددة أو النطاقات المسماة في ملفات Excel، يجب علينا مسح بعضها لأنها لم يتم الرجوع إليها مرة أخرى.

## **إزالة النطاق المسمى في MS Excel**

لإزالة نطاق مسمى من Excel، يمكنك اتباع هذه الخطوات:
1. افتح Microsoft Excel وافتح المصنف الذي يحتوي على النطاق المسمى.
2. انتقل إلى علامة "الصيغ" في شريط أدوات Excel.
3. انقر على زر "مدير الأسماء" في مجموعة "الأسماء المحددة". سيفتح ذلك صندوق حوار مدير الأسماء.
4. في صندوق حوار مدير الأسماء، حدد النطاق المسمى الذي تريد إزالته.
5. انقر على الزر "حذف". قم بتأكيد الحذف عندما يُطلب.
6. انقر على الزر "إغلاق" لإغلاق صندوق حوار مدير الأسماء.
7. احفظ المصنف للحفاظ على التغييرات.

## **حذف نطاق مسمى باستخدام Aspose.Cells for JavaScript عبر C++**
باستخدام Aspose.Cells for JavaScript عبر C++، يمكنك إزالة النطاقات المسماة أو الأسماء المحددة بواسطة [النص](https://reference.aspose.com/cells/javascript-cpp/namecollection/#remove-string-) أو [الفهرس](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-) في القائمة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Named Ranges Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted a named range by text.
            worksheets.names.remove("NamedRange");

            // Deleted a defined name by index. Ensure to check the count before removal.
            if (worksheets.names.count > 0) {
                worksheets.names.removeAt(0);
            }

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

ملاحظة: إذا تم الإشارة إلى الاسم المعرف بواسطة الصيغ، لا يمكن إزالته. يمكننا فقط إزالة صيغة الاسم المعرف.

## **إزالة بعض النطاقات المسماة**
عندما نقوم بإزالة اسم محدد، يجب علينا التحقق مما إذا كانت تتم الرجوع إليه في جميع الصيغ في الملف.
لتحسين أداء إزالة النطاقات المعرفة، يمكننا إزالتها معًا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Remove Named Ranges Example</h1>
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

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Delete some defined names.
            worksheets.names.remove(["NamedRange1", "NamedRange2"]);

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named ranges removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إزالة الأسماء المحددة المكررة**
تصاب بعض ملفات Excel بالضرر بسبب تكرار الأسماء المعرفة. لذلك، يمكننا إزالة الأسماء المكررة لإصلاح الملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Remove Duplicate Defined Names</h1>
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

            // Instantiate a new Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Deleted some defined names.
            worksheets.names.removeDuplicateNames();

            // Save the workbook to retain the changes.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Duplicate defined names removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
