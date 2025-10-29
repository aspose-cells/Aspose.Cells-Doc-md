---
title: دمج و إلغاء دمج الخلايا باستخدام جافاسكريبت عبر C++
linktitle: دمج وفك دمج الخلايا
description: Aspose.Cells مكتبة جافا سكريبت للعمل مع ملفات الجدول الإلكتروني، يدعم دمج وفصل الخلايا. ستقدم هذه المقالة كيفية دمج وفصل الخلايا باستخدام مكتبة Aspose.Cells، مع خيارات لتخصيص نمط الخلية المدمجة.
keywords: Aspose.Cells، مكتبة جافا سكريبت، جدول بيانات، دمج الخلايا، فصل الخلايا، إعدادات النمط، أنماط مخصصة
type: docs
weight: 190
url: /ar/javascript-cpp/merging-and-unmerging-cells/
---

{{% alert color="primary" %}} 

تدعم Aspose.Cells هذه الميزة ويمكنها أيضًا دمج الخلايا في ورقة العمل. يمكنك فصل أو تقسيم الخلايا المدمجة أيضًا. الإشارة المرجعية للخلية المدمجة هي الإشارة المرجعية للخلية اليسرى العلوية في النطاق المحدد الأصلي.

{{% /alert %}} 
## **مقدمة**
غالبًا ما لا ترغب في نفس عدد الخلايا في كل صف أو عمود. على سبيل المثال، قد ترغب في وضع عنوان في خلية تمتد عبر عدة أعمدة. أو، إذا كنت تقوم بإنشاء فاتورة، قد ترغب في أقل عدد من الأعمدة للمجموع. لدمج خلية واحدة من خلايا أكثر من اثنين، قم بدمجهم. يتيح Microsoft Excel للمستخدمين تحديد الملفات ودمجها لتنظيم جدول البيانات بالطريقة التي يرغبون فيها.

{{% alert color="primary" %}} 

يرجى ملاحظة أنه عند دمج الخلايا، يتم الاحتفاظ فقط بالبيانات الموجودة في الخلية العليا اليسرى. إذا كانت هناك بيانات في الخلايا الأخرى في النطاق، فسيتم حذف هذه البيانات. التشكيل أيضًا يعتمد على خلية المرجع بحيث عند دمج الخلايا، يتم تطبيق إعدادات التنسيق الخاصة بالخلية العليا اليسرى على الخلية المدمجة. عند تقسيم الخلية، تحتفظ الخلايا الجديدة بإعدادات التنسيق الأصلية الخاصة بها.

{{% /alert %}} 
## **دمج الخلايا في ورقة العمل**
### **دمج الخلايا في Microsoft Excel**
الخطوات التالية تصف كيفية دمج الخلايا في ورق العمل باستخدام برنامج MS Excel.

1. قم بنسخ البيانات التي تريدها إلى أعلى يسار الخلية ضمن النطاق.
1. حدد الخلايا التي تريد دمجها.
1. لدمج الخلايا في صف أو عمود وتوسيط محتوى الخلية، انقر على أيقونة **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **دمج الخلايا باستخدام Aspose.Cells**
فئة خانات Aspose.Cells.Cells تحتوي على بعض الطرق المفيدة للمهمة. على سبيل المثال، الطريقة `merge()` تدمج الخلايا في خلية واحدة ضمن نطاق محدد.

المثال التالي يوضح كيفية دمج الخلايا (C6:E7) في ورق العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Cells Example</h1>
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
            // Create a Workbook.
            const wbk = new Workbook();

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

            // Saving the Workbook and providing download link
            const outputData = wbk.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **رفع الدمج (تقسيم) الخلايا المدمجة**
### **استخدام Microsoft Excel**
الخطوات التالية تصف كيفية تقسيم الخلايا المدمجة باستخدام Microsoft Excel.

1. حدد الخلية المدمجة.
   عندما يتم دمج الخلايا، يتم تحديد **دمج وتوسيط** في شريط الأدوات **التنسيق**.
1. انقر على **دمج وتوسيط** في شريط الأدوات **التنسيق**.

### **استخدام Aspose.Cells**
فئة خلايا Aspose.Cells.Cells تحتوي على طريقة تسمى `unmerge()` تفصل الخلايا إلى حالتها الأصلية. تقوم الطريقة بإلغاء دمج الخلايا باستخدام مرجع الخلية في نطاق الخلايا المدمجة.

المثال التالي يوضح كيفية تقسيم الخلايا المدمجة (C6). يستخدم المثال الملف الذي تم إنشاؤه في المثال السابق ويقوم بتقسيم الخلايا المدمجة.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Unmerge Cells Example</title>
    </head>
    <body>
        <h1>Unmerge Cells Example</h1>
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

            // Create a Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create a Worksheet and get the first sheet.
            const worksheet = workbook.worksheets.get(0);

            // Create a Cells object to fetch all the cells.
            const cells = worksheet.cells;

            // Unmerge the cells at row 5, column 2 spanning 2 rows and 3 columns
            cells.unMerge(5, 2, 2, 3);

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'unmergingcells.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Cells unmerged successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [كشف الخلايا المدمجة في ورقة العمل](/cells/ar/javascript-cpp/detect-merged-cells-in-a-worksheet/)
