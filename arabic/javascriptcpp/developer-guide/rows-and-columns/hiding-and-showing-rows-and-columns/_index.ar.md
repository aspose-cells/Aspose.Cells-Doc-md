---
title: إخفاء وإظهار الصفوف والأعمدة باستخدام جافاسكرابت عبر C++
linktitle: إخفاء وعرض الصفوف والأعمدة
type: docs
weight: 60
url: /ar/javascript-cpp/hiding-and-showing-rows-and-columns/
description: تعلم كيفية إخفاء وإظهار الصفوف والأعمدة في ورقة عمل باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

في بعض الأحيان، من المنطقي إخفاء بعض الصفوف أو الأعمدة في ورقة عمل وعرضها لاحقًا. يوفر Microsoft Excel هذه الميزة وكذلك Aspose.Cells.

{{% /alert %}}

## **التحكم في رؤية الصفوف والأعمدة**

 يوفر Aspose.Cells for JavaScript عبر C++ فئة ، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) ، التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تم مناقشة بعض منها أدناه. 

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء الطريقتين [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) و [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) على التوالي. كلا الطريقتين يتطلب معلمة فهرس الصف والعمود لإخفاء الصف أو العمود المحدد.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Row and Column Example</h1>
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

            // Instantiating a Workbook object with Uint8Array
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the 3rd row of the worksheet
            worksheet.cells.hideRow(2);

            // Hiding the 2nd column of the worksheet
            worksheet.cells.hideColumn(1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Row and column hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **عرض الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء الطريقتين [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) و [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) على التوالي. كلا الطريقتين تتطلب معلمات:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Unhide Rows and Columns Example</title>
    </head>
    <body>
        <h1>Unhide Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unhiding the 3rd row and setting its height to 13.5
            worksheet.cells.unhideRow(2, 13.5);

            // Unhiding the 2nd column and setting its width to 8.5
            worksheet.cells.unhideColumn(1, 8.5);

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

{{% alert color="primary" %}}

عند جعل عمود مخفي مرئي، إذا كنت بحاجة إلى استعادته إلى عرضه السابق أو إلى عرضه الأصلي، يرجى إلغاء إخفاؤه بعرض سلبي. على سبيل المثال: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **إخفاء عدة صفوف وأعمدة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء الطريقتين [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) و [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) على التوالي. كلا الطريقتين يتطلبان فهرس الصف أو العمود الابتدائي وعدد الصفوف أو الأعمدة التي ينبغي إخفاؤها كمعلمات.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Rows and Columns</title>
    </head>
    <body>
        <h1>Hide Rows and Columns Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4, and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: 'application/octet-stream' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Rows and columns hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

من الممكن أيضًا استخدام طرق [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRows-number-number-number-) و[**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumns-number-number-number-) من فئة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) لجعل صفوف وأعمدة متعددة مرئية.

{{% /alert %}}
