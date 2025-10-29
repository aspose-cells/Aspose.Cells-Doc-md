---
title: عرض وإخفاء الصفوف والأعمدة وقوابض التمرير باستخدام جافا سكريبت عبر ++C
linktitle: إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير
type: docs
weight: 20
url: /ar/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/
description: يعرض هذا المقال كيفية عرض وإخفاء صفوف وأعمدة ورقة عمل إكسل برمجياً باستخدام جافا سكريبت عبر ++C. والتحكم في ظهور أشرطة التمرير وإخفاء صفوف وأعمدة متعددة بكفاءة.
---

{{% alert color="primary" %}}  
توفر Aspose.Cells وسائل للتحكم في رؤية الصفوف، الأعمدة وأشرطة التمرير بورقة العمل.  
{{% /alert %}}  

## **إظهار وإخفاء الصفوف والأعمدة**  

يوفر Aspose.Cells for JavaScript عبر ++C فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل من مايكروسوфта. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح للمطورين الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) التي تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. سنناقش بعض هذه الطرق أدناه.  

### **إظهار الصفوف والأعمدة**  

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء الطريقتين [**unhideRow(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideRow-number-number-) و [**unhideColumn(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#unhideColumn-number-number-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) على التوالي. كلا الطريقتين تتطلب معلمات:  

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.  
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unhide Row and Column Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.unhideRow(2, 13.5);
            worksheet.cells.unhideColumn(1, 8.5);

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
عند جعل عمود مخفي مرئياً، إذا كنت بحاجة لاستعادته إلى عرضه السابق أو عرضه الأصلي، يرجى إلغاء إخفاء العمود بعرض سالب. على سبيل المثال: worksheet.Cells.unhideColumn(5, -1)  
{{% /alert %}}  

### **إخفاء الصفوف والأعمدة**  

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء الطريقتين [**hideRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRow-number-) و [**hideColumn(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumn-number-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) على التوالي. كلا الطريقتين يتطلب معلمة فهرس الصف والعمود لإخفاء الصف أو العمود المحدد.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Hide Row/Column Example</h1>
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

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Hide the 3rd row (index 2) and 2nd column (index 1)
            worksheet.cells.hideRow(2);
            worksheet.cells.hideColumn(1);

            // Save the modified workbook and provide a download link
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

### **إخفاء صفوف وأعمدة متعددة**  

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء الطريقتين [**hideRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideRows-number-number-) و [**hideColumns(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#hideColumns-number-number-) من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) على التوالي. كلا الطريقتين يتطلبان فهرس الصف أو العمود الابتدائي وعدد الصفوف أو الأعمدة التي ينبغي إخفاؤها كمعلمات.  

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding 3, 4 and 5 rows in the worksheet (rows are zero-based index)
            worksheet.cells.hideRows(2, 3);

            // Hiding 2 and 3 columns in the worksheet (columns are zero-based index)
            worksheet.cells.hideColumns(1, 2);

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

## **إظهار وإخفاء شريط التمرير**  

يُستخدم شريط التمرير للتنقل في محتويات أي ملف. عادة ما تكون هناك نوعين من شرائط التمرير:  

- شرائط التمرير العمودية  
- شرائط التمرير الأفقية  

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.  

### **التحكم في رؤية شرائط التمرير**  

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، تمثل ملف إكسل. توفر فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في ظهور أشرطة التمرير، استخدم الخاصيتين [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) و [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--). [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) و [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) هما خصائص من نوع Boolean، مما يعني أن هذه الخصائص يمكنها فقط تخزين قيمة **true** أو **false**.  

#### **جعل أشرطة التمرير مرئية**  

اجعل أشرطة التمرير مرئية عن طريق تعيين خاصية [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) أو [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) للفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) إلى **صحيح**.  

#### **إخفاء أشرطة التمرير**  

إخف أشرطة التمرير عن طريق تعيين خاصية [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--) أو [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--) للفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) إلى **خطأ**.  

**كود عينة**  

بالأسفل يوجد شيفرة كاملة تفتح ملف إكسل، book1.xls، ثم تخفي كلتي الشريطين وتحفظ الملف المعدل بشكل output.xls.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Hide Scrollbars Example</h1>
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

            // Hiding the vertical scroll bar of the Excel file
            workbook.settings.isVScrollBarVisible = false;

            // Hiding the horizontal scroll bar of the Excel file
            workbook.settings.isHScrollBarVisible = false;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Scrollbars hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
