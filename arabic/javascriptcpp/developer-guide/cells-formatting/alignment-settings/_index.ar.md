---
title: إعدادات المحاذاة
linktitle: إعدادات المحاذاة
description: في مكتبة Aspose.Cells، يمكنك استخدام إعدادات محاذاة الخلية لضبط تنسيق وعرض النص باستخدام JavaScript عبر C++. توفر هذه الوثيقة خطوات مفصلة وكود عينة لاستخدام Aspose.Cells لضبط إعدادات محاذاة الخلية.
keywords: Aspose.Cells، محاذاة الخلية، المحاذاة الأفقية، المحاذاة الرأسية، التفاف النص JavaScript عبر C++
type: docs
weight: 20
url: /ar/javascript-cpp/cells-alignment-settings/
---

## **ضبط إعدادات المحاذاة**

### **إعدادات المحاذاة في Microsoft Excel**

أي شخص قد استخدم Microsoft Excel لتنسيق الخلايا سيكون متعودًا على إعدادات المحاذاة في Microsoft Excel.

كما يمكنك رؤية من الشكل أعلاه، هناك أنواع مختلفة من خيارات المحاذاة:

- محاذاة النص (أفقية وعمودية)
- المسافة البادئة.
- التوجيه.
- التحكم بالنص.
- اتجاه النص.

كل إعدادات المحاذاة هذه مدعومة تمامًا بواسطة Aspose.Cells ويتم مناقشتها بمزيد من التفصيل أدناه.

### **إعدادات المحاذاة في Aspose.Cells**

 يوفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تتيح الوصول إلى كل ورقة عمل في ملف إكسل. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). يمثل كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) كائنًا من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

يوفر Aspose.Cells طرق [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) و [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) لفئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) التي تُستخدم للحصول على وتعيين تنسيق الخلية. توفر فئة [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) خصائص مفيدة لضبط إعدادات المحاذاة.

اختر أي نوع محاذاة نص باستخدام تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype). أنواع محاذاة النص المعرفة مسبقًا في تعداد [**TextAlignmentType**](https://reference.aspose.com/cells/javascript-cpp/textalignmenttype) هي:

|** أنواع محاذاة النص **|** الوصف **|
| :- | :- |
|Bottom|يمثل محاذاة النص السفلي
|Center|يمثل محاذاة النص الوسطية
|CenterAcross|تمثل محاذاة النص في وسط النص|
|Distributed|تمثل توزيع محاذاة النص|
|Fill|تمثل ملء محاذاة النص|
|General|تمثل محاذاة النص العامة|
|Justify|تمثل محاذاة النص التبريري|
|Left|يمثل محاذاة النص اليسار|
|Right|يمثل محاذاة النص اليمين|
|Top|يمثل محاذاة النص العلوي|
|JustifiedLow|يُحاذي النص بطول كاشيدا معدل للنص العربي.|
|ThaiDistributed|يوزع النص التايلاندي خصوصًا، لأن كل حرف يُعامل ككلمة.|

{{% alert color="primary" %}}

يمكنك أيضًا تطبيق إعداد التوزيع المبرر باستخدام طريقة [**Style.isJustifyDistributed(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isJustifyDistributed-boolean-).

{{% /alert %}}

#### **المحاذاة الأفقية**

استخدم طريقة [**horizontalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#horizontalAlignment-textalignmenttype-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) لمحاذاة النص أفقيًا.

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Visit Aspose!");

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



#### **المحاذاة الرأسية**

مماثل للمحاذاة الأفقية، استخدم طريقة [**verticalAlignment**](https://reference.aspose.com/cells/javascript-cpp/style/#verticalAlignment-textalignmenttype-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) لمحاذاة النص عموديًا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Create Workbook Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Clearing all the worksheets
            workbook.worksheets.clear();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal/vertical alignment of the text in the "A1" cell via style
            const style = cell.style;
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
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


#### **المسافة البادئة**

من الممكن تعيين مستوى المسافة البادئة للنص في خلية باستخدام طريقة [**indentLevel**](https://reference.aspose.com/cells/javascript-cpp/style/#indentLevel-number-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Set Cell Indent Level Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the horizontal alignment of the text in the "A1" cell
            const style = cell.style;

            // Setting the indentation level of the text (inside the cell) to 2
            style.indentLevel = 2;

            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



#### **الاتجاه**

قم بضبط اتجاه (تدوير) النص في خلية باستخدام طريقة [**rotationAngle**](https://reference.aspose.com/cells/javascript-cpp/style/#rotationAngle-number-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Modify Cell</h1>
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
            // This example creates a new workbook, updates A1, sets rotation, and saves the file.
            const fileInput = document.getElementById('fileInput');

            // Instantiate a new Workbook (blank)
            const workbook = new Workbook();

            // Obtain reference to the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Setting the rotation of the text (inside the cell) to 25
            style.rotationAngle = 25;

            // Assign the modified style back to the cell
            cell.style = style;

            // Save the Excel file in Excel 97-2003 format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **التحكم في النص**

يناقش القسم التالي كيفية التحكم في النص عن طريق تعيين التفاف النص، وتقليل حجم النص للتناسب وخيارات التنسيق الأخرى.

##### **تفاف النص**

جعل النص يتدفق داخل خلية أسهل في القراءة: يتكيف ارتفاع الخلية لاحتواء كل النص، بدلاً من قطعه أو تسربه إلى خلايا مجاورة. قم بتشغيل أو إيقاف تشغيل تدفق النص باستخدام طريقة [**isTextWrapped(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#isTextWrapped-boolean-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Wrapping Text Example</title>
    </head>
    <body>
        <h1>Wrapping Text Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Open first Worksheet in the workbook
            const ws = workbook.worksheets.get(0);

            // Get Worksheet Cells Collection
            const cells = ws.cells;

            // Increase the width of First Column Width
            cells.columns.get(0).width = 35;

            // Increase the height of first row
            cells.rows.get(0).height = 36;

            // Add Text to the First Cell
            const cellRef = cells.checkCell(0, 0);
            cellRef.value = "I am using the latest version of Aspose.Cells to test this functionality";

            // Make Cell's Text wrap
            const style = cellRef.style;
            style.isTextWrapped = true;
            cellRef.style = style;

            // Save Excel File
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WrappingText.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


##### **تقليص للتناسب**

إحدى الخيارات لتغليف النص في حقل هي تصغير حجم النص ليتناسب مع أبعاد الخلية. يتم ذلك بضبط طريقة [**shrinkToFit(boolean)**](https://reference.aspose.com/cells/javascript-cpp/style/#shrinkToFit-boolean-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) على **true**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Cell Style Example</title>
    </head>
    <body>
        <h1>Set Cell Style Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Getting the style of the cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.shrinkToFit = true;

            // Applying the style back to the cell
            cell.style = style;

            // Saving the Excel file in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


##### **دمج الخلايا**

مثل Microsoft Excel، يدعم Aspose.Cells دمج عدة خلايا في خلية واحدة. يوفر Aspose.Cells طريقتين لهذه المهمة. إحدى الطرق هي استدعاء طريقة [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) لمجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). تتطلب طريقة [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) المعلمات التالية لدمج الخلايا:

- الصف الأول: الصف الأول من حيث بدء الدمج.
- العمود الأول: العمود الأول من حيث بدء الدمج.
- عدد الصفوف: عدد الصفوف التي تم دمجها.
- عدد الأعمدة: عدد الأعمدة المدمجة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Cells and Style Example</h1>
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

            // Create a Workbook.
            const wbk = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = wbk.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Merge some Cells (C6:E7) into a single C6 Cell.
            cells.merge(5, 2, 2, 3);

            // Input data into C6 Cell.
            const cell = cells.get(5, 2);
            cell.value = "This is my value";

            // Create a Style object to fetch the Style of C6 Cell.
            const style = cell.style;

            // Create a Font object
            const font = style.font;

            // Set the name.
            font.name = "Times New Roman";

            // Set the font size.
            font.size = 18;

            // Set the font color
            font.color = AsposeCells.Color.Blue;

            // Bold the text
            font.isBold = true;

            // Make it italic
            font.isItalic = true;

            // Set the background color of C6 Cell to Red
            style.foregroundColor = AsposeCells.Color.Red;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Apply the Style to C6 Cell.
            cell.style = style;

            // Save the Workbook.
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


الطريقة الأخرى هي استدعاء أولاً طريقة [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) لمجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) لإنشاء نطاق من الخلايا ليتم دمجها. تتلقى طريقة [**createRange**](https://reference.aspose.com/cells/javascript-cpp/cells/#createRange-string-string-) نفس مجموعة المعلمات كما في الطريقة [**merge**](https://reference.aspose.com/cells/javascript-cpp/cells/#merge-number-number-number-number-) وتعيد كائن [**Range**](https://reference.aspose.com/cells/javascript-cpp/range). كما يوفر كائن [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) طريقة [**merge**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) لدمج النطاق المحدد في كائن [**Range**](https://reference.aspose.com/cells/javascript-cpp/range).

##### **اتجاه النص**

من الممكن تعيين ترتيب قراءة النص في الخلايا. ترتيب القراءة هو الترتيب البصري الذي يظهر فيه الأحرف والكلمات وما إلى ذلك. على سبيل المثال، الإنجليزية هي لغة من اليسار إلى اليمين بينما العربية هي لغة من اليمين إلى اليسار.

يُضبط ترتيب القراءة باستخدام خاصية [**textDirection**](https://reference.aspose.com/cells/javascript-cpp/style/#textDirection-textdirectiontype-) لكائن [**Style**](https://reference.aspose.com/cells/javascript-cpp/style). يوفر Aspose.Cells أنواع اتجاه النص المعرفة مسبقًا في التعداد [**TextDirectionType**](https://reference.aspose.com/cells/javascript-cpp/textdirectiontype).

|**أنواع توجيه النص**|**الوصف**|
| :- | :- |
|Context|ترتيب القراءة متسق مع لغة الحرف الأول المُدخل|
|LeftToRight|الترتيب من اليسار إلى اليمين
|RightToLeft|الترتيب من اليمين إلى اليسار

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Modify A1 and Save</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextDirectionType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Obtaining the reference of first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "I am using the latest version of Aspose.Cells to test this functionality.";

            // Gets style in the "A1" cell
            const style = cell.style;

            // Shrinking the text to fit according to the dimensions of the cell
            style.textDirection = TextDirectionType.LeftToRight;

            // Apply the style back to the cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **مواضيع متقدمة**
- [تغيير توجيه الخلايا والاحتفاظ بالتنسيقات الحالية](/cells/ar/javascript-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [فواصل السطر وتفريغ النص](/cells/ar/javascript-cpp/line-breaks-and-text-wrapping/)
