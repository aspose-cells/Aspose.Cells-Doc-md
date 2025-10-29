---
title: إنشاء والوصول إلى النسخ من النطاقات المسماة باستخدام JavaScript عبر C++
linktitle: إنشاء الوصول ونسخ نطاقات الأسماء
type: docs
weight: 200
url: /ar/javascript-cpp/create-access-and-copy-named-ranges/
description: تعلم كيفية إنشاء والوصول ونسخ النطاقات المسماة في Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **مقدمة**  

عادةً، يتم استخدام تسميات الأعمدة والصفوف للإشارة إلى خلايا فردية. من الممكن إنشاء أسماء وصفية لتمثيل الخلايا، والنطاقات، والصيغ، أو القيم الثابتة. قد يشير الكلمة **اسم** إلى سلسلة من الأحرف تمثل خلية أو نطاق خلايا، أو صيغة، أو قيمة ثابتة. تعيين اسم لنطاق يعني أن هذا النطاق من الخلايا يمكن الإشارة إليه باسمه. استخدم أسماء سهلة الفهم، مثل منتجات، للإشارة إلى النطاقات التي يصعب فهمها، مثل المبيعات!C20:C30. يمكن استخدام العلامات في الصيغ التي تشير إلى البيانات على نفس ورقة العمل؛ إذا كنت تريد تمثيل نطاق على ورقة عمل أخرى، يمكنك استخدام اسم. *النطاقات المُعرفة باسم من بين أقوى ميزات Microsoft Excel، خاصة عند استخدامها كمصدر لنطاق لقوائم الاختيارات، والجداول المحورية، ومخططات البيانات، وغيرها.*  

## **العمل مع النطاق المسمى باستخدام Microsoft Excel**  

### **إنشاء نطاقات مسماة**  

الخطوات التالية تصف كيفية تسمية خلية أو نطاق خلايا باستخدام **MS Excel**. ينطبق هذا الأسلوب على **Microsoft Office Excel 2003**، **Microsoft Excel 97**، 2000، و 2002.  

1. حدد الخلية أو النطاق الذي ترغب في تسميته.  
2. انقر على **مربع الاسم** عند الطرف الأيسر من شريط الصيغة.  
3. اكتب اسم الخلايا.  
4. اضغط على ENTER.  

{{% alert color="primary" %}}  
لا يمكنك تسمية خلية أثناء تغيير محتويات الخلية.  
{{% /alert %}}  

## **العمل مع نطاق مسمى باستخدام Aspose.Cells**  

هنا، نستخدم واجهة برمجة التطبيقات Aspose.Cells للقيام بالمهمة.  
توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).  

### **إنشاء نطاق مسمى**  

من الممكن إنشاء نطاق مسمى عن طريق استدعاء [**createRange(string, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) الزائدة من مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells). إصدار نموذجي لـ [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-) يأخذ المعلمات التالية:  

- اسم الخلية العلوية اليسرى، اسم الخلية العلوية اليسرى في النطاق.  
- اسم الخلية السفلي الأيمن، اسم الخلية السفلي الأيمن في النطاق.  

عند استدعاء [**createRange(string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-)، فإنه يُرجع نطاق المصنوع حديثًا كنموذج من فئة [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). استخدم هذا [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) لتكوين النطاق المسمى. على سبيل المثال، قم بتعيين اسم النطاق باستخدام خاصية [**name**](https://reference.aspose.com/cells/javascript-cpp/range/#name--). يوضح المثال التالي كيفية إنشاء نطاق مسمّى للخلايا التي تمتد عبر B4:G14.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Creating a named range
            const range = worksheet.cells.createRange("B4", "G14");

            // Setting the name of the named range
            range.name = "TestRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

### **إدخال البيانات في الخلايا في النطاق المسمى**  

يمكنك إدخال البيانات في الخلايا الفردية لنطاق وفق النمط  

- **جافا سكريبت**: نطاق [صف،عمود]  

على سبيل المثال، لديك مجموعة مسماة من الخلايا التي تمتد بين A1:C4. تجعل المصفوفة 4 * 3 = 12 خلية. تتم ترتيب الخلايا الفردية في النطاق بشكل تسلسلي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

استخدم الخصائص التالية لتحديد الخلايا في المدى:  

- firstRow يعيد مؤشر أول صف في النطاق المسمي.  
- firstColumn يعيد مؤشر أول عمود في النطاق المسمي.  
- rowCount يعيد إجمالي عدد الصفوف في النطاق المسمي.  
- columnCount يعيد إجمالي عدد الأعمدة في النطاق المسمي.  

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Named Range Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet in the workbook.
            const worksheet1 = workbook.worksheets.get(0);

            // Create a range of cells based on H1:J4.
            const range = worksheet1.cells.createRange("H1", "J4");

            // Name the range.
            range.name = "MyRange";

            // Input some data into cells in the range.
            range.get(0, 0).value = "USA";
            range.get(0, 1).value = "SA";
            range.get(0, 2).value = "Israel";
            range.get(1, 0).value = "UK";
            range.get(1, 1).value = "AUS";
            range.get(1, 2).value = "Canada";
            range.get(2, 0).value = "France";
            range.get(2, 1).value = "India";
            range.get(2, 2).value = "Egypt";
            range.get(3, 0).value = "China";
            range.get(3, 1).value = "Philipine";
            range.get(3, 2).value = "Brazil";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangecells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range populated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

### **تحديد الخلايا في النطاق المسمى**  

يمكنك إدراج البيانات في الخلايا الفردية في المجموعة وفق النمط التالي:  

- **جافا سكريبت**: نطاق [صف،عمود]  

إذا كان لديك مدى يحمل اسم يمتد من A1:C4. المصفوفة تجعل 4 * 3 = 12 خلية. ترتب الخلايا في المدى الفردي بشكل متسلسل: Range[0,0], Range[0,1], Range[0,2], Range[1,0] ,Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].  

استخدم الخصائص التالية لتحديد الخلايا في المدى:  

- firstRow يعيد مؤشر أول صف في النطاق المسمي.  
- firstColumn يعيد مؤشر أول عمود في النطاق المسمي.  
- rowCount يعيد إجمالي عدد الصفوف في النطاق المسمي.  
- columnCount يعيد إجمالي عدد الأعمدة في النطاق المسمي.  

يظهر المثال التالي كيفية إدخال بعض القيم في الخلايا لنطاق معين.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Named Range</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Getting the specified named range
            const range = workbook.worksheets.rangeByName("TestRange");

            if (!range) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
                return;
            }

            // Identify range cells and display properties
            const firstRow = range.firstRow;
            const firstColumn = range.firstColumn;
            const rowCount = range.rowCount;
            const columnCount = range.columnCount;

            const html = [
                `<p>First Row : ${firstRow}</p>`,
                `<p>First Column : ${firstColumn}</p>`,
                `<p>Row Count : ${rowCount}</p>`,
                `<p>Column Count : ${columnCount}</p>`
            ].join('');

            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```  

### **الوصول إلى المدى المسمى**  

#### **الوصول إلى نطاق مسمى محدد**  

استدعاء [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) الكائن [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) الميثود للحصول على مدى بالاسم المحدد. تأخذ الميثود النموذجية [**rangeByName(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#rangeByName-string-) الاسم للمدى المسمى وتعيد المدى المحدد كمثيل لفئة [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). يوضح المثال التالي كيفية الوصول إلى مدى محدد بالاسم.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Named Range Example</title>
    </head>
    <body>
        <h1>Get Named Range Example</h1>
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

            // Instantiating a Workbook object
            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Getting the specified named range
            const worksheets = workbook.worksheets;
            const range = worksheets.rangeByName("TestRange");

            if (range !== null) {
                document.getElementById('result').innerHTML = `<p>Named Range : ${range.refersTo}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Named range "TestRange" not found.</p>';
            }
        });
    </script>
</html>
```  

#### **الوصول إلى كافة المدى المسمى في ورقة العمل**  

استدعِ طريقة [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) من مجموعة [**worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) للحصول على جميع النطاقات المعرفة في ورقة العمل. تقوم الطريقة [**namedRanges()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#namedRanges--) بإرجاع مصفوفة تحتوي على جميع النطاقات المعرفة في مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).  

يوضح المثال التالي كيفية الوصول إلى جميع النطاقات المسماة في ورق عمل.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Named Ranges</title>
    </head>
    <body>
        <h1>Get Named Ranges Example</h1>
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

            // Getting all named ranges
            const ranges = workbook.worksheets.namedRanges;

            if (ranges) {
                // Some collections expose 'count', others may expose 'length'
                const total = (typeof ranges.count !== 'undefined') ? ranges.count : ranges.length;
                document.getElementById('result').innerHTML = `<p style="color: green;">Total Number of Named Ranges: ${total}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No named ranges found.</p>';
            }
        });
    </script>
</html>
```  

### **نسخ المدى المسمى**  

توفر Aspose.Cells [**range.copy(Range, PasteOptions)**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-pasteoptions-) الميثود لنسخ مدى من الخلايا مع التنسيق في مدى آخر.  

المثال التالي يوضح كيفية نسخ مدى مصدر من الخلايا إلى مدى مسمى آخر.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Copy Ranges</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <p>Select an Excel file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiate a new Workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = workbook.worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { borderType: BorderType.TopBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.BottomBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.LeftBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { borderType: BorderType.RightBorder, style: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
