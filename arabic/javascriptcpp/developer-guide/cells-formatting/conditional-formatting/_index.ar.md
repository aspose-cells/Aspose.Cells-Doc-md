---
title: ضبط التنسيقات الشرطية لملفات Excel و ODS
linktitle: تنسيقات مشروطة
type: docs
weight: 60
url: /ar/javascript-cpp/conditional-formatting/
description: كيفية تطبيق التنسيقات الشرطية على ملفات إكسل و ODS باستخدام جافاسكريبت عبر C++.
keywords: تطبيق التنسيقات الشرطية جافاسكريبت عبر C++
---

## **مقدمة**

التنسيق الشرطي هو ميزة متقدمة تسمح لك بتطبيق تنسيقات على خلية أو نطاق خلايا وتغير ذلك التنسيق اعتمادًا على قيمة الخلية أو قيمة صيغة. على سبيل المثال، يمكنك جعل خلية غامقة فقط عندما تكون قيمة الخلية أكبر من 500. عندما تستوفي قيمة الخلية الشرط، يتم تطبيق التنسيق المحدد على الخلية. إذا لم تستوفِ قيمة الخلية الشرط، يتم استخدام التنسيق الافتراضي للخلية. في Microsoft Excel، اختر **تنسيق**، ثم **التنسيق الشرطي** لفتح مربع حوار التنسيق الشرطي.

Aspose.Cells تدعم تطبيق التنسيق الشرطي على الخلايا أثناء التشغيل. يوضح هذا المقال كيفية القيام بذلك. كما يوضح كيفية حساب اللون الذي يستخدمه Excel لتنسيق اللون الشرطي.

## **تطبيق التنسيق الشرطي**

Aspose.Cells تدعم التنسيق الشرطي بعدة طرق:

- باستخدام جدول البيانات للمصمم
- باستخدام طريقة النسخ.
- إنشاء التنسيق الشرطي أثناء التشغيل.

### **استخدام جدول البيانات للمصمم**

يمكن للمطورين إنشاء جدول بيانات للمصمم يحتوي على تنسيق شرطي في Microsoft Excel ثم فتح هذا الجدول بواسطة Aspose.Cells. تحمل Aspose.Cells وتحفظ جدول البيانات الخاص بالمصمم، مع الإبقاء على أي إعدادات تنسيق شرطي.

### **استخدام طريقة النسخ**

تسمح Aspose.Cells للمطورين بنسخ إعدادات التنسيق الشرطي من خلية إلى أخرى في ورقة العمل عن طريق استدعاء الطريقة [**Range.copy()**](https://reference.aspose.com/cells/javascript-cpp/range/#copy-range-).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Open workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get image data from the icon
            const imageData = icon.imageData;

            // Create a blob and provide download link for the image
            const blob = new Blob([imageData], { type: "image/jpeg" });
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```


## **تطبيق التنسيق الشرطي أثناء التشغيل**

Aspose.Cells تتيح لك إضافة وإزالة التنسيق الشرطي أثناء التشغيل. الأمثلة البرمجية أدناه تُظهر كيفية تحديد التنسيق الشرطي:

1. قم بإنشاء ورقة العمل.
1. أضف تنسيق شرطي فارغ.
1. حدد النطاق الذي ينبغي تطبيق التنسيق عليه.
1. حدد شروط التنسيق.
4. حفظ الملف.

بعد هذا المثال يأتي عدد من الأمثلة الصغيرة الأخرى التي توضح كيفية تطبيق إعدادات الخط، إعدادات الحدود، وأنماط.

أضاف Microsoft Excel 2007 تنسيقًا شرطيًا أكثر تقدمًا تدعمه Aspose.Cells أيضًا. توضح الأمثلة هنا كيفية استخدام التنسيق البسيط، في حين توضح أمثلة Microsoft Excel 2007 كيفية تطبيق تنسيق شرطي أكثر تقدمًا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
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
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.count;
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            let ca = AsposeCells.CellArea.createCellArea(0, 0, 0, 0);
            fcs.addArea(ca);

            ca = AsposeCells.CellArea.createCellArea(1, 1, 1, 1);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "=A2", "100");

            // Adds condition.
            const conditionIndex2 = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");

            // Sets the background color.
            const fc = fcs.get(conditionIndex);
            fc.style.backgroundColor = AsposeCells.Color.Red;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


### **تعيين الخط**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Conditional Formatting Icon Image</h1>
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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Get the A1 cell
            const cell = sheet.cells.get("A1");

            // Get the conditional formatting result object
            const cfr = cell.conditionalFormattingResult;

            // Get the icon set
            const icon = cfr.conditionalFormattingIcon;

            // Get the image data from the icon
            const imageData = icon.imageData;

            // Create a Blob and provide a download link for the image
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'imgIcon.out.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image';

            resultDiv.innerHTML = '<p style="color: green;">Image extracted successfully! Click the download link to save the image.</p>';
        });
    </script>
</html>
```



{{% alert color="primary" %}}

يمكنك تغيير نمط الخط فقط، لون النص، نمط التسطير، ونمط الإشطار فقط.

{{% /alert %}}

### **تعيين الحدود**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FormatConditionType, OperatorType, BorderType, CellBorderType, Color } = AsposeCells;

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
            // This example creates a new workbook, adds conditional formatting and offers the result for download.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(FormatConditionType.CellValue, OperatorType.Between, "50", "100");

            // Sets the borders' line style to dashed and colors
            const fc = fcs.get(conditionIndex);
            fc.style.borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Dashed;
            fc.style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Dashed;

            fc.style.borders.get(BorderType.LeftBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.RightBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.TopBorder).color = new Color(0, 255, 255);
            fc.style.borders.get(BorderType.BottomBorder).color = new Color(255, 255, 0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

يمكنك استخدام أنماط خط رفيع فقط للحد الخارجي. لا يُسمح بالخطوط القطرية.

{{% /alert %}}

### **تعيين النمط**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Add Conditional Formatting Example</h1>
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
            const file = fileInput.files && fileInput.files.length ? fileInput.files[0] : null;

            // Instantiate workbook from uploaded file or create a new one
            let workbook;
            if (file) {
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Adds an empty conditional formatting
            const index = sheet.conditionalFormattings.add();
            const fcs = sheet.conditionalFormattings.get(index);

            // Sets the conditional format range.
            const ca = AsposeCells.CellArea.createCellArea(0, 0, 5, 3);
            fcs.addArea(ca);

            // Adds condition.
            const conditionIndex = fcs.addCondition(AsposeCells.FormatConditionType.CellValue, AsposeCells.OperatorType.Between, "50", "100");
            const fc = fcs.get(conditionIndex);

            // Apply style using property assignments (getter/setter conversion)
            fc.style.pattern = AsposeCells.BackgroundType.ReverseDiagonalStripe;
            fc.style.foregroundColor = new AsposeCells.Color(255, 255, 0);
            fc.style.backgroundColor = new AsposeCells.Color(0, 255, 255);

            // Save workbook to browser downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting added. Click the download link to get the modified file.</p>';
        });
    </script>
    </body>
</html>
```



## **مواضيع متقدمة**  
- [إضافة التدرج اللوني ثنائي اللون والثلاثي اللون](/cells/ar/javascript-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [تطبيق التنسيق الشرطي في الأوراق العمل](/cells/ar/javascript-cpp/apply-conditional-formatting-in-worksheets/)  
- [تطبيق التظليل على الصفوف والأعمدة البديلة باستخدام التنسيق الشرطي](/cells/ar/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [توليد صور شريط بيانات التنسيق الشرطي](/cells/ar/javascript-cpp/generate-conditional-formatting-databars-images/)  
- [الحصول على مجموعات الرموز، أشرطة البيانات أو كائنات مقياس الألوان المستخدمة في التنسيق الشرطي](/cells/ar/javascript-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)
