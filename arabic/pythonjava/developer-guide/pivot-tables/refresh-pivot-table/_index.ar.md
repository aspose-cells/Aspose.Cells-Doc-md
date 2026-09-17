---
title: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Python via Java
linktitle: تحديث الجداول المحورية وذواكر التخزين المؤقت في Aspose.Cells for Python via Java
description: تعرف على كيفية تحديث الجداول المحورية في Aspose.Cells for Python via Java باستخدام واجهة برمجة التطبيقات للتحديث في الإصدار v26.7+. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Python via Java, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
توفر Aspose.Cells واجهة برمجة تطبيقات للتحديث متعددة الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري في أربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Python via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.refreshData()` على أنها مهجورة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والواعية بذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}

## المقدمة
نادرًا ما تكون عملية تحديث الجدول المحوري عملية واحدة. خلف الكواليس، تحافظ Aspose.Cells على سلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو مفتاح اختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.
سلسلة البيانات ذات الأربع طبقات هي:
1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. كل جدول محوري مبني فوق `PivotCache`؛ هذا هو المكان الذي يتم فيه جمع جميع البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرة من مصدر البيانات.
4. **Cells** — `Cells` ورقة العمل التي يعرض فيها `PivotTable` القيم والأنماط المحسوبة.

{{% alert color="primary" %}}
يشير `PivotCache.getSourceType()` (تعداد `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.refresh()` فقط أنواع المصادر **`SHEET`** و **`CONSOLIDATION`** — أي البيانات الموجودة في نطاقات ورقة العمل. لا يمكن تحديث المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) من خلال واجهة برمجة تطبيقات ذاكرة التخزين المؤقت حتى الآن.
{{% /alert %}}

بسبب هذه السلسلة، يوجد مسارا تحديث أساسيان في Aspose.Cells:
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون رحلة ذهاب وإياب إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات المصدر من خلايا ورقة العمل، لذا فإن نوع المصدر هو `SHEET` وتعمل عمليات التحديث كما هو موضح.

## البدء السريع
إذا كنت تحتاج فقط إلى أقصر كود ممكن يحدث كل جدول محوري في المصنف، فإن مكالمة واحدة تكفي:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
# إنشاء مصنف جديد
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# كتابة صف الرأس في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر عامي 2020 و 2021)
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(50)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(60)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(70)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(80)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(90)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(100)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(110)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(120)
# إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)
# تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refreshAll()
# حفظ المصنف
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

يشرح كل شيء آخر في هذه المقالة متى تختار واجهة برمجة تطبيقات أضيق بدلاً من ذلك.

## الاستيرادات المطلوبة
تعتمد جميع أمثلة Python في هذه المقالة على الاستيرادات التالية لأن أنواع الجداول المحورية توجد في مساحة الاسم `aspose.cells.pivot`:
- `import jpype`
- `import aspose.cells as cells`
تُستخدم وحدة `jpype` لتشغيل JVM، بينما تعرض `aspose.cells` أنواع المصنف/ورقة العمل/الخلية/الجدول المحوري المستخدمة في جميع أنحاء المقالة.

## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.refreshAll()`. تتنقل مكالمة واحدة عبر المصنف بأكمله — تحدث كل `PivotCache` من مصدرها ثم تعيد حساب كل `PivotTable` تابع. هذا هو الأسلوب الموصى به للتحديثات العامة للوثيقة بأكملها عندما لا يكون الأداء موضع قلق.
يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `refreshAll()` لجلب كل شيء محدّثًا في مكالمة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("blueberry")
worksheet.getCells().get("B3").putValue(2021)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("cherry")
worksheet.getCells().get("B5").putValue(2021)
worksheet.getCells().get("C5").putValue(120)
worksheet.getCells().get("A6").putValue("grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(180)
worksheet.getCells().get("A7").putValue("blueberry")
worksheet.getCells().get("B7").putValue(2020)
worksheet.getCells().get("C7").putValue(130)
worksheet.getCells().get("A8").putValue("kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(220)
worksheet.getCells().get("A9").putValue("cherry")
worksheet.getCells().get("B9").putValue(2020)
worksheet.getCells().get("C9").putValue(140)
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
worksheet.getCells().get("C2").putValue(300)
worksheet.getCells().get("C5").putValue(250)
worksheet.getCells().get("C9").putValue(400)
worksheet.refreshPivotTables()
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة
في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية التي تعيش في ورقة عمل محددة واحدة — على سبيل المثال، عندما تكون الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، توفر Aspose.Cells `Worksheet.refreshPivotTables()`، والتي تكون محصورة في مثيل `Worksheet` واحد.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# كتابة 8 صفوف من البيانات (الصفوف 2-9، بحيث تتطابق مع نطاق المصدر A1:C9)
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(150)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(250)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(350)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(450)
# إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ومصدره A1:C9
pivotIndex = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# تعيين الحقول: Fruit إلى الصف، Year إلى العمود، Amount إلى البيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# تعديل خاصية عرض/تخطيط — هذا تغيير خاص بالعرض فقط،
# لذلك لا يتطلب إعادة قراءة البيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)
# تقوم calculateData() بإعادة عرض جدول المحوري هذا (البيانات + النمط) من
# البيانات الموجودة بالفعل في PivotCache. ولأن البيانات المصدر لم تتغير،
# لا يتم إجراء أي جولة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
# في خلايا ورقة العمل.
pivotTable.calculateData()
# حفظ المصنف على القرص
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## تحديث جدول محوري واحد
عندما تريد تحكمًا دقيقًا في جدول محوري واحد، فإن واجهة برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت تمنحك خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.

### تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`
إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على تلك السلية.

### تغير العرض/التخطيط فقط — استخدم `calculateData()`
إذا كانت بيانات المصدر *لم* تتغير ولكن تم تعديل إعدادات عرض أو تخطيط الجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة حساب. في هذه الحالة، `pivotTable.calculateData()` هو الخيار الصحيح.
يعدل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
غالبًا ما يحتوي المصنف على جداول محورية متعددة كلها تستند إلى ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث مجمع، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.getPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

## الانتقال من `PivotTable.refreshData()` المهجور
قبل Aspose.Cells for Python via Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري على حدة. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة على أنها **مهجورة** ويجب استبدالها بواجهات برمجة التطبيقات الواعية بذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعل أسلوب `refreshData()` لكل جدول إشكاليًا في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها، حتى عندما لم يتغير المصدر.
البدائل الموصى بها هي:
يوضح المثال التالي النمط الفعّال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت واحدة.

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | مكالمة واحدة؛ تغطي كل ذواكر التخزين المؤقت والجداول. |
| تحديث الجداول المحورية فقط في ورقة واحدة | `Worksheet.refreshPivotTables()` | محصور في ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدث كل الجداول المحورية على ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتخطى رحلة المصدر غير الضرورية. |
| سرد كل الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدم للتعداد قبل التحديث المجمع. |
عمليًا، فضّل واجهات برمجة التطبيقات القائمة على ذاكرة التخزين المؤقت على `refreshData()` المهجور لكل جدول. إنها واعية بذواكر التخزين المؤقت المشتركة، وتتجنب جلب المصدر الزائد عن الحاجة، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.

## الأخطاء الشائعة
- **نسيان التحديث قبل الحفظ.** لا يكتب الجدول المحوري قيمه المعروضة في ورقة العمل إلا عند تحديث سلسلة البيانات الخاصة به. إذا قمت بتعديل خلايا المصدر، فاستدعِ `PivotCache.Refresh()` (أو `Workbook.RefreshAll()`) قبل `Workbook.save()`، وإلا فإن الملف المحفوظ لا يزال يحتوي على القيم المجمعة القديمة.
- **استدعاء `RefreshData()` المهجور لكل جدول.** في الإصدار v26.7، تم وضع علامة `PivotTable.RefreshData()` على أنها مهجورة وتعيد جلب المصدر لكل مكالمة. مع الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت، يعني هذا جلب المصدر N مرة بشكل زائد عن الحاجة. استبدل بمكالمة `PivotCache.Refresh()` واحدة متبوعة بـ `CalculateData()` لكل جدول.
- **التحديث عند تغير التخطيط فقط.** إذا قمت فقط بتغيير عرض الجدول المحوري (ترتيب الأعمدة، `ConsolidationFunction`، إلخ) دون لمس بيانات المصدر، فإن `PivotCache.Refresh()` غير ضروري وبطيء. استدعِ `pivotTable.CalculateData()` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة.
- **المصدر الخارجي غير مدعوم من قبل `PivotCache.Refresh()`.** إذا كان مصدر الجدول المحوري يأتي من اتصال خارجي (قاعدة بيانات، مكعب OLAP، إلخ)، فلا يمكن لـ `PivotCache.Refresh()` تحديثه في الإصدار v26.7 — فهو يدعم حاليًا فقط أنواع مصادر `Sheet` و `Consolidation`. بالنسبة للمصادر الخارجية، أعد فتح المصنف أو أعد بناء ذاكرة التخزين المؤقت من المصدر.

```csharp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

{{< app/cells/assistant language="python" >}}