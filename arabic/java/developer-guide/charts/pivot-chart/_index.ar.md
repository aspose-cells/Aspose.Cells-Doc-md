---
title: كيفية إضافة جدول محوري باستخدام Aspose.Cells
linktitle: مخطط محوري
type: docs
weight: 100
url: /ar/java/how-to-add-pivot-chart/
description: كيفية إضافة جدول محوري باستخدام Aspose.Cells.
keywords: PivotChart
---
## ما هو PivotChart

PivotChart في Excel هو تمثيل رسومي للبيانات تم إنشاؤه من PivotTable. يتيح للمستخدمين تصور البيانات وتحليلها ديناميكيًا من خلال تلخيص وعرض المعلومات في شكل رسوم بيانية. تكون PivotCharts تفاعلية ويمكن تعديلها بسهولة لعرض وجهات نظر مختلفة للبيانات، مما يجعلها أداة قوية لتحليل البيانات والعرض في Excel.

## كيفية إضافة جدول محوري باستخدام Aspose.Cells
### **إنشاء جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورق العمل باستخدام أسلوب PutValue/setValue لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات الجدول الدوري.
1. أضف جدول محوري إلى ورقة العمل عن طريق استدعاء طريقة add في مجموعة PivotTables (مغلّفة في كائن الورقة).
1. الوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير فهرسه.
1. استخدم أيًا من كائنات الجدول الدوري المغلّفة في كائن PivotTable لإدارة الجدول.

يتم إعطاء عينة الكود أدناه. تنفيذ الكود يولد ملفًا جديدًا: pivotTable_test.xls.

**بيانات الإدخال** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**جدول الجدول الدوري الناتج**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **إنشاء رسم بياني محوري استنادًا إلى جدول الجدول الدوري**

لإنشاء رسم بياني محوري باستخدام Aspose.Cells:

1. أضف رسم بياني.
1. قم بتعيين PivotSource للرسم البياني للإشارة إلى جدول محوري موجود في جدول البيانات.
1. قم بتعيين سمات أخرى.

أدناه الكود المستخدم لتنفيذ المهمة من قبل المكون. تنفيذ الكود يولد ملفًا جديدًا: pivotChart_test.xls.

**ورقة الرسم البياني الدوري**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

يوضح هذا المقال كيفية إنشاء جداول محورية ورسوم بيانية محورية باستخدام Aspose.Cells. نأمل أن يساعدك في استخدام هذه الميزات في سيناريوهاتك الخاصة.

استفاد Aspose.Cells من سنوات من الأبحاث والتصميم والضبط الدقيق.

نرحب باستفساراتكم وتعليقاتكم واقتراحاتكم في [منتدى Aspose.Cells](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}
