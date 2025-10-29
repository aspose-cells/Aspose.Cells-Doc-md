---
title: إنشاء مسميات نطاقات مخصصة للمصنف وورقة العمل باستخدام جافا سكريبت عبر ك++
linktitle: النطاق المسمى
type: docs
weight: 40
url: /ar/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: تعلم كيفية إنشاء مسميات نطاقات مخصصة للمصنف وورقة العمل باستخدام سكربت Aspose.Cells for Java عبر C++. 
---

{{% alert color="primary" %}} 

يسمح Microsoft Excel للمستخدمين بتحديد مجالات مسماة بنطاقين مختلفين: نطاق العمل (المعروف أيضا باسم نطاق عالمي) ونطاق الورقة العمل.

- يمكن الوصول إلى مجالات مسماة ذات نطاق العمل من أي ورقة عمل ضمن هذا المصنف ببساطة عن طريق استخدام اسمها.
- تتم الوصول إلى مجالات المسميات ذات نطاق ورقة العمل باستخدام مرجع لورقة العمل المعينة التي تم إنشاء المسمى فيها.

يوفر سكربت Aspose.Cells for Java عبر C++ نفس الوظيفة التي توفرها Microsoft Excel لإضافة مسميات نطاقات مخصصة للمصنف وورقة العمل. عند إنشاء مسمى نطاق على ورقة عمل، يجب استخدام إشارات الورقة في المسمى لتحديده كمسمى نطاق ورقي.

{{% /alert %}} 
## **إضافة نطاق مسمى بنطاق سجل العمل**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>WorkbookScope Named Range Example</title>
    </head>
    <body>
        <h1>WorkbookScope Named Range Example</h1>
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

            // If a file is provided, load it; otherwise create a new blank workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells from Cell A1 to C10
            const workbookScope = cells.createRange("A1", "C10");

            // Assign the name to workbook scope named range
            workbookScope.name = "workbookScope";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkbookScope.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range "workbookScope" created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
## **إضافة نطاق مسمى بنطاق ورق العمل**


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Assign Range Name Example</h1>
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

            // Create new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get first worksheet of the workbook
            const sheet = workbook.worksheets.get(0);

            // Get worksheet's cells collection
            const cells = sheet.cells;

            // Create a range of Cells
            const localRange = cells.createRange("A1", "C10");

            // Assign name to range with sheet reference
            localRange.name = "Sheet1!local";

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إنشاء الوصول ونسخ نطاقات مسماة](/cells/ar/javascript-cpp/create-access-and-copy-named-ranges/)
- [تنسيق وتعديل نطاقات مسماة](/cells/ar/javascript-cpp/format-and-modify-named-ranges/)
- [الحصول على نطاق مع روابط خارجية](/cells/ar/javascript-cpp/get-range-with-external-links/)
- [تنفيذ نطاقات غير متتابعة](/cells/ar/javascript-cpp/implementing-non-sequential-ranges/)
