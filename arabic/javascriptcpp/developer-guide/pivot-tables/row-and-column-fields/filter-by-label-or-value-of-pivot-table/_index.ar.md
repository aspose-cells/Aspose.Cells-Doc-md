---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: يدعم Aspose.Cells for JavaScript via C++ إمكانات شاملة لتصفية الجداول المحورية. يشرح هذا المقال كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسمية والتاريخ والقيمة وأفضل 10، وكذلك من خلال إخفاء عناصر الجدول المحوري أو إظهارها.
keywords: Aspose.Cells, مكتبة JavaScript عبر C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أفضل 10, عنصر محوري, إخفاء عنصر محوري
type: docs
weight: 10
url: /ar/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في جدول محوري. يمكنك تطبيق مرشحات التسمية على حقول الصفوف أو الأعمدة القائمة على النصوص، أو استخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا التاريخ والوقت فقط أو على خلايا فارغة، أو تطبيق مرشحات القيم على الأرقام المجمعة، أو استخدام مرشحات أفضل 10 للترتيب حسب حقل قيمة، أو إخفاء عناصر الجدول المحوري الفردية وإظهارها يدويًا باستخدام الخاصية `isHidden`. تتوفر كل استراتيجية من خلال واجهات API مخصصة في الصنفين `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، لكن الملخصات الخام غالبًا ما تحتوي على معلومات أكثر بكثير مما يلزم عرضه. التصفية هي الآلية الأساسية لحصر جدول محوري في الصفوف أو الأعمدة أو القيم المهمة في تقرير محدد. يعكس Aspose.Cells for JavaScript via C++ إمكانات التصفية المتاحة في Microsoft Excel ويتيح الوصول إليها برمجيًا، بحيث يمكن أتمتة عملية إنشاء التقارير بالكامل.
يتناول هذا المقال استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يصفية عناصر حقول الصفوف أو الأعمدة بناءً على تسمياتها النصية.
2. **مرشح التاريخ** — يصفية حقول الصفوف أو الأعمدة التي لا تحتوي إلا على قيم التاريخ والوقت (أو خلايا فارغة).
3. **مرشح القيمة** — يصفية العناصر بناءً على القيم المجمعة لحقل بيانات.
4. **مرشح أفضل 10** — يعرض فقط أعلى N عناصر أو أدنى N عناصر بعد ترتيبها حسب حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — التحكم اليدوي في قابلية ظهور كل عنصر فرعي في الحقل.
تستخدم كل طريقة من هذه الطرق أسلوبًا مختلفًا في الصنف `PivotField` أو خاصية في الصنف `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `pivotCache.refresh()` على الجدول المحوري حتى تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يتيح لك مرشح التسمية تصفية عناصر حقل صف أو عمود بمقارنة تسمياتها النصية مع نمط. وهذا مفيد عندما تريد عرض المنتجات التي تبدأ أسماؤها بحرف معين فقط، أو التي تحتوي على كلمة محددة، أو التي تطابق أي معيار آخر يستند إلى التسمية.
يوفر Aspose.Cells تصفية حسب التسمية من خلال الأسلوب `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. تحدد الوسيطة `filterType` وضع المقارنة (`CaptionBeginsWith`، `CaptionContains`، `CaptionEndsWith`، `CaptionDoesNotContain`، `CaptionIsNotBlank`، `CaptionIsBlank`، وغيرها). توفر الوسيطتان `label1` و`label2` نص المقارنة — مرّر `""` إلى `label2` عندما تحتاج إلى مطابقة قيمة واحدة فقط، مثل مطابقة نص يبدأ بنمط أو يحتوي عليه.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبق مرشح تسمية بحيث تظل العناصر التي تبدأ تسمياتها ببادئة محددة فقط ظاهرة، ويحدّث الجدول المحوري، ويحفظ النتيجة.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **مرشح التاريخ**
تتيح لك مرشحات التاريخ تضييق جدول محوري وفق معايير تستند إلى التاريخ، مثل اليوم أو الأسبوع الماضي أو الشهر الحالي أو الربع التالي أو نطاق تاريخ محدد. وهي مرشحات متخصصة لا تعمل إلا مع الحقول التي تخزن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصفوف أو الأعمدة على خلايا التاريخ والوقت أو قيم فارغة فقط. وإذا احتوى الحقل المصدر على أنواع بيانات أخرى مثل الأرقام أو النصوص، فلن ينتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ وأن تكون جميع القيم إما قيم `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
يوفر Aspose.Cells تصفية حسب التاريخ من خلال الأسلوب `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. يحتوي تعداد `PivotFilterType` على قيم تاريخية مخصصة مثل `Today`، `Yesterday`، `LastWeek`، `ThisWeek`، `NextWeek`، `LastMonth`، `ThisMonth`، `NextMonth`، `LastQuarter`، `ThisQuarter`، `NextQuarter`، `LastYear`، `ThisYear`، `NextYear`، و`Between`. ووفقًا لنوع المرشح المحدد، تمرر قيمة واحدة من نوع `DateTime` أو قيمتين من هذا النوع، وفي حالة `Between` تمرر تاريخي البداية والنهاية.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري له حقل تاريخ في منطقة الصفوف، ويطبق مرشح تاريخ يقصر العناصر الظاهرة على نطاق تاريخ محدد، ويحدّث الجدول المحوري، ويحفظ المصنف.
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
        const { Workbook } = AsposeCells;
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **مرشح القيمة**
تعمل مرشحات القيم على القيم المجمعة التي يحسبها الجدول المحوري في منطقة بياناته. وبدلًا من مطابقة التسميات النصية، تقارن الإجماليات الرقمية بحد. ومن أمثلة الاستخدامات الشائعة عرض المنتجات التي يتجاوز مجموع مبيعاتها مبلغًا مستهدفًا فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق محدد فقط.
يوفر Aspose.Cells تصفية القيم من خلال الأسلوب `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. تحدد الوسيطة `valueFieldIndex` حقل البيانات الذي يجب تقييمه (استخدم `pivotTable.getDataFields().indexOf(dataField)` أو تكرار المجموعة للعثور على موضعه). وتستخدم الوسيطة `filterType` قيمًا مثل `ValueGreaterThan`، `ValueLessThan`، `ValueBetween`، `ValueEqual`، `ValueNotEqual`، `ValueGreaterThanOrEqual`، و`ValueLessThanOrEqual`. وأما الوسيطتان من النوع `double` فتوفران قيمة حد أو قيمتي حد.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبق مرشح قيمة يحتفظ فقط بالعناصر التي يتجاوز مجموع مبيعاتها المجمعة حدًا رقميًا، ويحدّث الجدول المحوري، ويحفظ المصنف.

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
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **مرشح أفضل 10**
مرشح أفضل 10 هو شكل متخصص من مرشح القيمة لا يحتفظ إلا بأعلى N عناصر أو أدنى N عناصر استنادًا إلى حقل قيمة محدد. ويُستخدم عادةً في تقارير الترتيب مثل «أفضل 10 منتجات حسب الإيرادات» أو «أدنى 5 مناطق حسب عدد المبيعات».

{{% alert color="primary" %}}
لا يكون مرشح أفضل 10 فعالًا إلا إذا كان الجدول المحوري يحتوي على حقل قيمة محوري واحد أو أكثر في منطقة البيانات. ومن دون حقل قيمة واحد على الأقل، لا توجد قيمة مجمعة يمكن ترتيب العناصر بناءً عليها، ولا يمكن تطبيق المرشح.
يوفر Aspose.Cells تصفية أفضل 10 من خلال الأسلوب `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. الوسيطة `valueFieldIndex` هي فهرس حقل البيانات الذي تُستخدم قيمه المجمعة لترتيب العناصر، وتحدد `filterType` وحدة قياس `itemCount` (إذ يحتفظ `Count` بعدد ثابت من العناصر، بينما يحتفظ `Percent` بنسبة مئوية من العناصر بحيث تكون `itemCount` هي النسبة نفسها)، وتحدد `isTop` ما إذا كان ينبغي الاحتفاظ بأعلى العناصر (`true`) أو أدنى العناصر (`false`)، ويحدد `itemCount` عدد العناصر أو النسبة المئوية التي ينبغي الاحتفاظ بها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبق مرشح أفضل 10 للاحتفاظ بأعلى 10 عناصر فقط حسب مجموع المبيعات، ويحدّث الجدول المحوري، ويحفظ المصنف.
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
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
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
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **التصفية عبر إخفاء عناصر الجدول المحوري أو إظهارها**
بالإضافة إلى واجهات API الخاصة بالتصفية، يتيح لك Aspose.Cells التحكم مباشرةً في قابلية ظهور كل عنصر محوري فردي. ومن خلال التكرار في مجموعة `pivotField.getPivotItems()` وتبديل قيمة الخاصية `isHidden`، يمكنك استبعاد عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي ضبط `pivotItem.isHidden = true` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي ضبط `pivotItem.isHidden = false` إلى إظهاره مجددًا وجعله ظاهرًا.
هذا الأسلوب مفيد عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعنصر بعينه، مثل إخفاء عدد قليل من الفئات المحددة التي لا ينبغي أن تظهر في تقرير معين. يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ويحدّث الجدول المحوري، ويحفظ المصنف.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **الملخص**
يوفر Aspose.Cells for JavaScript via C++ مجموعة كاملة من إمكانات تصفية الجداول المحورية، بما يطابق ما يوفره Microsoft Excel. تغطي مرشحات التسمية والتاريخ والقيم أكثر سيناريوهات التحليل شيوعًا، بينما يُستخدم مرشح أفضل 10 في تقارير الترتيب. وعندما تكون قاعدة التصفية غير منتظمة، توفر الخاصية `pivotItem.isHidden` خيارًا بديلًا مرنًا على مستوى العنصر. ويتيح لك الجمع بين هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح التسمية ثم إخفاء عناصر محددة — إنشاء تقارير جداول محورية دقيقة الاستهداف بالكامل من خلال التعليمات البرمجية.

{{< app/cells/assistant language="javascript-cpp" >}}