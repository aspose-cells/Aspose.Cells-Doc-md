---
title: إعداد خيارات الطباعة باستخدام جافا سكريبت عبر C++
linktitle: ضبط خيارات الطباعة
type: docs
weight: 40
url: /ar/javascript-cpp/setting-print-options/
description: توضح هذه المقالة كيفية ضبط خيارات الطباعة لميزة إعداد صفحة ورقة العمل في إكسل برمجياً باستخدام واجهة برمجة تطبيقات جافا سكريبت ومكتبة C++. يمكنك تعيين منطقة الطباعة، عناوين الطباعة، وترتيب الصفحة.
keywords: تعيين منطقة الطباعة في إكسل بواسطة جافا سكريبت عبر C++، تعيين عناوين الطباعة في إكسل بواسطة جافا سكريبت عبر C++، تعيين ترتيب الصفحة في إكسل بواسطة جافا سكريبت عبر C++
---

{{% alert color="primary" %}}

توفر إعدادات تهيئة الصفحة في ميكروسوفت إكسيل العديد من خيارات الطباعة التي تسمح للمستخدمين بالتحكم في كيفية طباعة صفحات ورق العمل.

{{% /alert %}}

## **ضبط خيارات الطباعة**

تسمح هذه الخيارات بالطباعة:

- تحديد منطقة طباعة معينة على ورقة عمل.
- طباعة العناوين.
- طباعة خطوط الشبكة.
- طباعة عناوين الصفوف/الأعمدة.
- تحقيق جودة مسودة.
- طباعة التعليقات.
- طباعة أخطاء الخلية.
- تعريف ترتيب الصفحات.

 يدعم Aspose.Cells for JavaScript عبر C++ جميع خيارات الطباعة التي تقدمها مايكروسوفت إكسل ويمكن للمطورين بسهولة تكوين هذه الخيارات لجداول البيانات باستخدام الخصائص التي تقدمها فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). يتم مناقشة كيفية استخدام هذه الخصائص بمزيد من التفصيل أدناه.

### **تعيين منطقة الطباعة**

اف فعل، منطقة الطباعة تشمل جميع مناطق ورقة العمل التي تحتوي على بيانات. يمكن للمطورين تحديد منطقة الطباعة المحددة لورقة العمل.

لتحديد منطقة طباعة محددة، استخدم خاصية [**PageSetup.printArea**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printArea--) لفئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup). قم بتعيين نطاق الخلايا الذي يحدد منطقة الطباعة لهذه الخاصية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Set Print Area Example</title>
    </head>
    <body>
        <h1>Set Print Area Example</h1>
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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Specifying the cells range (from A1 cell to T35 cell) of the print area
            pageSetup.printArea = "A1:T35";

            // Save the workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintArea_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print area set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **تحديد عناوين الطباعة**

تسمح Aspose.Cells لك بتعيين تكرار رؤوس الصف والعمود على جميع الصفحات من ورقة العمل المطبوعة. للقيام بذلك، استخدم خاصيتي [**PageSetup.printTitleColumns**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleColumns--) و [**PageSetup.printTitleRows**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printTitleRows--) لفئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup).

يتم تعريف الصفوف أو الأعمدة التي ستتكرر عن طريق تمرير أرقامها. على سبيل المثال، يتم تعريف الصفوف كـ $1:$2 والأعمدة كـ $A:$B.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Set Print Title</title>
    </head>
    <body>
        <h1>Set Print Title Columns and Rows Example</h1>
        <p>You may optionally select an existing Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Defining column numbers A & B as title columns
            pageSetup.printTitleColumns = "$A:$B";

            // Defining row numbers 1 & 2 as title rows
            pageSetup.printTitleRows = "$1:$2";

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPrintTitle_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Print title columns and rows set successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **تحديد خيارات الطباعة الأخرى**

توفر فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) أيضًا عدة خصائص أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- [**PageSetup.printGridlines**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printGridlines--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة الشبكة أم لا.
- [**PageSetup.printHeadings**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printHeadings--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة عناوين الصفوف والأعمدة أم لا.
- [**PageSetup.blackAndWhite**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#blackAndWhite--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة ورقة العمل بالألوان الأسود والأبيض أم لا.
- [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--): يحدد ما إذا كان سيتم عرض تعليقات الطباعة على ورقة العمل أم في النهاية.
- [**PageSetup.printDraft**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printDraft--): خاصية من نوع منطقي تحدد ما إذا كنت تريد طباعة الورقة بدون رسومات.
- [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--): يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هو معروض، فارغ، شرطة أو غير متوفر.

 لضبط خصائص [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) و [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--)، يوفر Aspose.Cells for JavaScript عبر C++ أيضًُا اثنين من القيم enumeration، [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) و [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) التي تحتوي على قيم معرف مسبقًا تُعين إلى خصائص [**PageSetup.printComments**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printComments--) و [**PageSetup.printErrors**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#printErrors--) على التوالي.

القيم المعرف بها مسبقًا في التعداد [**PrintCommentsType**](https://reference.aspose.com/cells/javascript-cpp/printcommentstype) مدرجة أدناه مع أوصافها.

|**أنواع التعليقات المطبوعة**|**الوصف**|
| :- | :- |
|PrintInPlace|تحدد طباعة التعليقات كما هي معروضة على ورقة العمل.|
|PrintNoComments|تحدد عدم طباعة التعليقات.|
|PrintSheetEnd|تحدد طباعة التعليقات في نهاية ورقة العمل.|

القيم المعرف بها مسبقًا من تعداد [**PrintErrorsType**](https://reference.aspose.com/cells/javascript-cpp/printerrorstype) مدرجة أدناه مع أوصافها.

| **أنواع أخطاء الطباعة** | **الوصف** |
| :- | :- |
|PrintErrorsBlank|يحدد عدم طباعة الأخطاء.
|PrintErrorsDash|يحدد طباعة الأخطاء على شكل "--".
|PrintErrorsDisplayed|يحدد طباعة الأخطاء على النحو الذي يتم عرضه.
|PrintErrorsNA|يحدد طباعة الأخطاء على شكل "#N/A".

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Other Print Options</title>
    </head>
    <body>
        <h1>Other Print Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintCommentsType, PrintErrorsType } = AsposeCells;

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
                // Create a new workbook if no file provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Allowing to print gridlines
            pageSetup.printGridlines = true;

            // Allowing to print row/column headings
            pageSetup.printHeadings = true;

            // Allowing to print worksheet in black & white mode
            pageSetup.blackAndWhite = true;

            // Allowing to print comments as displayed on worksheet
            pageSetup.printComments = PrintCommentsType.PrintInPlace;

            // Allowing to print worksheet with draft quality
            pageSetup.printDraft = true;

            // Allowing to print cell errors as N/A
            pageSetup.printErrors = PrintErrorsType.PrintErrorsNA;

            // Saving the modified workbook to Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OtherPrintOptions_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **تحديد ترتيب الصفحة**

تقدم فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) الخاصية [**PageSetup.order**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#order--) التي تُستخدم لترتيب صفحات متعددة من ورقة العمل ليتم طباعتها. هناك احتمالان لترتيب الصفحات على النحو التالي.

- يطبع جميع الصفحات إلى الأسفل قبل طباعة أي صفحات إلى اليمين.
- يطبع الصفحات من اليسار إلى اليمين قبل طباعة الصفحات الموجودة أدنى.

تقدم Aspose.Cells تعدادًا، [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype)، يحتوي على جميع أنواع الترتيب المعرفة مسبقًا.

القيم المعرفة مسبقًا في تعداد [**PrintOrderType**](https://reference.aspose.com/cells/javascript-cpp/printordertype) مدرجة أدناه.

| **أنواع ترتيب الطباعة** | **الوصف** |
| :- | :- |
|DownThenOver|يمثل ترتيب الطباعة كاسفل ثم يمين.
|OverThenDown|يمثل ترتيب الطباعة كيمين ثم أسفل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Set Page Order Example</title>
    </head>
    <body>
        <h1>Set Page Order Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PrintOrderType } = AsposeCells;

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

            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;
            pageSetup.order = PrintOrderType.OverThenDown;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetPageOrder_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page order set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
