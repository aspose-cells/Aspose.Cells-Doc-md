---
title: إدراج وحذف الصفوف والأعمدة من ملف إكسل
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/javascript-cpp/inserting-and-deleting-rows-and-columns/
description: يعرض هذا المقال كيفية إدراج وحذف الصفوف والأعمدة بواسطة Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: تُدير Aspose.Cells JavaScript عبر C++ الصفوف والأعمدة، إدراج الصفوف والأعمدة، حذف الصفوف والأعمدة
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل. 
لتلبية هذه المتطلبات، يوفر Aspose.Cells for JavaScript عبر C++ مجموعة بسيطة جدًا من الفئات والطرق، والتي تناقش أدناه.

### **إدارة الصفوف والأعمدة**

يوفر Aspose.Cells for JavaScript عبر C++ فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) تسمح بالوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. من بين هذه الطرق ما يلي.

{{% alert color="primary" %}}

عند إضافة الصفوف أو الأعمدة، يتم إزاحة المحتوى في ورقة العمل إلى الأسفل أو إلى اليمين، وعند إزالة الصفوف أو الأعمدة، يتم إزاحة المحتوى للأعلى أو إلى اليسار.

{{% /alert %}}


## **إدراج الصفوف والأعمدة**

### **كيفية إدراج صف**

إدراج صف في ورقة العمل في أي مكان عن طريق استدعاء طريقة [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تأخذ طريقة [**insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) مؤشر الصف الذي سيتم إدراج الصف الجديد فيه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Insert Row Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Inserting a row into the worksheet at 3rd position (index 2)
            worksheet.cells.insertRow(2);

            // Saving the modified Excel file as Excel97To2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية إدراج عدة صفوف**

لإضافة صفوف متعددة إلى ورقة العمل، استدعي طريقة [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تأخذ الطريقة [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) معلمتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Rows Example</title>
    </head>
    <body>
        <h1>Insert Rows Example</h1>
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

            // Inserting 10 rows into the worksheet starting at index 2
            worksheet.cells.insertRows(2, 10);

            // Saving the modified Excel file (Excel 97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية إدراج صف مع تنسيق**

لإدراج صف بالتنسيق، استخدم التحميل الزائد [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) الذي يأخذ [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) كمعلمة. اضبط الخاصية [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) من فئة [**InsertOptions**](https://reference.aspose.com/cells/javascript-cpp/insertoptions) باستخدام تعداد [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/). يحتوي التعداد [**CopyFormatType**](https://reference.aspose.com/cells/javascript-cpp/copyformattype/) على ثلاثة أعضاء كما هو مدرج أدناه.

- SameAsAbove: يقوم بتنسيق الصف مثل الصف الذي يسبقه.
- نفس_كما_أسفل: تنسيق الصف بنفس تنسيق الصف أدناه.
- Clear: يُمسح التنسيق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Inserting a Row With Formatting Example</title>
    </head>
    <body>
        <h1>Inserting a Row With Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, InsertOptions, CopyFormatType, Utils } = AsposeCells;

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

            // Setting Formatting options
            const insertOptions = new InsertOptions();
            insertOptions.copyFormatType = CopyFormatType.SameAsAbove;

            // Inserting a row into the worksheet at 3rd position
            worksheet.cells.insertRows(2, 1, insertOptions);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertingARowWithFormatting.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **كيفية إدراج عمود**

كما يمكن للمطورين إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تأخذ الطريقة [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertColumn-number-boolean-) مؤشر العمود الذي سيتم إدراج العمود الجديد فيه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Insert Column Example</title>
    </head>
    <body>
        <h1>Insert Column Example</h1>
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

            // Inserting a column into the worksheet at 2nd position
            worksheet.cells.insertColumn(1);

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **حذف الصفوف والأعمدة**

### **كيفية حذف عدة صفوف**

لحذف صفوف متعددة من ورقة العمل، استدعِ طريقة [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تأخذ الطريقة [**deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) معلمتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Delete Rows Example</title>
    </head>
    <body>
        <h1>Delete Rows Example</h1>
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting 10 rows from the worksheet starting from 3rd row (index 2)
            worksheet.cells.deleteRows(2, 10);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **كيفية حذف عمود**

لحذف عمود من ورقة العمل في أي مكان، استدعِ طريقة [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تأخذ الطريقة [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteColumn-number-boolean-) مؤشر العمود الذي سيتم حذفه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Delete Column Example</title>
    </head>
    <body>
        <h1>Delete Column Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Deleting a column from the worksheet at 5th position (zero-based index 4)
            worksheet.cells.deleteColumn(4);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Column deleted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
