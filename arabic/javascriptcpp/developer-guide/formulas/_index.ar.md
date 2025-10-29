---
title: إدارة صيغ ملفات إكسل مع جافا سكريبت عبر C++
linktitle: الصيغ
type: docs
weight: 122
url: /ar/javascript-cpp/using-formulas-or-functions-to-process-data/
description: تعلم كيفية إدارة صيغ ملفات إكسل من خلال Script عبر C++. يمكن لـ Aspose.Cells ببساطة الحصول على وتعيين وحساب صيغ ملفات Excel.
keywords: كيفية حساب الصيغ في جافا سكريبت عبر C++، الصيغ والدوال باستخدام جافا سكريبت عبر C++، إدارة الدوال المدمجة في جافا سكريبت عبر C++، كيفية استخدام وظائف الإضافة مع جافا سكريبت عبر C++، كيفية استخدام صيغة المصفوفة via JavaScript عبر C++، كيفية استخدام صيغة R1C1 في جافا سكريبت عبر C++.
---

## **مقدمة**

واحدة من الميزات المثيرة في Microsoft Excel هي قدرته على معالجة البيانات باستخدام الصيغ والدوال. يوفر Microsoft Excel مجموعة من الدوال والصيغ المدمجة التي تساعد المستخدمين على إجراء حسابات معقدة بسرعة. كما توفر Aspose.Cells مجموعة كبيرة من الدوال والصيغ المدمجة التي تساعد المطورين على حساب القيم بسهولة. كما تدعم Aspose.Cells وظائف الإضافة. بالإضافة إلى ذلك، تدعم Aspose.Cells الصيغ المُصفوفة وصيغ R1C1.

## **كيفية استخدام الصيغ والوظائف**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--). يمثل كل عنصر في مجموعة Cells كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell).

من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي يقدمها الفئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell)، كما هو موضح بالتفصيل أدناه.

- باستخدام الوظائف الداخلية.
- باستخدام وظائف الإضافة.
- العمل مع صيغ الصيغة السابقة.
- إنشاء صيغة R1C1.

## **كيفية استخدام الوظائف المضمنة**

الدوال المدمجة أو الصيغ توفر كوظائف جاهزة لتقليل جهود ووقت المطورين. راجع [قائمة الدوال المدمجة](/cells/ar/javascript-cpp/supported-formula-functions/) التي يدعمها Aspose.Cells. يتم سرد الدوال بالترتيب الأبجدي. ستدعم المستقبل المزيد من الدوال.

يدعم Aspose.Cells معظم الصيغ أو الدوال التي تقدمها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال API أو [مُصمم جدول البيانات](/cells/ar/javascript-cpp/what-is-a-designer-spreadsheet/). يدعم Aspose.Cells مجموعة واسعة من الصيغ الرياضية، النصوص، Boolean، التاريخ/الوقت، الإحصائية، قواعد البيانات، البحث، المراجع.

استخدم خاصية [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) للصف ال [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) لإضافة صيغة إلى خلية. **الصيغ المعقدة**, مثل

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, مدعومة أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية، يجب دائمًا بدء السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدام فاصلة (,) لفصل معلمات الوظيفة.

في المثال أدناه، يتم تطبيق صيغة معقدة على خلية الصفراء من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). تستخدم الصيغة الوظيفة المضمنة **IF** المقدمة بواسطة Aspose.Cells.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            worksheet.cells.get("A1").putValue(1);

            // Adding a value to "A2" cell
            worksheet.cells.get("A2").putValue(2);

            // Adding a value to "A3" cell
            worksheet.cells.get("A3").putValue(3);

            // Adding a SUM formula to "A4" cell
            worksheet.cells.get("A4").formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated A4 value: ${value}. Click the download link to get the generated file.</p>`;
        });
    </script>
</html>
```

## **كيفية استخدام الوظائف المضافة**

يمكننا أن نضع بعض الصيغ التي يحددها المستخدم والتي نريد تضمينها كملحق إكسل. عند تعيين وظيفة cell.formula تعمل الدوال المدمجة بشكل جيد، ومع ذلك هناك حاجة لتعيين الدوال أو الصيغ المخصصة باستخدام وظائف الإضافة.

يوفر Aspose.Cells ميزات لتسجيل وظائف الإضافة باستخدام [**Worksheets.registerAddInFunction(string, string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#registerAddInFunction-string-string-boolean-). بعد ذلك، عند تعيين cell.formula = أي دالة من الإضافة، يحتوي ملف إكسل الناتج على القيمة المحسوبة من وظيفة الإضافة.

يجب تنزيل ملف XLAM التالي لتسجيل وظيفة الإضافة في عينة الكود أدناه. بالمثل، يمكن تنزيل الملف الناتج "test_udf.xlsx" لفحص الناتج.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Register Add-In Function Example</title>
    </head>
    <body>
        <h1>Register Add-In Function Example</h1>
        <p>Select the add-in file (.xlam/.xla) that contains the UDFs to register:</p>
        <input type="file" id="addInInput" accept=".xlam,.xla" />
        <button id="runExample">Register Add-In & Create Workbook</button>
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
            const fileInput = document.getElementById('addInInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an add-in file (.xlam/.xla).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const addinData = new Uint8Array(arrayBuffer);

            // Create empty workbook
            const workbook = new Workbook();

            // Register macro enabled add-in along with the function name
            const id = workbook.worksheets.registerAddInFunction(addinData, "TEST_UDF", false);

            // Register more functions in the file (if any)
            workbook.worksheets.registerAddInFunction(id, "TEST_UDF1");

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first cell
            const cell = worksheet.cells.get("A1");

            // Set formula name present in the add-in
            cell.formula = "=TEST_UDF()";

            // Save workbook to output XLSX format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'test_udf.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Add-in registered and formula set successfully! Click the download link to get the workbook.</p>';
        });
    </script>
</html>
```

## **كيفية استخدام صيغة مصفوفة**

صيغ المصفوفة هي صيغ تأخذ مصفوفات، بدلاً من الأرقام الفردية، كتغيرات لوظائف تكون الصيغة. عند عرض صيغة المصفوفة، يكون محاطًا بالأقواس الإعتيادية ({}).

تعيد بعض وظائف Microsoft Excel مصفوفات القيم. لحساب نتائج متعددة باستخدام صيغة مصفوفة، أدخل المصفوفة في نطاق الخلايا بعدد الصفوف والأعمدة نفس معدلات الوسائط المصفوفات.

من الممكن تطبيق صيغة مصفوفة على خلية عن طريق استدعاء الوظيفة [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) الخاصة بفئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). تأخذ الوظيفة [**arrayFormula(string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#arrayFormula-string-number-number-) معلمات التالية:

- **صيغة مصفوفة**, صيغة المصفوفة.
- **عدد الصفوف**, عدد الصفوف لملء نتيجة صيغة المصفوفة.
عدد الأعمدة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LINEST Example</h1>
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

            // Adding a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding values to cells
            worksheet.cells.get("A1").value = 1;
            worksheet.cells.get("A2").value = 2;
            worksheet.cells.get("A3").value = 3;

            worksheet.cells.get("B1").value = 4;
            worksheet.cells.get("B2").value = 5;
            worksheet.cells.get("B3").value = 6;

            worksheet.cells.get("C1").value = 7;
            worksheet.cells.get("C2").value = 8;
            worksheet.cells.get("C3").value = 9;

            // Adding a SUM/LINEST array formula to "A6" cell
            worksheet.cells.get("A6").arrayFormula = { formula: "=LINEST(A1:A3,B1:C3,TRUE,TRUE)", rows: 5, cols: 3 };

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A6").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value: ${value}</p>`;
        });
    </script>
</html>
```

## **كيفية استخدام الصيغة R1C1**

أضف صيغة مرجعية R1C1 إلى خلية مع خاصية فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) وخاصية [**r1C1Formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#r1C1Formula--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set R1C1 Formula Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Setting an R1C1 formula on the "A11" cell,
            // Row and Column indices are relative to destination index
            const cell = worksheet.cells.get("A11");
            cell.r1C1Formula = "=SUM(R[-10]C[0]:R[-7]C[0])";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">R1C1 formula set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [السابقون والموكّلون](/cells/ar/javascript-cpp/precedents-and-dependents/)
- [تعيين الروابط الخارجية في الصيغ](/cells/ar/javascript-cpp/set-external-links-in-formulas/)
- [نشر الصيغة في الجدول أو كائن القائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة](/cells/ar/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [وضع صيغة لنطاق مسمى](/cells/ar/javascript-cpp/setting-formula-for-named-range/)
- [تعيين الصيغ - إشعار للمستخدمين غير الناطقين بالإنكليزية](/cells/ar/javascript-cpp/setting-formulas-notice-for-non-english-users/)
- [تعيين الصيغ المشتركة](/cells/ar/javascript-cpp/setting-shared-formula/)
- [تحديد الصفوف القصوى للصيغة المشتركة](/cells/ar/javascript-cpp/specify-maximum-rows-of-shared-formula/)
- [الدوال المدعومة في إكسل](/cells/ar/javascript-cpp/supported-formula-functions/)
