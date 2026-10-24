---
title: تجميع حقول الجدول المحوري في الجدول المحوري
linktitle: تجميع حقول الجدول المحوري في الجدول المحوري
description: تعلّم كيفية تجميع حقول الصفوف والأعمدة المحورية في جدول محوري إلى فترات زمنية مثل الأشهر والأرباع السنوية ونطاقات رقمية باستخدام PivotField.group و PivotFieldGroupOptions في Aspose.Cells for Python عبر Java.
keywords: Aspose.Cells, جدول محوري, تجميع حقل محوري, PivotField.group, PivotFieldGroupOptions, تجميع التواريخ, تجميع الأرقام, أشهر, أرباع سنة, نطاق رقمي, Python
type: docs
weight: 80
url: /ar/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يكون تجميع الحقول المحورية مفيدًا عندما يحتوي حقل الصفوف أو الأعمدة في جدول محوري على عناصر متعددة ومتباينة، مثل حقل تواريخ يحتوي على مئات التواريخ، أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يجمع التجميع هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر وأرباع سنة وسنوات، والأرقام إلى نطاقات مثل 0-1 و2-3 و4-5. وبهذا يصبح الجدول المحوري الكبير مدمجًا وأسهل في التحليل. توفر Aspose.Cells هذه الإمكانية من خلال طريقة `PivotField.group()` (التجميع التلقائي حسب نوع البيانات) و`PivotField.group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يقوم تجميع التواريخ بلفّ التواريخ الفردية في فترات زمنية أكبر، مثل الأيام والأشهر والأرباع السنوية والسنوات، وبناء تسلسل هرمي زمني (مثل السنوات والأرباع والأشهر). وتصبح الاتجاهات عبر الزمن واضحة بنظرة واحدة، وتصبح كل فترة زمنية حقلاً محوريًا مستقلًا في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- يتوفر التجميع فقط للحقول الموضوعة في منطقة الصفوف أو الأعمدة في الجدول المحوري. لا يمكن تجميع حقل بيانات (قيمة) مباشرة. لتجميع حقل كهذا يجب أولًا إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
يفحص الحمل الزائد `PivotField.group()` بلا معاملات نوع بيانات الحقل ويجمعه تلقائيًا. الحقل الذي يحتوي على تواريخ فقط (وفارغات) يُجمع حسب الأشهر. والحقل الذي يحتوي على أرقام فقط (وفارغات) يُجمع في نطاقات رقمية بفاصل تلقائي.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# تحميل مصنف العينة
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# تجميع حقل الصف الأول تلقائيًا.
# يحتوي الحقل على تواريخ، لذلك يتم تجميعها حسب الأشهر.
field = pt.getRowFields().get(0)
field.group()
# حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **تجميع الحقول المحورية بخيارات مخصصة**
توفر فئة `PivotFieldGroupOptions` إعدادات تجميع مخصصة. لحقول التواريخ، عيّن `StartDate` و`EndDate` و`GroupTypes`. وللحقول الرقمية، عيّن `StartNumber` و`EndNumber` و`Interval`. تتحكم الخاصية `NewPivotField` في ما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع السنوية**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري النموذجي حسب الأشهر والأرباع السنوية بين تاريخ بداية وتاريخ نهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وإجراء التجميع، وحساب بيانات الجدول المحوري، وحفظ النتيجة المُجمَّعة. تُظهر لقطة الشاشة التأثير: حقل صف التاريخ مُجمَّع الآن حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.GroupTypes` يتم تجاهله. بصرف النظر عن الترتيب الذي تُسرد به أنواع المجموعات، تُعرض الحقول المُجمَّعة دائمًا من أكبر فترة زمنية إلى الأصغر: السنوات، الأرباع، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال تُسرد الأشهر قبل الأرباع في `options.GroupTypes`، ومع ذلك تُعرض الأرباع كمستوى خارجي والأشهر كمستوى داخلي.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# تحميل مصنف العينة
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# الوصول إلى ورقة العمل الثانية والجدول المحوري الخاص بها
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والأرباع
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# حساب بيانات الجدول المحوري وحفظ ملف الإخراج
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![جدول محوري مُجمَّع حسب الأشهر والأرباع السنوية](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي في نطاقات**
`FieldTwo` في الجدول المحوري النموذجي هو في البداية حقل بيانات (قيمة). ولأن حقول الصفوف أو الأعمدة فقط هي التي يمكن تجميعها، يستدعي الكود أولًا `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يقوم بتحديث الجدول المحوري، ثم يجمع الحقل الرقمي في النطاقات 0-1 و2-3 و4-5 باستخدام `StartNumber = 0` و`EndNumber = 5` و`Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Load the sample workbook
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Access the second worksheet and its pivot table
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo is a data field: move it to the row area first,
# because only row/column fields can be grouped
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Group the numeric field into the ranges 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Calculate the pivot table data and save the output file
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إيقاف الأحمال الزائدة لطريقة `PivotField.groupBy()` وإزالتها من واجهة الـ API. تعد `PivotField.group()` و`PivotField.group(PivotFieldGroupOptions)` البدائل.
- في Microsoft Excel، يستبدل تجميع حقل رقمي الحقل المحوري الأصلي بنطاقات مُجمَّعة، بينما ينشئ تجميع حقل تاريخ حقولاً محورية جديدة (واحدة لكل مستوى مجموعة، مثل الأرباع والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع طرق `PivotField.group()` نفس سلوك Excel. توجد الخاصية `PivotFieldGroupOptions.NewPivotField` للتوافق مع الإصدارات الأقدم: قيمتها الافتراضية هي false لتجميع الأرقام وtrue لتجميع التاريخ والوقت؛ اضبطها على false إذا كنت تريد أن يحل تجميع التواريخ محل الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- لا تسري الخاصية `PivotFieldGroupOptions.Interval` إلا على تجميع الأرقام وتجميع التواريخ حسب الأيام (مثل تجميع التواريخ في فترات 7 أيام)؛ ويتم تجاهلها عندما تُجمع التواريخ حسب الأشهر أو الأرباع السنوية أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/python-java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/python-java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/python-java/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/python-java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}