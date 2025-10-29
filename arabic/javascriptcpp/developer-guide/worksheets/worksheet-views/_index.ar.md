---
title: عرض ملفات ورقة العمل باستخدام JavaScript عبر C++
linktitle: عروض الورقة العمل
type: docs
weight: 40
url: /ar/javascript-cpp/worksheet-views/
description: ستصف هذه المقالة كيفية استخدام JavaScript و API JavaScript للتفاعل مع معاينة فاصل الصفحة لمصنف إكسل وورقة العمل. العمل مع الألواح المنقسمة، والألواح المجمدة، ونسبة التكبير أيضًا.
---

## **معاينة كسر الصفحة**

يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

عرض عادي هو العرض الافتراضي لورقة العمل. معاينة فاصل الصفحة هو عرض تحرير يعرض ورقة العمل كما ستطبع. تُظهر معاينة فاصل الصفحة البيانات التي ستذهب على كل صفحة بحيث يمكنك ضبط منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells for JavaScript عبر C++، يمكن للمطورين تمكين وضع العرض العادي أو وضع معاينة فاصل الصفحة.

### **التحكم في أوضاع العرض**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

يتمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتمكين العرض العادي أو وضع معاينة فواصل الصفحات، استخدم [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مع [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--). [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) هو خاصية منطقية، مما يعني أنه يمكنها تخزين قيمة صحيحة أو خاطئة فقط.

#### **تمكين العرض العادي**

قم بتعيين صفحة العمل إلى العرض العادي عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) الخاصية في فئة [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) إلى **false**.

#### **تمكين معاينة كسر الصفحة**

يمكن تعيين أي صفحة عمل إلى وضع معاينة فواصل الصفحات عن طريق ضبط [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) الخاصية في فئة [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) إلى **true**. بذلك يقوم بتبديل صفحة العمل من العرض العادي إلى معاينة فواصل الصفحات.

يلي أدناه مثال كامل يوضح كيفية استخدام [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) لتمكين وضع معاينة فواصل الصفحات لأول ورقة عمل في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). يتم تبديل العرض إلى معاينة فواصل الصفحات لأول ورقة عمل عن طريق ضبط [**Worksheet.isPageBreakPreview()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isPageBreakPreview--) إلى **true**. يتم حفظ الملف المعدل باسم output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Page Break Preview</title>
    </head>
    <body>
        <h1>Page Break Preview Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Displaying the worksheet in page break preview
            worksheet.isPageBreakPreview = true;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **عامل التكبير**

### **استخدام Microsoft Excel**

يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

### **Aspose.Cells وعامل التكبير**

تسمح Aspose.Cells للمطورين بتعيين عامل تكبير الورقة.
توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل صفحة عمل في ملف Excel.

تمثل صفحة العمل في فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة صفحات العمل. لتعيين عامل تكبير الورقة، استخدم [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) في فئة [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--). يتم تعيين عامل التكبير عن طريق تعيين قيمة رقمية (صحيحة) إلى الخاصية [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--).

 يتضح أدناه مثال كامل يوضح كيفية استخدام الخاصية [**Worksheet.zoom**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#zoom--) لضبط عامل التكبير لورقة العمل الأولى في ملف Excel.

يتم فتح ملف book1.xls عن طريق إنشاء مثيل للفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). تُعين عامل التكبير للورقة العمل الأولى على 75 ويتم حفظ الملف المعدل ك output.xls.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Set Worksheet Zoom Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting the zoom factor of the worksheet to 75
            worksheet.zoom = 75;

            // Saving the modified Excel file (Excel97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Zoom set to 75 successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تجميد الألواح**

### **استخدام Microsoft Excel**

تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

### **Aspose.Cells & تجميد الألواح**

تسمح Aspose.Cells للمطورين بتطبيق تجميد الألواح على ورق العمل أثناء التشغيل.

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخواص والطرق لإدارة أوراق العمل. لضبط الألواح المجمدة، استدعِ طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) من فئة ورقة العمل. تأخذ طريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوح الأيسر.

يتم فتح ملف book1.xls بالاتصال ببناء الفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) أثناء إنشائه وتجميد عدد قليل من الصفوف والأعمدة في الورقة العمل الأولى. يتم حفظ الملف المعدل ك output.xls.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام الطريقة [**Worksheet.freezePanes(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#freezePanes-number-number-number-number-) لتجميد الصفوف والأعمدة (بداية من C4، الممثلة بالصف الرابع والعمود الثالث، حيث الصفوف والأعمدة تبدأ من فهرس 0) من ورقة العمل الأولى لملف Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Freeze Panes Example</title>
    </head>
    <body>
        <h1>Freeze Panes Example</h1>
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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Applying freeze panes settings: topRows = 3, leftColumns = 2, top = 3, left = 2
            worksheet.freezePanes(3, 2, 3, 2);

            // Saving the modified Excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/octet-stream" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Freeze panes applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تقسيم الألواح**

إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.

### **تطبيق وإزالة تقسيم الألواح**

#### **تقسيم الألواح**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. لتنفيذ عروض متقسمة، استخدم [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) لفئة [**Worksheet.split()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#split--). لإزالة تقسيم الألواح، استخدم الطريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Split Window Example</title>
    </head>
    <body>
        <h1>Split Worksheet Window Example</h1>
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

            // Instantiate a new workbook and open the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Set the active cell (converted from setActiveCell -> activeCell)
            sheet.activeCell = "A20";

            // Split the worksheet window
            sheet.split();

            // Save the excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet window split and active cell set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

بعد تشغيل الكود أعلاه، سيحتوي الملف الذي تم إنشاؤه على عرض مقسم.

#### **إزالة النوافذ**

قم بإزالة أجزاء الانقسام باستخدام الطريقة [**Worksheet.removeSplit()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#removeSplit--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Active Cell and Remove Split Example</h1>
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

            // Instantiate a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Set the active cell
            worksheet.activeCell = "A20";

            // Split the worksheet window - remove any existing split
            worksheet.removeSplit();

            // Save the modified workbook and provide a download link
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

## **مواضيع متقدمة**
- [إخفاء عرض القيم الصفرية في صفحة العمل](/cells/ar/javascript-cpp/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب الصفحة العمل](/cells/ar/javascript-cpp/set-worksheet-tab-color/)
- [إظهار وإخفاء خطوط الشبكة ورؤوس الصف والعمود](/cells/ar/javascript-cpp/show-and-hide-gridlines-and-row-column-headers/)
- [إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير](/cells/ar/javascript-cpp/show-and-hide-rows-columns-and-scroll-bars/)
- [إظهار وإخفاء الأوراق العمل وعلامات التبويب](/cells/ar/javascript-cpp/show-and-hide-worksheets-and-tabs/)
- [إظهار الصيغ بدلاً من القيم في ورقة العمل](/cells/ar/javascript-cpp/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدام خيارات فحص الأخطاء](/cells/ar/javascript-cpp/use-error-checking-options/)
