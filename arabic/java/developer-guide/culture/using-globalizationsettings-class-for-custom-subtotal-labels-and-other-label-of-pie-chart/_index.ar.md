---
title: استخدام فئة GlobalizationSettings لتخصيص علامات مجموع جزئي مخصصة وعلامة أخرى لمخطط البيت
type: docs
weight: 50
url: /ar/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**
فقد قامت واجهات برمجة التطبيقات Aspose.Cells بتعريض فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) للتعامل مع السيناريوهات التي يرغب المستخدم في استخدام تسميات مخصصة للمجموعات الفرعية في ورق العمل. بالإضافة إلى ذلك، يمكن استخدام فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) أيضًا لتعديل تسمية **أخرى** لرسم الدائري أثناء عرض ورقة العمل أو الرسم البياني.
## **مقدمة في فئة GlobalizationSettings**
تقدم فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) حاليًا 3 طرق يمكن تجاوزها في فئة مخصصة للحصول على تسميات المجموعات الفرعية المرغوبة أو لعرض نص مخصص لتسمية **أخرى** لرسم الدائري.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): يحصل على اسم الإجمالي للدالة.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): يحصل على اسم الإجمالي العام للدالة.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): يحصل على اسم تسميات "أخرى" لرسوم بيانية دائريّة.
### **علامات مخصصة للمجاميع الجزئية**
يمكن استخدام فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) لتخصيص تسميات المجموع الفرعي عن طريق تجاوز الطرق [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) و [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) كما هو موضح لاحقًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 لزراعة التسميات المخصصة، يُطلب تعيين [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) إلى نسخة من فئة *CustomSettings* المعرفة أعلاه قبل إضافة المجاميع الفرعية إلى ورقة العمل.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

يعمل فقط فئة [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) لإضافة مجاميع فرعية جديدة. إذا احتوت ورقة العمل بالفعل على مجاميع فرعية، فلا يمكن تعديل تسمياتها.

{{% /alert %}} 
### **نص مخصص لعلامة "أخرى" لمخطط البيت**
يقدم [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) طريقة [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) التي تساعد على إعطاء تسمية "أخرى" لرسوم بيانية دائريّة قيمة مخصصة. يحدد المقتطف التالي فئة مخصصة ويتجاوز طريقة [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) للحصول على تسمية مخصصة استنادًا إلى اللغة الافتراضية المحددة لل JVM.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


تحميل الرقم الجدول الموجود يحتوي على شريحة ويقوم بإظهار الشريحة لصورة أثناء استخدام فئة *CustomSettings* التي تم إنشاؤها سابقًا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


فيما يلي الصورة الناتجة عندما يتم تعيين لغة الجهاز على فرنسا. كما ترون أن التسمية "Other" قد تم ترجمتها إلى "Autre" كما هو محدد في فئة *CustomSettings*.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
