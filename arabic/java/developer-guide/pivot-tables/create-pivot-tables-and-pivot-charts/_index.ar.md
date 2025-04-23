---
title: إنشاء جداول محورية ورسوم بيانية محورية
type: docs
weight: 10
url: /ar/java/create-pivot-tables-and-pivot-charts/
description: إنشاء جداول محورية ورسوم بيانية محورية باستخدام واجهة برمجة التطبيقات Aspose.Cells for Java.
keywords: جدول excel create pivot table java، excel create pivot chart java، excel create pivot table and pivot chart java، create excel pivot table java، create excel pivot chart java، create excel pivot table and pivot chart java، java create excel pivot table and pivot chart، كيفية إنشاء جدول محوري excel ورسم بياني محوري java
---

{{% alert color="primary" %}}

الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال، قد تحتوي على مئات الإدخالات الخاصة بالفواتير في قائمة داخل صفحة العمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل، المنتج أو التاريخ. باستخدام مايكروسوفت إكسل يمكن بسرعة إعادة ترتيب المعلومات في الجدول المحوري عن طريق سحب الأزرار إلى موقع جديد.

الرسم البياني المحوري هو تمثيل رسومي تفاعلي للبيانات في الجدول المحوري. تم إدخال الرسوم البيانية المحورية في إكسل 2000. باستخدام الرسم البياني المحوري يصبح أسهل فهم البيانات نظرًا لأن الجدول المحوري يقوم تلقائيًا بإنشاء المجاميع الفرعية والمجاميع.

يدعم Aspose.Cells [الجداول المحورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-table) و[الرسوم البيانية المحورية](/cells/ar/java/create-pivot-tables-and-pivot-charts/#creating-a-pivot-chart-based-on-the-pivot-table).

{{% /alert %}}

## **إضافة الجداول المحورية والرسوم البيانية**

توفر Aspose.Cells مجموعة خاصة من الفئات المستخدمة لإنشاء الجداول المحورية. يتم استخدام هذه الفئات لإنشاء وتعيين كائنات PivotTable، والتي تعمل كبنية أساسية لكائن PivotTable:

- PivotField، حقل في تقرير جدول محوري.
- PivotFields، مجموعة من جميع كائنات PivotField في جدول محوري.
- PivotTable، تقرير PivotTable على صفحة العمل.
- PivotTables، مجموعة من جميع كائنات PivotTable على صفحة العمل.

### **التحضير لاستخدام Aspose.Cells**

1. قم بتنزيل وتثبيت Aspose.Cells.Zip:
   1. [تحميل Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. قم بفك الضغط عنها في جهاز التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. إنشاء مشروع
   1. يمكنك إما إنشاء مشروع باستخدام محرر جافا مثل Eclipse أو إنشاء برنامج بسيط باستخدام NotePad.
1. إضافة مسار الفئة:
   لتعيين مسار الفئة باستخدام Eclipse:
   1. استخراج Aspose.Cells.jar و dom4j_1.6.1.jar من Aspose.Cells.zip.
   1. ضبط مسار الفئة للمشروع في Eclipse:
   1. حدد مشروعك في الإكليبس ثم انقر فوق القوائم مشروع -> الخصائص.
   1. حدد “Java Build Path” في الجانب الأيسر من نافذة العرض المنبثق، ثم حدد علامة التبويب “المكتبات”، انقر على “إضافة JARs” أو “إضافة JARs الخارجية” لتحديد Aspose.Cells.jar و dom4j_1.6.1.jar وأضفها إلى مسارات البناء.
   1. كتابة التطبيق لاستدعاء واجهات برمجة التطبيقات من مكونات Aspose.
      أو يمكنك ضبطه خلال التشغيل في سطر الأوامر في نظام التشغيل ويندوز.

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName 

{{< /highlight >}}

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

## مقالات ذات صلة

- [ترتيب مخصص في جدول محوري](/cells/ar/java/custom-sorting-in-pivot-table/)
- [تنسيق جدول الجدول المحوري](/cells/ar/java/formatting-pivot-table/)
- [تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة](/cells/ar/java/refresh-and-calculate-pivot-table-having-calculated-items/)
- [تعطيل شرائط الجدول المحوري](/cells/ar/java/disable-pivot-table-ribbons/)

{{< app/cells/assistant language="java" >}}
