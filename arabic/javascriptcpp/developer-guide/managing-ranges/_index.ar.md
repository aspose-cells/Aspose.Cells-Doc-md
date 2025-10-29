---
title: إدارة النطاقات باستخدام جافا سكريبت عبر ++C
linktitle: النطاقات
type: docs
weight: 105
url: /ar/javascript-cpp/managing-ranges/
description: تعلم كيفية إدارة النطاقات في إكسل باستخدام Script عبر C++. أنشئ النطاقات، قم بتعيين القيم، الأنماط، وأداء عمليات مختلفة.
---

## **مقدمة**

في إكسل، يمكنك اختيار خلايا متعددة باستخدام تحديد الماوس؛ المجموعة المختارة تسمى "نطاق".

على سبيل المثال، يمكنك النقر على زر الماوس الأيسر في الخلية "A1" من إكسل ثم السحب إلى الخلية "C4". يمكن أيضًا إنشاء المنطقة المستطيلة التي حددتها ككائن بسهولة عن طريق استخدام Aspose.Cells for JavaScript عبر C++.

إليك كيفية إنشاء نطاق، وضع قيمة، تعيين نمط، وأداء عمليات أكثر على كائن "النطاق".

## **إدارة النطاقات باستخدام Aspose.Cells for JavaScript عبر C++**

توفر Aspose.Cells فئةً تمثل ملف Microsoft Excel، وتحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل تمثل بواسطة فئة [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells).

### **إنشاء المدى**

عندما ترغب في إنشاء منطقة مستطيلية تمتد عبر A1:C4، يمكنك استخدام الشيفرة التالية:

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells (converted from getWorksheets().get(0).getCells() to properties)
            const cells = workbook.worksheets.get(0).cells;

            // Create Range A1:C4
            const range = cells.createRange("A1:C4");

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Range A1:C4 created successfully. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **وضع قيمة في الخلايا من المدى**

فلنفترض أن لديك مدى من الخلايا يمتد عبر A1:C4. يحتوي المصفوفة على 4 * 3 = 12 خلية. ترتبت الخلايا الفردية للمدى على التوالي: Range[0,0], Range[0,1], Range[0,2], Range[1,0], Range[1,1], Range[1,2], Range[2,0], Range[2,1], Range[2,2], Range[3,0], Range[3,1], Range[3,2].

توضح الأمثلة التالية كيفية إدخال بعض القيم في الخلايا للنطاق

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Range Value Example</title>
    </head>
    <body>
        <h1>Range Value Example</h1>
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

            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            const range = cells.createRange("A1:C4");

            range.get(0, 0).value = "A1";
            range.get(0, 1).value = "B1";
            range.get(0, 2).value = "C1";
            range.get(3, 0).value = "A4";
            range.get(3, 1).value = "B4";
            range.get(3, 2).value = "C4";

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeValueTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```

### **تعيين أسلوب للخلايا من المدى**

 يوضح المثال التالي كيفية تعيين نمط خلايا النطاق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Style Example</h1>
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

            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Gets Cells
            const cells = workbook.worksheets.get(0).cells;
            // Creates Range
            const range = cells.createRange("A1:C4");
            // Puts value
            range.get(0, 0).value = "A1";
            range.get(3, 2).value = "C4";
            // Sets Style
            let style00 = workbook.createStyle();
            style00.pattern = AsposeCells.BackgroundType.Solid;
            style00.foregroundColor = new AsposeCells.Color(255, 0, 0); // Red
            range.get(0, 0).style = style00;
            let style32 = workbook.createStyle();
            style32.pattern = AsposeCells.BackgroundType.HorizontalStripe;
            style32.foregroundColor = new AsposeCells.Color(0, 255, 0); // Green
            range.get(3, 2).style = style32;
            // Saves the Workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RangeStyleTest.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```

### **الحصول على النطاق الحالي من المدى**

CurrentRegion هو خاصية تقوم بإرجاع كائن Range يمثل المنطقة الحالية 

المنطقة الحالية هي نطاق محصور بأي مزيج من الصفوف الفارغة والأعمدة الفارغة. للقراءة فقط

 في إكسل، يمكنك الحصول على منطقة CurrentRegion بواسطة:
 1. حدد منطقة (نطاق1) باستخدام مربع الماوس.
 2. انقر على "الصفحة الرئيسية - تحرير - البحث والتحديد - الانتقال الخاص - المنطقة الحالية"، أو استخدم "Ctrl+Shift+*"، سترى أن إكسل يساعدك تلقائيًا على تحديد منطقة (نطاق2). الآن، أنشئها، نطاق2 هو المنطقة الحالية لنطاق1.

يرجى تحميل ملف الاختبار التالي، فتحه في إكسل، استخدام مربع الماوس لتحديد منطقة "A1:D7"، ثم النقر على "Ctrl+Shift+*"، سترى المنطقة "A1:C3" تم تحديدها.

[current_region.xlsx](current_region.xlsx)

الآن يرجى تشغيل المثال التالي لمعرفة كيف يعمل في Aspose.Cells:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Current Region Example</h1>
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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Get Cells
            const cells = worksheet.cells;

            // Create Range
            const src = cells.createRange("A1:D7");

            // Get CurrentRegion (converted from getCurrentRegion())
            const A1C3 = src.currentRegion;

            // Save the workbook (no modifications were required by original code)
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.current_region.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Current region obtained successfully. Click the download link to download the file.</p>';
        });
    </script>
</html>
```


## **مواضيع متقدمة**
- [ملء تلقائي لنطاق ملف Excel](/cells/ar/javascript-cpp/autofill-ranges/)
- [نسخ النطاقات من Excel](/cells/ar/javascript-cpp/copy-ranges-of-Excel/)
- [نسخ بيانات النطاق فقط](/cells/ar/javascript-cpp/copy-range-data-only/)
- [نسخ بيانات النطاق بالتنسيق](/cells/ar/javascript-cpp/copy-range-data-with-style/)
- [نسخ نمط النطاق فقط](/cells/ar/javascript-cpp/copy-range-style-only/)
- [إنشاء مجموعة الاتحاد](/cells/ar/javascript-cpp/create-union-range/)
- [قص ولصق النطاق](/cells/ar/javascript-cpp/cut-and-paste-cells/)
- [حذف النطاقات](/cells/ar/javascript-cpp/delete-ranges-from-Excel/)
- [الحصول على عنوان خلية عدد الإزاحة الكاملة للعمود والصف الكامل للنطاق](/cells/ar/javascript-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [إدراج النطاقات](/cells/ar/javascript-cpp/insert-ranges-to-Excel/)
- [دمج أو فصل نطاق الخلايا](/cells/ar/javascript-cpp/merge-or-unmerge-range-of-cells/)
- [نقل مجموعة من الخلايا في ورقة العمل](/cells/ar/javascript-cpp/move-range-of-cells-in-a-worksheet/)
- [إنشاء أسماء مسماة محددة بنطاق العمل وورقة العمل](/cells/ar/javascript-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [البحث والاستبدال في بيانات النطاق](/cells/ar/javascript-cpp/search-and-replace-data-in-a-range/)
