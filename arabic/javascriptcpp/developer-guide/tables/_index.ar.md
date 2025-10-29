---
title: إنشاء وإدارة جداول ملفات Microsoft Excel باستخدام جافا سكريبت عبر C++
linktitle: الجداول
type: docs
weight: 150
url: /ar/javascript-cpp/create-and-format-table/
description: إدراج، تغيير الحجم، تحرير، حذف، وتنسيق جداول ملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **إنشاء جدول**

أحد ميزات الجداول الإلكترونية هو أنها تتيح لك إنشاء أنواع مختلفة من القوائم، على سبيل المثال: قوائم الهواتف، قوائم المهام، قوائم المعاملات، الأصول أو المطلوبات. يمكن لعدة مستخدمين العمل معًا لاستخدام وإنشاء وصيانة قوائم مختلفة.

يدعم Aspose.Cells إنشاء وإدارة القوائم.

### **مزايا كائن القائمة**

هناك العديد من المزايا عند تحويل قائمة البيانات إلى كائن قائمة فعلي

- يتم تضمين صفوف وأعمدة جديدة تلقائيًا.
- يمكن بسهولة إضافة صف إجمالي في أسفل القائمة لعرض الجمع والمتوسط والعد، إلخ.
- يتم دمج الأعمدة المضافة إلى اليمين تلقائيًا في كائن القائمة.
- ستتم توسيع الرسوم البيانية استنادًا إلى الصفوف والأعمدة تلقائيًا.
- ستتم توسيع النطاقات المسماة المخصصة للصفوف والأعمدة تلقائيًا.
- تكون القائمة محمية من حذف الصف والعمود بطريق الخطأ.

### **إنشاء كائن قائمة باستخدام Microsoft Excel**

- اختيار نطاق البيانات لإنشاء كائن القائمة
- يعرض ذلك حوار إنشاء القائمة.
- تنفيذ كائن القائمة للبيانات وتحديد الصف الإجمالي (اختر **البيانات**، ثم **قائمة**، تليها **الصف الإجمالي**).

### **استخدام واجهة برمجة تطبيقات Aspose.Cells**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف Excel لشركة Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

الورقة تمثلها فئة {0}. فئة {1} توفر مجموعة واسعة من الخصائص والطرق لإدارة ورقة العمل. لإنشاء {2} في ورقة العمل، استخدم الخاصية {3} من مجموعة {4} من فئة {5}. كل {6} هو، في الواقع، كائن من فئة {7}، والتي توفر أيضًا طريقة {8} لإضافة كائن قائمة وتحديد نطاق الخلايا الخاص به.

وفقًا لنطاق الخلايا المحدد، يتم إنشاء كائن القائمة بواسطة Aspose.Cells. استخدم سمات (على سبيل المثال، [**showTotals**](https://reference.aspose.com/cells/javascript-cpp/listobject/#showTotals--)، [**listColumns**](https://reference.aspose.com/cells/javascript-cpp/listobject/#listColumns--)، إلخ) من فئة [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) للتحكم في القائمة.

في المثال التالي، قمنا بإنشاء نفس [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) باستخدام API الخاص بـ Aspose.Cells كما أنشأنا باستخدام Microsoft Excel في القسم أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells ListObjects Example</title>
    </head>
    <body>
        <h1>ListObjects Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TotalsCalculation } = AsposeCells;

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

            const listObjects = workbook.worksheets.get(0).listObjects;

            listObjects.add(1, 1, 7, 5, true);

            const firstList = listObjects.get(0);
            firstList.showTotals = true;

            firstList.listColumns.get(4).totalsCalculation = TotalsCalculation.Sum;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">List created and totals calculated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تنسيق الجدول**

لإدارة وتحليل مجموعة من البيانات ذات الصلة، يمكن تحويل نطاق الخلايا إلى كائن قائمة (المعروف أيضًا باسم جدول Excel). الجدول هو سلسلة من الصفوف والأعمدة التي تحتوي على بيانات ذات صلة تدير بشكل مستقل عن البيانات في الصفوف والأعمدة الأخرى. بشكل افتراضي، كل عمود في الجدول له تمكين التصفية في الصف العلوي بحيث يمكنك تصفية أو فرز بيانات كائن القائمة بسرعة. يمكنك إضافة صف إجمالي (صف خاص في القائمة يوفر تشكيلة من الوظائف الإجمالية المفيدة للعمل مع البيانات العددية) إلى كائن القائمة الذي يوفر قائمة منسدلة من الوظائف الإجمالية لكل خلية في صف الإجمالي. توفر Aspose.Cells خيارات لإنشاء وإدارة القوائم (أو الجداول).

### **تنسيق كائن قائمة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف Excel لشركة Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثلها فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) توفر مجموعة واسعة من الخصائص والطرق لإدارة الأوراق. لإنشاء [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) في ورقة العمل، استخدم خاصية [**listObjects**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#listObjects--) من class [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). كل [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) هو، في الواقع، كائن من فئة [**ListObjectCollection**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/)، والتي توفر أيضًا طريقة [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/listobjectcollection/#add-number-number-number-number-boolean-) لإضافة كائن قائمة وتحديد نطاق الخلايا الذي ستتضمنه. وفقًا لنطاق الخلايا المحدد، يتم إنشاء [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) في ورقة العمل بواسطة Aspose.Cells. استخدم السمات (مثال، [**TableStyleType**](https://reference.aspose.com/cells/javascript-cpp/tablestyletype/)) من [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) لتنسيق الجدول بحسب متطلباتك.

المثال أدناه يضيف بيانات عينة إلى ورقة العمل، يضيف [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) ويطبق أنماطًا افتراضية عليه. دعم أنماط [**ListObject**](https://reference.aspose.com/cells/javascript-cpp/listobject/) بواسطة Microsoft Excel 2007/2010.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // This example does not require an input file; it creates a new workbook
            const workbook = new Workbook();

            // Obtaining the reference of the default(first) worksheet
            const sheet = workbook.worksheets.get(0);

            // Obtaining Worksheet's cells collection
            const cells = sheet.cells;

            // Setting the value to the cells (converted putValue -> value)
            cells.get(1, 1).value = "Employee";
            cells.get(1, 2).value = "Quarter";
            cells.get(1, 3).value = "Product";
            cells.get(1, 4).value = "Continent";
            cells.get(1, 5).value = "Country";
            cells.get(1, 6).value = "Sale";

            cells.get(2, 1).value = "David";
            cells.get(3, 1).value = "David";
            cells.get(4, 1).value = "David";
            cells.get(5, 1).value = "David";
            cells.get(6, 1).value = "James";
            cells.get(7, 1).value = "James";
            cells.get(8, 1).value = "James";
            cells.get(9, 1).value = "James";
            cells.get(10, 1).value = "James";
            cells.get(11, 1).value = "Miya";
            cells.get(12, 1).value = "Miya";
            cells.get(13, 1).value = "Miya";
            cells.get(14, 1).value = "Miya";
            cells.get(15, 1).value = "Miya";
            cells.get(2, 2).value = 1;
            cells.get(3, 2).value = 2;
            cells.get(4, 2).value = 3;
            cells.get(5, 2).value = 4;
            cells.get(6, 2).value = 1;
            cells.get(7, 2).value = 2;
            cells.get(8, 2).value = 3;
            cells.get(9, 2).value = 4;
            cells.get(10, 2).value = 4;
            cells.get(11, 2).value = 1;
            cells.get(12, 2).value = 1;
            cells.get(13, 2).value = 2;
            cells.get(14, 2).value = 2;
            cells.get(15, 2).value = 2;

            cells.get(2, 3).value = "Maxilaku";
            cells.get(3, 3).value = "Maxilaku";
            cells.get(4, 3).value = "Chai";
            cells.get(5, 3).value = "Maxilaku";
            cells.get(6, 3).value = "Chang";
            cells.get(7, 3).value = "Chang";
            cells.get(8, 3).value = "Chang";
            cells.get(9, 3).value = "Chang";
            cells.get(10, 3).value = "Chang";
            cells.get(11, 3).value = "Geitost";
            cells.get(12, 3).value = "Chai";
            cells.get(13, 3).value = "Geitost";
            cells.get(14, 3).value = "Geitost";
            cells.get(15, 3).value = "Geitost";

            cells.get(2, 4).value = "Asia";
            cells.get(3, 4).value = "Asia";
            cells.get(4, 4).value = "Asia";
            cells.get(5, 4).value = "Asia";
            cells.get(6, 4).value = "Europe";
            cells.get(7, 4).value = "Europe";
            cells.get(8, 4).value = "Europe";
            cells.get(9, 4).value = "Europe";
            cells.get(10, 4).value = "Europe";
            cells.get(11, 4).value = "America";
            cells.get(12, 4).value = "America";
            cells.get(13, 4).value = "America";
            cells.get(14, 4).value = "America";
            cells.get(15, 4).value = "America";

            cells.get(2, 5).value = "China";
            cells.get(3, 5).value = "India";
            cells.get(4, 5).value = "Korea";
            cells.get(5, 5).value = "India";
            cells.get(6, 5).value = "France";
            cells.get(7, 5).value = "France";
            cells.get(8, 5).value = "Germany";
            cells.get(9, 5).value = "Italy";
            cells.get(10, 5).value = "France";
            cells.get(11, 5).value = "U.S.";
            cells.get(12, 5).value = "U.S.";
            cells.get(13, 5).value = "Brazil";
            cells.get(14, 5).value = "U.S.";
            cells.get(15, 5).value = "U.S.";

            cells.get(2, 6).value = 2000;
            cells.get(3, 6).value = 500;
            cells.get(4, 6).value = 1200;
            cells.get(5, 6).value = 1500;
            cells.get(6, 6).value = 500;
            cells.get(7, 6).value = 1500;
            cells.get(8, 6).value = 800;
            cells.get(9, 6).value = 900;
            cells.get(10, 6).value = 500;
            cells.get(11, 6).value = 1600;
            cells.get(12, 6).value = 600;
            cells.get(13, 6).value = 2000;
            cells.get(14, 6).value = 500;
            cells.get(15, 6).value = 900;

            // Adding a new List Object to the worksheet
            const index = sheet.listObjects.add("A1", "F15", true);

            const listObject = sheet.listObjects.get(index);

            // Adding Default Style to the table (converted setter -> property)
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium10;

            // Show Total
            listObject.showTotals = true;

            // Set the Quarter field's calculation type (converted getter/setter -> property)
            listObject.listColumns.get(1).totalsCalculation = AsposeCells.TotalsCalculation.Count;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and table added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تحويل الجدول إلى ODS](/cells/ar/javascript-cpp/convert-table-to-ods/)
- [العثور على جداول الاستعلام وكائنات القائمة المتعلقة باتصالات البيانات الخارجية](/cells/ar/javascript-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [قراءة وكتابة الجدول مع مصدر بيانات جدول الاستعلام](/cells/ar/javascript-cpp/read-and-write-table-with-query-table-data-source/)
- [ضبط التعليق للجدول أو كائن القائمة داخل ورقة العمل](/cells/ar/javascript-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [الجداول والمدى](/cells/ar/javascript-cpp/tables-and-ranges/)
