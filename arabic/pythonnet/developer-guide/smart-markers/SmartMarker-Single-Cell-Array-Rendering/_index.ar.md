---
title: عرض المصفوفات في خلية واحدة عبر العلامات الذكية | Aspose.Cells for Python via .NET
description: تعلّم كيفية عرض بيانات المصفوفة في خلية واحدة باستخدام سمتي arrayassingle وarraydelimiter للعلامات الذكية في Aspose.Cells for Python via .NET.
linktitle: عرض المصفوفات في خلية واحدة | Aspose.Cells
url: /ar/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, مكتبة Python عبر .NET, جدول بيانات, العلامات الذكية, arrayassingle, arraydelimiter, مصفوفة في خلية واحدة, عرض المصفوفات, قالب
type: docs
weight: 195
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يمكن لـ Aspose.Cells عرض مصدر بيانات مصفوفة في خلية واحدة عبر العلامات الذكية. تعطّل السمة `arrayassingle` النشر الافتراضي عنصرًا تلو الآخر، وتحدد السمة `arraydelimiter` الفاصل الموضوع بين العناصر المدمجة — الفاصلة افتراضيًا، أو أي محرف واحد أو سلسلة متعددة الأحرف بين علامتي اقتباس تحددها.
{{% /alert %}}

## **مقدمة**

تعد العلامات الذكية في Aspose.Cells ميزة قائمة على القوالب تملأ بيانات الجداول ديناميكيًا باستخدام تعبيرات العلامات مثل `&=DataSource.Field`. توضع العلامة في مصنف مصمم، وعند معالجة القالب بواسطة `WorkbookDesigner`، تُستبدل العلامات بالقيم من مصدر البيانات المزود.
افتراضيًا، عندما تشير العلامة الذكية إلى حقل مصفوفة، على سبيل المثال `&=Product.Tags` المرتبط بقائمة تضم أربع قيم، يوسّع المحرك المصفوفة ويضع كل عنصر في خلية خاصة به، بنشر القيم رأسيًا في العمود أسفل العلامة. ورغم أن هذا السلوك مريح في السيناريوهات كثيرة، هناك حالات تفضّل فيها عرض المصفوفة بأكملها في خلية واحدة، مع دمج عناصرها وفصلها بفاصل تختاره.
تتكامل سمتا `arrayassingle` و`arraydelimiter`، المكتوبتين داخل أقواس العلامة الذكية بصيغة `name:value`، مع هذا المتطلب تحديدًا. تتيح لك الحفاظ على تخطيطات التقارير مضغوطة ومتوقعة، مع الاستمرار في العمل بصورة أصلية مع مصادر بيانات المصفوفات.

## **لماذا تحتاج إلى هذه الميزة**

### **سلوك النشر الافتراضي للمصفوفات**

عندما تشير العلامة الذكية إلى حقل مصفوفة، يوسّع Aspose.Cells المصفوفة عبر خلايا متعددة افتراضيًا. على سبيل المثال، تضع علامة مثل `&=Product.Tags` مقابل قائمة تضم أربع قيم كل قيمة في خلية خاصة بها أسفل العلامة، مما يدفع بقية محتوى القالب إلى مواضع أخرى وقد يفسد تخطيطات التقارير المصممة بعناية.

### **قيود حالات الاستخدام**

توجد حالات عملية كثيرة يكون فيها سلوك النشر الافتراضي غير مرغوب فيه:
- **التقارير الملخصة**: تحتاج إلى تخطيط مضغوط بسجل واحد في كل صف.
- **قوائم الوسوم أو التسميات أو الكلمات المفتاحية**: يلزم عرضها كقيم مفصولة بفواصل أو بفاصل أنبوبي داخل خلية واحدة.
- **رقائق التصفية أو مؤشرات الحالة**: تجمع عدة قيم في موضع واحد لتسهيل القراءة.
- **خطوط المعالجة اللاحقة** (تصدير CSV، عرض PDF، دمج البريد): تتوقع قيمة موحدة واحدة لكل خلية بدلًا من نطاق موسع.
- **التوافق عبر المنصات**: لا يمكن لبعض الجهات المستهلكة التعامل مع مصفوفات تمتد عبر خلايا متعددة.

### **الفجوة التي تملؤها**

بدون آلية مدمجة، سيضطر المطورون إلى معالجة البيانات مسبقًا في Python، أي دمج القوائم في نصوص مفصولة قبل ربطها بـ `WorkbookDesigner`. يؤدي هذا إلى تكرار المنطق، وتعقيد نماذج البيانات، وزيادة احتمال حدوث الأخطاء. وتلغي سمتا `arrayassingle` و`arraydelimiter` الحاجة إلى هذه التحويلة عبر التعامل مع التنسيق بشكل تعريفي داخل العلامة الذكية نفسها.

## **فوائد الميزة**

يمنح استخدام سمتي `arrayassingle` و`arraydelimiter` في العلامات الذكية عدة مزايا:
- **الاحتواء في خلية واحدة**: تُعرض جميع عناصر المصفوفة في خلية واحدة بالضبط، مما يحافظ على تخطيطات مضغوطة ومتوقعة.
- **التحكم في الفاصل المخصص**: يمكنك تحديد الفاصل الذي تريده، سواء كانت الفاصلة الافتراضية أو فاصلة منقوطة أو شرطة أو فاصل أنبوبي أو سلسلة متعددة الأحرف بين علامتي اقتباس مثل `" | "`.
- **التنسيق القائم على القالب**: لا يلزم أي كود إضافي لمعالجة البيانات مسبقًا، فقواعد التنسيق موجودة داخل وسم العلامة الذكية.
- **تقارير أنظف**: لم تعد بيانات المصفوفة تدفع بمحتوى القالب المجاور إلى صفوف أو أعمدة مختلفة.
- **أنواع بيانات متعددة الاستخدامات**: يعمل مع قوائم النصوص وقوائم الأرقام التي تُقدَّم كصفوف JSON.
- **التوافق مع الإصدارات السابقة**: عند حذف السمتين، يبقى سلوك النشر الأصلي محفوظًا، لذا تستمر القوالب الحالية في العمل دون تغيير.

## **كيفية استخدام هذه الميزة**

### **بنية العلامة الذكية**

تستخدم سمتا `arrayassingle` و`arraydelimiter` أسلوب سمات `name:value` الخاص بـ Aspose.Cells داخل أقواس العلامة الذكية القياسية. الصيغة العامة هي:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

تتكون العلامة من الأجزاء التالية:
- `&=DataSource.ArrayField` — العلامة الذكية القياسية التي تشير إلى حقل المصفوفة في مصدر البيانات المرتبط.
- `arrayassingle:true` — يوجه المحرك إلى عرض المصفوفة بأكملها في خلية واحدة بدلاً من نشر عناصرها.
- `arraydelimiter:;` — اختياري؛ يحدد الفاصل الموضوع بين عناصر المصفوفة. عند حذفه، تُستخدم فاصلة.

{{% alert color="warning" %}}
اكتب السمات بصيغة `name:value` (نقطتان، لا علامة يساوي) وافصل بين السمات المتعددة بفاصلة **من دون مسافات**. المسافة التالية للفاصلة تُزيح القيمة المحللة بمقدار حرف واحد؛ فالتعبير `(arrayassingle:true, arraydelimiter:;)` يؤدي إلى الدمج باستخدام الفاصل الخاطئ `:;` بدلًا من `;`.
{{% /alert %}}

### **أشكال الفاصل**

- يأتي المحرف الواحد مباشرةً بعد النقطتين: `arraydelimiter:;`، `arraydelimiter:-`، `arraydelimiter:*`.
- يُكتب الفاصل متعدد الأحرف داخل علامتي اقتباس مزدوجتين: `arraydelimiter:" | "`، `arraydelimiter:" - "`.

### **سير العمل خطوة بخطوة**

يصف سير العمل التالي كيفية عرض مصفوفة في خلية واحدة باستخدام العلامات الذكية.
1. **تحضير مصدر البيانات**: رتّب كل سجل في صورة كائن JSON يحمل في حقله مصفوفة، على سبيل المثال `{"Tags": ["C#", "Aspose"]}`. لا ترتبط حقول المصفوفات على هذه المنصة بكائنات أصناف Python العادية أو بالقواميس أو القوائم التي يتم تمريرها إلى `set_data_source`، وتُعد صفوف JSON الشكل الجدولي المدعوم.
2. **إنشاء مصنف مصمم**: أنشئ `Workbook` جديدًا، وأضف صف عنوان، وضع خلية علامة ذكية تشير إلى حقل المصفوفة مع السمة `arrayassingle`، و`arraydelimiter` عند الحاجة إلى فاصل مخصص.
3. **إنشاء WorkbookDesigner**: أنشئ `WorkbookDesigner` حول المصنف وأرفق صفوف JSON باستخدام `set_json_data_source`.
4. **معالجة العلامات**: استدعِ الأسلوب `WorkbookDesigner.process()` لتوسيع العلامات الذكية وملء المصنف بالبيانات الفعلية.
5. **حفظ النتيجة**: احفظ المصنف الناتج على القرص بصيغة XLSX أو أي تنسيق ملف مدعوم آخر.

### **مثال التعليمات البرمجية 1 — العرض الأساسي لمصفوفة نصوص**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Tags")
# No spaces inside the parentheses: attributes are name:value pairs
worksheet.cells.get("A2").put_value("&=Product.Tags(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-single.xlsx")
```

يطبع المثال القيمة المدمجة للمصفوفة بأكملها. تقع الوسوم الأربعة في خلية واحدة مفصولة بفاصلة افتراضية:

```
C#,Aspose,SmartMarker,Excel
```

### **مثال التعليمات البرمجية 2 — مصفوفة رقمية بفاصل مخصص**

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Scores")
# arraydelimiter:- joins the numbers with a hyphen
worksheet.cells.get("A2").put_value("&=Student.Scores(arrayassingle:true,arraydelimiter:-)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Student",
    '[{"Scores": [95, 88, 76, 100, 67]}]')
designer.process()
print(worksheet.cells.get("A2").string_value)
workbook.save("output-array-numeric.xlsx")
```

تُدمج أرقام JSON تمامًا كما تُدمج النصوص، إذ يحتفظ كل عنصر بنصه الرقمي العادي:

```
95-88-76-100-67
```

### **مثال التعليمات البرمجية 3 — مقارنة العرض الافتراضي بالعرض في خلية واحدة**

```python
import aspose.cells as ac

workbook = ac.Workbook()
cells = workbook.worksheets[0].cells
# Column B: default marker — values spread vertically down the column
cells.get("B1").put_value("Default")
cells.get("B2").put_value("&=Order.Items")
# Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").put_value("Single cell")
cells.get("C2").put_value("&=Order.Items(arrayassingle:true)")
designer = ac.WorkbookDesigner(workbook)
designer.set_json_data_source(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]')
designer.process()
for row in range(1, 6):
    b = cells.get(row, 1).string_value or ""
    c = cells.get(row, 2).string_value or ""
    if b or c:
        print(f"B{row + 1}=[{b}]  C{row + 1}=[{c}]")
workbook.save("output-array-comparison.xlsx")
```

تملأ العلامة الافتراضية خلية واحدة لكل عنصر في العمود B، بينما تجمع علامة `arrayassingle` المصفوفة نفسها في خلية واحدة في العمود C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **ملاحظات وأفضل الممارسات**

ضع النقاط التالية في الاعتبار عند العمل مع سمتي `arrayassingle` و`arraydelimiter`:
- تستخدم قيم السمات صيغة `name:value`. لا يُتعرف على صيغة علامة يساوي مثل `arrayassingle=true`، ويعود التنفيذ بصمت إلى سلوك النشر الافتراضي.
- افصل السمات بفاصلة من دون مسافات؛ فالمسافة التالية للفاصلة تُزيح قيمة الفاصل بمقدار حرف واحد، راجع التحذير أعلاه.
- يمكن أن تكون قيمة `arraydelimiter` محرفًا واحدًا مكتوبًا مباشرة بعد النقطتين، أو سلسلة متعددة الأحرف محاطة بعلامتي اقتباس مزدوجتين.
- عند حذف `arraydelimiter`، تُدمج العناصر بفاصلة.
- وفّر حقول المصفوفة عبر كائنات الصفوف في `set_json_data_source`. لا ترتبط كائنات Python العادية والقواميس التي تُمرَّر إلى `set_data_source` على هذه المنصة، ويعرض `ICellsDataTable` المخصص الذي يُرجع عموده قائمة Python نص حاوية القائمة بدلًا من دمج عناصرها.
- تحتفظ أرقام JSON بصيغتها العادية كأعداد صحيحة في الناتج المدمج.

## المقالات ذات الصلة
- [إضافة حقول التصفية إلى جدول محوري في Aspose.Cells لـ .NET](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية في Aspose.Cells for Python via .NET](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تعديل تخطيط حقل الصفحة في الجدول المحوري](/cells/ar/python-net/change-page-field-layout/)
- [تحويل Sparkline إلى صورة وHTML في Aspose.Cells for Python via .NET](/cells/ar/python-net/convert-sparkline-to-image-and-html/)
- [تحويل Excel إلى تنسيق OFD](/cells/ar/python-net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="python-net" >}}