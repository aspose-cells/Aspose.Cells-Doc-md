---
title: استخدام فئة GlobalizationSettings لتخصيص علامات مجموع جزئي مخصصة وعلامة أخرى لمخطط البيت
type: docs
weight: 70
url: /ar/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **سيناريوهات الاستخدام المحتملة**

وقد طرحت واجهة برمجة تطبيقات Aspose.Cells الفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) للتعامل مع السيناريوهات التي يرغب المستخدم في استخدام علامات مخصصة للمجاميع الجزئية في جدول بيانات. علاوة على ذلك، يمكن أيضًا استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) لتعديل العلامة **أخرى** لمخطط البيت أثناء استخراج الورقة العمل أو المخطط.

## **مقدمة في فئة GlobalizationSettings**

تقدم فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) حاليًا 3 طرق يمكن تجاوزها في فئة مخصصة للحصول على علامات مرجعية مرغوبة للمجاميع الجزئية أو لتصدير نص مخصص لعلامة **أخرى** لمخطط البيت.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname): يحصل على الاسم الكامل للوظيفة.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname): يستلم اسم المجموع الكلي للوظيفة.
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername): يستلم اسم "أخرى" لعلامات مخطط البيت.

### **علامات مخصصة للمجاميع الجزئية**

يمكن استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) لتخصيص علامات المجموع الجزئي عن طريق تجاوز الطرق [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) و [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname) كما يظهر فيما يلي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

من أجل حقن علامات مخصصة، يجب تعيين خاصية [**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) إلى مثيل من فئة **CustomSettings** المعرفة أعلاه قبل إضافة المجاميع الجزئية إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

تعمل فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) فقط لإضافة مجاميع جديدة. إذا كان جدول بيانات يحتوي بالفعل على مجاميع جزئية، فلا يمكن تعديل علاماتها.

{{% /alert %}}

### **نص مخصص لعلامة "أخرى" لمخطط البيت**

تقدم فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings) طريقة [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) التي تكون مفيدة لإعطاء علامة "أخرى" لمخطط البيت قيمة مخصصة. يحدد المقتطف التالي فئة مخصصة ويجاوز الطريقة [**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername) للحصول على علامة مخصصة بناءً على معرف الثقافة في النظام.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

المقتطف التالي يحمل جدول بيانات موجود يحتوي على مخطط بيت ويعرض المخطط إلى صورة مستخدمًا فئة **CustomSettings** التي تم إنشاؤها أعلاه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
