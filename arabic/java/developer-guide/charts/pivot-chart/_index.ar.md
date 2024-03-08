---
title: كيفية إضافة PivotChart باستخدام Aspose.Cells
linktitle: مخطط بياني محوري
type: docs
weight: 100
url: /ar/java/how-to-add-pivot-chart/
description: كيفية إضافة PivotChart باستخدام Aspose.Cells.
keywords: PivotChart
---
##  ما هو التخطيط المحوري

يعد PivotChart في Excel تمثيلاً رسوميًا للبيانات التي تم إنشاؤها من PivotTable. فهو يسمح للمستخدمين بتصور البيانات وتحليلها ديناميكيًا من خلال تلخيص المعلومات وعرضها في شكل مخطط. تعتبر PivotCharts تفاعلية ويمكن تعديلها بسهولة لإظهار وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات وعرضها في Excel.

##  كيفية إضافة PivotChart باستخدام Aspose.Cells
###  **إنشاء جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام أسلوب PutValue/setValue للكائن Cell. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات الجدول المحوري.
1. قم بإضافة جدول محوري إلى ورقة العمل عن طريق استدعاء أسلوب الإضافة الخاص بمجموعة PivotTables (المغلفة في كائن ورقة العمل).
1. قم بالوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به.
1. استخدم أيًا من كائنات الجدول المحوري المغلفة في كائن PivotTable لإدارة الجدول.

ويرد أدناه نموذج التعليمات البرمجية. يؤدي تنفيذ التعليمات البرمجية إلى إنشاء ملف جديد: PivotTable_test.xls.

**ادخال البيانات** 

![ما يجب القيام به:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**الجدول المحوري للإخراج**

![ما يجب القيام به:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **إنشاء مخطط محوري بناءً على الجدول المحوري**

لإنشاء مخطط محوري باستخدام Aspose.Cells:

1. أضف مخططًا.
1. قم بتعيين PivotSource للمخطط للإشارة إلى جدول محوري موجود في جدول البيانات.
1. تعيين سمات أخرى.

يوجد أدناه الرمز الذي يستخدمه المكون لإنجاز المهمة. يؤدي تنفيذ التعليمات البرمجية إلى إنشاء ملف جديد: PivotChart_test.xls.

**ورقة الرسم البياني المحوري**

![ما يجب القيام به:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

توضح هذه المقالة كيفية إنشاء جداول محورية ومخططات محورية باستخدام Aspose.Cells. ونأمل أن تساعدك على استخدام هذه الميزات في السيناريوهات الخاصة بك.

لقد استفاد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق.

 نرحب باستفساراتكم وتعليقاتكم واقتراحاتكم على[Aspose.Cells المنتدى](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
