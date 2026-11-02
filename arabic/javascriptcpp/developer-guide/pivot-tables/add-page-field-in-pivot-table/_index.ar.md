---
title: إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for JavaScript via C++
linktitle: إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for JavaScript via C++
description: تعلّم كيفية إضافة حقول التصفية وتهيئتها في الجداول المحورية باستخدام Aspose.Cells for JavaScript via C++، بما في ذلك إضافة حقول التصفية، وتطبيق التصفية ذات التحديد الفردي، والتصفية متعددة التحديد.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, جدول محوري, حقل تصفية, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, تصفية
type: docs
weight: 250
url: /ar/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells دعمًا كاملًا لدورة حياة حقول التصفية في الجداول المحورية. يمكنك إضافة حقل تصفية عبر واجهة API عالية المستوى أو عبر مجموعة `getPageFields()` ذات المستوى الأدنى، والتحكم في التصفية في وضع التحديد الفردي، أو مسحها لعرض جميع عناصر التصفية، أو تحويل الحقل إلى وضع متعدد التحديد ليتمكن المستخدمون من اختيار عدة عناصر تصفية مرة واحدة عبر واجهة المستخدم ذات مربعات الاختيار في Excel.
{{% /alert %}}

## **مقدمة**
حقل التصفية هو حقل محوري يتحكم في *المجموعة الفرعية* من بيانات المصدر التي يعرضها محتوى الجدول المحوري. يراه المستخدمون النهائيون على هيئة قائمة منسدلة أعلى الجدول المحوري عند عرضه في Excel، ويؤدي اختيار أحد عناصر التصفية المتاحة إلى إعادة بناء محتوى الجدول المحوري بحيث تلخّص السجلات التابعة لعنصر التصفية فقط. يتحول الحقل المحوري إلى حقل تصفية عند تسجيله بوصفه `PivotFieldType.Page` بدلاً من `PivotFieldType.Row` أو `PivotFieldType.Column` أو `PivotFieldType.Data`.

## **إضافة حقل تصفية**

### إضافة حقل تصفية باستخدام `addFieldToArea`
ينشئ المثال التالي مجموعة بيانات صغيرة تضم حقول الفاكهة والسنة والمبلغ، ويضع جدولًا محوريًا في الخلية E3، مع وضع `Fruit` في منطقة الصفوف و`Amount` في منطقة البيانات و`Year` في منطقة التصفية، ثم يحدّث الجدول المحوري ويحفظ المصنف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // إنشاء مصنف جديد
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // إعداد صف العناوين
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // ملء 9 صفوف ببيانات نموذجية: الفاكهة، السنة، المبلغ
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // إضافة جدول محوري مثبت عند الخلية E3
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // إضافة الحقول إلى مناطقها: الفاكهة كصف، والمبلغ كبيانات، والسنة كحقل صفحة
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // تحديث بيانات الجدول المحوري وحسابها
            pivotTable.calculateData();
            // حفظ المصنف
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### إضافة حقل تصفية باستخدام `getPageFields().add`
عند العمل بالفعل مع مثيل `PivotField`، يمكنك تمريره مباشرةً إلى `pivotTable.getPageFields().add(pivotField)`. يتم إنشاء الجدول المحوري وحقل التصفية تمامًا كما في السيناريو السابق؛ والفرق الوحيد هو أن تسجيل الحقل في منطقة التصفية يتم عبر استدعاء API ذي المستوى الأدنى.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // — The pivot table and page field are constructed exactly as in
            //   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
            //   Amount→Data). Below we obtain the Year PivotField from the
            //   BaseFields collection and pass it to PageFields.Add — the
            //   low-level alternative to AddFieldToArea. The result is
            //   functionally identical to Scenario 1a.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Headers
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Sample data (9 rows)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // Add pivot table at E3 covering A1:C10
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit -> Row, Amount -> Data (Year will go to Page below)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Low-level approach: grab the existing Year PivotField from BaseFields
            // and register it in the Page area via PageFields.Add(PivotField).
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Refresh so the new page field is reflected in the saved workbook
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **التصفية ذات التحديد الفردي (عرض عنصر تصفية واحد)**
في وضع التحديد الفردي الافتراضي، يُعرض حقل التصفية على هيئة قائمة منسدلة واحدة، ويحدد العدد الصحيح `pivotField.currentPageItem` عنصر التصفية الذي يتحكم في محتوى الجدول المحوري. يؤدي تعيين فهرس محدد إلى اختيار عنصر واحد بعينه، بينما يؤدي تعيين القيمة الخاصة `0x7FFD` (32765 عشريًا) إلى مسح التصفية بحيث تلخّص جميع عناصر التصفية في الوقت نفسه. التحديد الفردي هو الوضع الافتراضي، ولا تحتاج إلى تمكينه صراحةً.

### عرض جميع العناصر
تعيين `currentPageItem` إلى القيمة السحرية `0x7FFD` يعادل مسح التصفية: يلخّص محتوى الجدول المحوري جميع عناصر التصفية كما لو لم تُطبَّق أي تصفية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // إنشاء مصنف جديد
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // تعبئة بيانات الفاكهة/السنة/المبلغ
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // إنشاء جدول محوري عند E3
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // إعداد حقول الجدول المحوري: Fruit→Row، Amount→Data، Year→Page
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // امسح مرشح الصفحة بحيث يظهر كل عنصر في حقل الصفحة.
            // 0x7FFD (العشري 32765) هو قيمة خاصة تعني "جميع العناصر" —
            // أي ما يعادل تحديد "(الكل)" في قائمة حقول صفحة Excel.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

### عرض عنصر محدد
تعيين `currentPageItem` إلى فهرس صالح يختار عنصر تصفية واحدًا فقط. يمثل الفهرس موضع العنصر في قائمة عناصر حقل التصفية المرتبة، لذا يختار `1`، على سبيل المثال، العنصر الثاني بعد الفرز.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById("runExample").addEventListener("click", async () => {
                // إنشاء مصنف العمل
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // إضافة بيانات نموذجية (الفاكهة/السنة/المبلغ)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // إضافة جدول محوري عند E3
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // إضافة الحقول: Fruit→Row، Amount→Data، Year→Page
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // عمليات خاصة بحقل الصفحة
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = العنصر الثاني في الترتيب (مثل "2021")
                // تحديث الجدول المحوري وحساب بياناته
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **التصفية متعددة التحديد**
تحوّل التصفية متعددة التحديد قائمة التصفية المنسدلة إلى قائمة مربعات اختيار، وتتيح للمستخدم النهائي اختيار عدة عناصر تصفية في الوقت نفسه. تتيح Aspose.Cells خاصيتين تعملان معًا. يجب تعيين `pivotField.isMultipleItemSelectionAllowed` إلى `true` قبل أن تصبح واجهة المستخدم متعددة التحديد فعالة. وبعد تمكينها، تتحكم `pivotItem.isHidden` في العناصر التي تظهر في قائمة مربعات الاختيار، بحيث يمكنك إظهار جميع العناصر أو قصر قائمة السماح على عناصر محددة فقط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — يُنشأ الجدول المحوري وحقل الصفحة تمامًا كما في
                //   السيناريو 1a (بيانات Fruit/Year/Amount، الجدول المحوري عند E3، Fruit→Row،
                //   Amount→Data، Year→Page عبر AddFieldToArea).
                //   أدناه نطبّق التصفية متعددة التحديد على حقل الصفحة.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // بيانات العينة: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — تفعيل التحديد المتعدد على حقل الصفحة
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // الجزء أ — تحديد جميع العناصر (جعل كل عنصر ظاهرًا)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // الجزء ب — تحديد عناصر محددة فقط حسب القيمة المصدرية
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **ملاحظة:** عند استخدام التصفية متعددة التحديد عبر `pivotItem.isHidden`، **يجب أن يظل عنصر `PivotItem` واحدًا على الأقل ظاهرًا** (`isHidden === false`). إذا أخفيت جميع العناصر، فإن Excel إما ينهار عند فتح الملف أو يعرض جدولًا محوريًا فارغًا. تحقق دائمًا من أن قائمة السماح المستخدمة في التصفية متعددة التحديد تتضمن عنصرًا واحدًا على الأقل من بيانات المصدر.

## **اختيار واجهة API والوضع المناسبين**
يلخص الجدول التالي متى تُستخدم كل واجهة API والوضع المقابل لها، لتتمكن من اختيار التركيبة المناسبة دون قراءة جميع السيناريوهات بالتفصيل.
| السيناريو / حالة الاستخدام | واجهة API الموصى بها | الخاصية المستخدمة | ملاحظات |
|---|---|---|---|
| إضافة حقل تصفية باستخدام اسم عمود المصدر (الحالة الأكثر شيوعًا) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | غير منطبق | واجهة API عالية المستوى، في سطر واحد. استخدمها ما لم تكن بحاجة إلى مرجع إلى `PivotField`. |
| إضافة حقل تصفية عندما يكون لديك بالفعل كائن `PivotField` | `pivotTable.getPageFields().add(pivotField)` | غير منطبق | استخدمها عندما يكون كائن الحقل قد تم إنشاؤه في مكان آخر أو يلزم إعادة استخدامه. |
| التصفية حسب عنصر تصفية واحد (الوضع الافتراضي) | `pivotField.currentPageItem` | ضبطه على فهرس محدد | على سبيل المثال، يعرض `1` العنصر الثاني في القائمة المرتبة. |
| عرض جميع العناصر / مسح التصفية | `pivotField.currentPageItem` | ضبطه على `0x7FFD` | القيمة السحرية `0x7FFD` (32765 عشريًا) هي القيمة الخاصة التي تعني «جميع العناصر». |
| تمكين واجهة المستخدم متعددة التحديد في Excel | `pivotField.isMultipleItemSelectionAllowed` | ضبطه على `true` | مطلوب قبل أن تسري أي تعيينات لـ `isHidden`. |
| إخفاء / إظهار عناصر فردية في قائمة متعددة التحديد | `pivotItem.isHidden` | ضبطه لكل عنصر | يجب أن يظل عنصر واحد على الأقل ظاهرًا (`isHidden === false`). |

{{% alert color="primary" %}}
تذكّر دائمًا بقيد إبقاء عنصر واحد على الأقل ظاهرًا عند إعداد التصفية متعددة التحديد. إذا كانت جميع عناصر `PivotItem` في حقل تصفية متعدد التحديد مخفية، فإن Excel ينهار عند الفتح أو يعرض جدولًا محوريًا فارغًا. أنشئ قائمة السماح استنادًا إلى بيانات المصدر بحيث يظل عنصر واحد على الأقل ظاهرًا، وستفتح مصنفاتك المحفوظة بشكل موثوق على كل جهاز.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}