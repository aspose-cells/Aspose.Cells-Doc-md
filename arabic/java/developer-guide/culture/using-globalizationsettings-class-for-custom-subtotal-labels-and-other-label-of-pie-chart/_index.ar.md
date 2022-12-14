---
title: استخدام فئة GlobalizationSettings لملصقات المجموع الفرعي المخصص والتسميات الأخرى للمخطط الدائري
type: docs
weight: 50
url: /ar/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **سيناريوهات الاستخدام الممكنة**
 كشفت واجهات برمجة التطبيقات Aspose.Cells ملف[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) class من أجل التعامل مع السيناريوهات التي يرغب فيها المستخدم في استخدام تسميات مخصصة للمجاميع الفرعية في جدول بيانات. وعلاوة على ذلك، فإن[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)يمكن أيضًا استخدام class لتعديل**آخر** تسمية المخطط الدائري أثناء عرض ورقة العمل أو المخطط.
## **مقدمة في فئة GlobalizationSettings**
 ال[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) تقدم الفئة حاليًا الطرق الثلاثة التالية التي يمكن تجاوزها في فئة مخصصة للحصول على التسميات المطلوبة للمجموعات الفرعية أو لتقديم نص مخصص لـ**آخر** تسمية مخطط دائري.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): الحصول على الاسم الإجمالي للوظيفة.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): الحصول على الاسم الإجمالي الكلي للوظيفة.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): الحصول على اسم التصنيفات "الأخرى" للمخططات الدائرية.
### **تسميات مخصصة للمجموعات الفرعية**
 ال[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) يمكن استخدام الفئة لتخصيص تسميات الإجمالي الفرعي عن طريق تجاوز[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) كما هو موضح في المستقبل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 لإدخال ملصقات مخصصة ، يلزم تعيين ملف[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) الخاصية إلى مثيل*إعدادات مخصصة*الفئة المحددة أعلاه قبل إضافة الإجماليات الفرعية إلى ورقة العمل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 ال[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)فئة تعمل فقط لإضافة مجاميع فرعية جديدة. إذا كان جدول البيانات يحتوي بالفعل على مجاميع فرعية ، فلا يمكن تعديل تسمياتها.

{{% /alert %}} 
### **نص مخصص للتسمية الأخرى للمخطط الدائري**
 ال[العولمة الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) فئة تقدم[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) ) وهي طريقة مفيدة لمنح التسمية "أخرى" للمخططات الدائرية قيمة مخصصة. يحدد المقتطف التالي فئة مخصصة ويتجاوز[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) للحصول على تسمية مخصصة بناءً على تعيين اللغة الافتراضية لـ JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 يقوم المقتطف التالي بتحميل جدول بيانات موجود يحتوي على مخطط دائري ويعرض المخطط إلى صورة أثناء استخدام*إعدادات مخصصة*فئة تم إنشاؤها أعلاه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


 فيما يلي الصورة الناتجة عند ضبط الإعدادات المحلية للجهاز على فرنسا. كما ترى ، تمت ترجمة التسمية "أخرى" إلى "Autre" كما هو محدد في*إعدادات مخصصة*صف دراسي.

![ما يجب القيام به: image_بديل_نص](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
