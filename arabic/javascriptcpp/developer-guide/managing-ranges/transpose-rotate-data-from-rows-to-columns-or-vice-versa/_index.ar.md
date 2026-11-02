---
title: عكس النطاق
linktitle: عكس النطاق
description: تشرح هذه المقالة كيفية عكس أو تدوير البيانات من الصفوف إلى الأعمدة أو العكس في ملفات Excel باستخدام Aspose.Cells for JavaScript via C++ بثلاث طرق مختلفة.
keywords: Aspose.Cells, JavaScript via C++, جدول بيانات, عكس النطاق, تدوير البيانات, دالة عكس, صيغة المصفوفة الديناميكية, صيغة المصفوفة, Excel TRANSPOSE, من الصفوف إلى الأعمدة
type: docs
weight: 80
url: /ar/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ يدعم عكس (تدوير) البيانات بحيث تصبح الصفوف أعمدة والأعمدة صفوف بثلاث طرق مختلفة. النهج الأول يستخدم طريقة `range.transpose()` داخلية ويعمل على كل إصدار من Excel، بينما يستخدم الثاني `cell.setDynamicArrayFormula()` لكتابة صيغة مصفوفة ديناميكية حديثة `=TRANSPOSE(...)` تتدفق تلقائيًا على Excel 365 أو Excel 2021. النهج الثالث يستخدم `cell.setArrayFormula()` لكتابة صيغة مصفوفة كلاسيكية Ctrl+Shift+Enter (CSE) متوافقة مع إصدارات Excel القديمة. تستعرض هذه المقالة كل نهج مع تعليمات خطوة بخطوة وأمثلة كاملة على الشيفرة.
{{% /alert %}}

## **المقدمة**
يعني عكس النطاق تدويره بحيث يصبح ما كان صفًا عمودًا وما كان عمودًا صفًا، مما يعكس البيانات عبر القطر الرئيسي لها. في Microsoft Excel، تقوم دالة ورقة العمل `TRANSPOSE` بأداء هذه العملية، ويمكن الاطلاع على المرجع المفهومي في [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function). يمكن تطبيق هذا المفهوم برمجيًا على نطاق من الخلايا، وهو مفيد في العديد من السيناريوهات التجارية وتقارير الأعمال.
- إعادة توجيه تقارير المبيعات الفصلية أو السنوية حيث تُعرض الفصول عبر الصفحة والأقاليم أسفل الصفحة، أو العكس.
- تبديل توجيه المحاور في لوحات المعلومات أو المخططات بحيث يصبح التسلسل الزمني أسفل الصفحة بدلاً من عبرها.
- تعديل شكل البيانات المستوردة من الأنظمة الخارجية لتطابق التخطيط المتوقع من قِبل قوالب التحليل أو التقارير اللاحقة.
لجعل باقي المقالة أكثر وضوحًا، يستخدم كل مثال الجدول الصغير للمبيعات حسب المنطقة والربع. في مصنف العينة يشغل هذا الجدول النطاق **A1:D5**، مع ترك **A1** فارغًا كزاوية علوية يسارًا، وتحتوي **B1:D1** على رؤوس المناطق، وتحتوي **A2:A5** على رؤوس الأرباع.
| المنطقة | أوروبا | آسيا | أمريكا الشمالية |
|---------|--------|------|-------------------|
| الربع 1 | 21704714 | 8774099 | 12094215 |
| الربع 2 | 17987034 | 12214447 | 10873099 |
| الربع 3 | 19485029 | 14356879 | 15689543 |
| الربع 4 | 22567894 | 15763492 | 17456723 |
ثم تُقدِّم المقالة ثلاثة طرق مختلفة لعكس هذه البيانات باستخدام Aspose.Cells for JavaScript via C++، كل طريقةٍ ملائمة لإصدار Excel مختلف وحالة استخدام معينة.

## **النهج 1 — عكس النطاق في الموقع (Range.transpose)**
استخدم هذا النهج كلما رغبت في عكس البيانات دون استدعاء دالة `TRANSPOSE` في ورقة العمل. يعمل على **جميع إصدارات Excel** ولا يعتمد على المصفوفات الديناميكية، مما يجعله أكثر الخيارات أمانًا عبر الإصدارات. وهو مثالي عندما تحتاج فقط إلى القيم المعكوسة النهائية ولا تحتاج إلى إبقاء صيغة `TRANSPOSE` الأصلية في المصنف.

### **API المستخدمة**
`Range.transpose()` هي طريقة من نوع instance على الفئة `Aspose.Cells.Range`. عند استدعائها تُقلب النطاق في مكانه عن طريق تبديل صفوفه وأعمدته، بحيث يصبح ما كان صفًا عمودًا والعكس. تقوم الطريقة بتعديل الخلايا الأساسية مباشرةً دون كتابة صيغة.

### **الخطوات**
1. افتح المصنف المصدر مع تعيين `LoadOptions` إلى صيغة `.xlsx` عبر استدعاء `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استخرج أول ورقة عمل من المصنف باستخدام `workbook.getWorksheets().get(0)`.
3. احصل على مجموعة الخلايا للورقة عبر `worksheet.getCells()`.
4. أنشئ النطاق المصدر الذي يغطي **A1:D5** باستدعاء `cells.createRange("A1:D5")`.
5. استدعِ `source.transpose()` لتدوير النطاق في مكانه، مع تبديل الصفوف والأعمدة.
6. احفظ المصنف باستخدام `workbook.save(outputFile)`.
بعد العكس، يحتفظ النطاق المرجعي بالبيانات المتدوّرة. الصف الأول يصبح (فارغ، **أوروبا**، **آسيا**، **أمريكا الشمالية**) والعمود الأول يصبح (فارغ، **الربع 1**، **الربع 2**، **الربع 3**، **الربع 4**). كل عمود مبيعات أصلي يتحول إلى صف في النطاق المعكوس.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **النهج 2 — عكس باستخدام صيغة مصفوفة ديناميكية (Excel 365 / 2021)**
استخدم هذا النهج عندما تريد حفظ صيغة `=TRANSPOSE(A1:D5)` كصيغة حية في المصنف الناتج بحيث يتم تحديث النتيجة تلقائيًا إذا تغيرت البيانات المصدر، ويُفتح ملف Excel المستهدف في **Excel 365 / Excel 2021 أو لاحقًا** حيث تُدعم المصفوفات الديناميكية ومعامل الانسكاب.

### **API المستخدمة**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` هي طريقة على الفئة `Aspose.Cells.Cell` تُعيّن صيغة الخلية كـ **صيغة مصفوفة ديناميكية**. يقوم Excel بتقييم الصيغة مرة واحدة ويُسقِط النتيجة تلقائيًا في الخلايا المحيطة. المعامل الثالث، عند ضبطه على `true`، يُوجه Aspose.Cells لحساب القيم الناتجة وقت الكتابة.

### **الخطوات**
1. حمّل المصنف المصدر باستخدام `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. استخرج أول ورقة عمل واحصل على مجموعة خلاياها.
3. ضع صيغة المصفوفة الديناميكية في الخلية **A6**، أسفل النطاق المصدر، عبر استدعاء `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. يُستخدم كائن `new FormulaParseOptions()` لإعدادات افتراضية، والمعامل الثالث `true` يُخبر Aspose.Cells بمعاملة الصيغة كمصفوفة ديناميكية وتقييمها بحيث تُكتب القيم المنسكبة إلى المصنف.
5. احفظ المصنف باستخدام `workbook.save(outputFile)`.
الخلية **A6** تحتفظ بالصّيغة `=TRANSPOSE(A1:D5)` ويُسقِط Excel النتيجة تلقائيًا إلى النطاق **A6:E9**، وهو عبارة عن كتلة 4 صفوف × 5 أعمدة مساوية للبيانات المعكوسة.

{{% alert color="primary" %}}
هذا النهج يعمل **فقط على Excel 365 / 2021 أو لاحقًا**. الإصدارات القديمة من Excel لن تُنَسِق صيغ المصفوفات الديناميكية بشكل صحيح.
{{% /alert %}}

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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **النهج 3 — عكس باستخدام صيغة مصفوفة كلاسيكية (CSE)**
استخدم هذا النهج عندما تريد حفظ صيغة `TRANSPOSE` في المصنف لكن ملف Excel المستهدف قد يُفتح في **إصدارات Excel القديمة (ما قبل 2021، بما فيها 2019، 2016، 2013، وهكذا)** حيث لا يُدعَم الانسكاب الديناميكي. صيغة المصفوفة الكلاسيكية Ctrl+Shift+Enter (CSE) هي البديل المتوافق مع الإصدارات القديمة التي يمكن لجميع إصدارات Excel تقييمها.

### **API المستخدمة**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` هي طريقة على الفئة `Aspose.Cells.Cell` تُعيّن **صيغة مصفوفة كلاسيكية (CSE)** إلى الخلية المرجعية وتحدّد أبعاد المصفوفة الناتجة. يكتب Aspose.Cells علامة مصفوفة متعددة الخلايا بحيث يَقيم Excel الصيغة كتعبير مصفوفة واحد يُملأ النطاق المُعلن.

### **الخطوات**
1. حمّل المصنف المصدر كما هو موضح في النهج السابق.
2. استخرج أول ورقة عمل واحصل على مجموعة خلاياها.
3. استدعِ `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)`. المعامل الثاني `4` هو عدد صفوف المصفوفة الهدفية والمعامل الثالث `5` هو عدد الأعمدة.
4. احفظ المصنف باستخدام `workbook.save(outputFile)`.
الخلية **A6** هي مرساة صيغة المصفوفة وتُمتد المصفوفة المُقَيمة عبر 4 صفوف × 5 أعمدة بدءًا من A6، مطابقةً لأبعاد النطاق المعكوس A1:D5. يكتب Excel علامة صيغة مصفوفة واحدة عبر النطاق الناتج بحيث تُقيمها الإصدارات القديمة بشكل صحيح.

{{% alert color="primary" %}}
صيغ المصفوفة CSE هي الطريقة الكلاسيكية في Excel لتقييم تعبير `TRANSPOSE` وهذا النهج متوافق عالميًا عبر إصدارات Excel.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // تحميل دفتر العمل المصدر باستخدام خيارات التحميل xlsx
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // الوصول إلى ورقة العمل الأولى ومجموعة الخلايا الخاصة بها
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // تعيين صيغة المصفوفة الكلاسيكية CSE في الخلية A6.
                // الصيغة =TRANSPOSE(A1:D5) تدور النطاق المصدر المكوّن من 5 صفوف × 4 أعمدة
                // إلى مصفوفة مكوّنة من 4 صفوف × 5 أعمدة. الوسيط الثاني (4) هو عدد الصفوف
                // والوسيط الثالث (5) هو عدد الأعمدة للمصفوفة الناتجة.
                // Aspose.Cells يكتب علامة صيغة المصفوفة CSE بحيث يقوم Excel بتقييمها كـ
                // صيغة مصفوفة متعددة الخلايا واحدة، متوافقة مع إصدارات Excel القديمة
                // (2019، 2016، 2013، وما إلى ذلك) التي لا تدعم تدفق المصفوفة الديناميكي.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // حفظ دفتر العمل بحيث يتم الاحتفاظ بعلامة صيغة المصفوفة
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **المقارنة — متى يُستَخدم كل نهج**
| النهج | API / طريقة | إصدار Excel | هل تم حفظ الصيغة الأصلية؟ | نطاق الإخراج |
|-------|-------------|-------------|---------------------------|--------------|
| النهج 1 — عكس في الموقع | `range.transpose()` | جميع إصدارات Excel | لا (القيم فقط) | نطاق الارتكاز الأولي، 5×4 |
| النهج 2 — صيغة المصفوفة الديناميكية | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | نعم (ينسكب تلقائيًا) | يُنسَكَب من المرجع |
| النهج 3 — صيغة المصفوفة الكلاسيكية (CSE) | `cell.setArrayFormula()` | جميع إصدارات Excel | نعم (صيغة مصفوفة متعددة الخلايا) | حجم محدد صريح، 4×5 |
استخدم **النهج 1** عندما تحتاج إلى تحويل سريع متوافق عبر الإصدارات ولا تحتاج إلى الصيغة المعكوسة في الملف. استخدم **النهج 2** عندما تكون متأكدًا من وجود Excel حديث وتريد الصيغة الحية لتتحدث تلقائيًا إذا تغير المصدر. استخدم **النهج 3** عندما تحتاج إلى أقصى قدر من التوافق مع صيغ محفوظة عبر جميع إصدارات Excel، بما فيها الإصدارات القديمة التي لا تدعم المصفوفات الديناميكية.

{{< app/cells/assistant language="javascript-cpp" >}}