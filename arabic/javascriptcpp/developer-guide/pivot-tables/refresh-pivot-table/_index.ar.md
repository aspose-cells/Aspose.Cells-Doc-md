---
title: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for JavaScript via C++
linktitle: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for JavaScript via C++
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for JavaScript via C++ باستخدام واجهة API الخاصة بتحديث الجداول المحورية في الإصدار v26.7+. يغطي هذا المقال workbook.refreshAll وworksheet.refreshPivotTables وpivotCache.refresh وpivotTable.calculateData وpivotCache.getPivotTables مع أمثلة برمجية عملية.
keywords: Aspose.Cells, JavaScript via C++, جدول محوري, تحديث, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /ar/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يوفر Aspose.Cells واجهة API متدرجة للتحديث تتيح لك إعادة تحميل بيانات الجداول المحورية ضمن أربعة نطاقات مختلفة — من المصنف بالكامل إلى جدول محوري واحد. بدءًا من **Aspose.Cells for JavaScript via C++ v26.7**، أصبحت الطريقة القديمة `pivotTable.refreshData()` **مهجورة**، ويجب استبدالها بواجهات API أكثر كفاءة تعتمد على الذاكرة المؤقتة، كما هو موضح في هذه المقالة.
{{% /alert %}}

## مقدمة
نادرًا ما يقتصر تحديث جدول محوري على عملية واحدة. في الخلفية، يحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة في ورقة العمل. فهم هذه السلسلة هو مفتاح اختيار واجهة API المناسبة للتحديث في كل حالة.
سلسلة البيانات المكونة من أربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية أو استعلام قاعدة البيانات أو نطاق التجميع حيث توجد القيم الخام.
2. **PivotCache** — لقطة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ وهنا يتم جمع جميع البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والمرشحات. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، ولا يقرأ من مصدر البيانات مباشرةً.
4. **Cells** — خلايا ورقة العمل التي يعيدها `getCells()`، حيث يعرض `PivotTable` قيمه المحسوبة وأنماطه.

{{% alert color="primary" %}}
تشير `pivotCache.getSourceType()` (التعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من v26.7، تدعم `pivotCache.refresh()` نوعَي مصدر **`SHEET`** و**`CONSOLIDATION`** فقط — أي البيانات الموجودة في نطاقات ورقة العمل. ولا تزال المصادر الخارجية (قواعد البيانات والاتصالات الخارجية وما إلى ذلك) غير قابلة للتحديث عبر واجهة API الخاصة بذاكرة التخزين المؤقت.
نتيجة لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:
- **`pivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد انطلاقًا من البيانات المخزنة مؤقتًا بالفعل، من دون الرجوع إلى مصدر البيانات.
تعتمد جميع السيناريوهات في هذه المقالة على خلايا ورقة العمل كمصدر للبيانات، لذلك يكون نوع المصدر هو `SHEET` وتعمل عمليات التحديث كما هو موضح.
{{% /alert %}}

## البدء السريع
إذا كنت تحتاج فقط إلى أقصر الشيفرة الممكنة لتحديث جميع الجداول المحورية في المصنف، فاستدعاء واحد يكفي:

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
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

تشرح بقية هذه المقالة متى ينبغي اختيار واجهة API ذات نطاق أضيق.

## الاستيرادات المطلوبة
تبدأ جميع أمثلة JavaScript في هذه المقالة باستيراد الوحدة التالية، لأن أنواع الجداول المحورية متاحة عبر namespace `Aspose.Cells.Pivot`:
- `const Aspose = require('aspose.cells');`

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى ضمان أن تعكس كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف أحدث بيانات المصدر، فإن أبسط واجهات API وأكثرها شمولًا هي `workbook.refreshAll()`. يمر الاستدعاء الواحد عبر المصنف بالكامل — فتُحدَّث كل `PivotCache` من مصدره، ثم يُعاد حساب كل `PivotTable` تابع له. هذه هي الطريقة الموصى بها لتحديث المستند بالكامل في الحالات العامة عندما لا يكون الأداء موضع اعتبار.
ينشئ المثال التالي مصنفًا يتضمن نطاق مصدر للحقول Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدّل بعض قيم المصدر، ثم يستخدم `refreshAll()` لتحديث كل شيء باستدعاء واحد.

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
            const cells = worksheet.cells;
            // كتابة صف العناوين في الخلايا A1:C1
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و2021)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // تحديث جميع الجداول المحورية وذاكرات التخزين المؤقت الخاصة بها في المصنف
            workbook.refreshAll();
            // حفظ المصنف
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان، لا تحتاج إلا إلى تحديث الجداول المحورية الموجودة في ورقة عمل محددة — على سبيل المثال، عندما يكون معروفًا أن الجداول المحورية في أوراق العمل الأخرى لا علاقة لها بهذه العملية ولا ينبغي المساس بها. في هذه الحالة، توفر Aspose.Cells `worksheet.refreshPivotTables()`، وهي مقصورة على مثيل واحد من `Worksheet`.

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
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
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

## تحديث جدول محوري واحد
عندما تريد التحكم الدقيق في جدول محوري واحد، توفر واجهة API المعتمدة على ذاكرة التخزين المؤقتة خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أم إعدادات العرض أو التخطيط للجدول المحوري نفسه فحسب.

### تغيرت بيانات المصدر — استخدم `pivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، تكون نقطة الدخول المناسبة هي `pivotTable.getPivotCache().refresh()`. يعيد هذا الاستدعاء قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت، ثم يعيد حساب كل `PivotTable` يعتمد على تلك الذاكرة.

### تغير العرض أو التخطيط فقط — استخدم `pivotTable.calculateData()`
إذا *لم* تتغير بيانات المصدر، ولكن تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فحسب (على سبيل المثال، نقل حقل إلى منطقة مختلفة أو تبديل إعداد التحديث عند الفتح)، فليس هناك حاجة إلى الرجوع إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة، ولا يلزم سوى إعادة حساب `PivotTable` المعروض. في هذه الحالة، يكون `pivotTable.calculateData()` هو الخيار المناسب.
يعدّل المثال التالي خاصية لا تتعلق بالمصدر في الجدول المحوري، ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الحالية.

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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // كتابة صف العناوين: الفاكهة / السنة / المبلغ
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // كتابة 8 صفوف من البيانات (الصفوف 2-9، بما يتوافق مع نطاق المصدر A1:C9)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // إضافة جدول محوري في خلية الوجهة E3، مع أخذ البيانات من A1:C9
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // تعيين الحقول: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // تعديل خاصية العرض/التخطيط — هذا تغيير يتعلق بالمظهر فقط،
                // لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
                pivotTable.refreshDataOnOpeningFile = false;
                // يعيد CalculateData() رسم عرض جدول المحور هذا (البيانات + النمط) من
                // البيانات الموجودة بالفعل في PivotCache. ولأن بيانات المصدر لم تتغير،
                // فلا يتم تنفيذ رحلة ذهاب وإياب إلى المصدر — تتم إعادة حساب القيم المخزنة مؤقتًا فقط
                // في خلايا ورقة العمل.
                pivotTable.calculateData();
                // حفظ المصنف على القرص
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

يحتوي المصنف غالبًا على العديد من الجداول المحورية التي تستند جميعها إلى ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل تنفيذ تحديث جماعي، أو لتشخيص أثر الذاكرة المؤقتة المشتركة — استخدم `pivotCache.getPivotTables()`. تعيد هذه الطريقة مجموعة تضم كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المحددة.

## الانتقال من الطريقة المهجورة `pivotTable.refreshData()`
قبل Aspose.Cells for JavaScript via C++ v26.7، كانت الطريقة المعتادة لتحديث جدول محوري هي استدعاء `pivotTable.refreshData()` على كل جدول محوري على حدة. اعتبارًا من v26.7، أصبحت هذه الطريقة **مهجورة**، ويجب استبدالها بواجهات API المعتمدة على ذاكرة التخزين المؤقتة والموضحة أعلاه.
هناك سببان يجعلان نهج `refreshData()` لكل جدول غير عملي في تطبيقات العالم الحقيقي:
- يعيد جلب بيانات المصدر *في كل مرة* تُستدعى فيها، حتى عندما لا يكون المصدر قد تغير.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الجديد الأكثر كفاءة للمصنفات التي تحتوي على عدة جداول محورية تشترك في ذاكرة تخزين مؤقت واحدة.

## أي واجهة API ينبغي أن أستخدم؟
يلخص الجدول التالي واجهات التحديث المتاحة ومتى تختار كل منها.
| الهدف | واجهة API الموصى بها | الملاحظات |
|------|-----------------|-------|
| تحديث كل ما في المصنف | `workbook.refreshAll()` | استدعاء واحد؛ يشمل جميع الذواكر المؤقتة والجداول المحورية. |
| تحديث الجداول المحورية في ورقة عمل واحدة فقط | `worksheet.refreshPivotTables()` | مقصورة على ورقة عمل واحدة. |
| تغيرت بيانات المصدر الخاصة بذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | تحديث جميع الجداول المحورية المرتبطة بتلك الذاكرة المؤقتة المشتركة. |
| تغيرت إعدادات العرض أو التخطيط فقط | `pivotTable.calculateData()` | يتجنب الرجوع غير الضروري إلى المصدر. |
| تعداد جميع الجداول المحورية في ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدمها لتعدادها قبل التحديث الجماعي. |
في الممارسة العملية، يُفضّل استخدام واجهات API المعتمدة على ذاكرة التخزين المؤقتة بدلًا من نهج `refreshData()` المهجور لكل جدول. فهي تأخذ الذواكر المؤقتة المشتركة في الاعتبار، وتتجنب عمليات جلب المصدر المتكررة، وتتيح لك اختيار أصغر نطاق يحقق متطلبات التحديث.

## المشكلات الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة بياناته. إذا عدّلت خلايا المصدر، فاستدعِ `pivotCache.refresh()` (أو `workbook.refreshAll()`) قبل `workbook.save()`، وإلا فسيظل الملف المحفوظ يحتوي على القيم المجمّعة القديمة.
- **استدعاء الطريقة المهجورة `refreshData()` لكل جدول.** في v26.7، أصبحت `pivotTable.refreshData()` مهجورة وتعيد جلب المصدر في كل استدعاء. مع وجود عدة جداول محورية تشترك في ذاكرة تخزين مؤقت، يعني ذلك N عمليات جلب زائدة عن الحاجة للمصدر. استبدل ذلك باستدعاء واحد لـ `pivotCache.refresh()` يليه `pivotTable.calculateData()` لكل جدول.
- **التحديث عندما يكون التخطيط وحده هو ما تغير.** إذا غيّرت عرض الجدول المحوري فقط (ترتيب الأعمدة، `getConsolidationFunction()`، وما إلى ذلك) دون المساس ببيانات المصدر، فسيكون `pivotCache.refresh()` غير ضروري وقد يكون بطيئًا. استدعِ `pivotTable.calculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الحالية.
- **مصدر خارجي لا يدعمه `pivotCache.refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، وما إلى ذلك)، فلن يستطيع `pivotCache.refresh()` تحديثه في v26.7 — فهو يدعم حاليًا نوعَي مصدر البيانات `SHEET` و`CONSOLIDATION` فقط. أما المصادر الخارجية، فأعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

{{< app/cells/assistant language="javascript-cpp" >}}