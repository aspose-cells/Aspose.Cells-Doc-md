---
title: عرض أو تصفية أفضل 10 عناصر في الجدول المحوري
linktitle: عرض أو تصفية أفضل 10 عناصر في الجدول المحوري
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى تصنيفًا فقط في حقل من الجدول المحوري باستخدام Aspose.Cells for JavaScript via C++. تتناول هذه المقالة طريقة top10AutoShow في Excel 97-2003، وقراءة الخيارات الحالية باستخدام top10AutoShowSettings، وتصفية أفضل 10 في Excel 2007-365 عبر filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, جدول محوري, أفضل 10, عرض تلقائي, top10AutoShow, top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ar/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
قد يصعب قراءة الجدول المحوري الذي يسرد كل عنصر من حقل صف عندما يحتوي الحقل على عشرات العناصر. لا يعرض تقرير أفضل 10 سوى العناصر الأعلى أو الأدنى ترتيبًا، وهو ما تحتاج إليه تقارير الترتيب تحديدًا، مثل «أفضل 5 منتجات حسب الإيرادات» أو «أدنى 3 مناطق حسب عدد المبيعات». تدعم Aspose.Cells آليتين لذلك، تمثّلان جيلين من إصدارات Microsoft Excel.
- **العرض التلقائي في Excel 97-2003** — الطريقة `PivotField.top10AutoShow()`. يمثل هذا الإعداد الكلاسيكي «عرض أفضل N عناصر أو أسوأها» المخزن مباشرةً في الحقل المحوري. يعمل مع جميع إصدارات Excel، القديمة والحديثة، لأنه جزء من تنسيق الجدول المحوري الأصلي.
- **تصفية أفضل 10 في Excel 2007-365** — الطريقة `PivotField.filterTop10()`. يمثل هذا مرشح القيم الحديث الموجود في «مرشحات القيم» ضمن قائمة الحقل. يُخزَّن ككائن `PivotFilter` مرتبط بالحقل، كما يتيح الترتيب استنادًا إلى عدد العناصر أو النسبة المئوية.

## **عرض أفضل 10 في Excel 97-2003 (top10AutoShow)**
يُهيَّأ العرض التلقائي الكلاسيكي باستدعاء واحد للطريقة `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, number count, number rankBy)`:
- `isAutoShow` — يتيح إعداد العرض التلقائي في الحقل أو يعطله.
- `isTop` — القيمة `true` تُبقي العناصر الأعلى ترتيبًا (الأعلى)، والقيمة `false` تُبقي العناصر الأدنى (الأدنى).
- `count` — عدد العناصر التي يجب إبقاؤها، مثل 10 لتقرير كلاسيكي لأفضل 10.
- `rankBy` — الفهرس بدءًا من الصفر لحقل **البيانات** الذي تُستخدم قيمه لترتيب العناصر. مرّر -1 لترتيب العناصر وفق الحقل نفسه.

يمكن أن يستند الترتيب إلى حقل قيم أو إلى الحقل نفسه. وفيما يلي خياران شائعان.

### **الترتيب حسب حقل قيم**
رتّب عناصر حقل الصف وفق حقل قيم عادي مثل `Sum of Sales`. ينشئ المثال التالي جدولًا محوريًا يحتوي على حقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أفضل رياضتين حسب المبيعات. قيمة `rankBy` هي 0 لأن `Sum of Sales` هو حقل البيانات الموجود في الفهرس 0.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Show the top 2 items ranked by "Sum of Sales" (data field index 0)
            sportField.top10AutoShow(true, true, 2, 0);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **الترتيب حسب الحقل نفسه**
يمكن استخدام الحقل نفسه لترتيب عناصره أيضًا؛ في هذه الحالة، مرّر -1 إلى `rankBy`. لا يلزم وجود حقل بيانات إضافي لهذا الخيار؛ يكفي أن يكون الحقل مدرجًا في منطقة الصفوف (أو الأعمدة). يعرض المثال التالي أدنى ثلاث رياضات مرتبة وفق الحقل نفسه. عند حفظ هذا الإعداد، لا يتضمن XML للجدول المحوري السمة `rankBy`، لأن -1 هي القيمة الافتراضية للتنسيق، وتُقرأ قيمة `rankBy` على أنها -1.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Show the bottom 3 items ranked by the field itself (rankBy = -1)
            sportField.top10AutoShow(true, false, 3, -1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **قراءة خيارات العرض التلقائي الحالية**
تعيد الخاصية `PivotField.top10AutoShowSettings` كائنًا من النوع `PivotFieldTop10AutoShowSettings` يتيح الوصول إلى خيارات العرض التلقائي المحفوظة حاليًا في الحقل. استخدمه لفحص كيفية عرض العناصر في مصنف موجود أو جدول محوري أعدت تهيئته للتو، بما في ذلك المصنفات المحمّلة من ملف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const settings = sportField.top10AutoShowSettings;
                const autoShowEnabled = settings.isAutoShow;
                const direction = settings.isTop ? "Top" : "Bottom";
                const itemCount = settings.autoShowCount;
                const rankingDataFieldIndex = settings.rankBy;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

تتوافق هذه الإعدادات مع سمات العرض التلقائي الكلاسيكية المكتوبة في XML للجدول المحوري (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`)، لذا فإن القيم المقروءة هي القيم التي تعتمدها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- بعد استدعاء `top10AutoShow()`، استدعِ `pivotTable.calculateData()` مرة أخرى؛ لا تظهر الإعدادات في التخطيط المعروض إلا عند إعادة الحساب التالية.
- تنطبق إعدادات العرض التلقائي على حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يقع فقط في منطقة الصفحة (التصفية) بهذه الطريقة، لأن عناصره لا تظهر في جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أفضل 10 (filterTop10)**
تتيح إصدارات Excel الحديثة ميزة أفضل 10 كمرشح قيم في قائمة الحقل (مرشحات القيم، أفضل 10...). يوفر Aspose.Cells هذه الميزة عبر الطريقة `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`، التي تنشئ كائن `PivotFilter` وتعيده:
- `valueFieldIndex` — الفهرس بدءًا من الصفر لحقل البيانات الذي تُستخدم قيمه المجمّعة لترتيب العناصر.
- `type` — يحدد ما يعنيه `itemCount`. يُبقي `PivotFilterType.Count` عددًا ثابتًا من العناصر (خيار «العناصر» في مربع الحوار). يُبقي `PivotFilterType.Percent` نسبة مئوية من العناصر، لذا تكون `itemCount` هي النسبة المئوية نفسها؛ أي أن 30 يُبقي أفضل 30 في المئة. ويرتب `PivotFilterType.Sum` العناصر بناءً على مجموع قيمها التراكمي.
- `isTop` — القيمة `true` للأعلى، والقيمة `false` للأدنى.
- `itemCount` — N في عبارة «أفضل N»، وتعتمد وحدته على `type`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
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
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            });
            const pivotTable = worksheet.pivotTables.add("=A1:C16", 2, 5);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Keep the top 3 items ranked by "Sum of Sales" (data field index 0)
            sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 3);
            pivotTable.pivotCache.refresh();
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-filter.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
إعداد العرض التلقائي والطريقة `filterTop10` هما ميزتان منفصلتان. يكتب العرض التلقائي سمة `autoShow` الكلاسيكية على الحقل المحوري، وتعتمدها جميع إصدارات Excel منذ Excel 97. أما `filterTop10` فيكتب مدخل `PivotFilter` حديثًا يتطلب Excel 2007 أو أحدث. وعند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. بالنسبة إلى المستندات التي يجب أن تظل قابلة للقراءة والكتابة عبر أدوات الإصدارات القديمة، فضّل استخدام `top10AutoShow`؛ أما في المصنفات الحديثة، فضّل استخدام `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **مقالات ذات صلة**
- [تجميع الحقول المحورية في الجدول المحوري](/cells/ar/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}