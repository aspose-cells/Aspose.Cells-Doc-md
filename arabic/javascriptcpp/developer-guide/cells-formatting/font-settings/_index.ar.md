---
title: إعدادات الخط باستخدام JavaScript عبر C++
linktitle: إعدادات الخط
description: Aspose.Cells هي مكتبة جافاسكريبت للعمل مع ملفات جداول البيانات. تدعم تعيين إعدادات الخط للخلية، مما يسمح للمستخدمين بتخصيص نمط وخصائص الخط للخلية. ستقدم هذه المقالة مقدمة حول كيفية استخدام مكتبة Aspose.Cells لضبط إعدادات خط الخلية.
keywords: Aspose.Cells، الخلايا، إعدادات الخط، الأنماط، الخصائص، جافاسكريبت عبر C++
type: docs
weight: 30
url: /ar/javascript-cpp/cells-font-settings/
---

{{% alert color="primary" %}}  
يمكن التحكم في مظهر النص عن طريق تغيير إعدادات الخط. يمكن أن تتضمن إعدادات الخط الاسم والنمط والحجم واللون وتأثيرات أخرى للخطوط. تدعم Aspose.Cells أيضًا تكوين إعدادات الخط للخلايا تمامًا مثل Microsoft Excel.  
{{% /alert %}}  

## **تكوين إعدادات الخط**  

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل من مايكروسوفت. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). كل عنصر في مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) يمثل كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).  

توفر Aspose.Cells فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) + طرق [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) و [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) التي تُستخدم للحصول على وتعيين أسلوب تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) خصائص لضبط إعدادات الخط.  

### **تعيين اسم الخط**  

يمكن للمطورين تطبيق أي خط على النص داخل خلية باستخدام طريقة [**name**](https://reference.aspose.com/cells/javascript-cpp/font/#name-string-) للكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook</button>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font name to "Times New Roman"
            style.font.name = "Times New Roman";

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **تعيين نمط الخط إلى عريض**  

يمكن للمطورين جعل النص عريضًا عن طريق ضبط طريقة [**isBold**](https://reference.aspose.com/cells/javascript-cpp/font/#isBold-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) على **true**.   

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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font weight to bold
            style.font.isBold = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and A1 updated. Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **تعيين حجم الخط**  

ضبط حجم الخط باستخدام طريقة [**size**](https://reference.aspose.com/cells/javascript-cpp/font/#size-number-) من كائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--).  

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
            const resultDiv = document.getElementById('result');

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.count;
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font size to 14
            style.font.size = 14;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **تعيين لون الخط**  

استخدم طريقة [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-) للكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) لضبط لون الخط. اختر أي لون من تعداد الألوان (جزء من جافاسكريبت) وقم بتعيينه إلى الطريقة [**color**](https://reference.aspose.com/cells/javascript-cpp/font/#color-color-).  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Worksheet and Set Cell Style Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font color to blue
            style.font.color = AsposeCells.Color.Blue;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and cell styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### **تعيين نوع تسطير الخط**  

استخدم طريقة [**underline**](https://reference.aspose.com/cells/javascript-cpp/font/#underline-fontunderlinetype-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) لتحت underline النص. تقدم Aspose.Cells أنواعunderline للخط المعرفة مسبقًا في تعداد [**FontUnderlineType**](https://reference.aspose.com/cells/javascript-cpp/fontunderlinetype).  

|**أنواع تسطير الخط**|**الوصف**|  
| :- | :- |  
|Accounting|تسطير واحد للحساب|  
|Double|تسطير مزدوج|  
|DoubleAccounting|تسطير حسابي مزدوج|  
|None|بدون تسطير|  
|Single|تسطير واحد|  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FontUnderlineType } = AsposeCells;

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the font to be underlined
            style.font.underline = FontUnderlineType.Single;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready to download.</p>';
        });
    </script>
</html>
```


### **ضبط تأثير شطب**  

تطبيق الخط عبر تحديد طريقة [**isStrikeout**](https://reference.aspose.com/cells/javascript-cpp/font/#isStrikeout-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) إلى **true**.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting the strike out effect on the font
            style.font.isStrikeout = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **ضبط تأثير الرمز الفرعي**  

تطبيق الحالة الفرعية عبر تحديد طريقة [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) لكائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) إلى **true**.  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Add Worksheet</h1>
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
            const resultDiv = document.getElementById('result');

            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet and get its index
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access the "A1" cell
            const cell = worksheet.cells.get("A1");

            // Set value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtain the style of the cell
            const style = cell.style;

            // Set strikeout on the font
            style.font.isStrikeout = true;

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



### **ضبط تأثير الرمز العلوي على الخط**  

يمكن للمطورين تطبيق تأثير المرفوع على الخط عبر تعيين طريقة [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) من كائن [**Font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) إلى **true**.  

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Obtaining the style of the cell
            const style = cell.style;

            // Setting superscript effect
            style.font.isSuperscript = true;

            // Applying the style to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


## **مواضيع متقدمة**  
- [تطبيق تأثيرات الرمز العلوي والرمز السفلي على الخطوط](/cells/ar/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/)  
- [الحصول على قائمة الخطوط المستخدمة في جدول بيانات أو كتاب عمل](/cells/ar/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/)
