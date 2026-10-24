---
title: تجميع الحقول المحورية في الجدول المحوري
linktitle: تجميع الحقول المحورية في الجدول المحوري
description: تعلّم كيفية تجميع حقول الصفوف والأعمدة للجدول المحوري في فترات زمنية مثل الأشهر والأرباع المالية ونطاقات رقمية باستخدام PivotField.group و PivotFieldGroupOptions في Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, جدول محوري, تجميع حقل محوري, PivotField.group, PivotFieldGroupOptions, تجميع التواريخ, تجميع الأرقام, أشهر, أرباع مالية, نطاق رقمي, Node.js
type: docs
weight: 80
url: /ar/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يكون تجميع الحقول المحورية مفيدًا عندما يحتوي حقل الصفوف أو الأعمدة في الجدول المحوري على عناصر مميزة كثيرة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يعمل التجميع على طي هذه العناصر في أقسام ذات معنى: التواريخ في أشهر وأرباع مالية وسنوات، والأرقام في نطاقات مثل 0-1 و 2-3 و 4-5. هذا يجعل الجدول المحوري الكبير مضغوطًا وأسهل في التحليل. يوفر Aspose.Cells for Node.js via Java هذه الإمكانية من خلال الطريقة `PivotField.group()` (التجميع التلقائي حسب نوع البيانات) و `PivotField.group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يقوم تجميع التواريخ بجمع التواريخ الفردية في فترات أكبر مثل الأيام والأشهر والأرباع المالية والسنوات، ويبني تسلسلًا هرميًا زمنيًا (مثل السنوات، الأرباع المالية، الأشهر). تصبح الاتجاهات على مر الزمن واضحة للوهلة الأولى، وتصبح كل مستوى فترة حقلًا محوريًا خاصًا به في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- لا يتوفر التجميع إلا للحقول الموضوعة في منطقة الصفوف أو الأعمدة في الجدول المحوري. لا يمكن تجميع حقل بيانات (قيمة) مباشرةً. لتجميع حقل كهذا يجب عليك أولًا إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
تفحص النسخة المحمَّلة بدون معاملات من `PivotField.group()` نوع بيانات الحقل وتجمعه تلقائيًا. يتم تجميع الحقل الذي يحتوي على تواريخ فقط (وفراغات) حسب الأشهر. يتم تجميع الحقل الذي يحتوي على أرقام فقط (وفراغات) في نطاقات رقمية باستخدام فاصل تلقائي.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// تجميع حقل الصف الأول تلقائيًا.
// الحقل يحتوي على تواريخ، لذلك يتم تجميعه حسب الأشهر.
let field = pt.getRowFields().get(0);
field.group();
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **تجميع الحقول المحورية بخيارات مخصصة**
توفر الفئة `PivotFieldGroupOptions` تكوين تجميع مخصصًا. بالنسبة للحقول الزمنية، عيّن `StartDate` و `EndDate` و `GroupTypes`. وبالنسبة للحقول الرقمية، عيّن `StartNumber` و `EndNumber` و `Interval`. تتحكم الخاصية `NewPivotField` في ما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظات في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع المالية**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري للعينة حسب الأشهر والأرباع المالية بين تاريخ بداية وتاريخ نهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وينفذ التجميع، ويحسب بيانات الجدول المحوري، ويحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: أصبح حقل صف التاريخ الآن مجمعًا حسب الأرباع المالية والأشهر.
لاحظ أن ترتيب القيم في `options.GroupTypes` يتم تجاهله. بصرف النظر عن الترتيب الذي تُذكر فيه أنواع المجموعات، تُعرض الحقول المجمعة دائمًا من أكبر فترة إلى أصغر فترة: السنوات، الأرباع المالية، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال تُذكر الأشهر قبل الأرباع المالية في `options.GroupTypes`، ومع ذلك تُعرض الأرباع المالية كمستوى خارجي والأشهر كمستوى داخلي.

```javascript
const AsposeCells = require("aspose.cells");
// تحميل دفتر العمل النموذجي
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية والجدول المحوري الخاص بها
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والأرباع
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// حساب بيانات الجدول المحوري وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![جدول محوري مجمع حسب الأشهر والأرباع المالية](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي في نطاقات**
يُعدّ `FieldTwo` في الجدول المحوري للعينة في البداية حقل بيانات (قيمة). نظرًا لأنه لا يمكن تجميع سوى حقول الصفوف أو الأعمدة، يستدعي الكود أولًا `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يُحدّث الجدول المحوري، ثم يجمع الحقل الرقمي في النطاقات 0-1 و 2-3 و 4-5 باستخدام `StartNumber = 0` و `EndNumber = 5` و `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// تحميل مصنف العينة
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول محوري فيها
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo هو حقل بيانات: انقله إلى منطقة الصفوف أولاً،
// لأنه فقط حقول الصفوف/الأعمدة يمكن تجميعها
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// تجميع الحقل الرقمي في النطاقات 0-1، 2-3، 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// حساب بيانات الجدول المحوري وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إيقاف النُسخ المحمَّلة زيادةً من `PivotField.GroupBy()` وإزالتها من واجهة الـ API. تُعدّ `PivotField.group()` و `PivotField.group(PivotFieldGroupOptions)` البديل.
- في Microsoft Excel، يستبدل تجميع حقل رقمي الحقل المحوري الأصلي بالنطاقات المجمعة، بينما ينشئ تجميع حقل تاريخ حقولاً محورية جديدة (واحد لكل مستوى مجموعة، مثل الأرباع المالية والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells for Node.js via Java 26.10، تتبع طرائق `PivotField.group()` نفس السلوك المتبع في Excel. توجد الخاصية `PivotFieldGroupOptions.NewPivotField` للتوافق مع الإصدارات الأقدم: تكون قيمتها الافتراضية false لتجميع الأرقام و true لتجميع التاريخ والوقت؛ عيّنها على false إذا أردت أن يحل تجميع التاريخ محل الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- تأخذ الخاصية `PivotFieldGroupOptions.Interval` مفعولها فقط في التجميع الرقمي وفي تجميع التواريخ حسب الأيام (مثلًا، تجميع التواريخ في فترات مدتها 7 أيام)؛ ويتم تجاهلها عندما تُجمع التواريخ حسب الأشهر أو الأرباع المالية أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/nodejs-java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/nodejs-java/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}