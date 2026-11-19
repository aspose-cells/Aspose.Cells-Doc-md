---
title: عرض مصفوفة في خلية واحدة باستخدام SmartMarker | Aspose.Cells for Node.js via Java
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمات العلامة الذكية `arrayassingle` و`arraydelimiter` في Aspose.Cells for Node.js via Java.
linktitle: عرض مصفوفة SmartMarker في خلية واحدة
url: /ar/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, مكتبة Node.js عبر Java, جدول بيانات, العلامات الذكية, arrayassingle, arraydelimiter, مصفوفة في خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يمكن لـ Aspose.Cells عرض مصدر بيانات مصفوفة في خلية واحدة عبر العلامات الذكية. توقف السمة `arrayassingle` النشر الافتراضي عنصرًا تلو الآخر، وتحدد السمة `arraydelimiter` الفاصل الموضوع بين العناصر المدمجة — فاصلة افتراضيًا، أو أي حرف منفرد أو سلسلة متعددة الأحرف بين علامتَي اقتباس تحددها.
{{% /alert %}}

## **مقدمة**

تعد العلامات الذكية في Aspose.Cells ميزة قائمة على القوالب تملأ بيانات الجداول ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. توضع العلامة في مصنف تصميم، وعندما تتم معالجة القالب بواسطة `WorkbookDesigner`، تُستبدل العلامات بالقيم من مصدر البيانات المزوَّد.
افتراضيًا، عندما تشير علامة ذكية إلى حقل مصفوفة، مثل `&=Product.Tags` المرتبط بمصفوفة تضم أربع قيم، يوسع المحرك المصفوفة ويضع كل عنصر في خلية خاصة به، مبثوثًا القيم رأسيًا إلى أسفل العمود أسفل العلامة. ورغم أن هذا السلوك مريح في سيناريوهات كثيرة، هناك مواقف تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج العناصر وفصلها بفاصل تختاره.
تقدم السمات `arrayassingle` و`arraydelimiter`، المكتوبة داخل أقواس العلامة الذكية بصيغة `name:value`، حلًا مباشرًا لهذا المتطلب. تتيح لك الحفاظ على تخطيطات التقارير مضغوطة ومتوقعة مع الاستمرار في العمل أصلًا مع مصادر بيانات المصفوفات.

## **لماذا هذه الميزة مطلوبة**

### **سلوك نشر المصفوفات الافتراضي**

عندما تشير علامة ذكية إلى حقل مصفوفة، يوسع Aspose.Cells المصفوفة افتراضيًا عبر خلايا متعددة. على سبيل المثال، تضع علامة مثل `&=Product.Tags`، عند تطبيقها على مصفوفة تحتوي على أربع قيم، كل قيمة في خلية خاصة أسفل العلامة، مما يدفع بقية محتوى القالب إلى الخارج وقد يؤدي إلى كسر تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

توجد سيناريوهات عملية كثيرة يكون فيها سلوك النشر الافتراضي غير مرغوب فيه:
- **تقارير بأسلوب الملخص** التي تحتاج إلى تخطيط مضغوط من صف واحد لكل سجل.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية** التي يلزم عرضها كقيم مفصولة بفواصل أو خطوط أنابيب داخل خلية واحدة.
- **عناصر التصفية أو مؤشرات الحالة** التي تجمع قيمًا متعددة في موضع واحد لتسهيل القراءة.
- **خطوط المعالجة اللاحقة**، مثل تصدير CSV وعرض PDF ودمج البريد، التي تتوقع قيمة موحدة واحدة لكل خلية بدل نطاق موسّع.
- **التوافق عبر المنصات**، حيث لا يمكن لبعض الجهات المستهلكة التعامل مع مصفوفات ممتدة عبر خلايا متعددة.

### **الفجوة التي يسدها**

بدون آلية مدمجة، سيضطر المطورون إلى معالجة البيانات مسبقًا في JavaScript، بدمج المصفوفات في سلاسل ذات فواصل قبل ربطها بمصمم المصنف. يكرر هذا الأسلوب منطقًا، ويعقد نماذج البيانات، ويزيد احتمال وقوع الأخطاء. وتلغي سمتا `arrayassingle` و`arraydelimiter` الحاجة إلى هذا الحل البديل عبر التعامل مع التنسيق بطريقة تعريفية داخل العلامة الذكية نفسها.

## **مزايا الميزة**

يوفر استخدام السمتين `arrayassingle` و`arraydelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء في خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على تخطيطات مضغوطة ومتوقعة.
- **التحكم في الفاصل المخصص**: حدد الفاصل الذي تفضله — الفاصلة الافتراضية، أو فاصلة منقوطة، أو شرطة، أو خط أنابيب، أو سلسلة متعددة الأحرف بين علامتَي اقتباس مثل `" | "`.
- **التنسيق المعتمد على القالب**: لا يلزم أي كود إضافي لمعالجة البيانات مسبقًا؛ فقواعد التنسيق موجودة داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع بمحتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدام**: يعمل مع مصفوفات السلاسل المزوَّدة كصفوف JSON، بما في ذلك القيم الرقمية المعروضة كنصوص.
- **التوافق مع الإصدارات السابقة**: عند حذف السمتين، يبقى سلوك النشر الأصلي كما هو، لذا تواصل القوالب الحالية العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صيغة العلامة الذكية**

تستخدم سمتا `arrayassingle` و`arraydelimiter` أسلوب سمات `name:value` الخاص بـ Aspose.Cells داخل أقواس علامة ذكية قياسية. الصيغة العامة هي:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayField` — العلامة الذكية القياسية التي تشير إلى حقل المصفوفة في مصدر البيانات المرتبط.
- `arrayassingle:true` — يوجه المحرك إلى عرض المصفوفة بأكملها في خلية واحدة بدل نشر عناصرها.
- `arraydelimiter:;` — اختيارية؛ تحدد الفاصل الموضوع بين عناصر المصفوفة. وعند حذفها، تُستخدم فاصلة.

{{% alert color="warning" %}}
اكتب السمات بصيغة `name:value` (نقطتان، لا علامة يساوي) وافصل بين السمات المتعددة بفاصلة **من دون مسافات**. تؤدي المسافة بعد الفاصلة إلى إزاحة القيمة المحلَّلة بمقدار حرف واحد — إذ ستدمج `(arrayassingle:true, arraydelimiter:;)` باستخدام الفاصل الخاطئ `:;` بدلًا من `;`.
{{% /alert %}}

### **أشكال الفاصل**

- يأتي الحرف المفرد مباشرة بعد النقطتين: `arraydelimiter:;`، `arraydelimiter:-`، `arraydelimiter:*`.
- يكتب الفاصل متعدد الأحرف بين علامتَي اقتباس مزدوجتين: `arraydelimiter:" | "`، `arraydelimiter:" - "`.

### **سير العمل خطوة بخطوة**

يوضح سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تهيئة مصدر البيانات**: نظّم كل سجل في صورة كائن JSON يحتوي حقله على مصفوفة، مثل `{"Tags": ["C#", "Aspose"]}`. لا يتم ربط كائنات ومصفوفات JavaScript العادية التي تمرر إلى `setDataSource` على هذه المنصة — صفوف JSON هي الصيغة الجدولية المدعومة.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف عنوان، وضع خلية علامة ذكية تشير إلى حقل المصفوفة مع السمة `arrayassingle` (و`arraydelimiter` عند الحاجة إلى فاصل مخصص).
3. **إنشاء WorkbookDesigner**: أنشئ `WorkbookDesigner` حول المصنف وأرفق صفوف JSON باستخدام `setJsonDataSource`.
4. **معالجة العلامات**: استدع الأسلوب `workbookDesigner.process()` لتوسيع العلامات الذكية وتعبئة المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي تنسيق ملف آخر مدعوم.

### **مثال برمجي 1 — العرض الأساسي لمصفوفة سلاسل**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

يطبع المثال القيمة المدمجة للمصفوفة بأكملها. تقع الوسوم الأربعة في خلية واحدة، مفصولة بفاصلة افتراضية:

```
C#,Aspose,SmartMarker,Excel
```

### **مثال برمجي 2 — القيم الرقمية مع فاصل مخصص**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

عند توفير الدرجات كسلاسل JSON، تحافظ النتيجة المدمجة على الأرقام دون تنسيق:

```
95-88-76-100-67
```

{{% alert color="note" %}}
تصل أرقام JSON الممررة عبر محرك Java كأعداد مزدوجة، لذا يدمج `[95, 88]` على هيئة `95.0-88.0`. ضع الأرقام بين علامتَي اقتباس في صفوف JSON عندما تريد نص الأعداد الصحيحة كما هو في الخلية المدمجة.
{{% /alert %}}

### **مثال برمجي 3 — مقارنة العرض الافتراضي بالعرض في خلية واحدة**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

تملأ العلامة الافتراضية خلية واحدة لكل عنصر في العمود B، بينما تجمع علامة `arrayassingle` المصفوفة نفسها في خلية واحدة في العمود C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في الاعتبار عند العمل مع السمتين `arrayassingle` و`arraydelimiter`:
- تستخدم قيم السمات صيغة `name:value`. ولا يتم التعرف على صيغة علامة يساوي مثل `arrayassingle=true`، بل يعود بصمت إلى سلوك النشر الافتراضي.
- افصل السمات بفاصلة ومن دون مسافات؛ فالمسافة بعد الفاصلة تزيح قيمة الفاصل بمقدار حرف واحد، كما ورد في التحذير أعلاه.
- قد تكون قيمة `arraydelimiter` حرفًا مفردًا مكتوبًا مباشرة بعد النقطتين، أو سلسلة متعددة الأحرف مغلقة بعلامتَي اقتباس مزدوجتين.
- عند حذف `arraydelimiter`، تُدمج العناصر بفاصلة.
- وفّر حقول المصفوفة عبر كائنات صفوف `setJsonDataSource`؛ فكائنات ومصفوفات JavaScript العادية التي تمرر إلى `setDataSource` لا يتم ربطها على هذه المنصة.
- تصل أرقام JSON كأعداد مزدوجة عبر محرك Java (`95` يُدمج على هيئة `95.0`)؛ ضع القيم الرقمية بين علامتَي اقتباس في صفوف JSON عندما يكون نص الأعداد الصحيحة الدقيق مهمًا.
- ضع العلامة الذكية في خلية ذات عرض كافٍ لعرض السلسلة المدمجة الناتجة؛ وإلا فقد يفيض المحتوى بصريًا إلى الخلايا المجاورة، وفقًا على التنسيق.

## المقالات ذات الصلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/nodejs-java/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Node.js via Java](/cells/ar/nodejs-java/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}