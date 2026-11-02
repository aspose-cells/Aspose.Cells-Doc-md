---
title: قراءة ملفات DBF وكتابتها
linktitle: قراءة ملفات DBF وكتابتها
description: Aspose.Cells هي مكتبة JavaScript عبر C++ للعمل مع ملفات جداول البيانات، وتدعم قراءة ملفات dBASE III وdBASE IV (DBF) وكتابتها. توضح هذه المقالة كيفية استيراد البيانات من ملفات DBF وتصديرها إليها باستخدام Aspose.Cells، بما في ذلك تفاصيل تنسيق الملف والميزات المدعومة وأمثلة خطوة بخطوة.
keywords: Aspose.Cells, مكتبة JavaScript عبر C++, DBF, dBASE, قراءة DBF, كتابة DBF, استيراد DBF, تصدير DBF, تنسيق الملف, .dbf
type: docs
weight: 200
url: /ar/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells دعمًا كاملًا لقراءة ملفات DBF (dBASE) وكتابتها. يمكنك تحميل ملفات dBASE III وdBASE IV الحالية إلى كائن `Workbook`، ومعالجة البيانات باستخدام API الغني في Aspose.Cells، ثم إعادة حفظ المصنف بتنسيق DBF لاستخدامه مع تطبيقات قواعد البيانات القديمة.
{{% /alert %}}

## **مقدمة**
DBF (ملف قاعدة البيانات) هو تنسيق ملف لقواعد البيانات قديم قدمته dBASE في مطلع الثمانينيات. وعلى الرغم من قدم هذا التنسيق، لا تزال ملفات DBF مستخدمة على نطاق واسع في قطاعات متعددة لتخزين البيانات المنظمة، ولا سيما في المحاسبة وأنظمة المعلومات الجغرافية (GIS) والتطبيقات المتخصصة الأخرى. تتيح لك Aspose.Cells دمج هذه الملفات القديمة بسلاسة في سير عمل جداول البيانات الحديثة.
تدعم المكتبة قراءة ملفات DBF وكتابتها، مما يمنحك القدرة على:
- استيراد البيانات من ملفات DBF الحالية إلى كائنات `Workbook` في Aspose.Cells لمزيد من المعالجة أو التحويل إلى تنسيقات أخرى.
- إنشاء ملفات DBF جديدة من الصفر أو من خلال تحويل البيانات من تنسيقات جداول بيانات أخرى.
- الحفاظ على تعريفات الحقول وأنواع البيانات وبنى السجلات عند نقل البيانات من وإلى تنسيق DBF.
يمكن أيضًا فتح ملفات DBF مباشرةً في Microsoft Excel وتطبيقات جداول البيانات الأخرى، مما يجعلها جسرًا مريحًا بين الأنظمة القديمة وأدوات جداول البيانات الحديثة.

## **إصدارات DBF والميزات المدعومة**
تدعم Aspose.Cells إصدارات تنسيق DBF التالية:
- **dBASE III** — النسخة الأصلية والأكثر دعمًا من تنسيق DBF.
- **dBASE IV** — إصدار موسع يدعم أنواع بيانات إضافية وأحجام حقول أكبر.

### الميزات المدعومة
توفر المكتبة دعمًا شاملًا للعمليات التالية:
- قراءة بيانات DBF إلى كائن `Workbook` مع الحفاظ على جميع السجلات وتعريفات الحقول.
- إعادة كتابة بيانات المصنف بتنسيق DBF لتصديرها إلى تطبيقات متوافقة مع dBASE.
- معالجة أنواع البيانات الشائعة المستخدمة في ملفات DBF، بما في ذلك حقول الأحرف والأرقام والتواريخ والمنطقية.
- الحفاظ على تعريفات الحقول مثل اسم الحقل ونوعه وطوله أثناء عمليات القراءة والكتابة.

### القيود والاعتبارات
عند العمل مع ملفات DBF، ضع القيود التالية في الاعتبار:
- الحد الأقصى لعدد الحقول في كل ملف هو **128**.
- الحد الأقصى لحجم السجل هو **4000 بايت**.
- تقتصر أسماء الحقول على **10 أحرف**، ويجب أن تكون بالأحرف الكبيرة، ولا يمكن أن تحتوي على مسافات.
- تُخزن قيم التاريخ في ملفات DBF بتنسيق `YYYYMMDD`.
- قد يختلف ترميز الأحرف حسب التطبيق المصدر (وغالبًا ما يكون Windows-1252 أو إحدى صفحات الترميز OEM).

## **قراءة ملف DBF**
يتيح لك Aspose.Cells تحميل البيانات من ملف DBF إلى كائن `Workbook` بسهولة. تستخدم المكتبة فئة `LoadOptions` لتحديد تنسيق المصدر، مما يضمن تفسير البيانات بشكل صحيح أثناء عملية التحميل.

### قراءة ملف DBF باستخدام Aspose.Cells
لقراءة ملف DBF، عليك إنشاء كائن `LoadOptions`، وتعيين الخاصية `loadFormat` فيه إلى `LoadFormat.Dbf`، ثم تمريرها إلى مُنشئ `Workbook` مع مسار الملف. وبمجرد التحميل، تصبح البيانات متاحة عبر مجموعة `Worksheets`، حيث يمكنك المرور على الخلايا واستخراج القيم أو معالجة البيانات حسب الحاجة.
يوضح المثال التالي كيفية تحميل ملف DBF موجود إلى Aspose.Cells، والوصول إلى ورقة العمل الأولى فيه، وقراءة قيم الخلايا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
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
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
يمكنك فتح ملفات DBF مباشرةً في Microsoft Excel عن طريق تحديد الملف في مربع حوار الفتح. سيتعامل Excel مع ملف DBF على أنه جدول بيانات، ويعرض سجلاته في تخطيط جدولي. ويكون هذا مفيدًا للتحقق السريع من البيانات بعد قراءتها أو كتابتها باستخدام Aspose.Cells.
{{% /alert %}}

## **كتابة ملف DBF**
تتبع كتابة البيانات إلى ملف DBF نمطًا مشابهًا لحفظ أي تنسيق آخر لجداول البيانات باستخدام Aspose.Cells. تنشئ كائن `Workbook` أو تحمّله، ثم تملأ ورقة العمل بالبيانات، ثم تستدعي الطريقة `save` مع تحديد `SaveFormat.Dbf` كتنسيق الهدف.

### كتابة ملف DBF باستخدام Aspose.Cells
لإنشاء ملف DBF، اتبع الخطوات التالية:
1. أنشئ نسخة جديدة من `Workbook`.
2. احصل على ورقة العمل الأولى من مجموعة `Worksheets`.
3. املأ ورقة العمل ببياناتك، بما في ذلك الرؤوس في الصف الأول والسجلات في الصفوف التالية.
4. استدعِ طريقة `Workbook.save`، مع تمرير مسار الملف و`SaveFormat.Dbf` كمعاملين.
يوضح المثال التالي كيفية إنشاء ملف DBF جديد من الصفر. يملأ ورقة العمل ببيانات نموذجية تحتوي على أنواع بيانات مختلفة، مثل النصوص والأرقام والتواريخ، لتوضيح كيفية التعامل مع أنواع الحقول عند التصدير إلى تنسيق DBF.

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
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
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
            // رؤوس الأعمدة
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // الصف الأول من البيانات
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // الصف الثاني من البيانات
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // الصف الثالث من البيانات
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // الصف الرابع من البيانات
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // الصف الخامس من البيانات
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // تعيين عرض الأعمدة لتحسين سهولة القراءة
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
عند كتابة البيانات إلى ملف DBF، تأكد من توافق بياناتك مع قيود هذا التنسيق. يجب ألا يزيد طول أسماء الحقول على 10 أحرف، ويجب ألا تحتوي على مسافات. لن يتم حفظ السجلات التي يتجاوز حجمها الإجمالي 4000 بايت بشكل صحيح. يجب أن تكون التواريخ قيم تاريخ صالحة يمكن تمثيلها بتنسيق YYYYMMDD.
{{% /alert %}}

## **اعتبارات أنواع البيانات والتنسيق**
عند نقل البيانات بين Aspose.Cells وتنسيق DBF، من المهم فهم كيفية تعيين أنواع البيانات بين النظامين لضمان سلامة البيانات.

### تعيين أنواع الخلايا إلى أنواع حقول DBF
تُحوَّل قيم خلايا Aspose.Cells تلقائيًا إلى أنواع حقول DBF المناسبة عند الحفظ:
- تُعيَّن **النصوص** إلى حقول الأحرف (`C`).
- تُعيَّن **القيم الرقمية**، بما في ذلك الأعداد الصحيحة والعشرية، إلى حقول الأرقام (`N`).
- تُعيَّن **قيم التاريخ** إلى حقول التاريخ (`D`) بتنسيق `YYYYMMDD`.
- تُعيَّن **القيم المنطقية** إلى حقول منطقية (`L`).

### الترميز
قد تستخدم ملفات DBF ترميزات أحرف مختلفة حسب التطبيق الذي أنشأها. يتولى Aspose.Cells معالجة الترميز تلقائيًا في معظم الحالات، لكن إذا واجهت مشكلات في عرض الأحرف، فقد تحتاج إلى التحقق من ترميز الملف المصدر.

### قواعد أسماء الحقول
يجب أن تستوفي أسماء حقول DBF القواعد التالية:
- أقصى طول هو 10 أحرف.
- يجب أن تبدأ بحرف.
- لا يمكن أن تحتوي على مسافات أو أحرف خاصة.
- تُخزن بالأحرف الكبيرة بغض النظر عن حالة الأحرف المستخدمة في الإدخال.

### التحقق من الناتج
بعد كتابة ملف DBF، يمكنك التحقق من النتيجة عن طريق فتحه في Microsoft Excel أو أي تطبيق متوافق مع dBASE. يجب أن تظهر البيانات في تخطيط جدولي، مع أسماء الحقول رؤوسًا للأعمدة، وتكون السجلات معبأة وفقًا للبيانات التي قدمتها.

## **التحويل بين DBF والتنسيقات الأخرى**
من أكثر حالات الاستخدام العملية لقراءة ملفات DBF وكتابتها باستخدام Aspose.Cells هو تحويل البيانات بين تنسيق DBF وتنسيقات جداول البيانات الحديثة مثل XLSX وXLS وCSV. وبما أن Aspose.Cells يدعم مجموعة واسعة من التنسيقات، يمكنك بسهولة تحميل ملف DBF وإعادة حفظه بأي تنسيق مدعوم آخر، أو إجراء العملية العكسية.

{{< app/cells/assistant language="javascript-cpp" >}}