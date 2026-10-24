---
title: تجميع الحقول المحورية في الجدول المحوري
linktitle: تجميع الحقول المحورية في الجدول المحوري
description: تعرف على كيفية تجميع الحقول المحورية للصفوف والأعمدة في الجدول المحوري إلى فترات زمنية مثل الأشهر والأرباع ونطاقات رقمية باستخدام PivotField.group وPivotFieldGroupOptions في Aspose.Cells for Java.
keywords: Aspose.Cells, جدول محوري, تجميع الحقول المحورية, PivotField.group, PivotFieldGroupOptions, تجميع التواريخ, تجميع الأرقام, الأشهر, الأرباع, النطاق الرقمي, Java
type: docs
weight: 80
url: /ar/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **سيناريوهات الاستخدام المحتملة**
- يُعد تجميع الحقول المحورية مفيدًا عندما يحتوي حقل الصفوف أو حقل الأعمدة في الجدول المحوري على عناصر متعددة ومميزة، مثل حقل تاريخ يحتوي على مئات التواريخ أو حقل رقمي يحتوي على قيم متفرقة كثيرة. يدمج التجميع هذه العناصر في أقسام ذات معنى: التواريخ إلى أشهر وأرباع وسنوات، والأرقام إلى نطاقات مثل `0-1` و`2-3` و`4-5`. يجعل ذلك الجدول المحوري الكبير مضغوطًا وأسهل في التحليل. يوفر Aspose.Cells هذه الإمكانية من خلال طريقة `PivotField.group()` (التجميع التلقائي حسب نوع البيانات) و`PivotField.group(PivotFieldGroupOptions)` (خيارات التجميع المخصصة).
- يحوّل تجميع التواريخ التواريخ الفردية إلى فترات أكبر، مثل الأيام والأشهر والأرباع والسنوات، ويُنشئ تسلسلًا هرميًا زمنيًا (على سبيل المثال السنوات، الأرباع، الأشهر). تصبح الاتجاهات عبر الوقت مرئية بنظرة واحدة، وتصبح كل مستوى من الفترات حقلاً محوريًا خاصًا به في منطقة الصفوف أو الأعمدة في الجدول المحوري.
- يتوفر التجميع فقط للحقول الموضوعة في منطقة الصفوف (ROW) أو الأعمدة (COLUMN) في الجدول المحوري. لا يمكن تجميع حقل البيانات (القيمة) مباشرة. لتجميعه يجب أولًا إضافته إلى منطقة الصفوف أو الأعمدة في الجدول المحوري.

## **تجميع الحقول المحورية تلقائيًا**
يفحص التحميل الزائد `PivotField.group()` الذي لا يقبل معاملات نوع بيانات الحقل ويجمعه تلقائيًا. الحقل الذي يحتوي على تواريخ فقط (وفراغات) يُجمع حسب الأشهر. والحقل الذي يحتوي على أرقام فقط (وفراغات) يُجمع إلى نطاقات رقمية باستخدام فاصل تلقائي.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **تجميع الحقول المحورية بخيارات مخصصة**
توفر فئة `PivotFieldGroupOptions` تكوين التجميع المخصص. لحقول التواريخ، عيّن `startDate` و`endDate` و`groupTypes`. أما للحقول الرقمية، فعليك تعيين `startNumber` و`endNumber` و`interval`. تتحكم الخاصية `newPivotField` فيما إذا كان التجميع ينشئ حقولاً محورية جديدة بجانب الحقل الأصلي (راجع قسم الملاحظة في نهاية هذه المقالة).

### **تجميع حقل تاريخ حسب الأشهر والأرباع**
يجمع المثال التالي حقل صف التاريخ في الجدول المحوري النموذجي حسب الأشهر والأرباع بين تاريخ بداية ونهاية. يقوم الكود بتحميل [ملف Excel النموذجي](sampleGroupPivotFieldsInPivotTable.xlsx)، وتنفيذ التجميع، وحساب بيانات الجدول المحوري، وحفظ النتيجة المجمعة. تُظهر لقطة الشاشة التأثير: أصبح حقل صف التاريخ الآن مُجمعًا حسب الأرباع والأشهر.
لاحظ أن ترتيب القيم في `options.groupTypes` يتم تجاهله. بغض النظر عن الترتيب الذي تُسرد به أنواع المجموعات، يتم دائمًا عرض الحقول المجمعة من أكبر فترة إلى أصغرها: السنوات، الأرباع، الأشهر، الأيام، الساعات، الدقائق، الثواني. في هذا المثال تم ذكر الأشهر قبل الأرباع في `options.groupTypes`، ومع ذلك يتم عرض الأرباع كمستوى خارجي والأشهر كمستوى داخلي.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![الجدول المحوري مُجمع حسب الأشهر والأرباع](group-pivot-fields-in-the-pivot-table_1.png)

### **تجميع حقل رقمي إلى نطاقات**
يعد `FieldTwo` في الجدول المحوري النموذجي حقل بيانات (قيمة) في البداية. نظرًا لأن التجميع متاح فقط لحقول الصفوف أو الأعمدة، يستدعي الكود أولًا `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` لنقل `FieldTwo` إلى منطقة الصفوف، ثم يُحدّث الجدول المحوري، ثم يجمع الحقل الرقمي إلى النطاقات `0-1` و`2-3` و`4-5` باستخدام `startNumber = 0` و`endNumber = 5` و`interval = 2`.

```java
import com.aspose.cells.*;
// تحميل المصنف النموذجي
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// الوصول إلى ورقة العمل الثانية وجدول المحور الخاص بها
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo هو حقل بيانات: انقله إلى منطقة الصفوف أولاً،
// لأنه يمكن تجميع حقول الصفوف/الأعمدة فقط
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// تجميع الحقل الرقمي إلى النطاقات 0-1، 2-3، 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
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
- تم إهمال التحميلات الزائدة لطريقة `PivotField.groupBy()` وإزالتها من واجهة الـAPI. تعتبر `PivotField.group()` و`PivotField.group(PivotFieldGroupOptions)` البدائل.
- في Microsoft Excel، عند تجميع حقل رقمي يستبدل التجميع الحقل المحوري الأصلي بنطاقات مجمعة، بينما ينشئ تجميع حقل التاريخ حقولاً محورية جديدة (واحد لكل مستوى مجموعة، مثل الأرباع والأشهر) بجانب الحقل الأصلي. بدءًا من Aspose.Cells 26.10، تتبع طرق `PivotField.group()` نفس سلوك Excel. توجد الخاصية `PivotFieldGroupOptions.newPivotField` للتوافق مع الإصدارات الأقدم: قيمتها الافتراضية false لتجميع الأرقام وtrue لتجميع التاريخ والوقت؛ عيّنها إلى false إذا كنت تريد أن يحلّ تجميع التواريخ محل الحقل المحوري الأصلي بدلاً من إنشاء حقول محورية جديدة.
- تسري الخاصية `PivotFieldGroupOptions.interval` فقط لتجميع الأرقام ولتجميع التواريخ حسب الأيام (على سبيل المثال، تجميع التواريخ في فترات مدتها 7 أيام)، ويتم تجاهلها عند تجميع التواريخ حسب الأشهر أو الأرباع أو السنوات.
{{% /alert %}}

## **مقالات ذات صلة**
- [إضافة حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/java/pivot-table-add-row-and-column-fields/)
- [تصفية الجداول المحورية حسب التسمية أو القيمة](/cells/ar/java/filter-by-label-or-value-of-pivot-table/)
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/java/add-page-field-in-pivot-table/)
- [تطبيق نمط على الجدول المحوري](/cells/ar/java/apply-style-to-pivot-table/)
- [تحديث الجدول المحوري](/cells/ar/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}