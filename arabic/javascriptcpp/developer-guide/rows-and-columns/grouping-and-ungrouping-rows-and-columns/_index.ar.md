---
title: تجميع وفك تجميع الصفوف والأعمدة باستخدام جافاسكرابت عبر C++
linktitle: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 50
url: /ar/javascript-cpp/grouping-and-ungrouping-rows-and-columns/
description: اكتشاف كيفية تجميع وفك تجميع الصفوف والأعمدة في إكسل باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

|**تجميع الصفوف والأعمدة.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة تجميع الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف مايكروسوفت إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) الذي يسمح بالوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل، حيث سنناقش أدناه بعض هذه الطرق بمزيد من التفاصيل.

### **تجميع الصفوف والأعمدة**

من الممكن تجميع الصفوف أو الأعمدة عبر استدعاء طريقي [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupRows-number-number-boolean-) و[**groupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#groupColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). كلا الطريقتين يقبل المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Rows and Columns Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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

            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows and columns grouped successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

يمكن للمطورين تكوين إعدادات التجميع هذه باستخدام خاصية [**outline**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#outline--) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

### **صفوف ملخصية أسفل التفاصيل**

من الممكن التحكم في ما إذا كانت صفوف الملخص تظهر أسفل التفاصيل عن طريق تعيين الخاصية [**summaryRowBelow**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryRowBelow--) من فئة [**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline) إلى **true** أو **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Group Rows/Columns and Set Outline</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Setting SummaryRowBelow property to false
            worksheet.outline.summaryRowBelow = false;

            // Saving the modified Excel file (Excel97To2003 -> .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **أعمدة ملخصية على يمين التفاصيل**

يمكن للمطورين أيضًا التحكم في عرض أعمدة الملخص إلى يمين التفاصيل من خلال تعيين الخاصية [**summaryColumnRight**](https://reference.aspose.com/cells/javascript-cpp/outline/#summaryColumnRight--) من فئة [**Outline**](https://reference.aspose.com/cells/javascript-cpp/outline) إلى **true** أو **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Group Rows and Columns Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Grouping first six rows and first three columns
            worksheet.cells.groupRows(0, 5, true);
            worksheet.cells.groupColumns(0, 2, true);

            // Set summary column to right
            worksheet.outline.summaryColumnRight = true;

            // Saving the modified Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إلغاء تجميع الصفوف والأعمدة**

لفك تجميع أي صفوف أو أعمدة مجمعة، استدعي طرق [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) و[**ungroupColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). كلا الطريقتين يقبلان معلمين:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#ungroupRows-number-number-boolean-) لديه تحميل مفرط يأخذ معلمة ثالثة من نوع منطقي. تعيينها إلى **true** يزيل جميع المعلومات المجمعة. وإلا، يتم إزالة معلومات التجميع الخارجية فقط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Ungroup Rows and Columns Example</h1>
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

            // Instantiating a Workbook object with file content
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Ungrouping first six rows (from 0 to 5)
            worksheet.cells.ungroupRows(0, 5);

            // Ungrouping first three columns (from 0 to 2)
            worksheet.cells.ungroupColumns(0, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
