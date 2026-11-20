---
title: تجميع حقول محورية في جدول محوري
linktitle: تجميع حقول محورية في جدول محوري
description: تعلم كيفية تجميع حقول محورية للصفوف والأعمدة في جدول محوري إلى فترات زمنية مثل الأشهر والربع السنوي ونطاقات رقمية باستخدام PivotField.group و PivotFieldGroupOptions في Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, جدول محوري, تجميع حقل محوري, PivotField.group, PivotFieldGroupOptions, تجميع تاريخ, تجميع رقم, أشهر, أرباع, نطاق رقمي, JavaScript via C++
type: docs
weight: 80
url: /ar/javascript-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يكون تجميع الحقول المحورية مفيدًا عندما يحتوي حقل صف أو عمود في جدول محوري على عدد كبير من العناصر المتميزة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يقوم التجميع بدمج هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر، أرباع، وسنوات، والأرقام إلى نطاقات مثل 0-1، 2-3، 4-5. هذا يجعل جدولًا محوريًا كبيرًا أكثر تجميعًا وأسهل في التحليل. توفر Aspose.Cells هذه الإمكانية عبر طريقة `PivotField.group()` (التجميع التلقائي حسب نوع البيانات) وطريقة `PivotField.group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يعمل تجميع التاريخ على تجميع التواريخ الفردية إلى فترات أكبر، مثل الأيام، الأشهر، الأرباع والسنوات، ويُنشئ هيكلًا زمنيًا (على سبيل المثال سنوات، أرباع، أشهر). تصبح الاتجاهات عبر الزمن واضحة بنظرة واحدة، وتصبح كل مستوى من الفترات حقلًا محوريًا خاصًا به في منطقة الصف أو العمود في جدول محوري.
- يتوفر التجميع فقط للحقول الموجودة في منطقة ROW أو COLUMN في جدول محوري. لا يمكن تجميع حقل البيانات (القيمة) مباشرة. لتجميع مثل هذا الحقل يجب أولاً إضافته إلى منطقة الصف أو العمود في جدول محوري.

## **تجميع الحقول المحورية تلقائيًا**
تستكشف نسخة `PivotField.group()` التي لا تحتوي على معلمات نوع البيانات للحقول وتقوم بتجميعها تلقائيًا. يتم تجميع الحقل الذي يحتوي فقط على تواريخ (وبعض الخلايا الفارغة) حسب الأشهر. أما الحقل الذي يحتوي فقط على أرقام (وبعض الخلايا الفارغة) فيتم تجميعه إلى نطاقات رقمية باستخدام فاصل تلقائي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group Pivot Fields Automatically</title>
    </head>
    <body>
        <h1>Auto-Group a Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the second worksheet and its pivot table
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the first row field automatically by its data type
                pt.rowFields.get(0).group();
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputAutoGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **تجميع الحقول المحورية باستخدام خيارات مخصصة**
توفر الفئة `PivotFieldGroupOptions` إعدادات مخصصة للتجميع. بالنسبة لحقول التاريخ، عيّن `startDate` و `endDate` و `groupTypes`. بالنسبة للحقول الرقمية، عيّن `startNumber` و `endNumber` و `interval`. تتحكم الخاصية `newPivotField` في ما إذا كان التجميع ينشئ حقولًا محورية جديدة إلى جانب الحقل الأصلي (انظر قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والربع السنوي**
تقوم المثال التالي بتجميع حقل التاريخ في صف جدول محوري نموذجي حسب الأشهر والربع السنوي بين تاريخي بدء وانتهاء. يحمل الكود ملف Excel [العينة](sampleGroupPivotFieldsInPivotTable.xlsx)، ينفّذ التجميع، يحسب بيانات جدول محوري، ويحفظ النتيجة المجمعّة. تُظهر لقطة الشاشة النتيجة: أصبح حقل التاريخ في الصف الآن مجمعًا حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.groupTypes` يُهمل. بغض النظر عن ترتيب أنواع التجميع المُدرجة، تُعرض الحقول المجمعّة دائمًا من أكبر فترة إلى أصغرها: سنوات، أرباع، أشهر، أيام، ساعات، دقائق، ثوانٍ. في هذا المثال تُدرج الأشهر قبل الأرباع في `options.groupTypes`، إلا أن الأرباع تُعرض كمستوى خارجي والأشهر كمستوى داخلي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Date Field by Months and Quarters</title>
    </head>
    <body>
        <h1>Group a Date Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // Group the date row field by months and quarters between the given dates
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startDate = new Date(2008, 1, 1);
                options.endDate = new Date(2008, 9, 5);
                options.groupTypes = [AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters];
                pt.rowFields.get(0).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputGroupPivotFieldsInPivotTable.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

![جدول محوري مُجَمَّع حسب الأشهر والربع السنوي](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي إلى نطاقات**
`FieldTwo` في جدول محوري نموذجي هو في البداية حقل بيانات (قيمة). نظرًا لأنه لا يمكن تجميع سوى حقول الصف أو العمود، يقوم الكود أولاً باستدعاء `PivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصف، ثم يحدّث جدول محوري، ثم يجمع الحقل الرقمي إلى النطاقات 0-1، 2-3 و 4-5 باستخدام `startNumber = 0`، `endNumber = 5` و `interval = 2`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Group a Numeric Field into Ranges</title>
    </head>
    <body>
        <h1>Group a Numeric Pivot Field</h1>
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
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select the sample Excel file.</p>';
                return;
            }
            try {
                // Load the sample workbook containing the pivot table
                const wb = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const ws = wb.worksheets.get(1);
                const pt = ws.pivotTables.get(0);
                // FieldTwo is a data field: move it to the row area first,
                // because only row/column fields can be grouped
                pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
                pt.calculateData();
                // Group the numeric field into the ranges 0-1, 2-3, 4-5
                const options = new AsposeCells.PivotFieldGroupOptions();
                options.startNumber = 0;
                options.endNumber = 5;
                options.interval = 2;
                pt.rowFields.get(1).group(options);
                pt.calculateData();
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputNumberGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إهمال إصدارات طريقة `PivotField.groupBy()` وإزالتها من واجهة برمجة التطبيقات. تُعد `PivotField.group()` و `PivotField.group(PivotFieldGroupOptions)` البدائل.
- في Microsoft Excel، يؤدي تجميع حقل رقمي إلى استبدال الحقل المحوري الأصلي بالنطاقات المُجمَّعة، بينما يؤدي تجميع حقل تاريخ إلى إنشاء حقول محورية جديدة (واحد لكل مستوى تجميع، مثل الأرباع والأشهر) بجوار الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع طرق `PivotField.group()` نفس السلوك كما في Excel. خاصية `PivotFieldGroupOptions.newPivotField` موجودة للتوافق مع الإصدارات القديمة: تكون قيمتها الافتراضية false لتجميع الأرقام وtrue لتجميع التاريخ والوقت؛ اضبطها إلى false إذا كنت تريد أن يستبدل تجميع التاريخ الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- خاصية `PivotFieldGroupOptions.interval` تؤثر فقط على تجميع الأرقام وعلى تجميع التاريخ بالأيام (على سبيل المثال، تجميع التواريخ إلى فترات 7 أيام)؛ يتم تجاهلها عندما يتم تجميع التواريخ بالأشهر أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصف والعمود في جدول محوري](/cells/ar/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [تصفية جداول محورية حسب التسمية أو القيمة](/cells/ar/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في جدول محوري](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [تطبيق التنسيق على جدول محوري](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تحديث جدول محوري](/cells/ar/javascript-cpp/refresh-pivot-table/)
- [التجميع المتقطع لعناصر حقول الجدول المحوري](/cells/ar/javascript-cpp/discrete-group-pivot-fields/)

{{< app/cells/assistant language="javascript-cpp" >}}