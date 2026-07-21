---
title: تحديث الجداول المحورية في Aspose.Cells for Python via .NET
linktitle: تحديث الجداول المحورية في Aspose.Cells for Python via .NET
description: تعلم كيفية تحديث الجداول المحورية في Aspose.Cells for Python via .NET باستخدام واجهة برمجة تطبيقات تحديث الجداول المحورية في الإصدار 26.7+. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على التعليمات البرمجية.
keywords: Aspose.Cells, Python via .NET, جدول محوري, تحديث, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

يوفر Aspose.Cells واجهة برمجة تطبيقات تحديث متدرجة تتيح لك إعادة تحميل بيانات الجدول المحوري بأربعة نطاقات مختلفة — من المصنف بأكمله إلى جدول محوري واحد. بدءًا من **Aspose.Cells for Aspose.Cells for Python via .NET v26.7**، تم وضع علامة على الطريقة `PivotTable.refresh_data()` كقديمة ويجب استبدالها بواجهات برمجة التطبيقات الأكثر كفاءة والواعية بالتخزين المؤقت الموضحة في هذه المقالة.

{{% /alert %}}

## مقدمة

نادرًا ما يكون تحديث الجدول المحوري عملية واحدة. خلف الكواليس، يحتفظ Aspose.Cells بسلسلة بيانات متدرجة تربط بيانات المصدر الأصلية بالقيم المعروضة التي تراها في ورقة العمل. يُعد فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة تطبيقات التحديث المناسبة لأي موقف.

سلسلة البيانات ذات الطبقات الأربع هي:

1. **مصدر البيانات** — نطاقات ورقة العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج حيث توجد القيم الخام.
2. **PivotCache** — اللقطة الموجودة في الذاكرة لمصدر البيانات. كل جدول محوري مبني فوق `PivotCache`؛ هذا هو المكان الذي يتم فيه جمع وتجميع جميع البيانات.
3. **PivotTable** — كائن العرض الذي يحدد حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، وليس مباشرةً من مصدر البيانات.
4. **الخلايا** — `Cells` الخاصة بورقة العمل التي يعرض فيها `PivotTable` القيم والأنماط المحسوبة.

من المفاهيم المهمة بشكل خاص **التخزين المؤقت المشترك**. عندما تشير جداول محورية متعددة في مصنف إلى نفس نطاق المصدر، فإنها تتشارك *مثيلًا واحدًا* من `PivotCache`. يمكن أن يشير `PivotCache` واحد إلى عدة جداول محورية، ويؤدي تحديث هذا التخزين المؤقت إلى تحديث كل `PivotTable` تابع له في وقت واحد.

{{% alert color="primary" %}}

يشير `PivotCache.source_type` (التعداد `PivotTableSourceType`) إلى مصدر بيانات التخزين المؤقت. اعتبارًا من الإصدار 26.7، يدعم `PivotCache.refresh()` فقط أنواع المصادر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات ورقة العمل. المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، وما إلى ذلك) غير قابلة للتحديث بعد من خلال واجهة برمجة تطبيقات التخزين المؤقت.

{{% /alert %}}

بسبب هذه السلسلة، يوجد مسارا تحديث أساسيان في Aspose.Cells:

- **`PivotCache.refresh()`** — يعيد تحميل المصدر إلى التخزين المؤقت ويعيد حساب جميع `PivotTable`s التابعة في عملية واحدة.
- **`PivotTable.calculate_data()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزنة مؤقتًا بالفعل، دون أي رحلة ذهاب وإياب إلى مصدر البيانات.

تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر من خلايا ورقة العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.

## الاستيرادات المطلوبة

تبدأ جميع أمثلة Python في هذه المقالة بعبارات الاستيراد الثلاث التالية لأن أنواع الجداول المحورية توجد في مساحة الاسم `aspose.cells.pivot`:

- `import sys`
- `import aspose.cells`
- `import aspose.cells.pivot`

## تحديث جميع الجداول المحورية في المصنف

عندما تحتاج إلى التأكد من أن كل تخزين مؤقت للجدول المحوري وكل جدول محوري في المصنف يعكس أحدث بيانات المصدر، فإن أبسط وأشمل واجهة برمجة تطبيقات هي `Workbook.refresh_all()`. تتجاوز مكالمة واحدة المصنف بأكمله — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` تابع. هذا هو النهج الموصى به لتحديثات المستندات الكاملة العامة حيث لا يكون الأداء مصدر قلق.

يبني المثال التالي مصنفًا بنطاق مصدر Fruit/Year/Amount، وينشئ جدولًا محوريًا واحدًا، ويعدل بعض قيم المصدر، ثم يستخدم `refresh_all()` لجلب كل شيء حتى تاريخه في مكالمة واحدة.

```python
import aspose.cells as ac

# إنشاء مصنف جديد
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف الرأس في الخلايا A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفاكهة عبر 2020 و 2021)
worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(50)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(60)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(70)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(80)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(90)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(100)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(110)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(120)

# إضافة جدول محوري: نطاق المصدر "A1:C9"، خلية الوجهة "E3"، الاسم "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تعيين حقول الجدول المحوري: Fruit إلى الصفوف، Year إلى الأعمدة، Amount إلى البيانات
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# تعديل عدة قيم Amount في بيانات المصدر لمحاكاة التغييرات
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# تحديث كل جدول محوري / ذاكرة تخزين مؤقت للجدول المحوري في المصنف
workbook.refresh_all()

# حفظ المصنف
workbook.save("output.xlsx")
```

## تحديث جميع الجداول المحورية في ورقة عمل واحدة

في بعض الأحيان تحتاج فقط إلى تحديث الجداول المحورية الموجودة في ورقة عمل واحدة محددة — على سبيل المثال، عندما يُعرف أن الجداول المحورية في أوراق العمل الأخرى غير مرتبطة ولا ينبغي لمسها. لهذه الحالة، يوفر Aspose.Cells `Worksheet.refresh_pivot_tables()`، التي تكون محصورة في مثيل `Worksheet` واحد.

هذا أكثر انتقائية من `Workbook.refresh_all()`: يتم تحديث الجداول المحورية الموجودة في ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية في أوراق العمل الأخرى دون مساس.

يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويضيف جدولًا محوريًا في ورقة العمل الأولى، ويعدل بعض قيم المصدر، ثم يحدث فقط الجداول المحورية في تلك الورقة.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("blueberry")
worksheet.cells["B3"].put_value(2021)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("cherry")
worksheet.cells["B5"].put_value(2021)
worksheet.cells["C5"].put_value(120)

worksheet.cells["A6"].put_value("grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(180)

worksheet.cells["A7"].put_value("blueberry")
worksheet.cells["B7"].put_value(2020)
worksheet.cells["C7"].put_value(130)

worksheet.cells["A8"].put_value("kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(220)

worksheet.cells["A9"].put_value("cherry")
worksheet.cells["B9"].put_value(2020)
worksheet.cells["C9"].put_value(140)

pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

worksheet.cells["C2"].put_value(300)
worksheet.cells["C5"].put_value(250)
worksheet.cells["C9"].put_value(400)

worksheet.refresh_pivot_tables()

workbook.save("output.xlsx")
```

## تحديث جدول محوري واحد

عندما تريد تحكمًا دقيقًا في جدول محوري واحد، تمنحك واجهة برمجة التطبيقات المعتمدة على التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغير فعليًا: بيانات المصدر الأساسية، أو إعدادات العرض/التخطيط للجدول المحوري نفسه فقط.

### تغيرت بيانات المصدر — استخدم `PivotCache.refresh()`

إذا تغيرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivot_table.pivot_cache.refresh()`. تعيد هذه المكالمة قراءة بيانات المصدر في التخزين المؤقت ثم تعيد حساب كل `PivotTable` يعتمد على هذا التخزين المؤقت.

{{% alert color="primary" %}}

نظرًا لأن الجداول المحورية تتشارك مثيلًا واحدًا من `PivotCache`، فإن استدعاء `PivotCache.refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على نفس التخزين المؤقت — وليس فقط الجدول الذي تشير إليه. إذا كان هناك جدولان محوريان يتشاركان نفس نطاق المصدر، فإن تحديث تخزين مؤقت واحد يحدّث كليهما.

{{% /alert %}}

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر لإظهار سلوك التخزين المؤقت المشترك هذا، ويعدل بعض قيم المصدر، ثم يحدث من خلال مرجع تخزين مؤقت واحد.

```python
import aspose.cells as ac

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف الرأس: الفاكهة / السنة / المبلغ
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة ما يقرب من 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

# إضافة الجدول المحوري الأول "Pivot1" مثبتًا عند الخلية E3، نطاق المصدر A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# تعيين الحقول لـ Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# إضافة الجدول المحوري الثاني "Pivot2" مثبتًا عند E15 باستخدام نفس نطاق المصدر A1:C9
# يتشارك كل من Pivot1 و Pivot2 في PivotCache واحد لأن نطاق المصدر متطابق.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# تعيين نفس الحقول لـ Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# تعديل عدة قيم خلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# تحديث PivotCache المشترك.
# نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذه المكالمة الواحدة
# تُحدّث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المُحدّث.
pivotTable1.pivot_cache.refresh()

# حفظ المصنف
workbook.save("output.xlsx")
```

### تغير العرض/التخطيط فقط — استخدم `calculate_data()`

إذا لم تتغير بيانات المصدر *ولكن* تم تعديل إعدادات عرض أو تخطيط الجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للقيام برحلة ذهاب وإياب إلى مصدر البيانات. يحتفظ التخزين المؤقت بالفعل بالبيانات الصحيحة؛ فقط `PivotTable` المعروض يحتاج إلى إعادة الحساب. في هذه الحالة، `pivot_table.calculate_data()` هو الخيار الصحيح.

هذا يتجنب جلب المصدر غير الضروري ويكون أسرع بكثير عندما تتشارك جداول محورية متعددة نفس التخزين المؤقت.

يعدل المثال التالي خاصية غير خاصة بالمصدر في الجدول المحوري ثم يستدعي `calculate_data()` لإعادة عرضه من التخزين المؤقت الموجود.

```python
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة 8 صفوف بيانات (الصفوف 2-9، ضمن نطاق المصدر A1:C9)
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(150)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(250)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(350)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(450)

# إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، ومصدره A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تعيين الحقول: الفاكهة للصفوف، السنة للأعمدة، المبلغ للبيانات
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# تعديل خاصية عرض/تخطيط — هذا تغيير خاص بالعرض فقط،
# لذلك لا يتطلب إعادة قراءة البيانات المصدر عبر PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() يعيد عرض جدول المحوري هذا (البيانات + النمط) من
# البيانات المخزنة بالفعل في PivotCache. نظرًا لأن البيانات المصدر لم تتغير،
# لا يتم تنفيذ أي رحلة ذهاب وإياب إلى المصدر — يتم فقط إعادة حساب القيم المخزنة مؤقتًا
# في خلايا ورقة العمل.
pivot_table.calculate_data()

# حفظ المصنف على القرص
workbook.save("output.xlsx")
```

## الحصول على جميع الجداول المحورية التي تتشارك نفس PivotCache

غالبًا ما يحتوي المصنف على العديد من الجداول المحورية التي تجلس فوق تخزين مؤقت مشترك واحد. لتعدادها — على سبيل المثال، قبل إجراء تحديث مجمع، أو لتشخيص تأثير التخزين المؤقت المشترك — استخدم `PivotCache.get_pivot_tables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` يعتمد على التخزين المؤقت المعطى.

هذه أيضًا هي الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان بالفعل نفس مثيل `PivotCache`: يمكنك مقارنة مراجع التخزين المؤقت، أو ببساطة تكرار المجموعة التي أرجعها `get_pivot_tables()` ومراقبة الجداول المحورية التي تظهر فيها.

ينشئ المثال التالي جدولين محوريين على نفس نطاق المصدر، ويتحقق من أنهما يتشاركان نفس مثيل التخزين المؤقت، ثم يُعدّد الجداول المحورية للتخزين المؤقت.

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "Sheet1"

worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)

pivot1_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = worksheet.pivot_tables[pivot1_index]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

pivot2_index = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = worksheet.pivot_tables[pivot2_index]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

same_cache = pivot_table1.pivot_cache is pivot_table2.pivot_cache
print("Pivot1 and Pivot2 share the same PivotCache: " + str(same_cache))

shared_pivot_tables = pivot_table1.pivot_cache.get_pivot_tables()
print("Number of pivot tables sharing the cache: " + str(len(shared_pivot_tables)))

for pt in shared_pivot_tables:
    print("Pivot table name: " + pt.name)

workbook.save("output.xlsx")
```

## الانتقال من `PivotTable.refresh_data()` المهجور

قبل Aspose.Cells for Aspose.Cells for Python via .NET v26.7، كانت الطريقة القياسية لتحديث جدول محوري هي استدعاء `PivotTable.refresh_data()` على كل جدول محوري على حدة. اعتبارًا من الإصدار 26.7، تم وضع علامة على هذه الطريقة كـ **مهجورة** ويجب استبدالها بواجهات برمجة التطبيقات الواعية بالتخزين المؤقت الموضحة أعلاه.

هناك سببان يجعل نهج `refresh_data()` لكل جدول يمثل مشكلة في المصنفات الواقعية:

- يعيد جلب البيانات من المصدر *في كل مرة* يتم استدعاؤها فيها، حتى عندما لا يكون المصدر قد تغير.
- كل مكالمة تحدّث التخزين المؤقت المشترك بالكامل. عندما تتشارك جداول محورية متعددة في تخزين مؤقت واحد، فإن استدعاء `refresh_data()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس التخزين المؤقت مرارًا وتكرارًا، وهو بطيء جدًا.

البدائل الموصى بها هي:

- **تحديث جميع الجداول المحورية في المصنف** → استخدم `workbook.refresh_all();`
- **تحديث بعضها** → استخدم `pivot_table.pivot_cache.refresh();` لتخزين مؤقت واحد. نظرًا لأن التخزين المؤقت مشترك، فإن هذه المكالمة الواحدة تحدّث كل جدول محوري مبني فوق هذا التخزين المؤقت. يمكن تخطي الجداول المحورية الأخرى التي تجلس على تخزين مؤقت تم تحديثه بالفعل بأمان.
- **تغير عرض/تخطيط الجدول المحوري فقط** → استخدم `pivot_table.calculate_data();` لإعادة العرض من التخزين المؤقت الموجود دون أي رحلة ذهاب وإياب إلى المصدر.

يوضح المثال التالي النمط الفعال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تتشارك تخزينًا مؤقتًا واحدًا.

```python
import aspose.cells as ac

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- بناء البيانات المصدر: فاكهة / سنة / مبلغ (رأس + 9 صفوف) ---
sheet.cells["A1"].put_value("Fruit")
sheet.cells["B1"].put_value("Year")
sheet.cells["C1"].put_value("Amount")

sheet.cells["A2"].put_value("Grape")      ; sheet.cells["B2"].put_value(2020); sheet.cells["C2"].put_value(1000)
sheet.cells["A3"].put_value("Blueberry")  ; sheet.cells["B3"].put_value(2020); sheet.cells["C3"].put_value(2000)
sheet.cells["A4"].put_value("Kiwi")       ; sheet.cells["B4"].put_value(2020); sheet.cells["C4"].put_value(1500)
sheet.cells["A5"].put_value("Cherry")     ; sheet.cells["B5"].put_value(2020); sheet.cells["C5"].put_value(2500)
sheet.cells["A6"].put_value("Grape")      ; sheet.cells["B6"].put_value(2021); sheet.cells["C6"].put_value(3000)
sheet.cells["A7"].put_value("Blueberry")  ; sheet.cells["B7"].put_value(2021); sheet.cells["C7"].put_value(1800)
sheet.cells["A8"].put_value("Kiwi")       ; sheet.cells["B8"].put_value(2021); sheet.cells["C8"].put_value(2200)
sheet.cells["A9"].put_value("Cherry")     ; sheet.cells["B9"].put_value(2021); sheet.cells["C9"].put_value(2700)

# --- إضافة الجدول المحوري الأول (Pivot1) في خلية الوجهة E3 ---
idx1 = sheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table1 = sheet.pivot_tables[idx1]
pivot_table1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- إضافة الجدول المحوري الثاني (Pivot2) على نفس نطاق المصدر ---
# يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت (PivotCache) مشتركة واحدة.
# هذا بالضبط هو السيناريو الذي يصبح فيه النهج القديم RefreshData() لكل جدول
# غير فعال: عند تحديث جدول واحد، يتم إعادة جلب الذاكرة المشتركة بالكامل،
# لذلك يؤدي تحديث عدد N من الجداول إلى نفس عملية الجلب المكلفة N مرات.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- تعديل عدة قيم للمبلغ في البيانات المصدر ---
sheet.cells["C2"].put_value(5000)   # Grape  2020
sheet.cells["C5"].put_value(7500)   # Cherry 2020
sheet.cells["C9"].put_value(9500)   # Cherry 2021

# --- النمط القديم (قبل الإصدار 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # يعيد الجلب من المصدر ويحدّث الذاكرة بالكامل
# pivot_table2.refresh_data();  # يعيد الجلب مرة أخرى — الذاكرة بالفعل محدّثة!
# كل استدعاء يعيد بناء الذاكرة المشتركة، لذلك N جداول = N من عمليات الجلب المتكررة.

# --- النمط الجديد في الإصدار 26.7+: تحديث الذاكرة المؤقتة مرة واحدة، ثم إعادة العرض حسب الحاجة ---
# استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدّلة إلى الذاكرة المشتركة
# ويعيد حساب العرض لكل جدول محوري يشير إليها.
# ولأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذا الاستدعاء الواحد
# يحدّث كلا الجدولين — دون الحاجة إلى جولة ثانية إلى المصدر.
pivot_table1.pivot_cache.refresh()

# CalculateData() يعيد عرض الجدول المحوري فقط (البيانات + النمط)
# من البيانات الموجودة بالفعل في الذاكرة المؤقتة — ولا يلمس المصدر.
# نستدعيها على Pivot2 هنا لإثبات واجهة برمجة التطبيقات فقط: بعد تحديث
# الذاكرة مرة واحدة، يمكن إعادة عرض أي جدول تابع دون العودة إلى المصدر.
# استخدم CalculateData() بمفردها عندما تتغير إعدادات عرض/تخطيط الجدول المحوري فقط
# وتكون الذاكرة المؤقتة محدّثة.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```

## أي واجهة برمجة تطبيقات للتحديث يجب أن أستخدم؟

يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل واحدة.

| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refresh_all()` | مكالمة واحدة؛ تغطي جميع التخزينات المؤقتة والجداول. |
| تحديث الجداول المحورية في ورقة واحدة فقط | `Worksheet.refresh_pivot_tables()` | محصورة في ورقة عمل واحدة. |
| تغيرت بيانات المصدر لتخزين مؤقت واحد | `pivot_table.pivot_cache.refresh()` | يحدّث جميع الجداول المحورية على ذلك التخزين المؤقت المشترك. |
| تغيرت إعدادات العرض/التخطيط فقط | `pivot_table.calculate_data()` | يتجنب رحلة المصدر غير الضرورية. |
| سرد جميع الجداول المحورية على تخزين مؤقت مشترك | `pivot_cache.get_pivot_tables()` | استخدم للتعداد قبل التحديث المجمع. |

عمليًا، يُفضل استخدام واجهات برمجة التطبيقات المعتمدة على التخزين المؤقت بدلاً من `refresh_data()` المهجور لكل جدول. إنها واعية بالتخزينات المؤقتة المشتركة، وتتجنب جلب المصدر الزائد، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث الخاصة بك.

{{< app/cells/assistant language="python" >}}