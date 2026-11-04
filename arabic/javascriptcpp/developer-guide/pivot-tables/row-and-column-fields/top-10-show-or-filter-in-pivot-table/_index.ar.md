---
title: عرض أو تصفية أعلى 10 في الجدول المحوري
linktitle: عرض أو تصفية أعلى 10 في الجدول المحوري
description: تعلّم كيفية عرض العناصر الأعلى أو الأدنى تصنيفًا فقط في حقل محوري باستخدام Aspose.Cells for JavaScript via C++. تتناول هذه المقالة خصائص AutoShow في Excel 97-2003 (isAutoShow والخصائص ذات الصلة)، وقراءة الخيارات الحالية، وتصفية أعلى 10 في Excel 2007-365 عبر filterTop10.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, جدول محوري, أعلى 10, العرض التلقائي, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /ar/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
يصعب قراءة الجدول المحوري الذي يسرد جميع عناصر حقل الصف عندما يضم الحقل عشرات العناصر. لا يعرض تقرير «أعلى 10» سوى العناصر الأعلى أو الأدنى ترتيبًا، وهو تحديدًا ما تحتاج إليه تقارير الترتيب — «أعلى 5 منتجات حسب الإيرادات» أو «أسفل 3 مناطق حسب عدد المبيعات». تدعم Aspose.Cells أسلوبين لهذا الغرض، يقابلهما جيلان من إصدارات Microsoft Excel.
- **ميزة `AutoShow` في Excel 97-2003** — خصائص `PivotField` الأربعة: `isAutoShow` و`isAscendShow` و`autoShowCount` و`autoShowField`. ويمثل ذلك الإعداد الكلاسيكي «عرض أعلى/أسفل N عنصر» المخزن مباشرةً على الحقل المحوري. ويعمل في جميع إصدارات Excel، القديمة والجديدة، لأنه جزء من صيغة الجدول المحوري الأصلية.
- **تصفية أعلى 10 في Excel 2007-365** — الطريقة `PivotField.filterTop10()`. ويمثل هذا مرشح القيم الحديث لأعلى 10 الموجود في قائمة الحقل ضمن مرشحات القيم. ويُخزَّن في صورة كائن `PivotFilter` مرتبط بالحقل، ويدعم الترتيب حسب عدد العناصر أو النسبة المئوية.

## **عرض أعلى 10 في Excel 97-2003 (`AutoShow`)**
تُضبط إعدادات `AutoShow` الكلاسيكية بإسناد أربع خصائص إلى `PivotField`:
- `isAutoShow` — يتيح إعداد `AutoShow` على الحقل أو يعطله.
- `isAscendShow` — قيمة `false` تبقي العناصر الأعلى ترتيبًا (أعلى)، بينما قيمة `true` تبقي الأدنى (أسفل).
- `autoShowCount` — عدد العناصر التي يجب الاحتفاظ بها، مثل 10 لتقرير أعلى 10 الكلاسيكي.
- `autoShowField` — الفهرس الذي يبدأ من الصفر لحقل **البيانات** الذي تُستخدم قيمه لترتيب العناصر. مرّر -1 لترتيب العناصر وفق الحقل نفسه.
يمكن أن يستند الترتيب إلى حقل قيمة أو إلى الحقل نفسه. وهناك تنفيذان طبيعيان، كما هو موضح أدناه.

### **الترتيب حسب حقل قيمة**
رتّب عناصر حقل الصف وفق حقل قيمة عادي مثل «مجموع المبيعات». يبني المثال التالي جدولًا محوريًا بحقل صف واحد (`Sport`) وحقل بيانات واحد (`Sales`)، ثم يعرض أعلى رياضتين حسب المبيعات. تكون `rankBy` بقيمة 0 لأن «مجموع المبيعات» هو حقل البيانات عند الفهرس 0.

```javascript
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
            // إظهار أهم عنصرين مرتبين حسب "مجموع المبيعات" (فهرس حقل البيانات 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
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
يمكن ترتيب الحقل وفق نفسه أيضًا — مرّر -1 إلى `autoShowField`. لا يلزم حقل بيانات إضافي لهذا التنفيذ؛ يكفي أن يكون الحقل في منطقة الصف (أو العمود). يوضح المثال التالي أدنى 3 رياضات مرتبة وفق الحقل نفسه. عند حفظ هذا الإعداد، لا تتضمن بنية XML للجدول المحوري سمة `rankBy` لأن -1 هي القيمة الافتراضية لصيغة الجدول المحوري، وتُقرأ القيمة -1 من خلال `autoShowField`.

```javascript
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
            // عرض آخر 3 عناصر مصنفة حسب الحقل نفسه (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
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

## **قراءة خيارات `AutoShow` الحالية**
تتيح خصائص `PivotField`، أي `isAutoShow` و`isAscendShow` و`autoShowCount` و`autoShowField`، الوصول إلى خيارات `AutoShow` المخزنة حاليًا على الحقل. استخدمها للتحقق من طريقة عرض عناصر مصنف موجود، أو جدول محوري قمت بتهيئته للتو، بما في ذلك المصنفات المحمّلة من ملف.

```javascript
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
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
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

تقابل الخصائص الأربع سمات `AutoShow` الكلاسيكية المكتوبة في XML الجدول المحوري (`autoShow` و`topAutoShow` و`itemPageCount` و`rankBy`)، لذا تكون القيم المقروءة هي القيم التي ستعتمدها جميع إصدارات Excel.

## **ملاحظة**

{{% alert color="primary" %}}
- بعد تغيير أي خاصية من خصائص `AutoShow`، أعد استدعاء `pivotTable.calculateData()` — لا تظهر هذه الإعدادات في التخطيط المعروض إلا عند إعادة الحساب التالية.
- تعمل إعدادات `AutoShow` مع حقول الصفوف والأعمدة. لا يمكن ترتيب حقل يقع في منطقة عامل التصفية (منطقة الصفحات) بهذه الطريقة، لأن عناصره لا تُعرض داخل جسم الجدول المحوري.
{{% /alert %}}

## **Excel 2007-365: تصفية أعلى 10 (`filterTop10`)**
تعرض إصدارات Excel الحديثة خيار أعلى 10 بوصفه مرشحًا للقيم في قائمة الحقل (مرشحات القيم، أعلى 10...). تحاكي Aspose.Cells هذه الميزة باستخدام الطريقة `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)`، التي تُعيد كائن `PivotFilter` المُنشأ:
- `valueFieldIndex` — الفهرس الذي يبدأ من الصفر لحقل البيانات الذي تُستخدم قيمه المجمعة لترتيب العناصر.
- `type` — ما يحدد معنى `itemCount`. يحتفظ `PivotFilterType.Count` بعدد ثابت من العناصر (خيار «العناصر» في مربع الحوار). يحتفظ `PivotFilterType.Percent` بنسبة مئوية من العناصر، لذا تكون قيمة `itemCount` هي النسبة المئوية نفسها؛ أي أن القيمة 30 تعني الاحتفاظ بأعلى 30 بالمئة. يرتب `PivotFilterType.Sum` العناصر بحسب التغطية التراكمية للقيم.
- `isTop` — قيمة `true` للأعلى، وقيمة `false` للأسفل.
- `itemCount` — الرقم N في «أعلى N»؛ تعتمد وحدة `itemCount` على `type`.

```javascript
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
    </script>
</html>
```

{{% alert color="primary" %}}
خصائص `AutoShow` و`filterTop10` هما ميزتان منفصلتان. يكتب `AutoShow` سمة `autoShow` الكلاسيكية على الحقل المحوري، وتحتكرمها جميع إصدارات Excel منذ Excel 97. ويكتب `filterTop10` إدخالًا حديثًا من نوع `PivotFilter`، وهو ما يتطلب Excel 2007 أو إصدارًا أحدث. عند فتح مصنف في إصدار أقدم من Excel، يعود الجدول المحوري الذي يستخدم المرشح الحديث إلى عرض جميع العناصر. وبالنسبة للوثائق التي يجب أن تُعالَج بدورة كاملة بواسطة أدوات قديمة، يُفضَّل استخدام خصائص `AutoShow`؛ أما المصنفات الحديثة، فيُفضَّل استخدام `filterTop10` لأنه يتكامل مع مرشحات القيم الأخرى.
{{% /alert %}}

## **المقالات ذات الصلة**
- [تجميع الحقول المحورية في الجدول المحوري](/cells/ar/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}