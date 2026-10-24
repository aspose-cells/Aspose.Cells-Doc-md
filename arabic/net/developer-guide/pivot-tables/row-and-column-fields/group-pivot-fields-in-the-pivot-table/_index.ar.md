---
title: تجميع الحقول المحورية في الجدول المحوري
linktitle: تجميع الحقول المحورية في الجدول المحوري
description: تعلّم كيفية تجميع حقول الصفوف والأعمدة المحورية في الجدول المحوري ضمن فترات زمنية مثل الأشهر والأرباع السنوية ونطاقات رقمية باستخدام PivotField.Group وPivotFieldGroupOptions في Aspose.Cells for .NET.
keywords: Aspose.Cells, جدول محوري, تجميع الحقول المحورية, PivotField.Group, PivotFieldGroupOptions, تجميع حسب التاريخ, تجميع حسب الأرقام, أشهر, أرباع سنوية, نطاق رقمي, C#
type: docs
weight: 80
url: /ar/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يُعد تجميع الحقول المحورية مفيدًا عندما يحتوي حقل صف أو عمود في الجدول المحوري على عناصر متعددة ومميزة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يعمل التجميع على دمج هذه العناصر في أقسام ذات معنى: التواريخ تتحول إلى أشهر وأرباع السنوات والسنوات، والأرقام تتحول إلى نطاقات مثل 0-1 و2-3 و4-5. هذا يجعل الجدول المحوري الكبير مدمجًا وأسهل في التحليل. يوفر Aspose.Cells هذه الإمكانية من خلال طريقة `PivotField.Group()` (التجميع التلقائي حسب نوع البيانات) و`PivotField.Group(PivotFieldGroupOptions)` (خيارات تجميع مخصصة).
- يقوم تجميع التواريخ بترتيب التواريخ الفردية إلى فترات أكبر مثل الأيام والأشهر والأرباع السنوية والسنوات، ويبني تسلسلًا زمنيًا هرميًا (مثل السنوات والأرباع والأشهر). تظهر الاتجاهات بمرور الوقت بشكل واضح للوهلة الأولى، ويصبح كل مستوى من مستويات الفترة حقلاً محوريًا مستقلاً في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- لا يتوفر التجميع إلا للحقول الموضوعة في منطقة الصفوف أو الأعمدة في الجدول المحوري. لا يمكن تجميع حقل البيانات (القيمة) مباشرةً. لتجميع مثل هذا الحقل، يجب عليك أولاً إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
يفحص الأسلوب الزائد `PivotField.Group()` بدون معاملات نوع بيانات الحقل ويجمعه تلقائيًا. يتم تجميع الحقل الذي يحتوي على التواريخ فقط (والفراغات) حسب الأشهر. يتم تجميع الحقل الذي يحتوي على الأرقام فقط (والفراغات) في نطاقات رقمية باستخدام فاصل زمني تلقائي.

```csharp
// تحميل ملف العمل النموذجي
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// تجميع حقل الصف الأول تلقائياً.
// يحتوي الحقل على تواريخ، لذا يتم تجميعها حسب الأشهر.
PivotField field = pt.RowFields[0];
field.Group();
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **تجميع الحقول المحورية بخيارات مخصصة**
يوفر الفئة `PivotFieldGroupOptions` إعدادات تجميع مخصصة. بالنسبة لحقول التاريخ، حدد `StartDate` و`EndDate` و`GroupTypes`. بالنسبة للحقول الرقمية، حدد `StartNumber` و`EndNumber` و`Interval`. تتحكم خاصية `NewPivotField` فيما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع السنوية**
يقوم المثال التالي بتجميع حقل صف التاريخ في الجدول المحوري النموذجي حسب الأشهر والأرباع السنوية بين تاريخ بداية ونهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وإجراء التجميع، وحساب بيانات الجدول المحوري، وحفظ النتيجة المجمعة. تظهر اللقطة التأثير: أصبح حقل صف التاريخ الآن مجمعًا حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.GroupTypes` يتم تجاهله. بصرف النظر عن الترتيب الذي يتم فيه سرد أنواع المجموعات، يتم دائمًا عرض الحقول المجمعة من أكبر فترة إلى أصغرها: السنوات، الأرباع، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال تم سرد الأشهر قبل الأرباع في `options.GroupTypes`، ومع ذلك يتم عرض الأرباع كمستوى خارجي والأشهر كمستوى داخلي.

```csharp
// تحميل مصنف العينة
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية والجدول المحوري الخاص بها
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// تجميع حقل الصف الأول (حقل تاريخ) حسب الأشهر والأرباع
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// حساب بيانات الجدول المحوري وحفظ ملف الإخراج
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![جدول محوري مجمع حسب الأشهر والأرباع السنوية](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي في نطاقات**
يعد `FieldTwo` في الجدول المحوري النموذجي حقل بيانات (قيمة) في البداية. ولأن حقول الصفوف أو الأعمدة فقط هي التي يمكن تجميعها، يستدعي الكود أولاً `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، وتحديث الجدول المحوري، ثم تجميع الحقل الرقمي في النطاقات 0-1 و2-3 و4-5 باستخدام `StartNumber = 0` و`EndNumber = 5` و`Interval = 2`.

```csharp
// تحميل مصنف العينة
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo هو حقل بيانات: انقله أولاً إلى منطقة الصفوف،
// لأن فقط حقول الصفوف/الأعمدة يمكن تجميعها
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// تجميع الحقل الرقمي إلى النطاقات 0-1، 2-3، 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// حساب بيانات جدول المحور وحفظ ملف الإخراج
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **ملاحظة**

{{% alert color="primary" %}}
- تم إيقاف وسائل التحميل الزائدة لطريقة `PivotField.GroupBy()` وإزالتها من سطح واجهة برمجة التطبيقات. تُعد `PivotField.Group()` و`PivotField.Group(PivotFieldGroupOptions)` البدائل.
- في Microsoft Excel، يقوم تجميع حقل رقمي باستبدال الحقل المحوري الأصلي بالنطاقات المجمعة، بينما ينشئ تجميع حقل تاريخ حقولاً محورية جديدة (حقل لكل مستوى تجميع، مثل الأرباع والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع وسائل `PivotField.Group()` نفس سلوك Excel. توجد خاصية `PivotFieldGroupOptions.NewPivotField` للتوافق مع الإصدارات الأقدم: تكون قيمتها الافتراضية false للتجميع الرقمي وtrue للتجميع حسب التاريخ والوقت؛ اضبطها على false إذا كنت تريد أن يحل تجميع التاريخ محل الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- لا تعمل خاصية `PivotFieldGroupOptions.Interval` إلا للتجميع الرقمي وتجميع التاريخ حسب الأيام (مثل تجميع التواريخ في فترات 7 أيام)؛ ويتم تجاهلها عند تجميع التواريخ حسب الأشهر أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/net/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/net/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/net/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/net/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}