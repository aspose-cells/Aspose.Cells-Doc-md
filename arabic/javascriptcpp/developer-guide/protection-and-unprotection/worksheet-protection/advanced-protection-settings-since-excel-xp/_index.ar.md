---
title: إعدادات حماية متقدمة منذ إكسل XP باستخدام جافا سكريبت عبر C++
linktitle: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

منذ إصدار Excel 2002 أو XP، أضافت Microsoft العديد من إعدادات الحماية المتقدمة.

{{% /alert %}}


## **مقدمة**

تقييد أو السماح للمستخدمين بـ:

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج صفوف أو أعمدة أو روابط تشعبية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

 يدعم Aspose.Cells for JavaScript عبر C++ جميع إعدادات الحماية المتقدمة التي تقدمها إكسل XP أو الإصدارات الأحدث.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **أدوات**, اختر **الحماية** ثم **حماية الورقة**. سيتم عرض مربع الحوار.

لعرض إعدادات الحماية المتاحة في Excel 2016:

1. من القائمة **ملف**, اختر **حماية الدفتر** ثم **حماية الورقة الحالية**.
1. حدد **حماية الورقة** في قائمة **مراجعة**.

سيؤدي اتباع الخطوات المذكورة أعلاه إلى إظهار مربع حوار يمكنك من خلاله السماح أو تقييد ميزات ورقة العمل أو تطبيق كلمة مرور على ورقة العمل.

### ** إعدادات حماية متقدمة باستخدام Aspose.Cells for JavaScript عبر C++**

 يدعم Aspose.Cells for JavaScript عبر C++ جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) خاصية [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) التي تُستخدم لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) هي في الواقع كائن لفئة [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection) التي تحتوي على عدة خصائص بوليانية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

يرجى عدم استدعاء طريقة [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) من فصل [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) عند استخدام الخاصية [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--). أيضًا، قم بحفظ الملف بصيغة Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط من Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد تحرير المستخدمين للخلايا، يجب قفل الخلايا قبل تطبيق أي إعدادات حماية. وإلا، يمكن تحرير الخلايا حتى وإن كانت ورقة العمل محمية. في Microsoft Excel XP، يمكن قفل الخلايا من خلال مربع الحوار التالي:

|**مربع الحوار لقفل الخلايا في Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن قفل الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells أيضًا. يمكن أن تحوي كل خلية تنسيق [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) يحتوي على خاصية Boolean، [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). قم بضبط الخاصية [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) على **true** أو **false** لقفل الخلية أو إلغاء قفلها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
