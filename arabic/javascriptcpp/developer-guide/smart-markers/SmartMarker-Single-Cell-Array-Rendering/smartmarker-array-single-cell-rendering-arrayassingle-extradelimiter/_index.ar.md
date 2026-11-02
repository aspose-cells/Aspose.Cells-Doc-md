---
title: عرض مصفوفة SmartMarker في خلية واحدة | Aspose.Cells for JavaScript via C++
linktitle: عرض مصفوفة SmartMarker في خلية واحدة | Aspose.Cells for JavaScript via C++
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي ArrayAsSingle وExtraDelimiter داخل العلامات الذكية مع Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, مكتبة Aspose.Cells for JavaScript via C++, جدول بيانات, العلامات الذكية, ArrayAsSingle, ExtraDelimiter, مصفوفة في خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
url: /ar/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells عرض بيانات المصفوفة في خلية واحدة عبر العلامات الذكية. ومن خلال استخدام السمة `ArrayAsSingle` مع السمة `ExtraDelimiter`، يستطيع المطورون التحكم في كيفية فصل عناصر المصفوفة داخل خلية واحدة، مع توفير تنسيق مرن للتقارير والقوالب.
{{% /alert %}}

## **مقدمة**
تُعد العلامات الذكية في Aspose.Cells ميزة قوية تعتمد على القوالب وتتيح لك تعبئة بيانات الجدول ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. تُوضع العلامة في مصنف التصميم، وعند معالجة القالب بواسطة `WorkbookDesigner`، تُستبدل العلامات بالقيم المستمدة من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة ذكية إلى خاصية مصفوفة، مثل `&=DataSource.Numbers`، يوسّع المحرك المصفوفة ويضع كل عنصر في خلية مجاورة منفصلة، إما أفقيًا عبر صف أو رأسيًا على طول عمود. وعلى الرغم من أن هذا السلوك مريح في سيناريوهات كثيرة، هناك حالات يُفضّل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج عناصرها وفصلها بفاصل تختاره.
تقدّم سمتا `ArrayAsSingle` و`ExtraDelimiter`، عند استخدامهما معًا داخل وسم علامة ذكية، حلاً مباشرًا لهذا المتطلب. وتتيحان لك إبقاء تخطيطات التقارير مضغوطة ومتوقعة، مع الحفاظ على سهولة التعامل مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة ضرورية**

### **سلوك توزيع المصفوفة الافتراضي**
عندما تشير علامة ذكية إلى خاصية مصفوفة، يوزّع Aspose.Cells المصفوفة على خلايا متعددة افتراضيًا. على سبيل المثال، عند تطبيق علامة مثل `&=Product.Tags` على مصفوفة تضم أربع سلاسل نصية، تضع كل قيمة في خلية خاصة بها، مما يؤدي إلى إزاحة بقية محتوى القالب وقد يعطل تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**
توجد حالات عملية كثيرة يكون فيها سلوك التوزيع الافتراضي غير مرغوب:
- **تقارير ملخصية** تحتاج إلى تخطيط مضغوط يخصص صفًا واحدًا لكل سجل.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية** التي يلزم عرضها كقيم مفصولة بفواصل أو بعلامات رأسية داخل خلية واحدة.
- **عناصر التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في موضع واحد لتسهيل القراءة.
- **مسارات المعالجة اللاحقة**، مثل تصدير CSV وعرض PDF ودمج البريد، التي تتوقع قيمة موحدة لكل خلية بدلًا من نطاق موسّع.
- **التوافق عبر الأنظمة الأساسية**، حيث لا تقبل بعض الجهات المستهلكة المصفوفات التي تمتد عبر خلايا متعددة.

### **الفجوة التي تسدها الميزة**
في غياب آلية مدمجة، كان على المطورين معالجة البيانات مسبقًا في JavaScript، وتحويل المصفوفات إلى سلاسل مفصولة قبل ربطها بمصمم المصنف. ويؤدي ذلك إلى تكرار المنطق، وتعقيد نماذج البيانات، وزيادة احتمال حدوث الأخطاء. وتلغي سمتا `ArrayAsSingle` و`ExtraDelimiter` الحاجة إلى هذا الحل البديل من خلال تعريف قواعد التنسيق داخل العلامة الذكية نفسها.

## **مزايا الميزة**
يوفر استخدام سمتي `ArrayAsSingle` و`ExtraDelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء في خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مع إبقاء التخطيطات مضغوطة ومتوقعة.
- **التحكم في الفاصل المخصص**: تحديد أي سلسلة فاصل تريدها، سواء كانت فاصلة أو فاصلة منقوطة أو شرطة أو علامة رأسية أو سطرًا جديدًا أو أي نص مخصص.
- **التنسيق المستند إلى القالب**: لا يلزم أي كود إضافي لمعالجة البيانات مسبقًا؛ وتوجد قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تزيح محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات مرنة**: تعمل مع السلاسل النصية والأرقام والتواريخ وأي نوع بيانات آخر يمكن فصله بفاصل.
- **التوافق الخلفي**: عند عدم إدراج السمتين، يبقى سلوك التوزيع الأصلي كما هو، لذا تواصل القوالب الحالية العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة العلامة الذكية**
تُمرَّر سمتا `ArrayAsSingle` و`ExtraDelimiter` كأزواج اسم-قيمة داخل أقواس العلامة الذكية القياسية. الصيغة العامة هي:

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
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayProperty` — العلامة الذكية القياسية التي تشير إلى خاصية المصفوفة في مصدر البيانات المرتبط.
- `arrayasSingle=true` — يوجّه المحرك إلى عرض المصفوفة بأكملها في خلية واحدة. ولا يُفعّل سلوك الخلية الواحدة إلا القيمة `true`.
- `extraDelimiter=", "` — يحدد الفاصل المدرج بين عناصر المصفوفة. القيمة عبارة عن سلسلة نصية حرفية؛ يمكن أن تكون فارغة أو سلسلة تتكون من محرف واحد أو سلسلة متعددة المحارف.

{{% alert color="primary" %}}
تقبل السمة `extraDelimiter` أي سلسلة نصية حرفية، بما في ذلك الفواصل متعددة المحارف والنصوص المخصصة وتسلسلات الهروب مثل `\n` لإخراج مفصول بأسطر جديدة. وإذا كانت المصفوفة فارغة، تُترك الخلية الناتجة فارغة.
{{% /alert %}}

### **سير العمل خطوة بخطوة**
يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تحضير مصدر البيانات**: أنشئ كائنًا أو بنية بيانات توفر خاصية تُرجع مصفوفة. يمكن أن تُرجع الخاصية مصفوفة من السلاسل النصية أو الأرقام أو أي نوع آخر من أنواع القيم المدعومة.
2. **إنشاء مصنف التصميم**: أنشئ `Workbook` جديدًا، وأضف صف عنوان، وضع علامة ذكية في خلية تشير إلى خاصية المصفوفة باستخدام سمتي `arrayasSingle` و`extraDelimiter`.
3. **إنشاء WorkbookDesigner**: أنشئ كائن `WorkbookDesigner`، وأرفق مصنف التصميم به، واربط مصدر البيانات باستخدام الطريقة `setDataSource`.
4. **معالجة العلامات**: استدعِ الطريقة `workbookDesigner.process()` لتوسيع العلامات الذكية وملء المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي صيغة ملف مدعومة أخرى.

### **مثال على التعليمات البرمجية 1 — العرض الأساسي لمصفوفة سلاسل نصية**

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
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **مثال على التعليمات البرمجية 2 — مصفوفة رقمية مع فاصل مخصص**

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
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // القسم 1: العلامة الذكية الافتراضية - يتم توزيع القيم أفقيًا عبر الخلايا
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // القسم 2: العرض في خلية واحدة باستخدام arrayasSingle وextraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // ربط مصدر البيانات ومعالجة العلامات الذكية
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // حفظ مصنف العمل الناتج
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **مثال على التعليمات البرمجية 3 — مقارنة السلوك الافتراضي بسلوك ArrayAsSingle**

### **ملاحظات وأفضل الممارسات**
عند العمل مع سمتي `ArrayAsSingle` و`ExtraDelimiter`، ضع النقاط التالية في الاعتبار:
- تُعامل قيمة `extraDelimiter` على أنها سلسلة نصية حرفية؛ استخدم محارف الهروب لأي محارف خاصة قد يفسّرها معالج القالب.
- تقبل السمة `arrayasSingle` قيمة منطقية، `true` / `false`. ولا يُفعّل سلوك الخلية الواحدة إلا `true`؛ وتعود أي قيمة أخرى إلى سلوك التوزيع الافتراضي.
- إذا كانت المصفوفة فارغة أو `null`، تُترك الخلية فارغة، أو تحتوي على سلسلة نصية فارغة بحسب نوع البيانات.
- تعمل الميزة مع مصادر بيانات كائنية، وكذلك مصادر بيانات جدولية يمكن فيها تحويل عمود إلى مصفوفات.
- لإخراج مفصول بأسطر جديدة، استخدم `\n` كقيمة للفاصل.

## مقالات ذات صلة
- [إضافة حقول تصفية إلى جدول محوري في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/javascript-cpp/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for JavaScript via C++](/cells/ar/javascript-cpp/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى صيغة OFD](/cells/ar/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}