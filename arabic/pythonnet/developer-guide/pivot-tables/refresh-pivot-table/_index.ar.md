---
title: تحديث الجداول المحورية في Aspose.Cells for Python via .NET
linktitle: تحديث الجداول المحورية في Aspose.Cells for Python via .NET
description: تعلّم كيفية تحديث الجداول المحورية في Aspose.Cells for Python via .NET باستخدام واجهة برمجة التطبيقات للتحديث في الإصدار v26.7+ وما بعده. تتناول هذه المقالة RefreshAll و RefreshPivotTables و PivotCache.Refresh و CalculateData و GetPivotTables مع أمثلة عملية على الشيفرة.
keywords: Aspose.Cells, Python via .NET, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /ar/python-net/refresh-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
يوفّر Aspose.Cells واجهة برمجة تطبيقات للتحديث بشكل متعدد الطبقات تتيح لك إعادة تحميل بيانات الجدول المحوري ضمن أربعة نطاقات مختلفة — من المصنف بأكمله وصولاً إلى جدول محوري واحد. بدءاً من **Aspose.Cells for Python via .NET الإصدار v26.7**، تم وضع علامة "مهجور" على الطريقة القديمة `PivotTable.refresh_data()`، ويُستحسن استبدالها بواجهات البرمجة الأكثر كفاءة واعتماداً على ذاكرة التخزين المؤقت الموضحة في هذه المقالة.
{{% /alert %}}
## مقدمة
نادراً ما تكون عملية تحديث الجدول المحوري عملية واحدة. فخلف الكواليس، يحتفظ Aspose.Cells بسلسلة بيانات متعددة الطبقات تربط بيانات المصدر الأصلية بالقيم المُقدَّمة التي تراها في ورقة العمل. إن فهم هذه السلسلة هو المفتاح لاختيار واجهة برمجة التطبيقات الصحيحة للتحديث في أي موقف.
سلسلة البيانات ذات الطبقات الأربع هي:
1. **مصدر البيانات** — نطاقات أوراق العمل الأصلية، أو استعلام قاعدة البيانات، أو نطاق الدمج الذي توجد فيه القيم الخام.
2. **PivotCache** — لقطة البيانات في الذاكرة. يُبنى كل جدول محوري فوق `PivotCache`؛ وهنا يتم تجميع كل البيانات وتجميعها.
3. **PivotTable** — كائن العرض الذي يعرّف حقول الصفوف والأعمدة والقيم والتصفية. يقرأ `PivotTable` *فقط* من `PivotCache` الخاص به، ولا يقرأ أبداً مباشرةً من مصدر البيانات.
4. **Cells** — مجموعة `Cells` الخاصة بورقة العمل، حيث يعرض `PivotTable` قيمه وأنماطه المحسوبة فيها.
من المفاهيم المهمة بشكل خاص مفهوم **ذاكرة التخزين المؤقت المشتركة**. عندما تشير جداول محورية متعددة في المصنف إلى نطاق المصدر نفسه، فإنها تتشارك `PivotCache` *واحداً* فقط. يمكن لـ `PivotCache` واحد أن تشير إليه جداول محورية عديدة، وإن تحديث ذاكرة التخزين المؤقت تلك يُحدث جميع `PivotTable` المعتمدة عليها دفعةً واحدة.
{{% alert color="primary" %}}
يشير `PivotCache.source_type` (وهو من النوع المعدود `PivotTableSourceType`) إلى مصدر بيانات ذاكرة التخزين المؤقت. اعتباراً من الإصدار v26.7، تدعم `PivotCache.refresh()` فقط نوعَي المصادر **`Sheet`** و **`Consolidation`** — أي البيانات الموجودة في نطاقات أوراق العمل. أما المصادر الخارجية (قواعد البيانات، الاتصالات الخارجية، إلخ) فلا يمكن تحديثها بعد من خلال واجهة برمجة التطبيقات المتعلقة بذاكرة التخزين المؤقت.
{{% /alert %}}
نظراً لهذه السلسلة، يوجد مسارا تحديث أساسيان في Aspose.Cells:
- **`PivotCache.refresh()`** — يعيد تحميل البيانات من المصدر إلى ذاكرة التخزين المؤقت ثم يعيد حساب جميع `PivotTable` المعتمدة عليها في عملية واحدة.
- **`PivotTable.calculate_data()`** — يعيد حساب عرض `PivotTable` واحد من البيانات المخزّنة مؤقتاً بالفعل، دون الحاجة إلى الرجوع إلى مصدر البيانات.
تستخدم جميع السيناريوهات في هذه المقالة بيانات مصدر موجودة في خلايا أوراق العمل، لذا فإن نوع المصدر هو `Sheet` وتعمل عمليات التحديث كما هو موضح.
## الاستيرادات المطلوبة
تبدأ جميع أمثلة Python في هذه المقالة بعبارات الاستيراد الثلاث التالية لأن أنواع الجداول المحورية تعيش في فضاء الأسماء `aspose.cells.pivot`:
## تحديث جميع الجداول المحورية في المصنف
عندما تحتاج إلى ضمان أن تعكس كل ذاكرة تخزين مؤقت وكل جدول محوري في المصنف أحدث بيانات المصدر، فإن أبسط واجهة برمجة تطبيقات وأكثرها شمولاً هي `Workbook.refresh_all()`. يتجاوز هذا الاستدعاء الواحد المصنف بأكمله — حيث تحدّث كل `PivotCache` من مصدره ثم تعيد حساب كل `PivotTable` المعتمدة عليه. هذه هي الطريقة الموصى بها للتحديثات العامة والشاملة للمستند عندما لا يكون الأداء مقلقاً.
يُنشئ المثال التالي مصنفاً بنطاق مصدر Fruit/Year/Amount، ويُنشئ جدولاً محورياً واحداً، ويُعدّل بعض قيم المصدر، ثم يستخدم `refresh_all()` لجلب كل شيء حتى أحدث إصدار في استدعاء واحد.
```python
import sys
import aspose.cells as ac

# إنشاء مصنف جديد
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف الرأس في الخلايا A1:C1
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة صفوف البيانات في الخلايا A2:C9 (8 صفوف من بيانات الفواكه عبر عامي 2020 و2021)
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

# تعيين حقول الجدول المحوري: الفاكهة إلى الصفوف، السنة إلى الأعمدة، المبلغ إلى البيانات
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# تعديل عدة قيم للمبلغ في بيانات المصدر لمحاكاة التغييرات
worksheet.cells["C2"].put_value(55)
worksheet.cells["C5"].put_value(85)
worksheet.cells["C9"].put_value(125)

# تحديث كل جدول محوري / ذاكرة التخزين المؤقت للجدول المحوري في المصنف
workbook.refresh_all()

# حفظ المصنف
workbook.save("output.xlsx")
```
## تحديث جميع الجداول المحورية على ورقة عمل واحدة
في بعض الأحيان، تحتاج فقط إلى تحديث الجداول المحورية الموجودة على ورقة عمل واحدة محددة — على سبيل المثال، عندما تعرف أن الجداول المحورية الموجودة على أوراق العمل الأخرى غير ذات صلة ولا ينبغي لمسها. لهذه الحالة، يوفّر Aspose.Cells واجهة `Worksheet.refresh_pivot_tables()`، وهي محصورة بنسخة `Worksheet` واحدة.
تكون هذه الواجهة أكثر انتقائية من `Workbook.refresh_all()`: إذ يتم تحديث الجداول المحورية الموجودة على ورقة العمل المستهدفة فقط، مع ترك أي جداول محورية على أوراق عمل أخرى دون تغيير.
يملأ المثال التالي نفس بيانات المصدر Fruit/Year/Amount، ويُضيف جدولاً محورياً على ورقة العمل الأولى، ويُعدّل بعض قيم المصدر، ثم يحدث فقط الجداول المحورية الموجودة على تلك الورقة.
```python
import sys
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
عندما تريد التحكم الدقيق في جدول محوري واحد، تتيح لك واجهة البرمجة المعتمدة على ذاكرة التخزين المؤقت خيارين. يعتمد الاختيار بينهما على ما تغيّر فعلاً: بيانات المصدر الأساسية، أم مجرد إعدادات العرض/التخطيط للجدول المحوري نفسه.
### تغيّرت بيانات المصدر — استخدم `PivotCache.refresh()`
إذا تغيّرت بيانات المصدر الأساسية، فإن نقطة الدخول الصحيحة هي `pivot_table.pivot_cache.refresh()`. تعيد هذه الاستدعاء قراءة بيانات المصدر إلى ذاكرة التخزين المؤقت ثم تعيد حساب كل `PivotTable` تعتمد على ذاكرة التخزين المؤقت تلك.
{{% alert color="primary" %}}
نظراً لأن الجداول المحورية تتشارك نسخة واحدة من `PivotCache`، فإن استدعاء `PivotCache.refresh()` يعيد حساب **جميع** الجداول المحورية المبنية على ذاكرة التخزين المؤقت نفسها — وليس فقط الجدول الذي تشير إليه. إذا كان هناك جدولان محوريان يتشاركان في نطاق المصدر نفسه، فإن تحديث ذاكرة تخزين مؤقت واحدة يُحدث كليهما.
{{% /alert %}}
يُنشئ المثال التالي جدولين محوريين على نطاق المصدر نفسه لتوضيح سلوك ذاكرة التخزين المؤقت المشتركة، ويُعدّل بعض قيم المصدر، ثم يحدث من خلال مرجع ذاكرة تخزين مؤقت واحد.
```python
import sys
import aspose.cells as ac

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة حوالي 9 صفوف بيانات (عنب / توت أزرق / كيوي / كرز عبر 2020-2021)
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

# إضافة جدول محوري أول "Pivot1" مثبت في الخلية E3، نطاق المصدر A1:C9
pivotIndex1 = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivotTable1 = worksheet.pivot_tables[pivotIndex1]

# تعيين الحقول لـ Pivot1
pivotTable1.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable1.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable1.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# إضافة جدول محوري ثانٍ "Pivot2" مثبت في E15 باستخدام نفس نطاق المصدر A1:C9
# كل من Pivot1 و Pivot2 يتشاركان PivotCache واحد لأن نطاق المصدر متطابق.
pivotIndex2 = worksheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivotTable2 = worksheet.pivot_tables[pivotIndex2]

# تعيين نفس الحقول لـ Pivot2
pivotTable2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivotTable2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivotTable2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# تعديل عدة قيم لخلايا المبلغ في بيانات المصدر لمحاكاة تغيير البيانات
worksheet.cells["C2"].put_value(150)
worksheet.cells["C4"].put_value(350)
worksheet.cells["C7"].put_value(650)

# تحديث PivotCache المشترك.
# نظرًا لأن Pivot1 و Pivot2 يتشاركان نفس PivotCache، فإن هذا الاستدعاء الواحد
# يقوم بتحديث كلا الجدولين المحوريين (البيانات + النمط) من المصدر المحدّث.
pivotTable1.pivot_cache.refresh()

# حفظ المصنف
workbook.save("output.xlsx")
```
### تغيّر العرض/التخطيط فقط — استخدم `calculate_data()`
إذا لم تتغيّر بيانات المصدر ولكن تغيّرت إعدادات العرض أو التخطيط للجدول المحوري فقط (على سبيل المثال، تم نقل حقل إلى منطقة مختلفة، أو تم تبديل إعداد التحديث عند الفتح)، فلا توجد حاجة للرجوع إلى مصدر البيانات. تحتوي ذاكرة التخزين المؤقت بالفعل على البيانات الصحيحة؛ يحتاج فقط `PivotTable` المعروض إلى إعادة حساب. في هذه الحالة، تكون `pivot_table.calculate_data()` هي الخيار الصحيح.
يتجنّب ذلك الجلب غير الضروري من المصدر وهو أسرع بكثير عندما تتشارك جداول محورية عديدة في ذاكرة التخزين المؤقت نفسها.
يُعدّل المثال التالي خاصية غير مصدرية للجدول المحوري ثم يستدعي `calculate_data()` لإعادة عرضه من ذاكرة التخزين المؤقت الموجودة.
```python
import sys
import aspose.cells as ac
import aspose.cells.pivot as acp

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# كتابة صف العناوين: الفاكهة / السنة / المبلغ
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# كتابة 8 صفوف من البيانات (الصفوف 2-9، تتطابق مع نطاق المصدر A1:C9)
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

# إضافة جدول محوري باسم "Pivot1" موضوع في خلية الوجهة E3، مصدره من A1:C9
pivot_index = worksheet.pivot_tables.add("A1:C9", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# تعيين الحقول: الفاكهة إلى الصف، السنة إلى العمود، المبلغ إلى البيانات
pivot_table.add_field_to_area(acp.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(acp.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(acp.PivotFieldType.DATA, "Amount")

# تعديل خاصية عرض/تخطيط — هذا تغيير للعرض فقط،
# لذلك لا يتطلب إعادة قراءة بيانات المصدر من خلال PivotCache.Refresh().
pivot_table.refresh_data_on_opening_file = False

# CalculateData() يعيد عرض جدولنا المحوري هذا (البيانات + النمط) من
# البيانات الموجودة بالفعل في PivotCache. ولأن بيانات المصدر لم تتغير،
# لا يتم تنفيذ رحلة دائرية إلى المصدر — فقط القيم المخزنة مؤقتًا يتم إعادة حسابها
# في خلايا ورقة العمل.
pivot_table.calculate_data()

# حفظ المصنف على القرص
workbook.save("output.xlsx")
```
## الحصول على جميع الجداول المحورية التي تشترك في نفس PivotCache
غالباً ما يحتوي المصنف على جداول محورية عديدة جميعها مبنية فوق ذاكرة تخزين مؤقت مشتركة واحدة. لتعدادها — على سبيل المثال، قبل إجراء تحديث دفعي، أو لتشخيص تأثير ذاكرة التخزين المؤقت المشتركة — استخدم `PivotCache.get_pivot_tables()`. تُرجع هذه الطريقة مجموعة كل `PivotTable` التي تعتمد على ذاكرة التخزين المؤقت المعطاة.
هذه هي أيضاً الطريقة الأكثر مباشرة للتأكد من أن جدولين محوريين يتشاركان فعلاً في نفس نسخة `PivotCache`: يمكنك مقارنة مراجع ذاكرة التخزين المؤقت، أو ببساطة تكرار المجموعة التي تُرجعها `get_pivot_tables()` ولاحظة أي الجداول المحورية تظهر فيها.
يُنشئ المثال التالي جدولين محوريين على نطاق المصدر نفسه، ويتحقق من أنهما يتشاركان نسخة ذاكرة التخزين المؤقت نفسها، ثم يعدّد الجداول المحورية لذاكرة التخزين المؤقت تلك.
```python
import sys
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
## الانتقال من `PivotTable.refresh_data()` المهجورة
قبل Aspose.Cells for Python via .NET الإصدار v26.7، كانت الطريقة المعيارية لتحديث جدول محوري هي استدعاء `PivotTable.refresh_data()` على كل جدول محوري على حدة. اعتباراً من الإصدار v26.7، تم وضع علامة **مهجور** على هذه الطريقة، ويجب استبدالها بواجهات البرمجة المعتمدة على ذاكرة التخزين المؤقت الموضحة أعلاه.
هناك سببان يجعلان نهج `refresh_data()` لكل جدول على حدة إشكالياً في المصنفات الواقعية:
- يعيد جلب البيانات من المصدر *في كل مرة* يُستدعى فيها، حتى عندما لا يتغيّر المصدر.
- كل استدعاء يُحدث ذاكرة التخزين المؤقت المشتركة بأكملها. عندما تتشارك جداول محورية عديدة في ذاكرة تخزين مؤقت واحدة، فإن استدعاء `refresh_data()` بشكل متكرر لكل جدول محوري يتسبب في إعادة جلب نفس ذاكرة التخزين المؤقت مراراً وتكراراً، وهو بطيء جداً.
البدائل الموصى بها هي:
- **لتحديث جميع الجداول المحورية في المصنف** ← استخدم `workbook.refresh_all();`
- **لتحديث بعضها** ← استخدم `pivot_table.pivot_cache.refresh();` لذاكرة تخزين مؤقت واحدة. ولأن ذاكرة التخزين المؤقت مشتركة، فإن هذا الاستدعاء الواحد يُحدث كل جدول محوري مبني فوق ذاكرة التخزين المؤقت تلك. أما الجداول المحورية الأخرى التي تجلس فوق ذاكرة تخزين مؤقت تم تحديثها بالفعل فيمكن تخطيها بأمان.
- **في حالة تغيّر عرض/تخطيط الجدول المحوري فقط** ← استخدم `pivot_table.calculate_data();` لإعادة العرض من ذاكرة التخزين المؤقت الموجودة دون أي رحلة إلى المصدر.
يوضّح المثال التالي النمط الفعّال الجديد للمصنفات ذات الجداول المحورية المتعددة التي تشترك في ذاكرة تخزين مؤقت واحدة.
```python
import sys
import aspose.cells as ac

# إنشاء مصنف جديد والوصول إلى ورقة العمل الأولى
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# --- بناء بيانات المصدر: الفاكهة / السنة / المبلغ (الترويسة + 9 صفوف) ---
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
# يتشارك كل من Pivot1 و Pivot2 ذاكرة تخزين مؤقت محورية واحدة أساسية.
# هذا هو بالضبط السيناريو الذي يصبح فيه نهج RefreshData() القديم لكل جدول
# غير فعال: تحديث جدول واحد يعيد جلب كامل ذاكرة التخزين المؤقت المشتركة،
# لذا فإن تحديث عدد N من الجداول يقوم بنفس الجلب المكلف عدد N من المرات.
idx2 = sheet.pivot_tables.add("A1:C9", "E15", "Pivot2")
pivot_table2 = sheet.pivot_tables[idx2]
pivot_table2.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table2.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table2.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# --- تعديل عدة قيم في المبلغ في بيانات المصدر ---
sheet.cells["C2"].put_value(5000)   # عنب  2020
sheet.cells["C5"].put_value(7500)   # كرز 2020
sheet.cells["C9"].put_value(9500)   # كرز 2021

# --- النمط القديم (قبل 26.7) — PivotTable.RefreshData() ---
# pivot_table1.refresh_data();  # يعيد الجلب من المصدر، ويحدّث كامل ذاكرة التخزين المؤقت
# pivot_table2.refresh_data();  # يعيد الجلب مرة أخرى — ذاكرة التخزين المؤقت جديدة بالفعل!
# كل استدعاء يعيد بناء ذاكرة التخزين المؤقت المشتركة، لذا N جداول = N من عمليات الجلب المكررة.

# --- النمط الجديد في الإصدار 26.7+: حدّث ذاكرة التخزين المؤقت مرة واحدة، ثم أعد العرض حسب الحاجة ---
# استدعاء واحد لـ PivotCache.Refresh() يسحب القيم المعدلة إلى ذاكرة التخزين المؤقت
# المشتركة ويعيد حساب عرض كل جدول محوري يشير إليها.
# نظراً لأن Pivot1 و Pivot2 يتشاركان ذاكرة تخزين مؤقت محورية واحدة، فإن هذا
# الاستدعاء الواحد يحدّث كلا الجدولين — لا حاجة إلى رحلة ذهاب وإياب ثانية للمصدر.
pivot_table1.pivot_cache.refresh()

# CalculateData() يعيد عرض الجدول المحوري فقط (البيانات + النمط) من البيانات
# الموجودة بالفعل في ذاكرة التخزين المؤقت — ولا يلمس المصدر.
# نستدعيها على Pivot2 هنا فقط لتوضيح الواجهة البرمجية: بعد أن تم تحديث
# ذاكرة التخزين المؤقت مرة واحدة، يمكن إعادة عرض أي جدول تابع دون العودة
# إلى المصدر. استخدم CalculateData() بمفردها عندما يكون قد تغير فقط
# إعدادات عرض/تخطيط الجدول المحوري وذاكرة التخزين المؤقت حالية.
pivot_table2.calculate_data()

workbook.save("output.xlsx")
```
## أي واجهة برمجة تحديث يجب أن أستخدم؟
يلخص الجدول التالي واجهات برمجة التطبيقات المتاحة للتحديث ومتى تختار كل منها.
| الهدف | واجهة برمجة التطبيقات الموصى بها | ملاحظات |
|------|-----------------|-------|
| تحديث كل شيء في المصنف | `Workbook.refresh_all()` | استدعاء واحد؛ يغطي جميع ذاكرات التخزين المؤقت والجداول. |
| تحديث الجداول المحورية على ورقة واحدة فقط | `Worksheet.refresh_pivot_tables()` | محصور بورقة عمل واحدة. |
| تغيّرت بيانات المصدر لذاكرة تخزين مؤقت واحدة | `pivot_table.pivot_cache.refresh()` | يحدث جميع الجداول المحورية على ذاكرة التخزين المؤقت المشتركة تلك. |
| تغيّرت إعدادات العرض/التخطيط فقط | `pivot_table.calculate_data()` | يتجنب الرحلة غير الضرورية إلى المصدر. |
| سرد جميع الجداول المحورية على ذاكرة تخزين مؤقت مشتركة | `pivot_cache.get_pivot_tables()` | يُستخدم للتعداد قبل التحديث المجمع. |
عملياً، يُفضّل استخدام واجهات البرمجة المعتمدة على ذاكرة التخزين المؤقت بدلاً من `refresh_data()` القديمة لكل جدول على حدة. فهي تدرك ذاكرات التخزين المؤقت المشتركة، وتتجنب عمليات الجلب المتكررة من المصدر، وتتيح لك اختيار أصغر نطاق يلبي متطلبات التحديث لديك.
## مقالات ذات صلة
- [Sparklines in Aspose.Cells for Python via .NET](/cells/ar/python-net/sparkline/)
{{< app/cells/assistant language="python" >}}