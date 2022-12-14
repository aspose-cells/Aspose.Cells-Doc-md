---
title: استخدام فئة GlobalizationSettings لملصقات المجموع الفرعي المخصص والتسميات الأخرى للمخطط الدائري
type: docs
weight: 70
url: /ar/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **سيناريوهات الاستخدام الممكنة**

 كشفت واجهات برمجة التطبيقات Aspose.Cells ملف[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)class من أجل التعامل مع السيناريوهات التي يرغب فيها المستخدم في استخدام تسميات مخصصة للمجاميع الفرعية في جدول بيانات. وعلاوة على ذلك، فإن[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)يمكن أيضًا استخدام class لتعديل**آخر** تسمية المخطط الدائري أثناء عرض ورقة العمل أو المخطط.

## **مقدمة في فئة GlobalizationSettings**

 ال[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) تقدم الفئة حاليًا الطرق الثلاثة التالية التي يمكن تجاوزها في فئة مخصصة للحصول على التسميات المطلوبة للمجموعات الفرعية أو لتقديم نص مخصص لـ**آخر** تسمية مخطط دائري.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): الحصول على الاسم الإجمالي للوظيفة.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): الحصول على الاسم الإجمالي الكلي للوظيفة.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): الحصول على اسم التصنيفات "الأخرى" للمخططات الدائرية.

### **تسميات مخصصة للمجموعات الفرعية**

 ال[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) يمكن استخدام الفئة لتخصيص تسميات الإجمالي الفرعي عن طريق تجاوز[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)الأساليب كما هو موضح في المستقبل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

 لإدخال ملصقات مخصصة ، يلزم تعيين ملف[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) الخاصية إلى مثيل**إعدادات مخصصة**الفئة المحددة أعلاه قبل إضافة الإجماليات الفرعية إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

 ال[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)فئة تعمل فقط لإضافة مجاميع فرعية جديدة. إذا كان جدول البيانات يحتوي بالفعل على مجاميع فرعية ، فلا يمكن تعديل تسمياتها.

{{% /alert %}}

### **نص مخصص للتسمية الأخرى للمخطط الدائري**

 ال[**العولمة الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) عروض الصف[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)طريقة مفيدة لمنح التسمية "أخرى" للمخططات الدائرية قيمة مخصصة. يحدد المقتطف التالي فئة مخصصة ويتجاوز[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)طريقة للحصول على تسمية مخصصة بناءً على معرف ثقافة النظام.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

 يقوم المقتطف التالي بتحميل جدول بيانات موجود يحتوي على مخطط دائري ويعرض المخطط إلى صورة أثناء استخدام**إعدادات مخصصة**فئة تم إنشاؤها أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
