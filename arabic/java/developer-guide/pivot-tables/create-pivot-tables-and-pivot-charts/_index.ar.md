---
title: إنشاء جداول محورية ومخططات محورية
type: docs
weight: 10
url: /ar/java/create-pivot-tables-and-pivot-charts/
description: قم بإنشاء جداول محورية ومخططات محورية باستخدام Aspose.Cells for Java API.
keywords: excel create pivot table java, excel create pivot chart java, excel create pivot table and pivot chart java, create excel pivot table java, create excel pivot chart java, create excel pivot table and pivot chart java, java create excel pivot table and pivot chart, how to create excel pivot table and pivot chart java
---
{{% alert color="primary" %}}

الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال ، قد يكون لديك المئات من إدخالات الفاتورة في قائمة بورقة عمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل أو المنتج أو التاريخ. باستخدام Microsoft Excel ، من الممكن إعادة ترتيب المعلومات في الجدول المحوري بسرعة عن طريق سحب الأزرار إلى موضع جديد.

المخطط المحوري هو تمثيل رسومي تفاعلي للبيانات في جدول محوري. تم تقديم المخططات المحورية في Excel 2000. ويسهل استخدام المخطط المحوري فهم البيانات نظرًا لأن الجدول المحوري ينشئ الإجماليات الفرعية والإجماليات تلقائيًا.

 Aspose.Cells يدعم[الجداول المحورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) و[المخططات المحورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **إضافة الجداول المحورية والمخططات**

يوفر Aspose.Cells مجموعة خاصة من الفئات المستخدمة لتكوين جداول محورية. تُستخدم هذه الفئات لإنشاء كائنات PivotTable وتعيينها ، والتي تعمل بمثابة كتل الإنشاء الأساسية لكائن PivotTable:

- PivotField ، حقل في تقرير جدول محوري.
- PivotFields ، مجموعة من كل كائنات PivotField في جدول محوري.
- PivotTable ، تقرير PivotTable في ورقة عمل.
- PivotTables ، مجموعة من كل كائنات PivotTable في ورقة العمل.

### **التحضير لاستخدام Aspose.Cells**

1. قم بتنزيل وتثبيت Aspose.Cells.Zip:
   1. [تحميل Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
 1. قم بفك ضغطه على جهاز الكمبيوتر الخاص بك.
 الجميع[Aspose](http://www.aspose.com/) المكونات ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.
1. أنشئ مشروعًا
 1. يمكنك إما إنشاء مشروع باستخدام محرر Java مثل Eclipse أو إنشاء برنامج بسيط باستخدام NotePad.
1. إضافة مسار الفصل:
 لتعيين مسار فئة باستخدام Eclipse:
1. قم باستخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
 1. قم بتعيين مسار الفصل للمشروع في Eclipse:
1. حدد مشروعك في Eclipse ثم انقر فوق قوائم Project-Properties.
 1. حدد "Java Build Path" في الجانب الأيسر من النافذة المنبثقة ، ثم حدد علامة التبويب "Libraries" ، وانقر فوق "Add JARs" أو "Add External JARs" لتحديد Aspose.Cells.jar و dom4j_1.6.1.jar وإضافتها في بناء المسارات.
 1. اكتب تطبيقًا لاستدعاء واجهات برمجة التطبيقات لمكونات Aspose.
 أو يمكنك ضبطه في وقت التشغيل في دوس موجه في Windows.

{{< highlight "java" >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

### **إنشاء جدول محوري**

لإنشاء جدول محوري باستخدام Aspose.Cells:

1. أضف بعض البيانات إلى خلايا ورقة العمل باستخدام أسلوب PutValue / setValue الخاص بالكائن Cell. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. سيتم استخدام البيانات كمصدر بيانات للجدول المحوري.
1. أضف جدولاً محوريًا إلى ورقة العمل عن طريق استدعاء طريقة إضافة مجموعة PivotTables (مغلفة في كائن ورقة العمل).
1. قم بالوصول إلى كائن PivotTable الجديد من مجموعة PivotTables بتمرير الفهرس الخاص به.
1. استخدم أيًا من كائنات الجدول المحوري المغلفة في كائن PivotTable لإدارة الجدول.

يتم إعطاء نموذج التعليمات البرمجية أدناه. يؤدي تنفيذ التعليمات البرمجية إلى إنشاء ملف جديد: pivotTable_test.xls.

**ادخال البيانات** 

![ما يجب القيام به: image_بديل_نص](create-pivot-tables-and-pivot-charts_1.png)

**الجدول المحوري الناتج**

![ما يجب القيام به: image_بديل_نص](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

### **إنشاء مخطط Pivot استنادًا إلى Pivot Table**

لإنشاء مخطط محوري باستخدام Aspose.Cells:

1. أضف مخططًا.
1. قم بتعيين PivotSource في المخطط للإشارة إلى جدول محوري موجود في جدول البيانات.
1. ضع سمات أخرى.

يوجد أدناه الرمز الذي يستخدمه المكون لإنجاز المهمة. يؤدي تنفيذ الكود إلى إنشاء ملف جديد: pivotChart_test.xls.

**ورقة الرسم البياني المحورية**

![ما يجب القيام به: image_بديل_نص](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

توضح هذه المقالة كيفية إنشاء الجداول المحورية والمخططات المحورية باستخدام Aspose.Cells. ونأمل أن تساعدك على استخدام هذه الميزات في السيناريوهات الخاصة بك.

لقد استفاد Aspose.Cells من سنوات من البحث والتصميم والضبط الدقيق.

 نرحب باستفساراتك وتعليقاتك واقتراحاتك على[Aspose.Cells المنتدى](https://forum.aspose.com/c/cells/9). نحن نضمن الرد السريع.

{{% /alert %}}

## مقالات ذات صلة

- [فرز مخصص في Pivot Table](/cells/ar/java/custom-sorting-in-pivot-table/)
- [تنسيق الجدول المحوري](/cells/ar/java/formatting-pivot-table/)
- [تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة](/cells/ar/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [تعطيل شرائط الجدول المحوري](/cells/ar/java/disable-pivot-table-ribbons/)

