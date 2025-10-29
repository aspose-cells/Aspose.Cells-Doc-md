---
title: حساب الصيغ باستخدام JavaScript عبر C++
linktitle: حساب الصيغ
description: تقدم هذه المقالة شرحًا لكيفية استخدام مكتبة Aspose.Cells لحساب الصيغ في Microsoft Excel باستخدام JavaScript عبر C++. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الطرق التي توفرها Aspose.Cells لحساب الصيغة والحصول على النتيجة. أخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، إكسل، الصيغ، الحسابات، الحساب المباشر للصيغة، حساب الصيغ بشكل متكرر، إضافة الصيغ باستخدام JavaScript عبر C++
type: docs
weight: 125
url: /ar/javascript-cpp/calculate-formulas/
---

## **إضافة صيغ وحساب النتائج**

تحتوي Aspose.Cells على محرك حساب الصيغ مدمج. فهي لا يمكنها فقط إعادة حساب الصيغ المستوردة من قوالب المصممين، بل تدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

 يدعم Aspose.Cells معظم الصيغ أو الوظائف التي تعتبر جزءًا من Microsoft Excel (اقرأ [قائمة الوظائف المدعومة من قبل محرك الحسابات](/cells/ar/javascript-cpp/supported-formula-functions/)). يمكن استخدام تلك الوظائف عبر واجهات برمجة التطبيقات أو جداول التصميم. يدعم Aspose.Cells مجموعة واسعة من الصيغ الرياضية، النصية، المنطقية، للتاريخ/الوقت، الإحصائية، قواعد البيانات، البحث، والمرجعية.

استخدم خاصية [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) أو أساليب [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) لإضافة صيغة إلى خليّة. عند تطبيق صيغة، ابدأ النص بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel، واستخدم فاصلة (,) لفصل معلمات الدالة.

لحساب نتائج الصيغ، يمكن للمستخدم استدعاء طريقة [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) التي تعالج جميع الصيغ المدمجة في ملف Excel. أو، يمكن للمستخدم استدعاء طريقة [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) التي تعالج جميع الصيغ المدمجة في ورقة. أو، يمكن للمستخدم أيضًا استدعاء طريقة [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) التي تعالج صيغة خلية واحدة:

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **مهم معرفته حول الصيغ**

{{% alert color="primary" %}}

وظيفة **Formula** وطرق **formula(...)** من فئة [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) تعمل بشكل مختلف عن طرق **calculate** من فئات [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)، و[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell). وظيفة **Formula** وطرق **formula(...)** تضيف ببساطة الصيغة إلى الخلية لكن لا تحسب النتيجة أثناء التشغيل. للحصول على نتيجة الصيغ، يرجى استدعاء طرق **calculate**.

{{% /alert %}}

## **حساب مباشر للصيغ**

Aspose.Cells لديه محرك حساب مضمن للصيغ. بالإضافة إلى حساب الصيغ المستوردة من ملف مصمم، يمكن لـ Aspose.Cells حساب نتائج الصيغ مباشرة.

أحيانًا، تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها إلى ورقة عمل. القيم المستخدمة في الصيغة موجودة بالفعل في ورقة عمل، وكل ما تحتاج إليه هو العثور على النتيجة لتلك القيم بناءً على صيغة Microsoft Excel دون إضافة الصيغة في ورقة عمل.

يمكنك استخدام واجهات برمجة تطبيقات محرك حساب الصيغ الخاص بـ Aspose.Cells لـ [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) إلى [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) لحساب نتائج مثل هذه الصيغ دون إضافتها إلى ورقة العمل:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

ينتج الكود أعلاه الناتج التالي:
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **كيفية حساب الصيغ بشكل متكرر**

عندما يكون هناك الكثير من الصيغ في دفتر العمل، ويحتاج المستخدم إلى حسابها بشكل متكرر أثناء تعديل جزء صغير منها، قد يكون من المفيد تمكين سلسلة حساب الصيغة: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **مهم معرفته**

{{% alert color="primary" %}}

افتراضيًا، يتم تعطيل سلسلة الحساب. لأن إنشاء السلسلة يتطلب أيضًا وقتًا إضافيًا، فإن المرة الأولى لحساب الصيغ ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) قد تستهلك مزيدًا من وقت معالجة CPU والذاكرة عند مقارنته بحساب الصيغ بدون سلسلة. إذا لم يكن المستخدم بحاجة إلى حساب الصيغ بشكل متكرر، فإن السلوك الافتراضي (حساب الصيغة مباشرة بدون إنشاء سلسلة حساب) هو الخيار الأفضل.

{{% /alert %}}

## **مواضيع متقدمة**
- [إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel](/cells/ar/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [حساب وظيفة IFNA باستخدام Aspose.Cells](/cells/ar/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [حساب الصيغة الصفية للجداول البيانات](/cells/ar/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [حساب وظائف MINIFS و MAXIFS في Excel 2016](/cells/ar/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [تقليل زمن حساب طريقة Cell.calculate](/cells/ar/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [اكتشاف المراجعة الدائرية](/cells/ar/javascript-cpp/detecting-circular-reference/)
- [الحساب المباشر للوظيفة المخصصة دون كتابتها في ورقة العمل](/cells/ar/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [تنفيذ محرك الحساب المخصص لتوسيع محرك الحساب الافتراضي لـ Aspose.Cells](/cells/ar/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [إيقاف أو إلغاء حساب الصيغ في سجل العمل](/cells/ar/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [ضبط وضع حساب الصيغة في سجل العمل](/cells/ar/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [استخدام وظيفة FormulaText في Aspose.Cells](/cells/ar/javascript-cpp/using-formulatext-function-in-aspose-cells/)
