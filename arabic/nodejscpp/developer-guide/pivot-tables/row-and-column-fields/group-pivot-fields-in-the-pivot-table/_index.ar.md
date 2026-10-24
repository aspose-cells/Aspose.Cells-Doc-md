---
title: تجميع حقول المحور في الجدول المحوري
description: تعلّم كيفية تجميع حقول محور الصفوف والأعمدة في جدول محوري إلى فترات زمنية مثل الأشهر والأرباع الماليات ونطاقات رقمية باستخدام PivotField.Group و PivotFieldGroupOptions في Aspose.Cells for Node.js via C++.
linktitle: تجميع حقول المحور
keywords: Aspose.Cells, الجدول المحوري, تجميع حقل محور, PivotField.Group, PivotFieldGroupOptions, تجميع حسب التاريخ, تجميع حسب الأرقام, الأشهر, الأرباع الماليات, النطاق الرقمي, JavaScript
type: docs
weight: 80
url: /ar/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام الممكنة**
- يكون تجميع حقول المحور مفيدًا عندما يحتوي حقل صف أو عمود في جدول محوري على العديد من العناصر المميزة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على العديد من القيم المتفرقة. يعمل التجميع على طي هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر وأرباع ماليات وسنوات، والأرقام إلى نطاقات مثل 0-1، 2-3، 4-5. يجعل ذلك الجدول المحوري الكبير مضغوطًا وأسهل في التحليل. توفر Aspose.Cells هذه الإمكانية من خلال `pivotField.group()` (التجميع التلقائي حسب نوع البيانات) و `pivotField.group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يعمل تجميع التواريخ على تجميع التواريخ الفردية في فترات أكبر، مثل الأيام والأشهر والأرباع الماليات والسنوات، وبناء تسلسل زمني هرمي (على سبيل المثال السنوات، الأرباع الماليات، الأشهر). تصبح الاتجاهات بمرور الوقت مرئية بنظرة واحدة، ويصبح كل مستوى فترة حقل محور خاص به في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- يتوفر التجميع فقط للحقول الموضوعة في منطقة الصفوف أو الأعمدة في جدول محوري. لا يمكن تجميع حقل بيانات (قيمة) مباشرةً. لتجميع مثل هذا الحقل، يجب عليك أولاً إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع حقول المحور تلقائيًا**
يفحص إصدار التحميل الزائد لـ `pivotField.group()` بدون معاملات نوع بيانات الحقل ويجمعه تلقائيًا. يتم تجميع الحقل الذي يحتوي فقط على تواريخ (وخلايا فارغة) حسب الأشهر. يتم تجميع الحقل الذي يحتوي فقط على أرقام (وخلايا فارغة) إلى نطاقات رقمية باستخدام فاصل زمني تلقائي.

```javascript
const AsposeCells = require("aspose.cells.node");
// تحميل ملف العمل النموذجي
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// تجميع حقل الصف الأول تلقائياً.
// يحتوي الحقل على تواريخ، لذلك يتم تجميعها حسب الأشهر.
const field = pt.getRowFields().get(0);
field.group();
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **تجميع حقول المحور باستخدام خيارات مخصصة**
توفر الفئة `PivotFieldGroupOptions` تكوين التجميع المخصص. لحقول التاريخ، عيّن `startDate` و `endDate` و `groupTypes`. للحقول الرقمية، عيّن `startNumber` و `endNumber` و `interval`. تتحكم الخاصية `newPivotField` فيما إذا كان التجميع ينشئ حقول محور جديدة بجانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع الماليات**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري للعينة حسب الأشهر والأرباع الماليات بين تاريخ بدء وانتهاء. يقوم الكود بتحميل [ملف Excel للعينة](sampleGroupPivotFieldsInPivotTable.xlsx)، وينفذ التجميع، ويحسب بيانات الجدول المحوري، ويحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: تم الآن تجميع حقل صف التاريخ حسب الأرباع الماليات والأشهر. لاحظ أنه يتم تجاهل ترتيب القيم في `options.groupTypes`. بغض النظر عن الترتيب الذي تُدرج به أنواع المجموعات، يتم دائمًا عرض الحقول المجمعة من أكبر فترة إلى أصغر: السنوات، الأرباع الماليات، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال، تم إدراج الأشهر قبل الأرباع الماليات في `options.groupTypes`، ومع ذلك يتم عرض الأرباع الماليات كمستوى خارجي والأشهر كمستوى داخلي.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والأرباع
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![جدول محوري مجمع حسب الأشهر والأرباع الماليات](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي إلى نطاقات**
يكون `FieldTwo` في الجدول المحوري للعينة في البداية حقل بيانات (قيمة). نظرًا لأنه يمكن تجميع حقول الصفوف أو الأعمدة فقط، يستدعي الكود أولاً `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ويُحدّث المحور، ثم يجمع الحقل الرقمي في النطاقات 0-1 و 2-3 و 4-5 باستخدام `startNumber = 0` و `endNumber = 5` و `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo هو حقل بيانات: انقله إلى منطقة الصفوف أولاً،
// لأنه يمكن فقط تجميع الحقول الموجودة في الصفوف/الأعمدة
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// تجميع الحقل الرقمي إلى النطاقات 0-1، 2-3، 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إيقاف تحميلات طرق `pivotField.groupBy()` وإزالتها من سطح واجهة برمجة التطبيقات. `pivotField.group()` و `pivotField.group(PivotFieldGroupOptions)` هما البديلان.
- في Microsoft Excel، يستبدل تجميع حقل رقمي حقل المحور الأصلي بنطاقات مجمعة، بينما ينشئ تجميع حقل تاريخ حقول محور جديدة (واحدة لكل مستوى مجموعة، على سبيل المثال الأرباع الماليات والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع طرق `pivotField.group()` نفس سلوك Excel. توجد الخاصية `pivotFieldGroupOptions.newPivotField` للتوافق مع الإصدارات الأقدم: يتم تعيينها افتراضيًا على false للتجميع الرقمي و true للتجميع حسب التاريخ والوقت؛ اضبطها على false إذا كنت تريد أن يستبدل تجميع التاريخ حقل المحور الأصلي بدلاً من إنشاء حقول محور جديدة.
- تأخذ الخاصية `pivotFieldGroupOptions.interval` مفعولها فقط للتجميع الرقمي وللتجميع حسب التاريخ بالأيام (على سبيل المثال، تجميع التواريخ في فترات 7 أيام)؛ يتم تجاهلها عند تجميع التواريخ حسب الأشهر أو الأرباع الماليات أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/nodejs-cpp/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/nodejs-cpp/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/nodejs-cpp/refresh-pivot-table/)
Count of code fences: 0 (since they're all replaced by placeholders) ✅
Alert block has balanced open and close tags ✅

### **تجميع حقل تاريخ حسب الأشهر والأرباع المالية**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري للعينة حسب الأشهر والأرباع المالية بين تاريخ بدء وانتهاء. يقوم الكود بتحميل [ملف Excel للعينة](sampleGroupPivotFieldsInPivotTable.xlsx)، وينفذ التجميع، ويحسب بيانات الجدول المحوري، ويحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: تم الآن تجميع حقل صف التاريخ حسب الأرباع المالية والأشهر. لاحظ أنه يتم تجاهل ترتيب القيم في `options.groupTypes`. بغض النظر عن الترتيب الذي تُدرج به أنواع المجموعات، يتم دائمًا عرض الحقول المجمعة من أكبر فترة إلى أصغر: السنوات، الأرباع المالية، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال، تم إدراج الأشهر قبل الأرباع المالية في `options.groupTypes`، ومع ذلك يتم عرض الأرباع المالية كمستوى خارجي والأشهر كمستوى داخلي.![جدول محوري مجمع حسب الأشهر والأرباع المالية](group-pivot-fields-in-the-pivot-table_1.png)

{{< app/cells/assistant language="nodejs-cpp" >}}