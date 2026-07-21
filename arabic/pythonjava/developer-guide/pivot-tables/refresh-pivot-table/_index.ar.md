---
title: تحديث الجداول المحورية في Aspose.Cells for Python via Java
linktitle: تحديث الجداول المحورية في Aspose.Cells for Python via Java
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Python via Java باستخدام واجهة برمجة التطبيقات للتحديث v26.7+. تتناول هذه المقالة RefreshAll وRefreshPivotTables وPivotCache.Refresh وCalculateData وGetPivotTables مع أمثلة عملية.
keywords: Aspose.Cells, Python via Java, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-java/refresh-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفر Aspose.Cells واجهة برمجة تطبيقات متعددة الطبقات للتحديث تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءًا من الإصدار **Aspose.Cells for Python via Java v26.7**، تم وضع علامة على الطريقة القديمة `PivotTable.refreshData()` باعتبارها مهجورة، ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والمدرِكة لذاكرة التخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

## المقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. في الخلفية، يحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات المناسبة للتحديث في أي موقف.

سلسلة البيانات المكونة من أربع طبقات هي:

1. **مصدر البيانات** — نطاقات أوراق العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق التجميع حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لبيانات المصدر. يُبنى كل جدول محوري فوق `PivotCache`؛ حيث يتم تجميع وتجميع جميع البيانات هنا.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` من `PivotCache` الخاص به *فقط*، وليس مباشرة من مصدر البيانات.
4. **الخلايا** — خلايا `Cells` في ورقة العمل التي يعرض فيها `PivotTable` قيمه وأنماطه المحسوبة.

من المفاهيم ذات الأهمية الخاصة **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيلًا واحدًا* من `PivotCache`. يمكن أن يشير `PivotCache` واحد إلى عدة جداول محورية، وتحديث ذاكرة التخزين المؤقت هذه يُحدث كل `PivotTable` تابع لها في وقت واحد.

{{% alert color="primary" %}}

يوضح `PivotCache.getSourceType()` (التعداد `PivotTableSourceType`) من أين جاءت بيانات ذاكرة التخزين المؤقت. اعتبارًا من الإصدار v26.7، يدعم `PivotCache.refresh()` فقط أنواع المصدر **`SHEET`** و**`CONSOLIDATION`** — أي البيانات الموجودة في نطاقات أوراق العمل. المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) لا يمكن تحديثها بعد عبر واجهة برمجة تطبيقات ذاكرة التخزين المؤقت.

{{% /alert %}}

نظرًا لهذه السلسلة، يوجد مساران أساسيان للتحديث في Aspose.Cells:

- **`PivotCache.refresh()`** — يعيد تحميل المصدر إلى ذاكرة التخزين المؤقت ويُعيد حساب جميع `PivotTable` التابعة في عملية واحدة.
- **`PivotTable.calculateData()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون أي رحلة ذهاب وإياب إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر من خلايا ورقة العمل، لذا فإن نوع المصدر هو `SHEET` وتعمل عمليات التحديث كما هو موضح.

## الاستيرادات المطلوبة

تعتمد جميع أمثلة Python في هذه المقالة على الاستيرادات التالية لأن أنواع الجداول المحورية توجد في مساحة الاسم `aspose.cells.pivot`:

- `import jpype`
- `import aspose.cells as cells`

تُستخدم وحدة `jpype` لتشغيل JVM، بينما تعرض `aspose.cells` أنواع المصنف/ورقة العمل/الخلية/الجدول المحوري المستخدمة طوال الوقت.

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى التأكد من أن كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.refreshAll()`. تتجاوز مكالمة واحدة المصنف بأكمله — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. هذا هو الأسلوب الموصى به للتحديثات الشاملة للمستند حيث لا يمثل الأداء مصدر قلق.

يُنشئ المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، ويُنشئ جدولًا محوريًا واحدًا، ويُعدّل بعض قيم المصدر، ثم يستخدم `refreshAll()` لجلب كل شيء حتى الآن في مكالمة واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف العناوين في الخلايا A1:C1
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر 2020 و 2021)
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

# تعيين حقول الجدول المحوري: الفاكهة للصفوف، السنة للأعمدة، المبلغ للبيانات
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# تعديل عدة قيم للمبلغ في البيانات المصدر لمحاكاة التغييرات
worksheet.getCells().get("C2").putValue(55)
worksheet.getCells().get("C5").putValue(85)
worksheet.getCells().get("C9").putValue(125)

# تحديث كل جدول محوري / ذاكرة تخزين مؤقتة في المصنف
workbook.refreshAll()

# حفظ المصنف
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يكون من المعروف أن الجداول المحورية في أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.refreshPivotTables()`، وهي محصورة في مثيل `Worksheet` واحد.

هذا أكثر انتقائية من `Workbook.refreshAll()`: يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.

يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويُضيف جدولًا محوريًا في ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يحدث الجداول المحورية في تلك الورقة فقط.

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

## تحديث جدول محوري واحد

عندما تريد التحكم الدقيق في جدول محوري واحد، تمنحك واجهة برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### تغيير بيانات المصدر — استخدم `PivotCache.refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivotTable.getPivotCache().refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت تلك.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تتشارك مثيل `PivotCache` واحدًا، فإن استدعاء `PivotCache.refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس ذاكرة التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا كان جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث ذاكرة تخزين مؤقت واحدة يحدّث كليهما.

{{% /alert %}}

يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة هذا، ويُعدّل بعض قيم المصدر، ثم يحدث من خلال مرجع ذاكرة تخزين مؤقت واحد.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف الرأس: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة حوالي 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

# إضافة أول جدول محوري "Pivot1" مثبت في الخلية E3، نطاق المصدر A1:C9
pivotIndex1 = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivotIndex1)

# تعيين حقول لـ Pivot1
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# إضافة جدول محوري ثانٍ "Pivot2" مثبت في E15 باستخدام نفس نطاق المصدر A1:C9
# يتشارك كل من Pivot1 و Pivot2 في PivotCache واحد لأن نطاق المصدر متطابق.
pivotIndex2 = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivotIndex2)

# تعيين نفس الحقول لـ Pivot2
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# تعديل قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
worksheet.getCells().get("C2").putValue(150)
worksheet.getCells().get("C4").putValue(350)
worksheet.getCells().get("C7").putValue(650)

# تحديث PivotCache المشترك.
# نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذه المكالمة الواحدة
# تُحدّث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المُحدّث.
pivotTable1.getPivotCache().refresh()

# حفظ المصنف
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

### تغيير العرض/التخطيط فقط — استخدم `calculateData()`

إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للعودة إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ فقط يحتاج `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، `pivotTable.calculateData()` هو الخيار الصحيح.

هذا يتجنب جلب المصدر غير الضروري وهو أسرع بكثير عندما تتشارك العديد من الجداول المحورية في نفس ذاكرة التخزين المؤقت.

يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `calculateData()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# كتابة صف الترويسة: الفاكهة / السنة / المبلغ
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# كتابة 8 صفوف من البيانات (الصفوف 2-9، لتطابق نطاق المصدر A1:C9)
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

# تعديل خاصية عرض/تخطيط — هذا تغيير على العرض فقط،
# لذلك لا يتطلب إعادة قراءة بيانات المصدر عبر PivotCache.Refresh().
pivotTable.setRefreshDataOnOpeningFile(False)

# تعمل CalculateData() على إعادة عرض جدول المحوري هذا (البيانات + النمط) من
# البيانات المخزنة بالفعل في PivotCache. نظرًا لأن بيانات المصدر لم تتغير،
# لا يتم إجراء أي رحلة دائرية إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
# في خلايا ورقة العمل.
pivotTable.calculateData()

# حفظ المصنف على القرص
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس جميعها فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعة، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.getPivotTables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على ذاكرة التخزين المؤقت المعطاة.

هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل نفس مثيل `PivotCache`: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي أرجعها `getPivotTables()` ومراقبة الجداول المحورية التي تظهر فيها.

يُنشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل ذاكرة التخزين المؤقت، ثم يعدد جداول ذاكرة التخزين المؤقت المحورية.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTable, PivotFieldType

# الكود المنقول هنا
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("Sheet1")

worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

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
worksheet.getCells().get("C6").putValue(500)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)

pivot1Index = worksheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.getPivotTables().get(pivot1Index)
pivotTable1.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable1.addFieldToArea(PivotFieldType.DATA, "Amount")

pivot2Index = worksheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.getPivotTables().get(pivot2Index)
pivotTable2.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable2.addFieldToArea(PivotFieldType.DATA, "Amount")

sameCache = pivotTable1.getPivotCache() is pivotTable2.getPivotCache()
print("Pivot1 and Pivot2 share the same PivotCache: " + str(sameCache))

sharedPivotTables = pivotTable1.getPivotCache().getPivotTables()
print("Number of pivot tables sharing the cache: " + str(len(sharedPivotTables)))

for pt in sharedPivotTables:
    print("Pivot table name: " + pt.getName())

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## الترحيل من الطريقة المهجورة `PivotTable.refreshData()`

قبل Aspose.Cells for Python via Java v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refreshData()` على كل جدول محوري بشكل فردي. اعتبارًا من الإصدار v26.7، تم وضع علامة على هذه الطريقة باعتبارها **مهجورة** ويجب استبدالها بواجهات برمجة التطبيقات المدرِكة لذاكرة التخزين المؤقت الموضحة أعلاه.

هناك سببان يجعل نهج `refreshData()` لكل جدول يمثل مشكلة في المصنفات الواقعية:

- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها، حتى عندما لا يكون المصدر قد تغير.
- كل مكالمة تحدّث ذاكرة التخزين المؤقت المشتركة بالكامل. عندما تتشارك العديد من الجداول المحورية في ذاكرة تخزين مؤقت واحدة، فإن استدعاء `refreshData()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.refreshAll();`
- **تحديث بعضها** → استخدم `pivotTable.getPivotCache().refresh();` لذاكرة تخزين مؤقت واحدة. نظرًا لأن ذاكرة التخزين المؤقت مشتركة، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق تلك ذاكرة التخزين المؤقت. يمكن تخطي الجداول المحورية الأخرى التي تجلس على ذاكرة تخزين مؤقت تم تحديثها بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivotTable.calculateData();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة ذهاب وإياب إلى المصدر.

يوضح المثال التالي النمط الفعال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تتشارك ذاكرة تخزين مؤقت واحدة.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)

# --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (الترويسة + 9 صفوف) ---
sheet.getCells().get("A1").putValue("Fruit")
sheet.getCells().get("B1").putValue("Year")
sheet.getCells().get("C1").putValue("Amount")

sheet.getCells().get("A2").putValue("Grape");      sheet.getCells().get("B2").putValue(2020); sheet.getCells().get("C2").putValue(1000)
sheet.getCells().get("A3").putValue("Blueberry");  sheet.getCells().get("B3").putValue(2020); sheet.getCells().get("C3").putValue(2000)
sheet.getCells().get("A4").putValue("Kiwi");       sheet.getCells().get("B4").putValue(2020); sheet.getCells().get("C4").putValue(1500)
sheet.getCells().get("A5").putValue("Cherry");     sheet.getCells().get("B5").putValue(2020); sheet.getCells().get("C5").putValue(2500)
sheet.getCells().get("A6").putValue("Grape");      sheet.getCells().get("B6").putValue(2021); sheet.getCells().get("C6").putValue(3000)
sheet.getCells().get("A7").putValue("Blueberry");  sheet.getCells().get("B7").putValue(2021); sheet.getCells().get("C7").putValue(1800)
sheet.getCells().get("A8").putValue("Kiwi");       sheet.getCells().get("B8").putValue(2021); sheet.getCells().get("C8").putValue(2200)
sheet.getCells().get("A9").putValue("Cherry");     sheet.getCells().get("B9").putValue(2021); sheet.getCells().get("C9").putValue(2700)

# --- إضافة الجدول المحوري الأول (Pivot1) في خلية الوجهة E3 ---
idx1 = sheet.getPivotTables().add("A1:C9", "E3", "Pivot1")
pivotTable1 = sheet.getPivotTables().get(idx1)
pivotTable1.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable1.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable1.addFieldToArea(PivotFieldType.Data, "Amount")

# --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
# يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت (PivotCache) أساسية واحدة.
# هذا هو بالضبط السيناريو الذي تصبح فيه طريقة RefreshData() القديمة لكل جدول غير فعالة:
# تحديث جدول واحد يعيد جلب ذاكرة التخزين المؤقت بالكامل،
# لذا فإن تحديث عدد N من الجداول يؤدي إلى نفس عملية الجلب المكلفة N مرات.
idx2 = sheet.getPivotTables().add("A1:C9", "E15", "Pivot2")
pivotTable2 = sheet.getPivotTables().get(idx2)
pivotTable2.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable2.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable2.addFieldToArea(PivotFieldType.Data, "Amount")

# --- تعديل عدة قيم للمبلغ في بيانات المصدر ---
sheet.getCells().get("C2").putValue(5000)   # عنب 2020
sheet.getCells().get("C5").putValue(7500)   # كرز 2020
sheet.getCells().get("C9").putValue(9500)   # كرز 2021

# --- النمط القديم (قبل الإصدار 26.7) — PivotTable.RefreshData() ---
# pivotTable1.RefreshData();  // يعيد الجلب من المصدر، ويحدّث ذاكرة التخزين المؤقت بالكامل
# pivotTable2.RefreshData();  // يعيد الجلب مرة أخرى — ذاكرة التخزين المؤقت حديثة بالفعل!
# كل استدعاء يعيد بناء ذاكرة التخزين المؤقت المشتركة، لذا N جداول = N من عمليات الجلب المتكررة.

# --- النمط الجديد للإصدار 26.7+: حدّث ذاكرة التخزين المؤقت مرة واحدة، ثم أعد العرض حسب الحاجة ---
# استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى ذاكرة التخزين المؤقت المشتركة
# ويعيد حساب عرض كل جدول محوري يشير إليها.
# نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذا الاستدعاء الواحد يحدّث
# كلا الجدولين — لا حاجة إلى رحلة ذهاب وإياب ثانية إلى المصدر.
pivotTable1.getPivotCache().refresh()

# CalculateData() يعيد عرض الجدول المحوري فقط (البيانات + النمط)
# من البيانات الموجودة بالفعل في ذاكرة التخزين المؤقت — ولا يصل إلى المصدر.
# نستدعيه على Pivot2 هنا فقط لتوضيح الواجهة البرمجية: بعد تحديث ذاكرة التخزين المؤقت مرة واحدة،
# يمكن إعادة عرض أي جدول تابع دون العودة إلى المصدر. استخدم CalculateData() بمفردها عندما تتغير
# إعدادات عرض/تخطيط الجدول المحوري فقط وتكون ذاكرة التخزين المؤقت حالية.
pivotTable2.calculateData()

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## ما هي واجهة برمجة تطبيقات التحديث التي يجب أن أستخدمها؟

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة منها.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refreshAll()` | مكالمة واحدة؛ تغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.refreshPivotTables()` | محصور في ورقة عمل واحدة. |
| تغيرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivotTable.getPivotCache().refresh()` | يحدّث جميع الجداول المحورية على تلك ذاكرة التخزين المؤقت المشتركة. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivotTable.calculateData()` | يتخطى رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivotCache.getPivotTables()` | استخدم للتعداد قبل التحديث بالجملة. |

عمليًا، فضّل واجهات برمجة التطبيقات المعتمدة على ذاكرة التخزين المؤقت على طريقة `refreshData()` المهجورة لكل جدول. إنها على دراية بذاكرة التخزين المؤقت المشتركة، وتتجنب عمليات جلب المصدر الزائدة، وتتيح لك اختيار أصغر نطاق يلبي متطلب التحديث لديك.

{{< app/cells/assistant language="python" >}}