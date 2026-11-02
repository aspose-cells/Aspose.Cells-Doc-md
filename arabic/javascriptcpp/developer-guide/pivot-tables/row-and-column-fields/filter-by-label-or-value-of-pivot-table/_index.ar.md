---
title: تصفية الجداول المحورية حسب التسمية أو القيمة
linktitle: تصفية الجداول المحورية حسب التسمية أو القيمة
description: Aspose.Cells for JavaScript via C++ يدعم إمكانات تصفية شاملة للجداول المحورية. توضح هذه المقالة كيفية تصفية بيانات الجدول المحوري باستخدام مرشحات التسمية والتاريخ والقيمة ومرشحات أفضل 10، وكذلك عن طريق إخفاء عناصر الجدول المحوري أو إظهارها.
keywords: Aspose.Cells, مكتبة JavaScript عبر C++, جدول بيانات, جدول محوري, تصفية, مرشح التسمية, مرشح القيمة, مرشح التاريخ, مرشح أفضل 10, عنصر الجدول المحوري, إخفاء عنصر الجدول المحوري
type: docs
weight: 10
url: /ar/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفّر Aspose.Cells خمس استراتيجيات عملية لتصفية البيانات المعروضة في جدول محوري. يمكنك تطبيق مرشحات التسمية على الحقول النصية في الصفوف أو الأعمدة، واستخدام مرشحات التاريخ عندما يحتوي الحقل على خلايا التاريخ والوقت أو خلايا فارغة فقط، وتطبيق مرشحات القيمة على الأرقام المجمعة، واستخدام مرشح أفضل 10 للترتيب وفق حقل قيمة، أو إخفاء عناصر الجدول المحوري الفردية وإظهارها يدويًا باستخدام الخاصية `isHidden`. تتاح كل استراتيجية عبر واجهات API مخصصة في الصنفين `PivotField` و`PivotItem`.
{{% /alert %}}

## **مقدمة**
تُعد الجداول المحورية أدوات تحليلية قوية، غير أن الملخصات الخام غالبًا ما تتضمّن معلومات أكثر بكثير مما يلزم عرضه. التصفية هي الآلية الأساسية لتضييق الجدول المحوري بحيث يقتصر على الصفوف أو الأعمدة أو القيم المهمة في تقرير معيّن. يوفّر Aspose.Cells for JavaScript via C++ إمكانات تصفية مماثلة لتلك المتاحة في Microsoft Excel، ويتيح الوصول إليها برمجيًا من أجل أتمتة إنشاء التقارير بالكامل.
تغطي هذه المقالة استراتيجيات التصفية التالية:
1. **مرشح التسمية** — يصفّي عناصر حقول الصفوف أو الأعمدة استنادًا إلى تسمياتها النصية.
2. **مرشح التاريخ** — يصفّي حقول الصفوف أو الأعمدة التي لا تحتوي إلا على قيم التاريخ والوقت (أو خلايا فارغة).
3. **مرشح القيمة** — يصفّي العناصر استنادًا إلى القيم المجمعة لحقل بيانات.
4. **مرشح أفضل 10** — يعرض أعلى N أو أدنى N عناصر فقط، مرتبةً وفق حقل قيمة.
5. **إخفاء / إظهار عناصر الجدول المحوري** — يتحكم يدويًا في قابلية ظهور كل عنصر فردي في الحقل.
تستخدم كل استراتيجية طريقة مختلفة في الصنف `PivotField` أو خاصية في الصنف `PivotItem`. بعد تطبيق أي مرشح، يجب استدعاء `pivotCache.refresh()` على الجدول المحوري حتى تعكس البيانات المخزنة مؤقتًا والقيم المحسوبة حالة المرشح الجديدة.

## **مرشح التسمية**
يتيح مرشح التسمية تصفية عناصر حقل الصف أو العمود بمقارنة تسمياتها النصية مع نمط. وهذا مفيد إذا أردت عرض المنتجات التي تبدأ أسماؤها بحرف محدد، أو تحتوي على كلمة معينة، أو تطابق أي معيار آخر قائم على التسمية.
يوفّر Aspose.Cells مرشح التسمية من خلال الطريقة `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)`. يحدد الوسيط `filterType` وضع المقارنة (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank`، إلخ). وتوفّر الوسائط `label1` و`label2` نص المقارنة — مرّر `""` إلى `label2` عند الحاجة إلى مطابقة قيمة واحدة فقط (مثل البدء بالنص أو الاحتواء).
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري موجود، ويطبّق مرشح تسمية لا يبقي ظاهرًا سوى العناصر التي تبدأ تسمياتها ببادئة محددة، ويحدّث الجدول المحوري، ويحفظ النتيجة.

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
                    // تحميل المصنف الموجود الذي يحتوي على جدول محوري
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // الوصول إلى ورقة العمل بواسطة الفهرس (ورقة العمل الأولى)
                    const worksheet = workbook.worksheets.get(0);
                    // الوصول إلى الجدول المحوري بواسطة الفهرس
                    const pivotTable = worksheet.pivotTables.get(0);
                    // استرجاع حقل الصف الأول PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // تطبيق مرشح التسميات — عرض عناصر الصف فقط التي تبدأ تسمياتها بالبادئةProvided
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // تحديث بيانات الجدول المحوري وإعادة حسابها حتى يسري المرشح
                    pivotTable.refreshData();
                    // حفظ المصنف مرة أخرى على القرص
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
تتيح مرشحات التاريخ تضييق جدول محوري وفق معايير مرتبطة بالتاريخ، مثل اليوم أو الأسبوع الماضي أو الشهر الحالي أو الربع التالي أو نطاق تاريخ محدد. وهي مرشحات متخصصة لا تعمل إلا مع الحقول التي تخزّن معلومات التاريخ والوقت.

{{% alert color="primary" %}}
لا يعمل مرشح التاريخ إلا إذا احتوت منطقة الصفوف أو الأعمدة على خلايا التاريخ والوقت أو خلايا فارغة فقط. إذا احتوى الحقل المصدر على أنواع بيانات أخرى، مثل الأرقام أو النصوص، فلن يُنتج مرشح التاريخ النتيجة المتوقعة. تأكد من تنسيق الحقل كتاريخ وأن جميع القيم عبارة عن نسخ `DateTime` صالحة أو خلايا فارغة قبل تطبيق هذا المرشح.
يوفّر Aspose.Cells مرشح التاريخ من خلال الطريقة `pivotField.filterByDate(PivotFilterType, DateTime[] values)`. يحتوي التعداد `PivotFilterType` على قيم تاريخية مخصصة، مثل `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear`, و`Between`. وبحسب نوع المرشح المختار، تمرّر إما قيمة `DateTime` واحدة أو قيمتَي `DateTime` (في حالة `Between`، تمرّر تاريخَي البداية والنهاية).
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يضم حقل تاريخ في منطقة الصفوف، ويطبّق مرشح تاريخ يقصر العناصر الظاهرة على نطاق تاريخ محدد، ويحدّث الجدول المحوري، ويحفظ المصنف.
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
                // تحميل المصنف الحالي الذي يحتوي على الجدول المحوري
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // الوصول إلى ورقة العمل التي تحتوي على الجدول المحوري (حسب الفهرس)
                const worksheet = workbook.worksheets.get(0);
                // الوصول إلى الجدول المحوري حسب الفهرس
                const pivotTable = worksheet.pivotTables.get(0);
                // استرجاع حقل PivotField الخاص بالتاريخ من منطقة الصفوف
                // (لا يعمل مرشح التاريخ إلا عندما تحتوي منطقة الصفوف/الأعمدة على خلايا التاريخ والوقت أو خلايا فارغة فقط)
                const dateField = pivotTable.rowFields.get(0);
                // تعريف معيار التاريخ لمرشح بين
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // تطبيق مرشح التاريخ على حقل الجدول المحوري
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // تحديث الجدول المحوري وإعادة حسابه حتى يسري المرشح
                pivotTable.refreshData();
                // حفظ المصنف
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
تعمل مرشحات القيمة على القيم المجمعة التي يحسبها الجدول المحوري في منطقة البيانات. وبدل مطابقة التسميات النصية، تقارن الإجماليات الرقمية بحدّ. ومن حالات الاستخدام النموذجية عرض المنتجات التي يزيد مجموع مبيعاتها عن مبلغ مستهدف فقط، أو المناطق التي يقع عدد معاملاتها ضمن نطاق محدد.
يوفّر Aspose.Cells مرشح القيمة من خلال الطريقة `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)`. يحدد الوسيط `valueFieldIndex` حقل البيانات المراد تقييمه (استخدم `pivotTable.getDataFields().indexOf(dataField)` أو تكرار عناصر المجموعة لإيجاد الموضع). ويستخدم الوسيط `filterType` قيمًا مثل `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual`, و`ValueLessThanOrEqual`. وتوفّر معاملتا النوع `double` قيمة العتبة أو قيمتيها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري، ويطبّق مرشح قيمة لا يبقي سوى العناصر التي تتجاوز مبيعاتها المجمعة حدًا رقميًا، ويحدّث الجدول المحوري، ويحفظ المصنف.

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
                // العثور على فهرس حقل البيانات يدويًا لأن PivotFieldCollection لا يحتوي على IndexOf
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
                pivotTable.refreshData();
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
مرشح أفضل 10 هو نوع متخصص من مرشح القيمة يحتفظ فقط بأعلى N أو أدنى N عناصر استنادًا إلى حقل قيمة محدد. ويُستخدم عادةً في تقارير الترتيب، مثل «أفضل 10 منتجات حسب الإيرادات» أو «أدنى 5 مناطق حسب عدد المبيعات».

{{% alert color="primary" %}}
لا يكون مرشح أفضل 10 فعالًا إلا إذا كان الجدول المحوري يحتوي على حقل قيمة واحد أو أكثر في منطقة البيانات. وبدون حقل قيمة واحد على الأقل، لا يوجد مقياس مجمّع لترتيب العناصر بناءً عليه، ولا يمكن تطبيق المرشح.
يوفّر Aspose.Cells مرشح أفضل 10 من خلال الطريقة `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)`. يحدد الوسيط `valueFieldIndex` فهرس حقل البيانات الذي تُرتَّب العناصر وفق قيمه المجمعة، ويحدد `filterType` وحدة `itemCount` (يحتفظ `Count` بعدد ثابت من العناصر، بينما يحتفظ `Percent` بنسبة مئوية من العناصر، بحيث تكون `itemCount` هي النسبة المئوية نفسها)، ويشير `isTop` إلى ما إذا كان ينبغي الاحتفاظ بأعلى العناصر (`true`) أو أدنى العناصر (`false`)، ويحدد `itemCount` عدد العناصر، أو النسبة المئوية، التي يجب الاحتفاظ بها.
يحمّل المثال التالي مصنفًا يحتوي على جدول محوري يتضمن حقل قيمة، ويطبّق مرشح أفضل 10 للإبقاء على أعلى 10 عناصر فقط وفق مجموع المبيعات، ويحدّث الجدول المحوري، ويحفظ المصنف.
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
                // تحميل مصنف العمل الحالي الذي يحتوي على جدول المحور
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // الوصول إلى ورقة العمل التي تحتوي على جدول المحور (الفهرس 0)
                const worksheet = workbook.worksheets.get(0);
                // الوصول إلى جدول المحور حسب الفهرس
                const pivotTable = worksheet.pivotTables.get(0);
                // التأكد من وجود حقل PivotField واحد على الأقل بقيمة في منطقة البيانات
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // استرجاع حقل PivotField المستهدف للصف (الحقل الذي نريد تطبيق Top 10 عليه)
                const rowField = pivotTable.rowFields.get(0);
                // يوجد حقل البيانات الأول (والوحيد) عند الفهرس 0؛ وترتيب Top 10 يعتمد عليه.
                const valueFieldIndex = 0;
                // تطبيق مرشح Top 10 على حقل الصف:
                //   - valueFieldIndex = 0 — حقل البيانات المستخدم لترتيب العناصر
                //   - filterType = PivotFilterType.Count (الإبقاء على عدد ثابت من العناصر؛
                //     would've interpret PivotFilterType.Percent 10 as "top 10 percent")
                //   - isTop = true (أفضل N؛ أما false فيعني أسفل N)
                //   - itemCount = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // تحديث بيانات جدول المحور وإعادة حسابه حتى يسري المرشح
                pivotTable.refreshData();
                // حفظ مصنف العمل
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
بالإضافة إلى واجهات API للتصفية المهيكلة، يتيح Aspose.Cells التحكم مباشرة في ظهور كل عنصر من عناصر الجدول المحوري. وبتكرار عناصر مجموعة `pivotField.getPivotItems()` التابعة للصنف `PivotField` وتبديل قيمة الخاصية `isHidden`، يمكنك إخفاء عناصر محددة بشكل انتقائي دون تطبيق مرشح قائم على الصيغة. يؤدي تعيين `pivotItem.isHidden = true` إلى إخفاء العنصر من الجدول المحوري، بينما يؤدي تعيين `pivotItem.isHidden = false` إلى إظهاره مجددًا.
هذا النهج مفيد عندما تكون قاعدة التصفية غير منتظمة أو خاصة بعناصر محددة، مثل إخفاء عدد قليل من الفئات ذات الأسماء المحددة التي ينبغي ألا تظهر في تقرير معين. يحمّل المثال التالي جدولًا محوريًا، ويخفي عنصرًا محددًا بالاسم، ويوضح كيفية إظهاره، ويحدّث الجدول المحوري، ويحفظ المصنف.

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
                // تحميل مصنف موجود يحتوي على جدول محوري
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // الوصول إلى ورقة العمل الأولى التي تحتوي على الجدول المحوري
                const sheet = workbook.worksheets.get(0);
                // الوصول إلى الجدول المحوري بواسطة الفهرس (أول جدول محوري في ورقة العمل)
                const pivotTable = sheet.pivotTables.get(0);
                // استرجاع حقل PivotField المستهدف (أول حقل تسميات صفوف سنخفي أو نظهر عناصره)
                const pivotField = pivotTable.rowFields.get(0);
                // التكرار عبر مجموعة PivotItems لحقل PivotField المحدد
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // إخفاء عناصر الجدول المحوري التي تطابق اسمًا/معيارًا محددًا
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // إظهار مثال على إلغاء الإخفاء: إعادة إظهار عنصر جدول محوري كان مخفيًا مسبقًا
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // تحديث الجدول المحوري وإعادة حسابه حتى تسري التغييرات
                pivotTable.refreshData();
                // حفظ المصنف — تظل العناصر المخفية موجودة في البيانات الأساسية
                // لكن تُستبعد من إخراج الجدول المحوري المعروض
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

## **ملخص**
يوفّر Aspose.Cells for JavaScript via C++ مجموعة متكاملة من إمكانات تصفية الجداول المحورية تتوافق مع الإمكانات المتاحة في Microsoft Excel. تغطي مرشحات التسمية والتاريخ والقيمة أكثر السيناريوهات التحليلية شيوعًا، بينما يتولى مرشح أفضل 10 تقارير الترتيب. عندما تكون قاعدة التصفية غير منتظمة، توفّر الخاصية `pivotItem.isHidden` حلًا بديلًا مرنًا على مستوى العنصر. ويتيح دمج هذه الاستراتيجيات — على سبيل المثال، تطبيق مرشح تسمية ثم إخفاء عناصر محددة — إنشاء تقارير جداول محورية مستهدفة بدقة بالكامل من خلال التعليمات البرمجية.

{{< app/cells/assistant language="javascript-cpp" >}}