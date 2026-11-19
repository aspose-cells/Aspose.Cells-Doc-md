---
title: عرض مصفوفة SmartMarker في خلية واحدة | Aspose.Cells for Python عبر Java
linktitle: عرض مصفوفة SmartMarker في خلية واحدة | Aspose.Cells for Python عبر Java
description: تعلم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمات العلامات الذكية arrayassingle وarraydelimiter في Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, مكتبة Python عبر Java, جدول بيانات, العلامات الذكية, arrayassingle, arraydelimiter, مصفوفة في خلية واحدة, عرض المصفوفة, قالب
type: docs
weight: 195
url: /ar/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يمكن لـ Aspose.Cells عرض مصدر بيانات من نوع مصفوفة في خلية واحدة عبر العلامات الذكية. توقف سمة `arrayassingle` التوزيع الافتراضي للعناصر منفردةً، وتحدد سمة `arraydelimiter` الفاصل المستخدم بين العناصر المدمجة، وهو الفاصلة افتراضيًا، أو أي حرف مفرد أو سلسلة متعددة الأحرف بين علامتَي اقتباس تحددها.
{{% /alert %}}

## **مقدمة**
تمثل العلامات الذكية في Aspose.Cells ميزة قائمة على القوالب، تُستخدم لتعبئة بيانات الجداول ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. توضع العلامة في مصنف مصمم، وعند معالجة القالب بواسطة `WorkbookDesigner`، تُستبدل العلامات بالقيم الواردة من مصدر البيانات المقدم.
افتراضيًا، عندما تشير علامة ذكية إلى حقل مصفوفة، مثل `&=Product.Tags` المرتبط بقائمة تضم أربع قيم، يوسع المحرك المصفوفة ويضع كل عنصر في خلية مستقلة، موزعًا القيم عموديًا في العمود أسفل العلامة. ورغم أن هذا السلوك مريح في السيناريوهات العديدة، توجد حالات تفضل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج العناصر وفصلها بفاصل تختاره.
تستهدف سمتا `arrayassingle` و`arraydelimiter`، المكتوبتان داخل أقواس العلامة الذكية بصيغة `name:value`، هذا المتطلب تحديدًا. تتيح لك الحفاظ على تخطيطات التقارير مدمجة ومتوقعة، مع الاستمرار في العمل مباشرةً مع مصادر بيانات المصفوفات.

## **الحاجة إلى هذه الميزة**

### **سلوك توزيع المصفوفة الافتراضي**
عندما تشير علامة ذكية إلى حقل مصفوفة، يوزع Aspose.Cells المصفوفة على خلايا متعددة افتراضيًا. على سبيل المثال، عند ربط علامة مثل `&=Product.Tags` بقائمة تضم أربع قيم، يضع كل عنصر في خلية مستقلة أسفل العلامة، مما يؤدي إلى إزاحة محتوى القالب الآخر وقد يعطل تخطيطات التقارير المصممة بعناية.

### **حدود حالات الاستخدام**
توجد سيناريوهات عملية كثيرة يكون فيها سلوك التوزيع الافتراضي غير مرغوب فيه:
- **تقارير بأسلوب الملخص** التي تحتاج إلى تخطيط مضغوط بسجل واحد في كل صف.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية** التي يجب عرضها كقيم مفصولة بفواصل أو بالشرطة العمودية داخل خلية واحدة.
- **شارات التصفية أو مؤشرات الحالة** التي تجمع عدة قيم في موضع واحد لتسهيل القراءة.
- **خطوط المعالجة اللاحقة**، مثل تصدير CSV وعرض PDF ودمج البريد، التي تتوقع قيمة موحدة واحدة لكل خلية بدلًا من نطاق موسّع.
- **التوافق عبر المنصات**، حيث لا يمكن لبعض التطبيقات المستهلكة التعامل مع مصفوفات تمتد عبر خلايا متعددة.

### **الفجوة التي يسدها**
بدون آلية مدمجة، سيضطر المطورون إلى المعالجة المسبقة للبيانات في Python، أي دمج القوائم في سلاسل مفصولة قبل ربطها بمصمم المصنف. يعيد هذا الأسلوب تنفيذ منطق المعالجة، ويعقد نماذج البيانات، ويزيد احتمال وقوع الأخطاء. وتُغني سمتا `arrayassingle` و`arraydelimiter` عن هذا الحل البديل عبر تنفيذ التنسيق بشكل إعلاني داخل العلامة الذكية نفسها.

## **مزايا الميزة**
يوفر استخدام سمتَي `arrayassingle` و`arraydelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء في خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على تخطيطات مدمجة ومتوقعة.
- **التحكم في الفاصل المخصص**: حدد الفاصل الذي تفضله، سواء كان الفاصلة الافتراضية أو الفاصلة المنقوطة أو الشرطة أو الشرطة العمودية أو سلسلة متعددة الأحرف بين علامتَي اقتباس مثل `" | "`.
- **التنسيق القائم على القالب**: لا يلزم كتابة أي كود إضافي للمعالجة المسبقة للبيانات؛ إذ تُعرَّف قواعد التنسيق داخل وسم العلامة الذكية.
- **تقارير أوضح**: لم تعد بيانات المصفوفة تزيح محتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **مرونة أنواع البيانات**: تعمل مع مصفوفات النصوص المقدمة في صفوف JSON، بما في ذلك القيم الرقمية المعروضة في صورة نصوص.
- **التوافق مع الإصدارات السابقة**: عند عدم تحديد السمتين، يبقى سلوك التوزيع الأصلي كما هو، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **صياغة العلامة الذكية**
تستخدم سمتا `arrayassingle` و`arraydelimiter` صيغة السمات `name:value` الخاصة بـ Aspose.Cells داخل أقواس العلامة الذكية القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

تتكوّن العلامة من الأجزاء التالية:
- `&=DataSource.ArrayField` — العلامة الذكية القياسية التي تشير إلى حقل المصفوفة في مصدر البيانات المرتبط.
- `arrayassingle:true` — يخبر المحرك بعرض المصفوفة بالكامل في خلية واحدة بدلًا من توزيع عناصرها.
- `arraydelimiter:;` — اختياري؛ يحدد الفاصل المستخدم بين عناصر المصفوفة. عند عدم تحديده، تُستخدم الفاصلة.

{{% alert color="warning" %}}
اكتب السمات بصيغة `name:value`، أي باستخدام نقطتين لا علامة يساوي، وافصل السمات المتعددة بفاصلة **من دون مسافات**. تزيح المسافة التالية للفاصلة القيمة المحللة بمقدار حرف واحد؛ لذا سيؤدي `(arrayassingle:true, arraydelimiter:;)` إلى دمج العناصر باستخدام الفاصل الخاطئ `:;` بدلًا من `;`.
{{% /alert %}}

### **صيغ الفاصل**
- تُكتب قيمة الحرف المفرد مباشرة بعد النقطتين: `arraydelimiter:;`، `arraydelimiter:-`، `arraydelimiter:*`.
- تُwritten قيمة الفاصل متعدد الأحرف بين علامتَي اقتباس مزدوجتين: `arraydelimiter:" | "`، `arraydelimiter:" - "`.

### **سير العمل خطوة بخطوة**
يوضح سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تجهيز مصدر البيانات**: نظّم كل سجل على هيئة كائن JSON يحتوي حقله على مصفوفة، مثل `{"Tags": ["C#", "Aspose"]}`. لا تُربط كائنات Python العادية أو القواميس الممرَّرة إلى `setDataSource` على هذه المنصة؛ أما الصفوف بصيغة JSON فهي الشكل الجدولي المدعوم.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف ترويسة، وضع خلية علامة ذكية تشير إلى حقل المصفوفة مع سمة `arrayassingle`، وإضافة `arraydelimiter` عند الحاجة إلى فاصل مخصص.
3. **إنشاء WorkbookDesigner**: أنشئ `WorkbookDesigner` مرتبطًا بالمصنف وأرفق صفوف JSON به باستخدام `setJsonDataSource`.
4. **معالجة العلامات**: استدعِ الأسلوب `WorkbookDesigner.process()` لتوسيع العلامات الذكية وملء المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو بأي تنسيق ملف آخر مدعوم.

### **مثال التعليمات البرمجية 1 — العرض الأساسي لمصفوفة نصوص**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-single.xlsx")
```

يطبع المثال القيمة المدمجة للمصفوفة بأكملها. توضع الوسوم الأربعة في خلية واحدة، مفصولة بفاصلة افتراضية:

```
C#,Aspose,SmartMarker,Excel
```

### **مثال التعليمات البرمجية 2 — القيم الرقمية مع فاصل مخصص**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Scores")
# arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]')
designer.process()
print(worksheet.getCells().get("A2").getStringValue())
workbook.save("output-array-numeric.xlsx")
```

عند تقديم الدرجات كسلاسل JSON، تحافظ النتيجة المدمجة على الأرقام كنص عادي:

```
95-88-76-100-67
```

{{% alert color="note" %}}
تصل أرقام JSON التي تمر عبر محرك Java بوصفها قيمًا مزدوجة، لذلك ستُدمج `[95, 88]` بوصفها `95.0-88.0`. ضع الأرقام بين علامتَي اقتباس في صفوف JSON عندما تريد نص الأعداد الصحيحة كما هو في الخلية المدمجة.
{{% /alert %}}

### **مثال التعليمات البرمجية 3 — مقارنة العرض الافتراضي بالعرض في خلية واحدة**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, WorkbookDesigner
workbook = Workbook()
cells = workbook.getWorksheets().get(0).getCells()
# Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default")
cells.get("B2").putValue("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell")
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)")
designer = WorkbookDesigner(workbook)
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).getStringValue() or ""
    c = cells.get(row, 2).getStringValue() or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

تملأ العلامة الافتراضية خلية واحدة لكل عنصر في العمود B، بينما تدمج علامة `arrayassingle` المصفوفة نفسها في خلية واحدة في العمود C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **ملاحظات وأفضل الممارسات**
ضع النقاط التالية في الاعتبار عند العمل مع سمتَي `arrayassingle` و`arraydelimiter`:
- تستخدم قيم السمات صيغة `name:value`. لا يتعرف النظام على صيغة علامة يساوي مثل `arrayassingle=true`، ويعود بصمت إلى سلوك التوزيع الافتراضي.
- افصل السمات بفاصلة ومن دون مسافات؛ فالمسافة بعد الفاصلة تزيح قيمة الفاصل بمقدار حرف واحد. راجع التحذير أعلاه.
- قد تكون قيمة `arraydelimiter` حرفًا مفردًا يُكتب مباشرة بعد النقطتين، أو سلسلة متعددة الأحرف محاطة بعلامتَي اقتباس مزدوجتين.
- عند عدم تحديد `arraydelimiter`، تُدمج العناصر بفاصلة.
- مرّر حقول المصفوفة ضمن كائنات الصفوف التي يتم تمريرها إلى `setJsonDataSource`؛ ولا تُربط كائنات Python العادية أو القواميس الممرَّرة إلى `setDataSource` على هذه المنصة.
- تصل أرقام JSON عبر محرك Java بوصفها قيمًا مزدوجة؛ يُدمج `95` بوصفه `95.0`. ضع القيم الرقمية بين علامتَي اقتباس في صفوف JSON عندما يكون تمثيل الأعداد الصحيحة الدقيق مهمًا.
- ضع العلامة الذكية في خلية تتمتع بعرض كافٍ لعرض السلسلة المدمجة الناتجة؛ وإلا، فقد يمتد المحتوى بصريًا إلى الخلايا المجاورة، وذلك يعتمد على تنسيق الملف.

## المقالات ذات الصلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells for Python عبر Java](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python عبر Java](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تعديل تخطيط حقول الصفحات في الجدول المحوري](/cells/ar/python-java/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python عبر Java](/cells/ar/python-java/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/python-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python" >}}