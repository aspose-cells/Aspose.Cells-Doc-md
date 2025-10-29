---
title: تنسيق الصفوف والأعمدة باستخدام JavaScript عبر C++
linktitle: الصفوف والأعمدة
type: docs
weight: 100
url: /ar/javascript-cpp/adjusting-row-height-and-column-width/
description: Aspose.Cells for JavaScript عبر C++ يمكن أن يدعم تغيير ارتفاع الصف أو عرض العمود، بالإضافة إلى تطبيق التنسيق على الصفوف أو الأعمدة.
keywords: تعيين ارتفاع الصف وعرض العمود، ضبط ارتفاع الصف وعرض العمود، تغيير ارتفاع الصف أو عرض العمود، تنسيق الصفوف والأعمدة، كيفية تعيين ارتفاع الصف وعرض العمود.
---

{{% alert color="primary" %}}
عند العمل مع جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. أحيانًا، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع أو العرض الحالي بحاجة إلى التغيير لعرض البيانات. عادةً، يقوم المستخدمون بضبط ارتفاعات الصفوف وعروض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن، مع Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.
{{% /alert %}}

## **العمل مع الصفوف**

### **كيفية ضبط ارتفاع الصف**

 يوفر Aspose.Cells for JavaScript عبر C++ فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل من Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) تتيح الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل. سيتم مناقشة بعضها بمزيد من التفصيل أدناه.

### **كيفية ضبط ارتفاع الصف**

من الممكن تعيين ارتفاع صف واحد من خلال استدعاء طريقة [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) لمجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). تأخذ طريقة [**rowHeight(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#rowHeight-number-number-) المعلمات التالية كما يلي:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Row Height Example</h1>
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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.rows.get(1).height = 13;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية ضبط ارتفاع كل الصفوف في ورقة عمل**

إذا احتاج المطورون إلى تعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل، يمكنهم القيام بذلك باستخدام خاصية [**standardHeight()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardHeight--) لمجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Standard Row Height</title>
    </head>
    <body>
        <h1>Set Standard Row Height Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the height of all rows in the worksheet to 15
            worksheet.cells.standardHeight = 15;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Standard row height set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **العمل مع الأعمدة**

### **كيفية ضبط عرض العمود**

حدد عرض العمود من خلال استدعاء مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) وطريقة [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-). تتطلب طريقة [**columnWidth(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidth-number-number-) المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Column Width Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Set Column Width</button>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of the second column to 17.5
            worksheet.cells.columns.get(1).width = 17.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية تعيين عرض العمود بالبكسل**

حدد عرض العمود من خلال استدعاء مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) وطريقة [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-). تتطلب طريقة [**columnWidthPixel(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#columnWidthPixel-number-number-) المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, عرض العمود المطلوب بالبكسل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Column Width In Pixels</title>
    </head>
    <body>
        <h1>Set Column Width In Pixels</h1>
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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Set the width of the column in pixels
            // Converted from: worksheet.getCells().setColumnWidthPixel(7, 200);
            // UNIVERSAL GETTER/SETTER CONVERSION applied:
            worksheet.cells.columnWidthPixel = [7, 200];

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetColumnWidthInPixels_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية ضبط عرض جميع الأعمدة في ورقة العمل**

لضبط عرض العمود نفسه لجميع الأعمدة في ورقة العمل، استخدم خاصية [**standardWidth()**](https://reference.aspose.com/cells/javascript-cpp/cells/#standardWidth--) لمجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Standard Width Example</title>
    </head>
    <body>
        <h1>Set Standard Width Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the width of all columns in the worksheet to 20.5
            worksheet.cells.standardWidth = 20.5;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Standard width set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تكييف صفوف وأعمدة تلقائيًا](/cells/ar/javascript-cpp/autofit-rows-and-columns/)
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/javascript-cpp/convert-text-to-columns-using-aspose-cells/)
- [نسخ الصفوف والأعمدة](/cells/ar/javascript-cpp/copying-rows-and-columns/)
- [حذف الصفوف والأعمدة الفارغة في ورقة العمل](/cells/ar/javascript-cpp/delete-blank-rows-and-columns-in-a-worksheet/)
- [تجميع وفك تجميع الصفوف والأعمدة](/cells/ar/javascript-cpp/grouping-and-ungrouping-rows-and-columns/)
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/javascript-cpp/hiding-and-showing-rows-and-columns/)
- [إدراج أو حذف الصفوف في ورقة عمل Excel](/cells/ar/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/)
- [إدراج وحذف الصفوف والأعمدة من ملف Excel](/cells/ar/javascript-cpp/inserting-and-deleting-rows-and-columns/)
- [إزالة الصفوف المكررة في ورقة العمل](/cells/ar/javascript-cpp/remove-duplicate-rows-in-a-worksheet/)
- [تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/javascript-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
