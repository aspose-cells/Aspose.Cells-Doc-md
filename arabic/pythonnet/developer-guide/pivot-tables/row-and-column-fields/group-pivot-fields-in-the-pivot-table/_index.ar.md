---
title: تجميع حقول الجدول المحوري في الجدول المحوري
linktitle: تجميع حقول الجدول المحوري في الجدول المحوري
description: تعرف على كيفية تجميع حقول الصفوف والأعمدة في جدول محوري ضمن فترات زمنية مثل الأشهر والأرباع ونطاقات رقمية باستخدام PivotField.Group وPivotFieldGroupOptions في Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, جدول محوري, تجميع حقل محوري, PivotField.Group, PivotFieldGroupOptions, تجميع حسب التاريخ, تجميع حسب الأرقام, الأشهر, الأرباع, نطاق رقمي, Python via .NET
type: docs
weight: 80
url: /ar/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يكون تجميع حقول الجدول المحوري مفيدًا عندما يحتوي حقل الصفوف أو الأعمدة في الجدول المحوري على العديد من العناصر المتميزة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على العديد من القيم المتناثرة. يعمل التجميع على طي هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر وأرباع وسنوات، والأرقام إلى نطاقات مثل 0-1 و2-3 و4-5. هذا يجعل الجدول المحوري الكبير مدمجًا وأسهل في التحليل. يوفر Aspose.Cells for Python via .NET هذه الإمكانية من خلال الطريقة `pivot_field.group()` (التجميع التلقائي حسب نوع البيانات) و`pivot_field.group(pivot_field_group_options)` (خيارات التجميع المخصصة).
- يعمل تجميع التواريخ على تجميع التواريخ الفردية في فترات زمنية أكبر، مثل الأيام والأشهر والأرباع والسنوات، وبناء تسلسل هرمي زمني (على سبيل المثال السنوات، الأرباع، الأشهر). تصبح الاتجاهات عبر الزمن واضحة للعين، وتصبح كل فترة مستوى حقلًا محوريًا خاصًا بها في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- يتوفر التجميع فقط للحقول الموضوعة في منطقة الصفوف أو الأعمدة في الجدول المحوري. لا يمكن تجميع حقل البيانات (القيمة) مباشرةً. لتجميع مثل هذا الحقل، يجب عليك أولاً إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع حقول الجدول المحوري تلقائيًا**
تقوم النسخة المحمّلة `pivot_field.group()` بدون معاملات بفحص نوع بيانات الحقل وتجميعه تلقائيًا. يتم تجميع الحقل الذي يحتوي فقط على تواريخ (وقيم فارغة) حسب الأشهر. يتم تجميع الحقل الذي يحتوي فقط على أرقام (وقيم فارغة) في نطاقات رقمية باستخدام فاصل زمني تلقائي.

```python
import aspose.cells as ac
# تحميل ملف العمل النموذجي
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# الوصول إلى ورقة العمل الثانية والجدول المحوري الخاص بها
pt = wb.worksheets[1].pivot_tables[0]
# تجميع حقل الصف الأول تلقائيًا.
# يحتوي الحقل على تواريخ، لذلك يتم تجميعها حسب الأشهر.
field = pt.row_fields[0]
field.group()
# حساب بيانات الجدول المحوري وحفظ ملف الإخراج
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **تجميع حقول الجدول المحوري بخيارات مخصصة**
توفر فئة `PivotFieldGroupOptions` إعدادات تجميع مخصصة. بالنسبة لحقول التواريخ، قم بتعيين `start_date` و`end_date` و`group_types`. بالنسبة للحقول الرقمية، قم بتعيين `start_number` و`end_number` و`interval`. تتحكم الخاصية `new_pivot_field` في ما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع**
يقوم المثال التالي بتجميع حقل تاريخ الصف في الجدول المحوري النموذجي حسب الأشهر والأرباع بين تاريخ بداية ونهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وتنفيذ التجميع، وحساب بيانات الجدول المحوري، وحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: تم الآن تجميع حقل تاريخ الصف حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.group_types` يتم تجاهله. بغض النظر عن الترتيب الذي يتم فيه سرد أنواع المجموعات، يتم دائمًا عرض الحقول المجمعة من أكبر فترة إلى أصغر: السنوات، الأرباع، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال يتم سرد الأشهر قبل الأرباع في `options.group_types`، ومع ذلك يتم عرض الأرباع كمستوى خارجي والأشهر كمستوى داخلي.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# تحميل ملف العمل النموذجي
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
pt = wb.worksheets[1].pivot_tables[0]
# تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والأرباع
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![جدول محوري مجمع حسب الأشهر والأرباع](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي في نطاقات**
يعد `FieldTwo` في الجدول المحوري النموذجي في البداية حقل بيانات (قيمة). نظرًا لأنه يمكن تجميع حقول الصفوف أو الأعمدة فقط، يستدعي الكود أولاً `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يقوم بتحديث الجدول المحوري، ثم تجميع الحقل الرقمي في النطاقات 0-1 و2-3 و4-5 باستخدام `start_number=0` و`end_number=5` و`interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# تحميل المصنف النموذجي
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo هو حقل بيانات: انقله إلى منطقة الصفوف أولاً،
# لأنه يمكن تجميع حقول الصفوف/الأعمدة فقط
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# تجميع الحقل الرقمي في النطاقات 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إيقاف نسخ الطريقة `pivot_field.group_by()` المحمّلة وإزالتها من واجهة API. تعد `pivot_field.group()` و`pivot_field.group(pivot_field_group_options)` البدائل.
- في Microsoft Excel، يستبدل تجميع حقل رقمي الحقل المحوري الأصلي بنطاقات مجمعة، بينما ينشئ تجميع حقل تاريخ حقولاً محورية جديدة (واحدة لكل مستوى مجموعة، على سبيل المثال الأرباع والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع طرق `pivot_field.group()` نفس سلوك Excel. توجد الخاصية `PivotFieldGroupOptions.new_pivot_field` للتوافق مع الإصدارات الأقدم: تكون قيمتها الافتراضية false لتجميع الأرقام وtrue لتجميع التاريخ والوقت؛ قم بتعيينها إلى false إذا كنت تريد أن يستبدل تجميع التاريخ الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- تأخذ الخاصية `PivotFieldGroupOptions.interval` تأثيرها فقط لتجميع الأرقام ولتجميع التواريخ حسب الأيام (على سبيل المثال، تجميع التواريخ في فترات 7 أيام)؛ يتم تجاهلها عندما يتم تجميع التواريخ حسب الأشهر أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/python-net/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-net/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/python-net/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-net/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}